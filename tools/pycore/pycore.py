#!/usr/bin/env python3
import argparse
import os
import re
import sys
from typing import List, Optional, Tuple

try:
    import xmlschema
    from xmlschema.validators import XsdElement, XsdGroup, XsdComplexType, XsdType
except ImportError:
    print("Missing dependency: xmlschema. Install with: pip install xmlschema", file=sys.stderr)
    sys.exit(1)

XS_NS = "http://www.w3.org/2001/XMLSchema"





def ensure_dir(path: str):
    os.makedirs(path, exist_ok=True)
    return path


def sanitize_namespace(ns: Optional[str]) -> str:
    if not ns:
        return "no_namespace"
    # Remove scheme to keep names shorter but predictable
    ns_no_scheme = re.sub(r"^[a-z]+://", "", ns)
    # Replace path separators and unsafe chars with underscores
    safe = re.sub(r"[^A-Za-z0-9._-]+", "_", ns_no_scheme.strip("/"))
    # Collapse multiple underscores
    safe = re.sub(r"_+", "_", safe)
    return safe or "namespace"


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


def display_type_name(xsd_type: Optional[XsdType]) -> str:
    if xsd_type is None:
        return "anyType"
    # xmlschema XsdType usually has .name (local) and .qname
    name = getattr(xsd_type, "name", None)  # local name, if named
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


def type_with_array_suffix(xsd_type: Optional[XsdType], max_occurs) -> str:
    tname = display_type_name(xsd_type)
    if isinstance(max_occurs, str) and max_occurs.lower() == "unbounded":
        return f"{tname}[]"
    try:
        if int(max_occurs) > 1:
            return f"{tname}[]"
    except Exception:
        pass
    return tname


def collect_child_elements_from_complex_type(xsd_complex_type: XsdComplexType) -> List[Tuple[str, str, str, str]]:
    """
    Returns rows for table:
    - Element (local name)
    - Usage (min..max)
    - Type (with [] suffix if max > 1)
    - Description (documentation)
    We use deep iteration over content model to include nested groups/choices.
    """
    rows = []
    content = getattr(xsd_complex_type, "content_type", None)
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
        typ = type_with_array_suffix(getattr(el, "type", None), getattr(el, "max_occurs", 1))
        desc = get_best_documentation_for_element(el)
        rows.append((name, usage, typ, desc))
    return rows


def collect_child_elements_from_group(xsd_group: XsdGroup) -> List[Tuple[str, str, str, str]]:
    rows = []
    iter_elems = getattr(xsd_group, "iter_elements", None)
    if iter_elems is None:
        return rows
    for el in iter_elems():
        if not isinstance(el, XsdElement):
            continue
        name = get_component_local_name(el)
        usage = format_usage(getattr(el, "min_occurs", 1), getattr(el, "max_occurs", 1))
        typ = type_with_array_suffix(getattr(el, "type", None), getattr(el, "max_occurs", 1))
        desc = get_best_documentation_for_element(el)
        rows.append((name, usage, typ, desc))
    return rows


def render_md_table(rows: List[Tuple[str, str, str, str]]) -> str:
    header = "| Element | Usage | Type | Description |\n|---|---|---|---|"
    if not rows:
        return header + "\n"
    lines = [header]
    for name, usage, typ, desc in rows:
        # Escape pipes in description
        safe_desc = desc.replace("|", "\\|")
        lines.append(f"| {name} | {usage} | {typ} | {safe_desc} |")
    return "\n".join(lines) + "\n"


def generate_markdown_for_element(el: XsdElement) -> str:
    name = get_component_local_name(el)
    top_desc = get_best_documentation_for_component(el)
    # Determine element's type and collect its child elements if complex
    el_type = getattr(el, "type", None)
    rows = []
    if isinstance(el_type, XsdComplexType):
        rows = collect_child_elements_from_complex_type(el_type)
    # Heading
    parts = [f"### Element {name}"]
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


def generate_markdown_for_complex_type(ct: XsdComplexType) -> str:
    name = get_component_local_name(ct)
    top_desc = get_best_documentation_for_component(ct)
    rows = collect_child_elements_from_complex_type(ct)
    parts = [f"### ComplexType {name}"]
    if top_desc:
        parts.append(top_desc.strip())
    parts.append(render_md_table(rows))
    return "\n\n".join(parts).strip() + "\n"


def generate_markdown_for_group(gr: XsdGroup) -> str:
    name = get_component_local_name(gr)
    top_desc = get_best_documentation_for_component(gr)
    rows = collect_child_elements_from_group(gr)
    parts = [f"### Group {name}"]
    if top_desc:
        parts.append(top_desc.strip())
    parts.append(render_md_table(rows))
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

def main():
    args = parse_args()
    xsd_path = args.xsd
    out_root = ensure_dir(args.output)

    # Load schema (resolves includes/imports)
    try:
        schema = xmlschema.XMLSchema(xsd_path)
    except Exception as e:
        print(f"Failed to load XSD schema: {e}", file=sys.stderr)
        sys.exit(2)

    # Prepare namespace mapping file
    ns_dirs = {}  # ns -> dir name
    ns_map_path = os.path.join(out_root, "namespaces.txt")

    def get_ns_dir(ns: Optional[str]) -> str:
        if ns not in ns_dirs:
            safe = sanitize_namespace(ns)
            ns_dirs[ns] = safe
            ensure_dir(os.path.join(out_root, safe))
        return os.path.join(out_root, ns_dirs[ns])

    # Collect and write Elements
    # xmlschema 2.x: schema.maps.elements is a dict of QName -> XsdElement
    elements_map = getattr(schema, "elements", None)
    if elements_map is None:
        elements_map = getattr(schema, "maps", None)
        if elements_map is not None:
            elements_map = getattr(elements_map, "elements", {})
    # Normalize to dict-like
    if hasattr(elements_map, "items"):
        elements_items = elements_map.items()
    else:
        elements_items = []

    for _qname, el in elements_items:
        if not isinstance(el, XsdElement):
            continue
        ns = get_component_namespace(el)
        ns_dir = get_ns_dir(ns)
        elements_dir = ensure_dir(os.path.join(ns_dir, "elements"))
        name = get_component_local_name(el)
        md = generate_markdown_for_element(el)
        write_file(os.path.join(elements_dir, f"{name}.md"), md)

    # Collect and write ComplexTypes (named only)
    types_map = getattr(schema, "types", None)
    if types_map is None:
        types_map = getattr(getattr(schema, "maps", None), "types", {})
    if hasattr(types_map, "items"):
        types_items = types_map.items()
    else:
        types_items = []

    for _qname, t in types_items:
        if not isinstance(t, XsdComplexType):
            continue
        # Only named complex types
        if not getattr(t, "name", None):
            continue
        ns = get_component_namespace(t)
        ns_dir = get_ns_dir(ns)
        cts_dir = ensure_dir(os.path.join(ns_dir, "complexTypes"))
        name = get_component_local_name(t)
        md = generate_markdown_for_complex_type(t)
        write_file(os.path.join(cts_dir, f"{name}.md"), md)

    # Collect and write Groups (named only)
    groups_map = getattr(schema, "groups", None)
    if groups_map is None:
        groups_map = getattr(getattr(schema, "maps", None), "groups", {})
    if hasattr(groups_map, "items"):
        groups_items = groups_map.items()
    else:
        groups_items = []

    for _qname, gr in groups_items:
        if not isinstance(gr, XsdGroup):
            continue
        if not getattr(gr, "name", None):
            continue
        ns = get_component_namespace(gr)
        ns_dir = get_ns_dir(ns)
        groups_dir = ensure_dir(os.path.join(ns_dir, "groups"))
        name = get_component_local_name(gr)
        md = generate_markdown_for_group(gr)
        write_file(os.path.join(groups_dir, f"{name}.md"), md)

    # Write namespace mapping file
    if ns_dirs:
        lines = []
        for ns, safe in ns_dirs.items():
            lines.append(f"{safe}\t{ns or '(no namespace)'}")
        write_file(ns_map_path, "\n".join(lines) + "\n")

    print(f"Documentation generated under: {out_root}")
    if ns_dirs:
        print("Namespaces:")
        for ns, safe in ns_dirs.items():
            print(f"  {safe} -> {ns or '(no namespace)'}")


if __name__ == "__main__":
    main()
