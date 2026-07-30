#!/usr/bin/env python3
"""
Markdown Builder for NeTEx templates
Extracts documentation from annotated XML templates and generates markdown tables
with type information from XSD schemas.
"""

import argparse
import os
from lxml import etree
from tools.configuration import TEMPLATES_DIR, XSD_FILE_PATH, SITE_TABLES_DIR

# Global XSD namespace
XSD_NS = {'xs': 'http://www.w3.org/2001/XMLSchema'}


def sanitize_for_markdown(text):
    """Sanitize text for markdown table cells by escaping pipes and replacing newlines with spaces"""
    if text is None:
        return ''
    # Escape pipe characters to prevent breaking markdown tables
    text = text.replace('|', '\\|')
    # Replace all newlines and carriage returns with spaces
    # Also collapse multiple spaces into single space
    text = text.replace('\r\n', ' ').replace('\n', ' ').replace('\r', ' ')
    # Collapse multiple spaces into single space
    text = ' '.join(text.split())
    return text


def _doc_text(nodes):
    """Join all text from potentially multiple xs:documentation nodes, including nested markup."""
    texts = []
    for n in nodes:
        t = n.xpath('string(.)')
        if t:
            texts.append(' '.join(t.split()))
    return ' '.join(texts).strip()


def _find_global_element(xsd_doc, qname_or_name):
    """Find a global xs:element by name or QName."""
    name = qname_or_name.split(':')[-1]
    els = xsd_doc.xpath(f"//xs:element[@name='{name}']", namespaces=XSD_NS)
    return els[0] if els else None


def _find_named_type_node(xsd_doc, type_qname):
    """Find a named complexType or simpleType by QName."""
    tname = type_qname.split(':')[-1]
    nodes = xsd_doc.xpath(
        f"//xs:complexType[@name='{tname}'] | //xs:simpleType[@name='{tname}']",
        namespaces=XSD_NS
    )
    return nodes[0] if nodes else None


def get_xsd_documentation_for_element(element, xsd_doc):
    """
    Robustly extract documentation for an XSD element by trying:
    1) Direct docs on the element
    2) Docs on referenced global element (@ref)
    3) Docs on the named type (type=)
    4) Docs on inline type
    5) Docs on substitutionGroup head
    """
    # 1) Direct docs on this element
    desc = _doc_text(element.xpath('./xs:annotation/xs:documentation', namespaces=XSD_NS))
    if desc:
        return sanitize_for_markdown(desc)

    # 2) If @ref, check the referenced global element
    ref = element.get('ref')
    if ref:
        ref_el = _find_global_element(xsd_doc, ref)
        if ref_el is not None:
            desc = _doc_text(ref_el.xpath('./xs:annotation/xs:documentation', namespaces=XSD_NS))
            if desc:
                return sanitize_for_markdown(desc)
            # For subsequent checks, treat the referenced element as the source
            element = ref_el

    # 3) Docs on the named type
    type_attr = element.get('type')
    if type_attr:
        type_node = _find_named_type_node(xsd_doc, type_attr)
        if type_node is not None:
            desc = _doc_text(type_node.xpath('.//xs:annotation/xs:documentation', namespaces=XSD_NS))
            if desc:
                return sanitize_for_markdown(desc)

    # 4) Docs on inline type
    inline = element.find('xs:complexType', XSD_NS)
    if inline is None:
        inline = element.find('xs:simpleType', XSD_NS)
    if inline is not None:
        desc = _doc_text(inline.xpath('.//xs:annotation/xs:documentation', namespaces=XSD_NS))
        if desc:
            return sanitize_for_markdown(desc)

    # 5) Docs on substitution group head
    sg = element.get('substitutionGroup')
    if sg:
        head = _find_global_element(xsd_doc, sg)
        if head is not None:
            desc = _doc_text(head.xpath('./xs:annotation/xs:documentation', namespaces=XSD_NS))
            if desc:
                return sanitize_for_markdown(desc)

    return ''


def load_xsd_type_info(xsd_path):
    """Load type and cardinality information from XSD with full XPath paths"""
    try:
        # Ensure the path is absolute
        xsd_path = os.path.abspath(xsd_path)
        xsd_dir = os.path.dirname(xsd_path)
        print(f"Loading XSD from: {xsd_path}")
        print(f"XSD exists: {os.path.exists(xsd_path)}")

        # Process the main XSD file and all its imports/includes
        return _process_xsd_file(xsd_path, xsd_dir)
    except Exception as e:
        print(f"Error loading XSD: {e}")
        return {}


def _get_xsd_element_path(element):
    """Get the logical XPath path for an XSD element, ignoring groups, types, choices"""
    path_parts = []
    current = element

    while current is not None and current.tag != 'schema':
        tag = current.tag if not hasattr(current, 'tag') or not callable(current.tag) else str(current.tag)

        # Skip xs:annotation, xs:complexType, xs:simpleType, xs:group, xs:choice, xs:sequence, xs:extension, xs:restriction
        if tag.endswith('}annotation') or tag.endswith('}complexType') or tag.endswith('}simpleType') or \
           tag.endswith('}group') or tag.endswith('}choice') or tag.endswith('}sequence') or \
           tag.endswith('}extension') or tag.endswith('}restriction'):
            current = current.getparent()
            continue

        # For xs:element, get the name
        if tag.endswith('}element'):
            name = current.get('name') or current.get('ref', '').split(':')[-1]
            if name:
                path_parts.insert(0, name)

        current = current.getparent()

    return '/'.join(path_parts) if path_parts else None


def _build_xsd_element_paths(xsd_doc):
    """
    Build a map of element paths to their metadata from XSD

    Returns a dict where keys are full element paths (e.g., 'ServiceFrame/lines/Line')
    and values are the element metadata. Also adds entries keyed by element name alone.
    """
    xsd_path_map = {}

    # Find all elements in the XSD
    all_elements = xsd_doc.xpath('//xs:element', namespaces=XSD_NS)

    for element in all_elements:
        # Get the logical path for this element
        path = _get_xsd_element_path(element)
        if not path:
            continue

        # Get element metadata
        name = element.get('name') or element.get('ref', '').split(':')[-1]

        # Resolve type: direct @type, or from @ref'ed global element, or inline types
        elem_type = element.get('type', '')
        if not elem_type:
            ref = element.get('ref')
            if ref:
                ref_name = ref.split(':')[-1]
                ref_el = xsd_doc.xpath(f"//xs:element[@name='{ref_name}']", namespaces=XSD_NS)
                if ref_el:
                    elem_type = ref_el[0].get('type', '') or ''
                    # If referenced element also has inline type with extension/restriction, resolve it
                    if not elem_type:
                        ref_inline_ct = ref_el[0].find('xs:complexType', XSD_NS)
                        ref_inline_st = ref_el[0].find('xs:simpleType', XSD_NS)
                        if ref_inline_ct is not None:
                            elem_type = ref_inline_ct.get('name', '') or ''
                            # Check for extension or restriction with base attribute in referenced element
                            if not elem_type:
                                ref_complex_content = ref_inline_ct.find('xs:complexContent', XSD_NS)
                                if ref_complex_content is not None:
                                    ref_extension = ref_complex_content.find('xs:extension', XSD_NS)
                                    ref_restriction = ref_complex_content.find('xs:restriction', XSD_NS)
                                    if ref_extension is not None:
                                        base = ref_extension.get('base', '')
                                        if base and ':' in base:
                                            base = base.split(':')[-1]
                                        elem_type = base or ''
                                    elif ref_restriction is not None:
                                        base = ref_restriction.get('base', '')
                                        if base and ':' in base:
                                            base = base.split(':')[-1]
                                        elem_type = base or ''
                                # If still no type, check for simpleContent
                                if not elem_type:
                                    ref_simple_content = ref_inline_ct.find('xs:simpleContent', XSD_NS)
                                    if ref_simple_content is not None:
                                        ref_simple_ext = ref_simple_content.find('xs:extension', XSD_NS)
                                        ref_simple_rest = ref_simple_content.find('xs:restriction', XSD_NS)
                                        if ref_simple_ext is not None:
                                            base = ref_simple_ext.get('base', '')
                                            if base and ':' in base:
                                                base = base.split(':')[-1]
                                            elem_type = base or ''
                                        elif ref_simple_rest is not None:
                                            base = ref_simple_rest.get('base', '')
                                            if base and ':' in base:
                                                base = base.split(':')[-1]
                                            elem_type = base or ''
                        elif ref_inline_st is not None:
                            elem_type = ref_inline_st.get('name', '') or ''
                            # For simpleType, also check for restriction with base in referenced element
                            if not elem_type:
                                ref_restriction = ref_inline_st.find('xs:restriction', XSD_NS)
                                if ref_restriction is not None:
                                    base = ref_restriction.get('base', '')
                                    if base and ':' in base:
                                        base = base.split(':')[-1]
                                    elem_type = base or ''
        if not elem_type:
            inline_ct = element.find('xs:complexType', XSD_NS)
            inline_st = element.find('xs:simpleType', XSD_NS)
            if inline_ct is not None:
                elem_type = inline_ct.get('name', '') or ''
                # If no name, check for extension or restriction with base attribute
                if not elem_type:
                    # Look for complexContent/extension or complexContent/restriction
                    complex_content = inline_ct.find('xs:complexContent', XSD_NS)
                    if complex_content is not None:
                        extension = complex_content.find('xs:extension', XSD_NS)
                        restriction = complex_content.find('xs:restriction', XSD_NS)
                        if extension is not None:
                            base = extension.get('base', '')
                            if base and ':' in base:
                                base = base.split(':')[-1]
                            elem_type = base or ''
                        elif restriction is not None:
                            base = restriction.get('base', '')
                            if base and ':' in base:
                                base = base.split(':')[-1]
                            elem_type = base or ''
                    # If still no type, check for simpleContent
                    if not elem_type:
                        simple_content = inline_ct.find('xs:simpleContent', XSD_NS)
                        if simple_content is not None:
                            simple_ext = simple_content.find('xs:extension', XSD_NS)
                            simple_rest = simple_content.find('xs:restriction', XSD_NS)
                            if simple_ext is not None:
                                base = simple_ext.get('base', '')
                                if base and ':' in base:
                                    base = base.split(':')[-1]
                                elem_type = base or ''
                            elif simple_rest is not None:
                                base = simple_rest.get('base', '')
                                if base and ':' in base:
                                    base = base.split(':')[-1]
                                elem_type = base or ''
            elif inline_st is not None:
                elem_type = inline_st.get('name', '') or ''
                # For simpleType, also check for restriction with base
                if not elem_type:
                    restriction = inline_st.find('xs:restriction', XSD_NS)
                    if restriction is not None:
                        base = restriction.get('base', '')
                        if base and ':' in base:
                            base = base.split(':')[-1]
                        elem_type = base or ''
        # Strip namespace prefix if present
        if elem_type and ':' in elem_type:
            elem_type = elem_type.split(':')[-1]

        min_occurs = element.get('minOccurs', '1')
        max_occurs = element.get('maxOccurs', '1')

        # Get robust description
        description = get_xsd_documentation_for_element(element, xsd_doc)

        meta = {
            'type': elem_type,
            'min_occurs': min_occurs,
            'max_occurs': max_occurs,
            'description': description
        }

        # Store metadata at the full path (path already includes the element name)
        if path not in xsd_path_map:
            xsd_path_map[path] = meta

        # Also store under just the element name for fallback
        if name and name not in xsd_path_map:
            xsd_path_map[name] = meta

    return xsd_path_map


def _process_xsd_file(xsd_path, base_dir, processed_files=None):
    """Process an XSD file and all its imports/includes recursively

    Returns a dict mapping type and element names to their metadata, with a '_paths' key
    that maps full element paths to metadata dicts.
    """
    if processed_files is None:
        processed_files = set()

    # Avoid circular processing
    if xsd_path in processed_files:
        return {}
    processed_files.add(xsd_path)

    type_info = {}
    path_based_info = {}

    try:
        xsd_doc = etree.parse(xsd_path)
        xsd_root = xsd_doc.getroot()

        # Get the target namespace from the schema element
        target_namespace = xsd_root.get('targetNamespace')
        if not target_namespace:
            target_namespace = xsd_root.nsmap.get(None, '')

        ns = {
            '': target_namespace,
            'xs': 'http://www.w3.org/2001/XMLSchema'
        }

        print(f"Processing XSD with namespace: {target_namespace}")

        # Process imports first
        current_dir = os.path.dirname(xsd_path)
        for import_elem in xsd_root.findall('xs:import', namespaces=XSD_NS):
            schema_location = import_elem.get('schemaLocation')
            if schema_location:
                import_path = os.path.normpath(os.path.join(current_dir, schema_location))
                if os.path.exists(import_path):
                    print(f"Processing import: {import_path}")
                    imported_types = _process_xsd_file(import_path, base_dir, processed_files)
                    # Merge type_info (types/elements)
                    type_info.update({k: v for k, v in imported_types.items() if k != '_paths'})
                    # Merge path-based info correctly
                    for path, meta in imported_types.get('_paths', {}).items():
                        if path not in path_based_info:
                            path_based_info[path] = meta
                else:
                    print(f"Import not found: {import_path}")

        # Process includes
        for include_elem in xsd_root.findall('xs:include', namespaces=XSD_NS):
            schema_location = include_elem.get('schemaLocation')
            if schema_location:
                include_path = os.path.normpath(os.path.join(current_dir, schema_location))
                if os.path.exists(include_path):
                    print(f"Processing include: {include_path}")
                    included_types = _process_xsd_file(include_path, base_dir, processed_files)
                    type_info.update({k: v for k, v in included_types.items() if k != '_paths'})
                    # Merge path-based info correctly
                    for path, meta in included_types.get('_paths', {}).items():
                        if path not in path_based_info:
                            path_based_info[path] = meta
                else:
                    print(f"Include not found: {include_path}")

        # Build path-based element information for this document
        doc_path_map = _build_xsd_element_paths(xsd_doc)
        for path, meta in doc_path_map.items():
            if path not in path_based_info:
                path_based_info[path] = meta

        # Extract complex types
        for complex_type in xsd_root.findall('.//xs:complexType', namespaces=ns):
            name = complex_type.get('name')
            if name:
                type_info[name] = {'type': 'complex', 'elements': {}, 'description': ''}

                # Extract documentation/description
                annotation = complex_type.find('xs:annotation', namespaces=ns)
                if annotation is not None:
                    doc = annotation.find('xs:documentation', namespaces=ns)
                    if doc is not None:
                        type_info[name]['description'] = sanitize_for_markdown(doc.xpath('string(.)'))

                # Extract elements within this complex type
                for element in complex_type.findall('.//xs:element', namespaces=ns):
                    elem_name = element.get('name')
                    elem_type = element.get('type')
                    min_occurs = element.get('minOccurs', '1')
                    max_occurs = element.get('maxOccurs', '1')

                    if elem_name:
                        # Get element description robustly
                        elem_description = get_xsd_documentation_for_element(element, xsd_doc)
                        type_info[name]['elements'][elem_name] = {
                            'type': elem_type,
                            'min_occurs': min_occurs,
                            'max_occurs': max_occurs,
                            'description': elem_description
                        }

        # Extract simple types
        for simple_type in xsd_root.findall('.//xs:simpleType', namespaces=ns):
            name = simple_type.get('name')
            if name:
                type_info[name] = {'type': 'simple', 'description': ''}
                annotation = simple_type.find('xs:annotation', namespaces=ns)
                if annotation is not None:
                    doc = annotation.find('xs:documentation', namespaces=ns)
                    if doc is not None:
                        type_info[name]['description'] = sanitize_for_markdown(doc.xpath('string(.)'))

        # Extract top-level elements
        for element in xsd_root.findall('.//xs:element', namespaces=ns):
            name = element.get('name')
            elem_type = element.get('type')
            min_occurs = element.get('minOccurs', '1')
            max_occurs = element.get('maxOccurs', '1')

            if name:
                elem_description = get_xsd_documentation_for_element(element, xsd_doc)
                type_info[name] = {
                    'type': elem_type,
                    'min_occurs': min_occurs,
                    'max_occurs': max_occurs,
                    'element_type': 'top_level',
                    'description': elem_description
                }

        # Store path-based info in type_info for later use
        type_info['_paths'] = path_based_info

        return type_info
    except Exception as e:
        print(f"Error processing {xsd_path}: {e}")
        return {}

def get_element_metadata_from_xsd_by_path(xsd_doc, xml_path):
    """
    Resolve metadata for the bottom element of a partial XML path
    by searching the XSD with a descendant chain (//).

    Behavior:
    - Build a descendant chain where each segment matches xs:element with either @name or @ref
      (with or without a namespace prefix).
    - Take the first full-chain match in document order. If none, fall back to matching the last
      segment anywhere.
    - Extract type from @type; if missing, follow @ref to the referenced global xs:element and
      take its @type or inline type; if still missing, look for inline type on the occurrence;
      finally, if still unknown, look at substitutionGroup head's type.
    - minOccurs/maxOccurs are taken from the matched element occurrence.
    - description is obtained via get_xsd_documentation_for_element(element, xsd_doc).

    Args:
        xsd_doc: lxml.etree parsed XSD document (ElementTree or Element)
        xml_path: partial path like 'SiteFrame/connections/DefaultConnection'

    Returns:
        dict with keys: type, min_occurs, max_occurs, description
        or None if no matching element is found.
    """
    if xsd_doc is None or not xml_path:
        return None

    parts = [p for p in xml_path.split('/') if p]

    # 1) Prefer an exact chain where each step matches @name only (stricter, less ambiguous)
    strict_chain = "//" + "//".join([f"xs:element[@name='{p}']" for p in parts])
    matches = xsd_doc.xpath(strict_chain, namespaces=XSD_NS)

    # 2) If not found, allow @name or @ref (with optional ns prefix) at each step
    if not matches:
        flexible_chain = "//" + "//".join(
            [f"xs:element[@name='{p}' or @ref='{p}' or contains(@ref, ':{p}')]" for p in parts]
        )
        matches = xsd_doc.xpath(flexible_chain, namespaces=XSD_NS)

    # 3) Fallback: match the last segment anywhere
    if not matches:
        last = parts[-1]
        matches = xsd_doc.xpath(
            f"//xs:element[@name='{last}' or @ref='{last}' or contains(@ref, ':{last}')]",
            namespaces=XSD_NS
        )
        if not matches:
            return None

    element = matches[0]  # first match in document order

    # --- Resolve type ---
    elem_type = element.get('type') or ''

    # If no @type, follow @ref to global element and read its type or inline type
    if not elem_type:
        ref = element.get('ref')
        if ref:
            ref_name = ref.split(':')[-1]
            ref_el = xsd_doc.xpath(f"//xs:element[@name='{ref_name}']", namespaces=XSD_NS)
            if ref_el:
                ref_el = ref_el[0]
                elem_type = ref_el.get('type') or ''
                if not elem_type:
                    inline_ct = ref_el.find('xs:complexType', XSD_NS)
                    inline_st = ref_el.find('xs:simpleType', XSD_NS)
                    if inline_ct is not None:
                        elem_type = inline_ct.get('name') or ''
                    elif inline_st is not None:
                        elem_type = inline_st.get('name') or ''

    # If still no type, check inline types on the occurrence
    if not elem_type:
        inline_ct = element.find('xs:complexType', XSD_NS)
        inline_st = element.find('xs:simpleType', XSD_NS)
        if inline_ct is not None:
            elem_type = inline_ct.get('name') or ''
        elif inline_st is not None:
            elem_type = inline_st.get('name') or ''

    # Optional: if still no type, try substitutionGroup head
    if not elem_type:
        sg = element.get('substitutionGroup')
        if sg:
            head_name = sg.split(':')[-1]
            head_el = xsd_doc.xpath(f"//xs:element[@name='{head_name}']", namespaces=XSD_NS)
            if head_el:
                elem_type = head_el[0].get('type') or ''

    # Normalize type to local name
    if elem_type and ':' in elem_type:
        elem_type = elem_type.split(':')[-1]

    # --- Cardinality from this occurrence ---
    min_occurs = element.get('minOccurs', '1')
    max_occurs = element.get('maxOccurs', '1')

    # --- Description via the robust helper you trust ---
    description = get_xsd_documentation_for_element(element, xsd_doc)

    return {
        'type': elem_type if elem_type else 'unknown',
        'min_occurs': min_occurs,
        'max_occurs': max_occurs,
        'description': description
    }



def get_cardinality(min_occurs, max_occurs):
    """Convert min/max occurs to cardinality string"""
    if min_occurs == '0' and max_occurs == '1':
        return '0..1'
    elif min_occurs == '1' and max_occurs == '1':
        return '1..1'
    elif min_occurs == '0' and max_occurs == 'unbounded':
        return '0..*'
    elif min_occurs == '1' and max_occurs == 'unbounded':
        return '1..*'
    else:
        return f"{min_occurs}..{max_occurs}"


def get_xml_element_path(element):
    """Get the logical XPath path for an XML element, excluding document wrapper"""
    path_parts = []
    current = element

    while current is not None:
        # Get the local name of the element
        if hasattr(current, 'tag') and not isinstance(current, etree._Comment):
            try:
                name = etree.QName(current).localname
                if name:
                    # Skip document wrapper elements
                    if name in ['PublicationDelivery', 'dataObjects', 'CompositeFrame', 'frames', 'ResourceFrame', 'SiteFrame']:
                        if name == 'PublicationDelivery':
                            break
                        current = current.getparent()
                        continue
                    else:
                        path_parts.insert(0, name)
            except Exception:
                pass

        current = current.getparent()

        # Stop if we reach the root element (PublicationDelivery in templates)
        if current is not None and hasattr(current, 'tag'):
            try:
                root_name = etree.QName(current).localname
                if root_name == 'PublicationDelivery':
                    break
            except Exception:
                pass

    return '/'.join(path_parts) if path_parts else None


def search_xsd_files_for_element(base_dir, element_name):
    """Search all XSD files in the directory structure for a specific element"""
    return search_xsd_files_for_element_with_parent(base_dir, element_name, None)


def search_xsd_files_for_element_with_parent(base_dir, element_name, parent_type=None):
    """Search all XSD files in the directory structure for a specific element,
    optionally within a parent complex type context
    """
    namespaces = {'xs': 'http://www.w3.org/2001/XMLSchema'}

    for root, dirs, files in os.walk(base_dir):
        for file in files:
            if file.endswith('.xsd'):
                file_path = os.path.join(root, file)
                try:
                    parser = etree.XMLParser()
                    xsd_doc = etree.parse(file_path, parser)

                    elements = []

                    if parent_type:
                        complex_type_xpath = f"//xs:complexType[contains(@name, '{parent_type}')]//xs:element[@name='{element_name}']"
                        elements = xsd_doc.xpath(complex_type_xpath, namespaces=namespaces)

                        if not elements:
                            complex_type_xpath_ref = f"//xs:complexType[contains(@name, '{parent_type}')]//xs:element[@ref='{element_name}']"
                            elements = xsd_doc.xpath(complex_type_xpath_ref, namespaces=namespaces)

                            if not elements:
                                complex_type_xpath_ref_ns = f"//xs:complexType[contains(@name, '{parent_type}')]//xs:element[contains(@ref, ':{element_name}')]"
                                elements = xsd_doc.xpath(complex_type_xpath_ref_ns, namespaces=namespaces)

                        if not elements:
                            complex_type_xpath_no_ns = f"//*[local-name()='complexType' and contains(@name, '{parent_type}')]//*[local-name()='element' and @name='{element_name}']"
                            elements = xsd_doc.xpath(complex_type_xpath_no_ns)

                            if not elements:
                                complex_type_xpath_no_ns_ref = f"//*[local-name()='complexType' and contains(@name, '{parent_type}')]//*[local-name()='element' and @ref='{element_name}']"
                                elements = xsd_doc.xpath(complex_type_xpath_no_ns_ref)

                        if elements:
                            return file_path
                        else:
                            continue
                    else:
                        element_xpath = f"//xs:element[@name='{element_name}']"
                        elements = xsd_doc.xpath(element_xpath, namespaces=namespaces)

                        if not elements:
                            element_xpath_no_ns = f"//*[local-name()='element' and @name='{element_name}']"
                            elements = xsd_doc.xpath(element_xpath_no_ns)

                        if elements:
                            return file_path

                except Exception:
                    continue

    return None


def find_best_xsd_path_match(xsd_path_info, xml_path, element_name):
    """Find the best matching XSD path for a given XML path and element name.

    Only returns:
    - exact full path match, or
    - element-name-only fallback.
    Avoids returning container paths that would leak container type.
    """
    if not xsd_path_info or not xml_path:
        return None

    # Exact match
    if xml_path in xsd_path_info:
        return xml_path, xsd_path_info[xml_path]

    # Element-only fallback
    elem_only = xml_path.split('/')[-1]
    if elem_only in xsd_path_info:
        return elem_only, xsd_path_info[elem_only]

    return None


def get_element_metadata(xsd_path, element_name, parent_type=None):
    """Extract detailed metadata for an element from XSD using XPath with substitution group support."""
    try:
        parser = etree.XMLParser()
        xsd_doc = etree.parse(xsd_path, parser)
        namespaces = {'xs': 'http://www.w3.org/2001/XMLSchema'}

        element = None

        # If parent_type is specified, try to find the element within that complex type first
        if parent_type:
            clean_parent_type = None
            parts = parent_type.split('|')
            for part in parts:
                if part and not part.startswith('MULTILINGUAL_'):
                    clean_parent_type = part
                    break
            if not clean_parent_type:
                clean_parent_type = parent_type

            # Try exact match first
            complex_type_xpath = f"//xs:complexType[@name='{clean_parent_type}']//xs:element[@name='{element_name}']"
            element = xsd_doc.xpath(complex_type_xpath, namespaces=namespaces)

            # Also try with ref attribute
            if not element:
                complex_type_xpath_ref = f"//xs:complexType[@name='{clean_parent_type}']//xs:element[@ref='{element_name}']"
                element = xsd_doc.xpath(complex_type_xpath_ref, namespaces=namespaces)
                if not element:
                    complex_type_xpath_ref_ns = f"//xs:complexType[@name='{clean_parent_type}']//xs:element[contains(@ref, ':{element_name}')]"
                    element = xsd_doc.xpath(complex_type_xpath_ref_ns, namespaces=namespaces)

            if not element:
                complex_type_xpath_no_ns = f"//*[local-name()='complexType' and @name='{clean_parent_type}']//*[local-name()='element' and @name='{element_name}']"
                element = xsd_doc.xpath(complex_type_xpath_no_ns)

                if not element:
                    complex_type_xpath_no_ns_ref = f"//*[local-name()='complexType' and @name='{clean_parent_type}']//*[local-name()='element' and @ref='{element_name}']"
                    element = xsd_doc.xpath(complex_type_xpath_no_ns_ref)

            if not element:
                complex_type_xpath_contains = f"//xs:complexType[contains(@name, '{clean_parent_type}')]//xs:element[@name='{element_name}']"
                element = xsd_doc.xpath(complex_type_xpath_contains, namespaces=namespaces)

                if not element:
                    complex_type_xpath_contains_ref = f"//xs:complexType[contains(@name, '{clean_parent_type}')]//xs:element[@ref='{element_name}']"
                    element = xsd_doc.xpath(complex_type_xpath_contains_ref, namespaces=namespaces)

            if not element:
                version_patterns = [
                    f"{clean_parent_type}_VersionStructure",
                    f"{clean_parent_type}VesionStructure",
                    f"{clean_parent_type}_Structure",
                    f"{clean_parent_type}_Type"
                ]
                for pattern in version_patterns:
                    if not element:
                        complex_type_xpath_pattern = f"//xs:complexType[@name='{pattern}']//xs:element[@name='{element_name}']"
                        element = xsd_doc.xpath(complex_type_xpath_pattern, namespaces=namespaces)
                        if not element:
                            complex_type_xpath_pattern_ref = f"//xs:complexType[@name='{pattern}']//xs:element[@ref='{element_name}']"
                            element = xsd_doc.xpath(complex_type_xpath_pattern_ref, namespaces=namespaces)
                        if element:
                            break

            if not element:
                rel_structure_parent = f"{clean_parent_type}_RelStructure"
                complex_type_xpath_rel = f"//xs:complexType[@name='{rel_structure_parent}']//xs:element[@ref='{element_name}']"
                element = xsd_doc.xpath(complex_type_xpath_rel, namespaces=namespaces)

                if not element:
                    complex_type_xpath_rel_contains = f"//xs:complexType[contains(@name, '{rel_structure_parent}')]//xs:element[@ref='{element_name}']"
                    element = xsd_doc.xpath(complex_type_xpath_rel_contains, namespaces=namespaces)

                if not element:
                    complex_type_xpath_rel_name = f"//xs:complexType[@name='{rel_structure_parent}']//xs:element[@name='{element_name}']"
                    element = xsd_doc.xpath(complex_type_xpath_rel_name, namespaces=namespaces)

                if not element:
                    complex_type_xpath_rel_name_contains = f"//xs:complexType[contains(@name, '{rel_structure_parent}')]//xs:element[@name='{element_name}']"
                    element = xsd_doc.xpath(complex_type_xpath_rel_name_contains, namespaces=namespaces)

            if not element:
                complex_type_xpath_contains_no_ns = f"//*[local-name()='complexType' and contains(@name, '{clean_parent_type}')]//*[local-name()='element' and @name='{element_name}']"
                element = xsd_doc.xpath(complex_type_xpath_contains_no_ns)

            # If not found in this file with parent context, search other XSD files with the parent context
            if not element:
                base_dir = os.path.dirname(os.path.abspath(xsd_path))
                found_in_file = search_xsd_files_for_element_with_parent(base_dir, element_name, clean_parent_type)
                if found_in_file is not None:
                    xsd_doc = etree.parse(found_in_file, parser)
                    namespaces = {'xs': 'http://www.w3.org/2001/XMLSchema'}
                    complex_type_xpath = f"//xs:complexType[contains(@name, '{clean_parent_type}')]//xs:element[@name='{element_name}']"
                    element = xsd_doc.xpath(complex_type_xpath, namespaces=namespaces)

                    if not element:
                        complex_type_xpath_ref = f"//xs:complexType[contains(@name, '{clean_parent_type}')]//xs:element[@ref='{element_name}']"
                        element = xsd_doc.xpath(complex_type_xpath_ref, namespaces=namespaces)

                        if not element:
                            complex_type_xpath_ref_ns = f"//xs:complexType[contains(@name, '{clean_parent_type}')]//xs:element[contains(@ref, ':{element_name}')]"
                            element = xsd_doc.xpath(complex_type_xpath_ref_ns, namespaces=namespaces)

                    if not element:
                        complex_type_xpath_no_ns = f"//*[local-name()='complexType' and contains(@name, '{clean_parent_type}')]//*[local-name()='element' and @name='{element_name}']"
                        element = xsd_doc.xpath(complex_type_xpath_no_ns)

                        if not element:
                            complex_type_xpath_no_ns_ref = f"//*[local-name()='complexType' and contains(@name, '{clean_parent_type}')]//*[local-name()='element' and @ref='{element_name}']"
                            element = xsd_doc.xpath(complex_type_xpath_no_ns_ref)

                    if element:
                        xsd_path = found_in_file  # Update path for later use

            # If parent_type was specified but still not found, do not fallback to generic
            if not element:
                return None
        else:
            # No parent_type specified, do a generic search
            element_xpath = f"//xs:element[@name='{element_name}']"
            element = xsd_doc.xpath(element_xpath, namespaces=namespaces)

            if not element:
                base_dir = os.path.dirname(os.path.abspath(xsd_path))
                found_in_file = search_xsd_files_for_element_with_parent(base_dir, element_name, None)
                if found_in_file is not None:
                    xsd_doc = etree.parse(found_in_file, parser)
                    namespaces = {'xs': 'http://www.w3.org/2001/XMLSchema'}
                    element_xpath = f"//xs:element[@name='{element_name}']"
                    element = xsd_doc.xpath(element_xpath, namespaces=namespaces)

                    if not element:
                        element_xpath_no_ns = f"//*[local-name()='element' and @name='{element_name}']"
                        element = xsd_doc.xpath(element_xpath_no_ns)
            if not element:
                return None

        element = element[0]

        # Cardinality
        min_occurs = element.get('minOccurs', '1')
        max_occurs = element.get('maxOccurs', '1')
        cardinality = get_cardinality(min_occurs, max_occurs)

        # Adjust for _RelStructure or parent with unbounded occurrence
        actual_parent_complex_type = None
        parent_elem = element.getparent()
        if parent_elem is not None:
            parent_max_occurs = parent_elem.get('maxOccurs')
            if parent_max_occurs == 'unbounded':
                cardinality = '0..*'
            elif parent_elem.tag.endswith('complexType') or etree.QName(parent_elem).localname == 'complexType':
                actual_parent_complex_type = parent_elem.get('name')

        if parent_type and '_RelStructure' in parent_type:
            cardinality = '0..*'
        elif actual_parent_complex_type and '_RelStructure' in actual_parent_complex_type:
            cardinality = '0..*'
        elif parent_type:
            base_dir = os.path.dirname(os.path.abspath(xsd_path))
            # quick scan across xsds for matching complex types containing _RelStructure
            for root, dirs, files in os.walk(base_dir):
                for file in files:
                    if file.endswith('.xsd'):
                        file_path = os.path.join(root, file)
                        try:
                            doc = etree.parse(file_path, parser)
                            ct_match = doc.xpath(
                                f"//xs:complexType[contains(@name, '{parent_type}') and contains(@name, '_RelStructure')]",
                                namespaces=namespaces
                            )
                            if ct_match:
                                cardinality = '0..*'
                                break
                        except Exception:
                            continue

        # Get type (follow ref and substitutionGroup if needed)
        element_type = "unknown"
        current_element = element
        visited_elements = set()

        if current_element.get('ref') and not current_element.get('type'):
            ref_name = current_element.get('ref').split(':')[-1]
            ref_element_xpath = f"//xs:element[@name='{ref_name}']"
            ref_element = xsd_doc.xpath(ref_element_xpath, namespaces=namespaces)
            if not ref_element:
                ref_element_xpath_no_ns = f"//*[local-name()='element' and @name='{ref_name}']"
                ref_element = xsd_doc.xpath(ref_element_xpath_no_ns)
            if ref_element:
                current_element = ref_element[0]

        while current_element is not None and current_element.get('name') not in visited_elements:
            visited_elements.add(current_element.get('name'))

            type_attr = current_element.get('type')
            if type_attr:
                element_type = type_attr.split(':')[-1]
                break

            simple_type = current_element.find('xs:simpleType', namespaces)
            complex_type = current_element.find('xs:complexType', namespaces)

            if simple_type is None:
                simple_type = current_element.find('simpleType')
            if complex_type is None:
                complex_type = current_element.find('complexType')

            if simple_type is not None:
                simple_type_name = simple_type.get('name')
                element_type = simple_type_name if simple_type_name else "inline simpleType"
                break
            elif complex_type is not None:
                complex_type_name = complex_type.get('name')
                element_type = complex_type_name if complex_type_name else element.get('name')
                break

            substitution_group = current_element.get('substitutionGroup')
            if substitution_group:
                head_name = substitution_group.split(':')[-1]
                head_xpath = f"//xs:element[@name='{head_name}']"
                head_element = xsd_doc.xpath(head_xpath, namespaces=namespaces)
                if head_element:
                    current_element = head_element[0]
                    continue

            break

        # Get robust description for this element
        description = get_xsd_documentation_for_element(element, xsd_doc)

        return {
            'cardinality': cardinality,
            'type': element_type,
            'description': sanitize_for_markdown(description or "")
        }

    except Exception as e:
        print(f"Warning: Could not extract metadata for {element_name}: {e}")
        return None


def is_container_parent(parent_type, element, xsd_type_info=None):
    """
    Detect if the given parent_type represents a container for the element.
    Containers are recognizable by element names starting with lowercase letters.
    """
    if not parent_type:
        return False

    # Extract actual parent name from parent_type (handle MULTILINGUAL_ prefix)
    actual_parent_name = None
    parts = parent_type.split('|')
    for part in parts:
        if part and not part.startswith('MULTILINGUAL_'):
            actual_parent_name = part
            break

    if not actual_parent_name:
        return False

    # Check for _RelStructure pattern
    if '_RelStructure' in parent_type or '_RelStructure' in actual_parent_name:
        return True

    # Check if parent name starts with lowercase letter (container pattern)
    if actual_parent_name[0].islower():
        # Check if element is the singular form of parent
        if actual_parent_name.endswith('s') and element == actual_parent_name[:-1]:
            return True

        # Known container patterns
        known_containers = ['quays', 'stopPlaces', 'facilities', 'privateCodes',
                            'alternativeNames', 'alternativeTexts', 'names', 'descriptions',
                            'texts', 'localServices', 'groupsOfLines', 'lines', 'notices',
                            'timeDemandType', 'timingLinks', 'journeyPatterns', 'stopAssignment',
                            'connections', 'scheduledStopPoints', 'destinationDisplays']

        if actual_parent_name in known_containers:
            return True

    return False


def get_container_cardinality(parent_type, element, current_card, xsd_type_info=None):
    """
    Get the appropriate cardinality for container elements.
    Returns the cardinality if it's a container, otherwise returns current_card unchanged.
    """
    if not is_container_parent(parent_type, element, xsd_type_info):
        return current_card

    # For containers, child elements should be 0..* or 1..*
    if current_card.startswith('0..*') or current_card.startswith('1..*'):
        return current_card

    return '0..*'


def enrich_from_xsd(item, xsd_doc, xsd_type_info, xsd_path):
    """
    Consolidated enrichment of element metadata (cardinality, type, description) from XSD sources.
    Tries path-based, then context-aware, then generic fallbacks, and applies container overrides.
    """
    element = item['element']
    card = item['card']
    xsd_type = item['type']
    description = item['description']
    parent_type = item.get('parent_type')
    xml_path = item.get('xml_path')

    # 1) Path-based lookup
    path_based = None
    if xsd_doc is not None and xml_path:
        path_based = get_element_metadata_from_xsd_by_path(xsd_doc, xml_path)
    if not path_based and xml_path:
        xsd_paths = xsd_type_info.get('_paths', {})
        match = find_best_xsd_path_match(xsd_paths, xml_path, element)
        if match:
            _, path_meta = match
            path_based = path_meta

    if path_based:
        if not card or card == '1..1':
            card = get_cardinality(path_based.get('min_occurs', '1'), path_based.get('max_occurs', '1'))
        # Only take non-empty, meaningful type from path-based metadata
        pb_type = path_based.get('type')
        if (not xsd_type or xsd_type == 'unknown') and pb_type:
            xsd_type = pb_type
        if not description:
            description = path_based.get('description', description)

    # 2) Context-aware fallback: run if we still lack type or description, regardless of path_based
    if xsd_path and ((not path_based) or (not xsd_type or xsd_type == 'unknown') or not description):
        meta = get_element_metadata(xsd_path, element, parent_type)
        if meta:
            if not card or card == '1..1':
                card = meta.get('cardinality', card)
            if not xsd_type or xsd_type == 'unknown':
                xsd_type = meta.get('type', xsd_type)
            if not description:
                description = meta.get('description', description)

    # 2b) Last-resort: if type still unknown/empty, try taking just the type from name-keyed xsd_type_info
    if (not xsd_type or xsd_type == 'unknown') and element in xsd_type_info:
        fallback_type = xsd_type_info[element].get('type')
        if fallback_type:
            xsd_type = fallback_type

    # 3) Generic xsd_type_info as fallback for card and description when safe
    xsd_info = xsd_type_info.get(element, {})
    if not parent_type and not path_based and xsd_info:
        if not description:
            description = xsd_info.get('description', description)
        if (not card or card == '1..1') and 'min_occurs' in xsd_info and 'max_occurs' in xsd_info:
            card = get_cardinality(xsd_info['min_occurs'], xsd_info['max_occurs'])
        if not xsd_type or xsd_type == 'unknown':
            xsd_type = xsd_info.get('type', xsd_type)
    if parent_type and xsd_info:
        if (not card or card == '1..1') and 'min_occurs' in xsd_info and 'max_occurs' in xsd_info:
            card = get_cardinality(xsd_info['min_occurs'], xsd_info['max_occurs'])
        if not xsd_type or xsd_type == 'unknown':
            xsd_type = xsd_info.get('type', xsd_type)

    # 4) Container/multilingual overrides
    multilingual_element_names = ['Text', 'Description', 'Name', 'ShortName', 'Label', 'Title', 'Subtitle']
    if element in multilingual_element_names and parent_type:
        actual_parent = next((p for p in parent_type.split('|') if p and not p.startswith('MULTILINGUAL_')), None)
        if actual_parent in multilingual_element_names:
            card = '0..*'
    card = get_container_cardinality(parent_type, element, card, xsd_type_info)

    return card, (xsd_type if xsd_type else 'unknown'), description


def parse_template_file(file_path, xsd_type_info):
    """Parse a single template file and extract documentation"""
    try:
        doc = etree.parse(file_path)
        root = doc.getroot()

        # Register namespace if present
        nsmap = root.nsmap
        ns = {}
        if None in nsmap:
            default_ns = nsmap[None]
            ns['default'] = default_ns

        # Find ch-root comments
        comments = root.xpath('//comment()', namespaces=ns)

        root_element = None

        for comment in comments:
            text = comment.text.strip() if comment.text else ''
            if 'ch-root' in text or 'ch-root' == text:
                root_element = comment.getparent()
                break

        # If no ch-root found, check if this is a ch-profile template
        has_ch_see = any('ch-see' in (comment.text.strip() if comment.text else '')
                         for comment in comments)

        if root_element is None and has_ch_see:
            root_element = root

        if root_element is None:
            print(f"Warning: No ch-root found in {file_path}")
            return None

        elements_data = []

        common_ancestor = root_element
        processed_elements = set()

        def get_preceding_comments(element):
            """Get comments that appear immediately before this element (sibling comments)"""
            parent = element.getparent()
            if parent is None:
                return []

            comments_list = []
            children = list(parent)
            elem_index = -1
            for i, child in enumerate(children):
                if child is element:
                    elem_index = i
                    break

            if elem_index > 0:
                for i in range(elem_index - 1, -1, -1):
                    child = children[i]
                    if isinstance(child, etree._Comment):
                        comments_list.insert(0, child)
                    else:
                        break

            return comments_list

        def process_element(element, level=0, parent_type_context=None, xml_path=None):
            """Recursively process an element and its children"""
            if hasattr(element, 'tag'):
                elem_name = etree.QName(element).localname
            else:
                return
            elem_id = element.get('id')

            if xml_path is None:
                xml_path = get_xml_element_path(element)

            multilingual_element_names = ['Text', 'Description', 'Name', 'ShortName', 'Label', 'Title', 'Subtitle']

            # Unique key
            if elem_name in multilingual_element_names and element.get('lang'):
                elem_key = f"{elem_name}_{element.get('lang')}_{elem_id}" if elem_id else f"{elem_name}_{element.get('lang')}"
            else:
                elem_key = f"{elem_name}_{elem_id}" if elem_id else elem_name

            if element.get('ref'):
                elem_key = f"{elem_key}_ref={element.get('ref')}"
            elem_key = f"{elem_key}_L{level}"

            if elem_key in processed_elements:
                return
            processed_elements.add(elem_key)

            # Comments and flags
            usage = 'ignored'
            note = ''
            is_referenced = False
            see_reference = None

            is_multilingual_child = 'MULTILINGUAL_PARENT' in (parent_type_context or '')

            child_comments = element.xpath('comment()')
            preceding_comments = get_preceding_comments(element)

            is_deprecated = False
            attrs_list = []
            has_ch_root = False

            if elem_name in multilingual_element_names and element.get('lang'):
                attrs_list.append('lang')

            for comment in child_comments:
                if comment.text:
                    comment_text = comment.text.strip()
                    if comment_text == 'ch-root' or 'ch-root' in comment_text:
                        has_ch_root = True
                        if parent_type_context is None:
                            parent_type_context = elem_name
                    elif comment_text.startswith('ch-usage:'):
                        usage = comment_text.replace('ch-usage:', '').strip()
                    elif comment_text.startswith('ch-note:'):
                        note = comment_text.replace('ch-note:', '').strip()
                    elif comment_text == 'ch-see':
                        is_referenced = True
                    elif comment_text.startswith('ch-see:'):
                        is_referenced = True
                        see_reference = comment_text.replace('ch-see:', '').strip()
                    elif comment_text == 'ch-deprecated':
                        is_deprecated = True
                    elif comment_text.startswith('ch-attrs:'):
                        attrs_str = comment_text.replace('ch-attrs:', '').strip()
                        attrs_list = [attr.strip() for attr in attrs_str.split()]

            for comment in preceding_comments:
                if comment.text:
                    comment_text = comment.text.strip()
                    if usage == 'ignored' or usage == '':
                        if comment_text.startswith('ch-usage:'):
                            usage = comment_text.replace('ch-usage:', '').strip()
                        elif comment_text.startswith('ch-note:'):
                            if note:
                                note = f"{comment_text.replace('ch-note:', '').strip()} {note}"
                            else:
                                note = comment_text.replace('ch-note:', '').strip()
                        elif comment_text == 'ch-see':
                            is_referenced = True
                        elif comment_text.startswith('ch-see:'):
                            is_referenced = True
                            see_reference = comment_text.replace('ch-see:', '').strip()
                        elif comment_text == 'ch-deprecated':
                            is_deprecated = True
                        elif comment_text.startswith('ch-attrs:'):
                            attrs_str = comment_text.replace('ch-attrs:', '').strip()
                            new_attrs = [attr.strip() for attr in attrs_str.split()]
                            for attr in new_attrs:
                                if attr not in attrs_list:
                                    attrs_list.append(attr)

            # Multilingual heuristics
            is_multilingual = False
            has_child_text_elements = False
            has_text_content = False
            for child in element:
                if isinstance(child, etree._Comment):
                    continue
                if isinstance(child, etree._Element):
                    child_name = etree.QName(child).localname
                    if child_name == 'Text':
                        has_child_text_elements = True
                else:
                    if hasattr(child, 'strip') and child.strip():
                        has_text_content = True
            is_multilingual = has_text_content and has_child_text_elements

            if elem_name in multilingual_element_names:
                parent = element.getparent()
                if parent is not None:
                    parent_name = etree.QName(parent).localname
                    if parent_name in multilingual_element_names:
                        is_multilingual = True

            # XSD info (basic; detailed enrichment later in markdown generation)
            xsd_info = xsd_type_info.get(elem_name, {})
            card = '1..1'
            xsd_type = 'unknown'

            if xsd_info:
                min_occurs = xsd_info.get('min_occurs', '1')
                max_occurs = xsd_info.get('max_occurs', '1')
                card = get_cardinality(min_occurs, max_occurs)
                xsd_type = xsd_info.get('type', 'unknown')
                print(f"{elem_name}: {xsd_type}")
            else:
                # Heuristics when XSD info not available
                print(f"use heuristics on {elem_name}")
                actual_parent_name = None
                if parent_type_context:
                    parts = parent_type_context.split('|')
                    for part in parts:
                        if part and not part.startswith('MULTILINGUAL_'):
                            actual_parent_name = part
                            break

                is_container_of_multilingual = False
                if elem_name in multilingual_element_names:
                    for child in element:
                        if hasattr(child, 'tag'):
                            try:
                                child_name = etree.QName(child).localname
                                if child_name in multilingual_element_names:
                                    is_container_of_multilingual = True
                                    break
                            except Exception:
                                pass

                if elem_name in multilingual_element_names and (is_container_of_multilingual or (actual_parent_name and actual_parent_name in multilingual_element_names)):
                    card = '0..*'

                if actual_parent_name:
                    if actual_parent_name and elem_name and len(actual_parent_name) > len(elem_name):
                        container_patterns = [
                            ('privateCodes', 'PrivateCode'),
                            ('alternativeTexts', 'AlternativeText'),
                            ('names', 'Name'),
                            ('descriptions', 'Description'),
                            ('texts', 'Text'),
                        ]
                        for container, child_type in container_patterns:
                            if actual_parent_name == container and elem_name == child_type:
                                card = '0..*'
                                break

            # Determine sub level markers - use + for indentation
            sub_markers = ''
            if level > 1:
                sub_markers = '+' * (level - 1)

            # Description is filled later from XSD; keep it empty here
            description = ''

            # Multilingual behavior: description kept empty; note contains ch-note only
            if elem_name in multilingual_element_names:
                description = ''

            if is_deprecated:
                if note:
                    note += ' NOTE: DEPRECATED'
                else:
                    note = 'NOTE: DEPRECATED'

            # Skip ignored/forbidden unless root or multilingual with explicit usage
            is_multilingual_with_usage = elem_name in multilingual_element_names and usage.lower() in ['optional', 'expected', 'mandatory']

            if usage.lower() in ['forbidden', 'ignored'] and not has_ch_root and not is_multilingual_with_usage:
                if not is_referenced:
                    for child in element:
                        if isinstance(child, etree._Element) and not isinstance(child, etree._Comment):
                            child_name = etree.QName(child).localname
                            child_xml_path = f"{xml_path}/{child_name}" if xml_path else child_name
                            process_element(child, level + 1, parent_type_context, child_xml_path)
                return

            # Display element name as-is
            display_element_name = elem_name

            elements_data.append({
                'sub': sub_markers,
                'element': display_element_name,
                'usage': usage,
                'card': card,
                'type': xsd_type,
                'description': description,
                'note': note,
                'is_referenced': is_referenced,
                'referenced_name': see_reference or elem_name,
                'level': level,
                'attributes': attrs_list,
                'is_deprecated': is_deprecated,
                'parent_type': parent_type_context,
                'xml_path': xml_path
            })

            # Process children unless referenced
            if not is_referenced:
                child_parent_type = elem_name
                if xsd_info and 'type' in xsd_info and xsd_info['type']:
                    xsd_type_name = xsd_info['type']
                    if isinstance(xsd_type_name, str) and xsd_type_name.endswith('_RelStructure'):
                        child_parent_type = xsd_type_name
                    elif elem_name and elem_name[0].islower() and xsd_type_name:
                        potential_rel_type = f"{elem_name}_RelStructure"
                        if potential_rel_type in xsd_type_info:
                            child_parent_type = potential_rel_type

                is_current_multilingual_parent = elem_name in multilingual_element_names and element.get('lang')

                for child in element:
                    if isinstance(child, etree._Comment):
                        continue
                    if not isinstance(child, etree._Element):
                        continue

                    child_name = etree.QName(child).localname
                    child_is_text = (child_name == 'Text')
                    child_is_multilingual_child = (is_multilingual or is_current_multilingual_parent) and child_is_text

                    if child_is_text and elem_name in multilingual_element_names:
                        child_is_multilingual_child = True

                    propagated_parent_type = child_parent_type
                    if child_is_multilingual_child:
                        propagated_parent_type = f"{propagated_parent_type}|MULTILINGUAL_PARENT" if propagated_parent_type else "MULTILINGUAL_PARENT"

                    child_xml_path = f"{xml_path}/{child_name}" if xml_path else child_name
                    process_element(child, level + 1, propagated_parent_type, child_xml_path)

        # Process starting from common ancestor
        root_element_name = None
        if hasattr(root_element, 'tag') and not isinstance(root_element, etree._Comment):
            root_element_name = etree.QName(root_element).localname

        if hasattr(common_ancestor, 'tag') and not isinstance(common_ancestor, etree._Comment):
            enhanced_root_context = root_element_name
            if root_element_name:
                root_xsd_info = xsd_type_info.get(root_element_name, {})
                if root_xsd_info and 'type' in root_xsd_info and root_xsd_info['type']:
                    enhanced_root_context = root_xsd_info['type']
            process_element(common_ancestor, parent_type_context=enhanced_root_context)

        return elements_data

    except Exception as e:
        print(f"Error processing {file_path}: {e}")
        return None


def generate_markdown_table(data, filename, xsd_path: str, xsd_type_info):
    """Generate markdown table from parsed data"""
    if not data:
        return ''

    # Load the XSD document for path-based element lookup
    xsd_doc = None
    if xsd_path and os.path.exists(xsd_path):
        try:
            xsd_doc = etree.parse(xsd_path)
        except Exception as e:
            print(f"Warning: Could not parse XSD {xsd_path}: {e}")

    # Separate data into top-level elements, attributes, and child elements
    top_level_elements = []
    attributes = []
    child_elements = []

    for item in data:
        if item['level'] == 0:
            top_level_elements.append(item)
        elif item['element'].startswith('@'):
            attributes.append(item)
        else:
            child_elements.append(item)

    # Extract root element name, ch-note, and attributes for caption and pre-table text
    root_element_name = None
    root_note = ""
    root_attributes = []
    for item in top_level_elements:
        if item['level'] == 0:
            root_element_name = item['element']
            root_note = item.get('note', '')
            root_attributes = item.get('attributes', [])
            break

    markdown = f"# {filename}\n\n"

    if root_note:
        markdown += f"{sanitize_for_markdown(root_note)}\n\n"

    if root_element_name:
        markdown += f"*Table: {root_element_name}*\n\n"

    markdown += "| Sub | Element | Usage | Card | Type | Description | Note |\n"
    markdown += "|-----|---------|-------|------|------|-------------|------|\n"

    # Add root element attributes if present (they should appear at the top of the table)
    if root_attributes:
        for attr in root_attributes:
            attr_usage = 'mandatory'
            attr_card = '1..1'
            attr_type = 'xsd:string'
            attr_desc = sanitize_for_markdown(f"Attribute {attr}")
            markdown += f"|  | @{attr} | {attr_usage} | {attr_card} | {attr_type} | {attr_desc} | |\n"

    # Process non-root top-level elements
    for item in top_level_elements:
        if item['level'] == 0:
            continue

        sub = item['sub']
        element = item['element']
        usage = item['usage']
        card = item['card']
        xsd_type = item['type']
        description = item['description']
        note = item.get('note', '')

        # Enrich from XSD
        if element == "Line":
            print("here we are")
        item_copy = dict(item)
        card, xsd_type, description = enrich_from_xsd(item_copy, xsd_doc, xsd_type_info, xsd_path)

        display_type = xsd_type if xsd_type and xsd_type != 'None' else 'unknown'
        description = sanitize_for_markdown(description)
        display_note = sanitize_for_markdown(note)
        markdown += f"| {sub} | {element} | {usage} | {card} | {display_type} | {description} | {display_note} |\n"

    # Process attributes
    for item in attributes:
        sub = item['sub']
        element = item['element']
        usage = item['usage']
        card = item['card']
        xsd_type = item['type']
        description = item['description']
        note = item.get('note', '')
        display_type = xsd_type if xsd_type and xsd_type != 'None' else 'unknown'
        description = sanitize_for_markdown(description)
        note = sanitize_for_markdown(note)

        markdown += f"| {sub} | {element} | {usage} | {card} | {display_type} | {description} | {note} |\n"

    # Process child elements
    for item in child_elements:
        sub = item['sub']
        element = item['element']
        usage = item['usage']
        card = item['card']
        xsd_type = item['type']
        description = item['description']
        note = item.get('note', '')

        # Enrich from XSD
        item_copy = dict(item)
        card, xsd_type, description = enrich_from_xsd(item_copy, xsd_doc, xsd_type_info, xsd_path)

        # Additional known container patterns for multilingual elements
        parent_type = item.get('parent_type')
        if parent_type:
            actual_parent_name = None
            parts = parent_type.split('|')
            for part in parts:
                if part and not part.startswith('MULTILINGUAL_'):
                    actual_parent_name = part
                    break

            if actual_parent_name:
                container_patterns = [
                    ('privateCodes', 'PrivateCode'),
                    ('alternativeTexts', 'AlternativeText'),
                    ('names', 'Name'),
                    ('descriptions', 'Description'),
                    ('texts', 'Text'),
                ]
                for container, child_type in container_patterns:
                    if actual_parent_name == container and element == child_type:
                        card = '0..*'
                        break

        if element.endswith('Ref') and 'versionRef=' in description:
            description = description.replace('versionRef=', 'version=')

        if item['is_referenced']:
            link_name = item['referenced_name']
            element = f"[{element}]({link_name}.md)"

        display_note = note if note else ''
        display_type = xsd_type if xsd_type and xsd_type != 'None' else 'unknown'
        description = sanitize_for_markdown(description)
        display_note = sanitize_for_markdown(display_note)
        markdown += f"| {sub} | {element} | {usage} | {card} | {display_type} | {description} | {display_note} |\n"

        if item['attributes']:
            for attr in item['attributes']:
                attr_usage = 'mandatory'
                attr_card = '1..1'
                attr_type = 'xsd:string'
                attr_desc = sanitize_for_markdown(f"Attribute {attr}")

                markdown += f"| {sub}+ | @{attr} | {attr_usage} | {attr_card} | {attr_type} | {attr_desc} | |\n"

    return markdown


def check_referenced_files_exist(data, template_dir):
    """Check if all referenced files exist and warn if not"""
    missing_files = []

    for item in data:
        if item['is_referenced'] and item['referenced_name']:
            ref_file = f"{item['referenced_name']}.xml"
            ref_path = os.path.join(template_dir, ref_file)
            if not os.path.exists(ref_path):
                missing_files.append(ref_file)

    if missing_files:
        print(f"Warning: Missing referenced files: {', '.join(missing_files)}")
        return False
    return True


def build_markdown_tables(input_path: str, output_path: str, xsd_path: str):
    # Load XSD type information
    print(f"Loading XSD from {xsd_path}")
    xsd_type_info = load_xsd_type_info(xsd_path)
    print(f"Loaded {len(xsd_type_info)} type definitions")

    # Create output directory
    os.makedirs(output_path, exist_ok=True)

    # Handle both directory and single file input
    if os.path.isfile(input_path) and input_path.endswith('.xml'):
        xml_files = [os.path.basename(input_path)]
        is_single_file = True
        base_dir = os.path.dirname(input_path) or '.'
    else:
        xml_files = [f for f in os.listdir(input_path)
                     if f.endswith('.xml') and not f.startswith(('ch-profile', 'ch-profile_'))]
        is_single_file = False
        base_dir = input_path

    for xml_file in xml_files:
        if xml_file.startswith(('ch-profile', 'ch-profile_')):
            print(f"Skipping ch-profile file: {xml_file}")
            continue

        print(f"Processing {xml_file}")
        file_path = os.path.join(base_dir, xml_file) if not is_single_file else input_path

        # Parse template
        data = parse_template_file(file_path, xsd_type_info)

        if data:
            # Check for missing referenced files (only for directory mode)
            if not is_single_file:
                check_referenced_files_exist(data, input_path)

            # Generate markdown filename
            md_filename = os.path.splitext(xml_file)[0] + '.md'
            md_path = os.path.join(output_path, md_filename)

            # Generate markdown content
            element_name = os.path.splitext(xml_file)[0]
            markdown_content = generate_markdown_table(data, element_name, xsd_path, xsd_type_info)

            # Write to file
            with open(md_path, 'w', encoding='utf-8') as f:
                f.write(markdown_content)

            print(f"Generated {md_path}")
        else:
            print(f"No data extracted from {xml_file}")

    file_count = len([f for f in xml_files if not f.startswith(('ch-profile', 'ch-profile_'))])
    print(f"Processed {file_count} files")


def parse_args():
    """Parse command line arguments"""
    parser = argparse.ArgumentParser(description='Generate markdown documentation from NeTEx templates')
    parser.add_argument('-i', '--input', default=TEMPLATES_DIR,
        help=f'Input folder or single XML file for faster testing (Default = {TEMPLATES_DIR})')
    parser.add_argument('-o', '--output', default=SITE_TABLES_DIR,
        help=f'Output folder for markdown files (Default = {SITE_TABLES_DIR})')
    parser.add_argument('-x', '--xsd', default=XSD_FILE_PATH,
        help=f'XSD schema file for type information (Default = {XSD_FILE_PATH})')
    return parser.parse_args()


def main():
    args = parse_args()
    build_markdown_tables(args.input, args.output, args.xsd)


if __name__ == '__main__':
    main()