#!/usr/bin/env python3
import argparse
import os
import sys
import logging
from typing import List, Optional, Tuple, Any

import xmlschema
from xmlschema import XsdElement, XsdType, XMLSchema10, XsdComponent
from xmlschema.validators import XsdGroup, XsdComplexType

XS_NS = "http://www.w3.org/2001/XMLSchema"

logger = logging.getLogger(__name__)

def local_name_from_qname(qname: Optional[str]) -> str:
    if not qname:
        return ""
    # Clark notation: {ns}local
    if qname.startswith("{"):
        return qname.split("}", 1)[1]
    # Already a local or prefixed name; best effort
    return qname.split(":")[-1]


def get_component_namespace(component) -> Optional[str]:
    # xmlschema components usually have .target_namespace
    return getattr(component, "target_namespace", None)


def get_component_local_name(component) -> str:
    # Try local_name if present, else from qname/name
    ln = getattr(component, "local_name", None)
    if ln:
        return ln
    # name is usually local name for named comps
    name = getattr(component, "name", None) or getattr(component, "qname", None)
    return local_name_from_qname(name)

def get_namespace_prefix(name: str) -> str:
    return name.split(":",1)[0]

def read_documentation_from_elem(elem) -> str:
    """
    Given the underlying XML element (lxml/Element or ElementTree), extract xs:annotation/xs:documentation text.
    """
    if elem is None:
        return ""
    # elem can be Element or may lack namespace prefixes; rely on Clark-notation
    docs = []
    # Walk children; avoid deep nested traversal beyond annotation
    for child in list(elem):
        # annotation may be in XS namespace
        if child.tag.endswith("annotation") or child.tag == f"{{{XS_NS}}}annotation":
            for doc in list(child):
                if doc.tag.endswith("documentation") or doc.tag == f"{{{XS_NS}}}documentation":
                    text = (doc.text or "").strip()
                    if text:
                        docs.append(text)
    return " ".join(docs).strip()


def get_best_documentation_for_element(el: XsdElement) -> str:
    """
    Try documentation in order:
    - The occurrence (local declaration with its own annotation)
    - The referenced global element (if ref=)
    - The element's type
    """
    # 1) From this element node
    doc = read_documentation_from_elem(getattr(el, "elem", None))
    if doc:
        return doc

    # 2) From referenced global
    ref = getattr(el, "ref", None)
    if ref is not None:
        doc = read_documentation_from_elem(getattr(ref, "elem", None))
        if doc:
            return doc

    # 3) From type
    el_type = getattr(el, "type", None)
    if el_type is not None:
        doc = read_documentation_from_elem(getattr(el_type, "elem", None))
        if doc:
            return doc

    return ""


def get_best_documentation_for_component(component) -> str:
    """
    For element/complexType/group: get top-level documentation.
    """
    # Primary: this component's elem
    doc = read_documentation_from_elem(getattr(component, "elem", None))
    if doc:
        return doc

    # For elements, try ref/type like above
    if isinstance(component, XsdElement):
        return get_best_documentation_for_element(component)

    return ""

def is_builtin_type(xsd_type: XsdType) -> bool:
    ns = getattr(xsd_type, "target_namespace", None)
    return ns == XS_NS


def retrieve_type_name(xsd_type: Optional[XsdType]) -> str:
    if xsd_type is None:
        return "anyType"
    # xmlschema XsdType usually has .name (local) and .qname
    name = getattr(xsd_type, "local_name", None)  # local name, if named
    if is_builtin_type(xsd_type) and name:
        return name  # e.g., string, int, date
    if name:
        return name  # named complex/simple type
    # Anonymous type: try base type or fallback
    base_type = getattr(xsd_type, "base_type", None)
    if base_type is not None and getattr(base_type, "name", None):
        return getattr(base_type, "name")
    # Last resort
    qname = getattr(xsd_type, "qname", None)
    if qname:
        return local_name_from_qname(qname)
    return "anonymousType"

def build_type_path(xsd_type: Optional[XsdType], name: str) -> str | None:
    if xsd_type is None:
        return None
    # xmlschema XsdType usually has .name (local) and .qname
    if is_builtin_type(xsd_type):
        return None  # e.g., string, int, date
    if name:
        return f"../types/{name}.md"  # named complex/simple type
    return None

def format_usage(min_occurs: Optional[int], max_occurs) -> str:
    def as_int(value, default):
        if value is None:
            return default
        if isinstance(value, str):
            if value.lower() == "unbounded":
                return "n"
        try:
            return int(value)
        except Exception:
            return default

    mino = as_int(min_occurs, 1)
    maxo = as_int(max_occurs, 1)
    if maxo == "n":
        return f"{mino}..n"
    return f"{mino}..{maxo}"


def build_linked_type_name(xsd_type: Optional[XsdType], max_occurs) -> str:
    tname = retrieve_type_name(xsd_type)
    tpath = build_type_path(xsd_type, tname)
    if isinstance(max_occurs, str) and max_occurs.lower() == "unbounded":
        tname = f"{tname}[]"
    if max_occurs and int(max_occurs) > 1:
        tname = f"{tname}[]"
    if tpath:
        return f"[{tname}]({tpath})"
    return tname

def collect_child_elements_from_element(node: XsdElement) -> List[Tuple[str, str, str, str]]:
    """
    Returns rows for table:
    - Element (local name)
    - Usage (min..max)
    - Type (with [] suffix if max > 1)
    - Description (documentation)
    We use deep iteration over content model to include nested groups/choices.
    """
    rows = []
    content = getattr(node, "content_type", None)
    if content is None:
        return rows

    # xmlschema's content_type for complex types often supports iter_elements()
    iter_elems = getattr(content, "iter_elements", None)
    if iter_elems is None:
        return rows

    # We keep a sequence; duplicates may appear if the model repeats; it's usually fine
    for el in iter_elems():
        if not isinstance(el, XsdElement):
            continue
        name = get_component_local_name(el)
        usage = format_usage(getattr(el, "min_occurs", 1), getattr(el, "max_occurs", 1))
        type_name = build_linked_type_name(getattr(el, "type", None), getattr(el, "max_occurs", 1))
        desc = get_best_documentation_for_element(el)
        rows.append((name, usage, type_name, desc))
    return rows

def collect_child_elements_from_complex_type(node: XsdComplexType) -> List[Tuple[str, str, str, str]]:
    """
    Returns rows for table:
    - Element (local name)
    - Usage (min..max)
    - Type (with [] suffix if max > 1)
    - Description (documentation)
    We use deep iteration over content model to include nested groups/choices.
    """
    rows = []
    content = getattr(node, "content", None)
    if content is None:
        return rows

    # xmlschema's content_type for complex types often supports iter_elements()
    elements = getattr(content, "elements", None)
    if elements is None:
        return rows

    # We keep a sequence; duplicates may appear if the model repeats; it's usually fine
    for el in elements:
        if not isinstance(el, XsdElement):
            continue
        name = get_component_local_name(el)
        usage = format_usage(getattr(el, "min_occurs", 1), getattr(el, "max_occurs", 1))
        type_name = build_linked_type_name(getattr(el, "type", None), getattr(el, "max_occurs", 1))
        desc = get_best_documentation_for_element(el)
        rows.append((name, usage, type_name, desc))
    return rows


def collect_child_elements_from_group(node: XsdGroup) -> List[Tuple[str, str, str, str]]:
    rows = []
    iter_elems = getattr(node, "iter_elements", None)
    if iter_elems is None:
        return rows
    for el in iter_elems():
        if not isinstance(el, XsdElement):
            continue
        name = get_component_local_name(el)
        usage = format_usage(getattr(el, "min_occurs", 1), getattr(el, "max_occurs", 1))
        type_name = build_linked_type_name(getattr(el, "type", None), getattr(el, "max_occurs", 1))
        desc = get_best_documentation_for_element(el)
        rows.append((name, usage, type_name, desc))
    return rows


def render_md_table(rows: List[Tuple[str, str, str, str]]) -> str:
    header = "| Element | Usage | Type | Description |\n|---|---|---|---|"
    if not rows:
        return header + "\n"
    lines = [header]
    for name, usage, type_name, desc in rows:
        # Escape pipes in description
        safe_desc = desc.replace("|", "\\|")
        lines.append(f"| {name} | {usage} | {type_name} | {safe_desc} |")
    return "\n".join(lines) + "\n"


def generate_markdown_for_node(node: XsdComponent) -> str:
    name = get_component_local_name(node)
    top_desc = get_best_documentation_for_component(node)
    # Determine element's type and collect its child elements if complex
    el_type = getattr(node, "type", None)
    rows = []
    if isinstance(el_type, XsdElement):
        rows = collect_child_elements_from_element(el_type)
    elif isinstance(el_type, XsdComplexType):
        rows = collect_child_elements_from_complex_type(el_type)
    elif isinstance(el_type, XsdGroup):
        rows = collect_child_elements_from_group(el_type)

    # Heading
    parts = [f"### {name}"]
    if top_desc:
        parts.append(top_desc.strip())

    parts.append(render_md_table(rows))
    # Optionally: include attributes table (commented out)
    # attrs_rows = []
    # if isinstance(el_type, XsdComplexType):
    #     for attr in getattr(el_type, "attributes", []):
    #         # Implement attribute documentation if desired
    #         pass
    # if attrs_rows:
    #     parts.append("#### Attributes\n")
    #     parts.append(render_attrs_table(attrs_rows))
    return "\n\n".join(parts).strip() + "\n"

def write_file(path: str, content: str):
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)

def parse_args():
    parser = argparse.ArgumentParser(
        description="Generate Markdown tables from an XSD schema (elements, complexTypes, groups)"
    )
    parser.add_argument("xsd", help="Path to the main XSD file")
    parser.add_argument(
        "--output",
        "-o",
        default=".",
        help="Path to the output directory.",
    )
    return parser.parse_args()

 # def get_ns_dir(ns: Optional[str]) -> str:
 #    if ns not in ns_dirs:
 #            safe = sanitize_namespace(ns)
 #            ns_dirs[ns] = safe
 #            ensure_dir(os.path.join(out_root, safe))
 #        return os.path.join(out_root, ns_dirs[ns])

def main():
    args = parse_args()
    xsd_path = args.xsd


    # Load schema (resolves includes/imports)
    try:
        schema = xmlschema.XMLSchema(xsd_path)
    except Exception as e:
        print(f"Failed to load XSD schema: {e}", file=sys.stderr)
        sys.exit(2)
    logger.info("Read XSD Schema from %s", xsd_path)

    out_dir = args.output
    write_md_of_elements(out_dir, schema)

    write_md_of_complexTypes(out_dir, schema)
    write_md_of_groups(out_dir, schema)

    print(f"Documentation generated under: {out_dir}")

def write_md_of_nodes(out_dir: str, nodes_name: str, node_type: type, schema: XMLSchema10):
    # Collect and write Elements
    nodes_map = getattr(schema, nodes_name, None)
    # Normalize to dict-like
    if hasattr(nodes_map, "items"):
        items = nodes_map.items()
    else:
        items = []

    for _qname, node in items:
        if not isinstance(node, node_type):
            continue
        if not getattr(node, "name", None):
            continue
        md = generate_markdown_for_node(node)
        ns_prefix = get_namespace_prefix(node.prefixed_name)
        nodes_path = os.path.join(out_dir, ns_prefix, nodes_name)
        os.makedirs(nodes_path, exist_ok=True)
        name = get_component_local_name(node)
        write_file(os.path.join(nodes_path, f"{name}.md"), md)

def write_md_of_elements(out_dir: str, schema: XMLSchema10):
    write_md_of_nodes(out_dir, "elements", XsdElement, schema)
    logger.info("Markdown of elements written to %s", out_dir)

def write_md_of_complexTypes(out_dir, schema: XMLSchema10):
    write_md_of_nodes(out_dir, "types", XsdComplexType, schema)
    logger.info("Markdown of types written to  %s", out_dir)

def write_md_of_groups(out_dir, schema: XMLSchema10):
    write_md_of_nodes(out_dir, "groups", XsdGroup, schema)
    logger.info("Markdown of groups written to  %s", out_dir)

if __name__ == "__main__":
    main()
