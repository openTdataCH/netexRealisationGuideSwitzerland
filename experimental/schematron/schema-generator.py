#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generate a restricted XSD 1.0 from a base XSD and a Schematron overlay.

Supported rule patterns in Schematron asserts:
- remove:  not(prefix:Child)  OR empty(prefix:Child)
- require: exists(prefix:Child) OR bare 'prefix:Child'
- allow:   count(prefix:Child) <= 1
    If the assert has @diagnostics pointing to a sch:diagnostic that contains an xs:element
    snippet, that snippet is inserted; otherwise, a default xs:string element is inserted.

Limitations:
- Handles xs:sequence only (no xs:choice/xs:all/xs:group).
- Traverses context paths by local-name only.
- Works on a single XSD file (no include/import resolution).

Usage:
    python generate_restricted_xsd.py --base StopPlace.xsd --sch Restrictions.sch --out StopPlaceRestricted.xsd
"""

import argparse
import re
from copy import deepcopy
from lxml import etree as ET

XS_NS = "http://www.w3.org/2001/XMLSchema"
SCH_NS = "http://purl.oclc.org/dsdl/schematron"
NS = {"xs": XS_NS, "sch": SCH_NS}


def parse_xml(path: str) -> ET._ElementTree:
    parser = ET.XMLParser(remove_blank_text=False)
    return ET.parse(path, parser)


def qname_local(token: str) -> str:
    """Return the local part of a QName-like token 'prefix:Local' or the token itself if no colon."""
    return token.split(":", 1)[-1]


def resolve_qname_in_rule(token: str, rule: ET._Element) -> ET.QName | None:
    """Resolve a QName token relative to a Schematron rule's namespace map. Returns ET.QName or None."""
    if ":" not in token:
        return None
    prefix, local = token.split(":", 1)
    uri = rule.nsmap.get(prefix)
    if not uri:
        return None
    return ET.QName(uri, local)


def parse_context_to_locals(context_expr: str) -> list[str]:
    """Split a Schematron rule context path into local names: 'netex:A/netex:B' -> ['A','B']."""
    steps = [s for s in context_expr.strip().split("/") if s]
    return [qname_local(s) for s in steps]


def find_global_element(xsd_root: ET._Element, lname: str) -> ET._Element | None:
    """Find top-level xs:element by local name."""
    elems = xsd_root.xpath(f"./xs:element[@name=$n]", namespaces=NS, n=lname)
    return elems[0] if elems else None


def element_complex_type(xsd_root: ET._Element, elem: ET._Element) -> ET._Element | None:
    """Resolve an xs:element to its complexType (named or anonymous)."""
    t = elem.get("type")
    if t:
        # Resolve by local name of @type (assume same schema)
        type_local = qname_local(t)
        types = xsd_root.xpath(f"./xs:complexType[@name=$n]", namespaces=NS, n=type_local)
        return types[0] if types else None
    # Anonymous complex type
    c = elem.find(f"{{{XS_NS}}}complexType")
    return c


def find_child_decl(ctype: ET._Element, lname: str) -> ET._Element | None:
    """Find a child xs:element with given name inside the complex type's xs:sequence (first match)."""
    if ctype is None:
        return None
    elems = ctype.xpath(f".//xs:sequence//xs:element[@name=$n]", namespaces=NS, n=lname)
    return elems[0] if elems else None


def context_complex_type(xsd_root: ET._Element, context_locals: list[str]) -> ET._Element | None:
    """Walk the context path to return the complexType of the last step."""
    if not context_locals:
        return None
    # Root step: global element
    root_el = find_global_element(xsd_root, context_locals[0])
    ctype = element_complex_type(xsd_root, root_el) if root_el is not None else None
    # Traverse down by named child elements
    for step in context_locals[1:]:
        child = find_child_decl(ctype, step)
        ctype = element_complex_type(xsd_root, child) if child is not None else None
        if ctype is None:
            break
    return ctype


# Regex helpers to classify asserts
RE_QNAME = re.compile(r"([A-Za-z_][\w\-.]*):([A-Za-z_][\w\-.]*)")
RE_REMOVE = re.compile(r"^(?:not|empty)\s*\(\s*[A-Za-z_][\w\-.]*:[A-Za-z_][\w\-.]*\s*\)\s*$")
RE_REQUIRE = re.compile(r"^exists\s*\(\s*[A-Za-z_][\w\-.]*:[A-Za-z_][\w\-.]*\s*\)\s*$")
RE_BARE = re.compile(r"^[A-Za-z_][\w\-.]*:[A-Za-z_][\w\-.]*$")  # treat as require
RE_ALLOW = re.compile(r"^count\s*\(\s*[A-Za-z_][\w\-.]*:[A-Za-z_][\w\-.]*\s*\)\s*<=\s*1\s*$")


def classify_assert(assert_el: ET._Element) -> dict | None:
    """
    Return dict with keys: op ('remove'|'require'|'allow'), child_local, assert_el
    or None if pattern not recognized.
    """
    test = (assert_el.get("test") or "").strip()
    m = RE_QNAME.search(test)
    if not m:
        return None
    child_local = m.group(2)
    if RE_REMOVE.match(test):
        return {"op": "remove", "child_local": child_local, "assert_el": assert_el}
    if RE_REQUIRE.match(test) or RE_BARE.match(test):
        return {"op": "require", "child_local": child_local, "assert_el": assert_el}
    if RE_ALLOW.match(test):
        return {"op": "allow", "child_local": child_local, "assert_el": assert_el}
    return None


def get_diagnostic_snippet(sch_tree: ET._ElementTree, assert_el: ET._Element) -> ET._Element | None:
    """Return first xs:element found in the referenced diagnostics of this assert, if any."""
    diag_ids = (assert_el.get("diagnostics") or "").strip()
    if not diag_ids:
        return None
    ids = [d for d in re.split(r"\s+", diag_ids) if d]
    if not ids:
        return None
    for d in ids:
        diags = sch_tree.xpath(f"//sch:diagnostic[@id=$id]", namespaces=NS, id=d)
        for diag in diags:
            elem = diag.find(f".//{{{XS_NS}}}element")
            if elem is not None:
                return elem
    return None


def ensure_min_occurs_one(elem: ET._Element) -> bool:
    """Ensure minOccurs='1' on an xs:element. Returns True if changed."""
    current = elem.get("minOccurs")
    if current != "1":
        elem.set("minOccurs", "1")
        return True
    return False


def remove_child_elements(ctype: ET._Element, child_local: str) -> int:
    """Remove all occurrences of xs:element[@name=child_local] under ctype/xs:sequence. Returns count removed."""
    count = 0
    nodes = ctype.xpath(f".//xs:sequence//xs:element[@name=$n]", namespaces=NS, n=child_local)
    for n in nodes:
        parent = n.getparent()
        if parent is not None:
            parent.remove(n)
            count += 1
    return count


def insert_child_element(ctype: ET._Element, new_elem: ET._Element) -> bool:
    """Insert a new child xs:element as last into ctype/xs:sequence. Creates sequence if missing."""
    seq = ctype.find(f"{{{XS_NS}}}sequence")
    if seq is None:
        seq = ET.SubElement(ctype, f"{{{XS_NS}}}sequence")
    seq.append(new_elem)
    return True


def default_new_element(child_local: str) -> ET._Element:
    """Create a default xs:element declaration with xs:string type and minOccurs=0."""
    e = ET.Element(f"{{{XS_NS}}}element", name=child_local, minOccurs="0")
    e.set("type", "xs:string")
    return e


def apply_operation(xsd_root: ET._Element,
                    sch_tree: ET._ElementTree,
                    context_locals: list[str],
                    op: dict,
                    log: list[str]) -> None:
    """
    Apply a single operation to the schema.
    op: {'op': 'remove'|'require'|'allow', 'child_local': 'Name', 'assert_el': <assert>}
    """
    ctype = context_complex_type(xsd_root, context_locals)
    if ctype is None:
        log.append(f"WARNING: Context not found: {'/'.join(context_locals)}")
        return

    child_local = op["child_local"]

    if op["op"] == "remove":
        removed = remove_child_elements(ctype, child_local)
        if removed:
            log.append(f"Removed {removed} occurrence(s) of element '{child_local}' in {'/'.join(context_locals)}")
        else:
            log.append(f"NOTE: Element '{child_local}' not found to remove in {'/'.join(context_locals)}")

    elif op["op"] == "require":
        el = find_child_decl(ctype, child_local)
        if el is None:
            log.append(f"WARNING: Element '{child_local}' not found to require in {'/'.join(context_locals)}")
        else:
            if ensure_min_occurs_one(el):
                log.append(f"Set minOccurs=1 on '{child_local}' in {'/'.join(context_locals)}")
            else:
                log.append(f"No change (minOccurs already 1) for '{child_local}' in {'/'.join(context_locals)}")

    elif op["op"] == "allow":
        # If exists already, nothing to do
        if find_child_decl(ctype, child_local) is not None:
            log.append(f"No change (element '{child_local}' already present) in {'/'.join(context_locals)}")
            return
        # Try to get snippet from diagnostics
        snippet = get_diagnostic_snippet(sch_tree, op["assert_el"])
        new_el = deepcopy(snippet) if snippet is not None else default_new_element(child_local)
        insert_child_element(ctype, new_el)
        if snippet is not None:
            log.append(f"Inserted element '{child_local}' from diagnostic into {'/'.join(context_locals)}")
        else:
            log.append(f"Inserted default xs:string element '{child_local}' into {'/'.join(context_locals)}")

    else:
        log.append(f"WARNING: Unknown operation '{op['op']}'")


def collect_ops_from_schematron(sch_tree: ET._ElementTree) -> list[tuple[list[str], dict]]:
    """
    Iterate Schematron rules and collect applicable operations.
    Returns list of tuples: (context_locals, op_dict).
    """
    ops = []
    rules = sch_tree.xpath("//sch:rule", namespaces=NS)
    for rule in rules:
        context = rule.get("context") or ""
        context_locals = parse_context_to_locals(context)
        for assert_el in rule.xpath("./sch:assert", namespaces=NS):
            classified = classify_assert(assert_el)
            if classified:
                ops.append((context_locals, classified))
    return ops


def main():
    ap = argparse.ArgumentParser(description="Generate restricted XSD from base XSD and Schematron restrictions.")
    ap.add_argument("--base", required=True, help="Path to base XSD file")
    ap.add_argument("--sch", required=True, help="Path to Schematron file")
    ap.add_argument("--out", required=True, help="Path to write restricted XSD")
    args = ap.parse_args()

    xsd_tree = parse_xml(args.base)
    xsd_root = xsd_tree.getroot()
    if xsd_root.tag != f"{{{XS_NS}}}schema":
        raise SystemExit("Base file does not appear to be an XML Schema (xs:schema).")

    sch_tree = parse_xml(args.sch)

    ops = collect_ops_from_schematron(sch_tree)
    if not ops:
        print("No recognizable operations found in Schematron. Writing a copy of the base XSD.")
        xsd_tree.write(args.out, encoding="UTF-8", xml_declaration=True, pretty_print=True)
        return

    log: list[str] = []
    for context_locals, op in ops:
        apply_operation(xsd_root, sch_tree, context_locals, op, log)

    # Write output
    xsd_tree.write(args.out, encoding="UTF-8", xml_declaration=True, pretty_print=True)

    print(f"Wrote {args.out}")
    if log:
        print("Changes:")
        for line in log:
            print(" -", line)


if __name__ == "__main__":
    main()
