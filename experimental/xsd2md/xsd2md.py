from lxml import etree
from typing import Optional, Tuple, List

XSD_NS = "http://www.w3.org/2001/XMLSchema"
NSMAP = {"xsd": XSD_NS}

def qname_local(q: Optional[str]) -> Optional[str]:
    if q is None:
        return None
    # strip namespace prefix, e.g. xsd:string -> string
    return q.split(":")[-1]

def find_global_complex_type(schema_root: etree._Element, type_name: str) -> Optional[etree._Element]:
    return schema_root.find(f"xsd:complexType[@name='{type_name}']", namespaces=NSMAP)

def find_global_element(schema_root: etree._Element, element_name: str) -> Optional[etree._Element]:
    return schema_root.find(f"xsd:element[@name='{element_name}']", namespaces=NSMAP)

def get_annotation_text(node: etree._Element) -> str:
    # Concatenate all xsd:documentation text content under this node
    docs = node.findall(".//xsd:annotation/xsd:documentation", namespaces=NSMAP)
    parts = []
    for d in docs:
        text = "".join(d.itertext()).strip()
        if text:
            parts.append(text)
    return " ".join(parts)

def format_usage(min_occurs: Optional[str], max_occurs: Optional[str], style="dots") -> str:
    # min_occurs/max_occurs are strings or None (defaults are 1)
    mino = int(min_occurs) if min_occurs is not None else 1
    maxo = max_occurs if max_occurs is not None else "1"
    maxo_str = "*" if maxo == "unbounded" else maxo
    if style == "colon":  # e.g., 0:* to match your sample
        return f"{mino}:{maxo_str}"
    else:  # default: 0..* style
        return f"{mino}..{maxo_str}"

def describe_inline_list(container: etree._Element) -> Optional[Tuple[str, str]]:
    """
    If container has an anonymous complexType with a single child element repeated,
    return a tuple (inner_name, inner_type_string). Else None.
    """
    ctype = container.find("xsd:complexType", namespaces=NSMAP)
    if ctype is None:
        return None
    seq = ctype.find("xsd:sequence", namespaces=NSMAP)
    if seq is None:
        return None
    elems = seq.findall("xsd:element", namespaces=NSMAP)
    # detect exactly one child element (which might be repeated)
    if len(elems) != 1:
        return None
    inner = elems[0]
    inner_name = inner.get("name")
    inner_type = inner.get("type")
    inner_type_str = None
    if inner_type is not None:
        inner_type_str = qname_local(inner_type)
    else:
        # inline type again; indicate 'complex' if no named type
        inner_type_str = "complex"
    # Append occurrence if repeated
    inner_max = inner.get("maxOccurs")
    if inner_max is None:
        pass
    elif inner_max == "unbounded":
        inner_type_str += "[]"
    elif inner_max != "1":
        inner_type_str += f"[x{inner_max}]"
    return inner_name, inner_type_str

def type_string_for_element(schema_root: etree._Element, el: etree._Element) -> str:
    t = el.get("type")
    if t is not None:
        return qname_local(t) or t
    # Inline complex or simple type
    # Try to detect a single repeated child as a "list of X"
    list_info = describe_inline_list(el)
    if list_info:
        inner_name, inner_type = list_info
        # Prefer named type if available, otherwise inner element name.
        if inner_type == "complex":
            return f"{inner_name}[]"
        return inner_type
    # Generic fallback
    if el.find("xsd:complexType", namespaces=NSMAP) is not None:
        return "complex"
    if el.find("xsd:simpleType", namespaces=NSMAP) is not None:
        # try to show base of restriction
        base = el.find(".//xsd:restriction", namespaces=NSMAP)
        if base is not None and base.get("base"):
            return qname_local(base.get("base")) or "simple"
        return "simple"
    return "unknown"

def get_immediate_children_of_complex_type(schema_root: etree._Element, complex_type: etree._Element) -> List[etree._Element]:
    # Only immediate xsd:element children under the first-level model group (sequence|choice|all)
    for tag in ("sequence", "choice", "all"):
        grp = complex_type.find(f"xsd:{tag}", namespaces=NSMAP)
        if grp is not None:
            return grp.findall("xsd:element", namespaces=NSMAP)
    return []

def resolve_element_complex_type(schema_root: etree._Element, element: etree._Element) -> Optional[etree._Element]:
    # If element has a named type, resolve it; else use its inline complexType if present
    type_name = element.get("type")
    if type_name:
        # Only resolve complex types; simple types won't have children
        ct = find_global_complex_type(schema_root, qname_local(type_name))
        return ct
    ctype = element.find("xsd:complexType", namespaces=NSMAP)
    return ctype

def generate_markdown_table_for_element(schema_root: etree._Element, element_name: str, usage_style="dots") -> str:
    top_el = find_global_element(schema_root, element_name)
    if top_el is None:
        raise ValueError(f"Top-level element '{element_name}' not found.")
    ctype = resolve_element_complex_type(schema_root, top_el)
    if ctype is None:
        raise ValueError(f"Element '{element_name}' is not complex or has no resolvable complex type.")
    children = get_immediate_children_of_complex_type(schema_root, ctype)
    rows = []
    # Header
    header = "| Element | Usage | Type | Description |\n|---|---|---|---|"
    rows.append(header)
    for child in children:
        name = child.get("name") or "(ref)"
        usage = format_usage(child.get("minOccurs"), child.get("maxOccurs"), style=usage_style)
        tstr = type_string_for_element(schema_root, child)
        desc = get_annotation_text(child)
        # Clean pipes to avoid breaking the table
        desc = desc.replace("|", "\\|")
        rows.append(f"| {name} | {usage} | {tstr} | {desc} |")
    return "\n".join(rows)

if __name__ == "__main__":
    import argparse, sys
    ap = argparse.ArgumentParser(description="Generate a Markdown table of child elements for a given XSD element.")
    ap.add_argument("xsd", help="Path to the XSD file")
    ap.add_argument("element", help="Name of the top-level element to document, e.g., StopPlace")
    ap.add_argument("--usage-style", choices=["dots", "colon"], default="dots",
                    help="How to render min/max (dots=0..*, colon=0:*)")
    args = ap.parse_args()

    tree = etree.parse(args.xsd)
    schema_root = tree.getroot()
    try:
        md = "### Elements\n"
        md += generate_markdown_table_for_element(schema_root, args.element, usage_style=args.usage_style)
        md += "\n"
        md += "### Substructure\n"
        md += "..."
        print(md)
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)
