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
        # Skip intermediate constructs that don't represent actual XML structure
        tag = current.tag if not hasattr(current, 'tag') or not callable(current.tag) else str(current.tag)
        
        # Skip xs:annotation, xs:complexType, xs:simpleType, xs:group, xs:choice, xs:sequence
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
    """Build a map of element paths to their metadata from XSD
    
    Returns a dict where keys are full element paths (e.g., 'ServiceFrame/lines/Line')
    and values are the element metadata.
    """
    namespaces = {'xs': 'http://www.w3.org/2001/XMLSchema'}
    xsd_path_map = {}
    
    # Find all elements in the XSD
    all_elements = xsd_doc.xpath('//xs:element', namespaces=namespaces)
    
    for element in all_elements:
        # Get the logical path for this element
        path = _get_xsd_element_path(element)
        if not path:
            continue
            
        # Get element metadata
        name = element.get('name') or element.get('ref', '').split(':')[-1]
        elem_type = element.get('type', '')
        min_occurs = element.get('minOccurs', '1')
        max_occurs = element.get('maxOccurs', '1')
        
        # Get description
        description = ''
        annotation = element.find('xs:annotation', namespaces=namespaces)
        if annotation is not None:
            doc = annotation.find('xs:documentation', namespaces=namespaces)
            if doc is not None and doc.text:
                description = sanitize_for_markdown(doc.text)
        
        # Store metadata at the full path (path already includes the element name)
        # If path is just the element name (e.g., 'Line'), use that
        # If path is a full path (e.g., 'ServiceFrame/lines/Line'), use that
        if path not in xsd_path_map:
            xsd_path_map[path] = {
                'type': elem_type,
                'min_occurs': min_occurs,
                'max_occurs': max_occurs,
                'description': description
            }
        else:
            # If there's already an entry at this path, this might be from a different file
            # Keep the first one for now (this could be enhanced)
            pass
        
        # Also store under just the element name for fallback
        if name not in xsd_path_map:
            xsd_path_map[name] = {
                'type': elem_type,
                'min_occurs': min_occurs,
                'max_occurs': max_occurs,
                'description': description
            }
    
    return xsd_path_map


def _process_xsd_file(xsd_path, base_dir, processed_files=None):
    """Process an XSD file and all its imports/includes recursively
    
    Returns a dict mapping element names to their metadata, but also builds
    a path-based structure for more accurate matching.
    """
    if processed_files is None:
        processed_files = set()
    
    # Avoid circular processing
    if xsd_path in processed_files:
        return {}
    processed_files.add(xsd_path)
    
    type_info = {}
    path_based_info = {}  # New: path-based element information
    
    try:
        xsd_doc = etree.parse(xsd_path)
        xsd_root = xsd_doc.getroot()
        
        # Get the target namespace from the schema element
        target_namespace = xsd_root.get('targetNamespace')
        if not target_namespace:
            # If no target namespace, use the default namespace
            target_namespace = xsd_root.nsmap.get(None, '')
        
        # Namespaces - use the actual target namespace of this file
        ns = {'': target_namespace,
              'xs': 'http://www.w3.org/2001/XMLSchema'
              }
        
        print(f"Processing XSD with namespace: {target_namespace}")
        
        # Process imports first (they may define types needed by this file)
        current_dir = os.path.dirname(xsd_path)
        for import_elem in xsd_root.findall('xs:import', namespaces={'xs': 'http://www.w3.org/2001/XMLSchema'}):
            schema_location = import_elem.get('schemaLocation')
            if schema_location:
                # Resolve relative paths relative to the current file's directory
                import_path = os.path.normpath(os.path.join(current_dir, schema_location))
                if os.path.exists(import_path):
                    print(f"Processing import: {import_path}")
                    imported_types = _process_xsd_file(import_path, base_dir, processed_files)
                    type_info.update(imported_types)
                    # Merge path-based info
                    for path, elements in imported_types.get('_paths', {}).items():
                        if path not in path_based_info:
                            path_based_info[path] = {}
                        path_based_info[path].update(elements)
                else:
                    print(f"Import not found: {import_path}")
        
        # Process includes
        for include_elem in xsd_root.findall('xs:include', namespaces={'xs': 'http://www.w3.org/2001/XMLSchema'}):
            schema_location = include_elem.get('schemaLocation')
            if schema_location:
                # Resolve relative paths relative to the current file's directory
                include_path = os.path.normpath(os.path.join(current_dir, schema_location))
                if os.path.exists(include_path):
                    print(f": {include_path}")
                    included_types = _process_xsd_file(include_path, base_dir, processed_files)
                    type_info.update(included_types)
                    # Merge path-based info
                    for path, elements in included_types.get('_paths', {}).items():
                        if path not in path_based_info:
                            path_based_info[path] = {}
                        path_based_info[path].update(elements)
                else:
                    print(f"Include not found: {include_path}")
        
        # Build path-based element information
        doc_path_map = _build_xsd_element_paths(xsd_doc)
        for path, elements in doc_path_map.items():
            if path not in path_based_info:
                path_based_info[path] = {}
            path_based_info[path].update(elements)
        
        # Extract complex types (for backward compatibility)
        for complex_type in xsd_root.findall('.//xs:complexType', namespaces=ns):
            name = complex_type.get('name')
            if name:
                type_info[name] = {'type': 'complex', 'elements': {}, 'description': ''}
                
                # Extract documentation/description
                annotation = complex_type.find('xs:annotation', namespaces=ns)
                if annotation is not None:
                    doc = annotation.find('xs:documentation', namespaces=ns)
                    if doc is not None and doc.text:
                        # Sanitize description to remove newlines
                        type_info[name]['description'] = sanitize_for_markdown(doc.text)
                
                # Extract elements within this complex type
                for element in complex_type.findall('.//xs:element', namespaces=ns):
                    elem_name = element.get('name')
                    elem_type = element.get('type')
                    min_occurs = element.get('minOccurs', '1')
                    max_occurs = element.get('maxOccurs', '1')
                    
                    if elem_name:
                        # Get element description
                        elem_description = ''
                        elem_annotation = element.find('xs:annotation', namespaces=ns)
                        if elem_annotation is not None:
                            elem_doc = elem_annotation.find('xs:documentation', namespaces=ns)
                            if elem_doc is not None and elem_doc.text:
                                # Sanitize description to remove newlines
                                elem_description = sanitize_for_markdown(elem_doc.text)
                        
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
                
                # Extract documentation
                annotation = simple_type.find('xs:annotation', namespaces=ns)
                if annotation is not None:
                    doc = annotation.find('xs:documentation', namespaces=ns)
                    if doc is not None and doc.text:
                        # Sanitize description to remove newlines
                        type_info[name]['description'] = sanitize_for_markdown(doc.text)
        
        # Extract top-level elements
        for element in xsd_root.findall('.//xs:element', namespaces=ns):
            name = element.get('name')
            elem_type = element.get('type')
            min_occurs = element.get('minOccurs', '1')
            max_occurs = element.get('maxOccurs', '1')
            
            if name:
                # Get element description
                elem_description = ''
                annotation = element.find('xs:annotation', namespaces=ns)
                if annotation is not None:
                    doc = annotation.find('xs:documentation', namespaces=ns)
                    if doc is not None and doc.text:
                        # Sanitize description to remove newlines
                        elem_description = sanitize_for_markdown(doc.text)
                
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
    
    except Exception as e:
        print(f"Error loading XSD: {e}")
        return {}


def get_element_metadata_from_xsd_by_path(xsd_doc, xml_path):
    """Get element metadata from XSD using the full XML path to find the correct element definition.
    
    This function constructs an XPath expression based on the XML path and searches for the
    corresponding element in the XSD. It then extracts type, minOccurs, maxOccurs, and description.
    
    Args:
        xsd_doc: Parsed XSD document (lxml.etree._ElementTree or _Element)
        xml_path: The XML path from the template (e.g., 'stopPlaces/StopPlace/quays/Quay')
        
    Returns:
        Dictionary with metadata (type, min_occurs, max_occurs, description) or None if not found
    """
    if xsd_doc is None or not xml_path:
        return None
    
    namespaces = {'xs': 'http://www.w3.org/2001/XMLSchema'}
    
    # Convert XML path to XSD XPath expression
    # XML path: stopPlaces/StopPlace/quays/Quay
    # XSD XPath: //xs:element[@name='stopPlaces']//xs:element[@name='StopPlace']//xs:element[@name='quays']//xs:element[@name='Quay']
    path_parts = xml_path.split('/')
    xpath_expr_parts = []
    
    for part in path_parts:
        # Handle both direct element names and ref attributes
        xpath_expr_parts.append(f"xs:element[@name='{part}']")
        # Also try with ref attribute for referenced elements
        xpath_expr_parts.append(f"xs:element[@ref='{part}']")
        xpath_expr_parts.append(f"xs:element[contains(@ref, ':{part}')]")
    
    # Build XPath expressions - try each possible combination
    # Start with the most specific (all parts as direct children)
    direct_xpath = f"//{'//'.join([f"xs:element[@name='{part}']" for part in path_parts])}"
    elem_def = xsd_doc.xpath(direct_xpath, namespaces=namespaces)
    
    if not elem_def:
        # Try with a more flexible approach - each part can be either @name or @ref
        # Build multiple XPath expressions and try them in order
        xpath_options = []
        
        def build_xpath_options(parts, index=0, current_parts=None):
            if current_parts is None:
                current_parts = []
            if index == len(parts):
                xpath_options.append('//' + '//'.join(current_parts))
                return
            
            part = parts[index]
            # Try @name first
            build_xpath_options(parts, index + 1, current_parts + [f"xs:element[@name='{part}']"])
            # Try @ref
            build_xpath_options(parts, index + 1, current_parts + [f"xs:element[@ref='{part}']"])
            # Try @ref with namespace
            build_xpath_options(parts, index + 1, current_parts + [f"xs:element[contains(@ref, ':{part}')]"])
        
        build_xpath_options(path_parts)
        
        for option in xpath_options:
            elem_def = xsd_doc.xpath(option, namespaces=namespaces)
            if elem_def:
                break
    
    if not elem_def:
        # Try a more permissive search - look for element with this name anywhere,
        # but check if it's in a context that matches the path
        element_name = path_parts[-1]  # The last part is the element we're looking for
        all_elements = xsd_doc.xpath(f"//xs:element[@name='{element_name}' or @ref='{element_name}']", namespaces=namespaces)
        
        if all_elements:
            # Try to find the best match by checking parent context
            for candidate in all_elements:
                # Check if this element has ancestors that match the path
                candidate_path = _get_xsd_element_path(candidate)
                if candidate_path and candidate_path.endswith(xml_path):
                    elem_def = [candidate]
                    break
                # Also check if the candidate's path matches any suffix of the xml_path
                elif candidate_path and xml_path.endswith(candidate_path):
                    elem_def = [candidate]
                    break
            
            if not elem_def:
                # If no perfect match, use the first candidate as fallback
                elem_def = [all_elements[0]]
    
    if not elem_def:
        return None
    
    element = elem_def[0]
    
    # Extract type attribute
    elem_type = element.get('type', '')
    if not elem_type:
        # Try to resolve type from ref attribute
        ref = element.get('ref', '')
        if ref:
            ref_name = ref.split(':')[-1]  # Remove namespace prefix
            # Find the referenced element
            ref_element = xsd_doc.xpath(f"//xs:element[@name='{ref_name}']", namespaces=namespaces)
            if ref_element:
                elem_type = ref_element[0].get('type', '')
    
    if not elem_type:
        # Try to get type from inline complexType or simpleType
        complex_type = element.find('xs:complexType', namespaces=namespaces)
        if complex_type is not None:
            elem_type = complex_type.get('name', '')
        simple_type = element.find('xs:simpleType', namespaces=namespaces)
        if simple_type is not None:
            elem_type = simple_type.get('name', '')
        
        if not elem_type:
            # Try without namespace
            complex_type = element.find('complexType')
            if complex_type is not None:
                elem_type = complex_type.get('name', '')
            simple_type = element.find('simpleType')
            if simple_type is not None:
                elem_type = simple_type.get('name', '')
    
    # Extract cardinality
    min_occurs = element.get('minOccurs', '1')
    max_occurs = element.get('maxOccurs', '1')
    
    # Extract description from annotation/documentation
    description = ''
    annotation = element.find('xs:annotation', namespaces=namespaces)
    if annotation is None:
        annotation = element.find('annotation')
    
    if annotation is not None:
        doc = annotation.find('xs:documentation', namespaces=namespaces)
        if doc is None:
            doc = annotation.find('documentation')
        
        if doc is not None and doc.text:
            description = doc.text.strip()
    
    # If no description found, try to follow substitution group chain
    if not description:
        substitution_group = element.get('substitutionGroup')
        if substitution_group:
            # Find the head element
            head_name = substitution_group.split(':')[-1]
            head_element = xsd_doc.xpath(f"//xs:element[@name='{head_name}']", namespaces=namespaces)
            if head_element:
                annotation = head_element[0].find('xs:annotation', namespaces=namespaces)
                if annotation is not None:
                    doc = annotation.find('xs:documentation', namespaces=namespaces)
                    if doc is not None and doc.text:
                        description = doc.text.strip()
    
    # Clean up type name (remove namespace prefix if present)
    if elem_type and ':' in elem_type:
        elem_type = elem_type.split(':')[-1]
    
    return {
        'type': elem_type if elem_type else 'unknown',
        'min_occurs': min_occurs,
        'max_occurs': max_occurs,
        'description': sanitize_for_markdown(description)
    }


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
    found_logical_root = False
    
    while current is not None:
        # Get the local name of the element
        if hasattr(current, 'tag') and not isinstance(current, etree._Comment):
            try:
                name = etree.QName(current).localname
                if name:
                    # Skip document wrapper elements
                    if name in ['PublicationDelivery', 'dataObjects', 'CompositeFrame', 'frames', 'ResourceFrame', 'SiteFrame']:
                        # These are document structure, not logical structure
                        if name == 'PublicationDelivery':
                            break
                        current = current.getparent()
                        continue
                    else:
                        path_parts.insert(0, name)
                        found_logical_root = True
            except:
                pass
        
        current = current.getparent()
        
        # Stop if we reach the root element (PublicationDelivery in templates)
        if current is not None and hasattr(current, 'tag'):
            try:
                root_name = etree.QName(current).localname
                if root_name == 'PublicationDelivery':
                    break
            except:
                pass
    
    return '/'.join(path_parts) if path_parts else None


def search_xsd_files_for_element(base_dir, element_name):
    """Search all XSD files in the directory structure for a specific element"""
    return search_xsd_files_for_element_with_parent(base_dir, element_name, None)


def search_xsd_files_for_element_with_parent(base_dir, element_name, parent_type=None):
    """Search all XSD files in the directory structure for a specific element,
    optionally within a parent complex type context
    
    If parent_type is specified, only returns files where the element is found
    within a complex type containing that parent_type name.
    """
    namespaces = {'xs': 'http://www.w3.org/2001/XMLSchema'}
    
    # Search through all XSD files in the directory tree
    for root, dirs, files in os.walk(base_dir):
        for file in files:
            if file.endswith('.xsd'):
                file_path = os.path.join(root, file)
                try:
                    parser = etree.XMLParser()
                    xsd_doc = etree.parse(file_path, parser)
                    
                    elements = []
                    
                    # If parent_type is specified, only look within that context
                    if parent_type:
                        # Try complex types containing parent_type with element by name
                        complex_type_xpath = f"//xs:complexType[contains(@name, '{parent_type}')]//xs:element[@name='{element_name}']"
                        elements = xsd_doc.xpath(complex_type_xpath, namespaces=namespaces)
                        
                        # Also try with @ref attribute (for referenced elements)
                        if not elements:
                            complex_type_xpath_ref = f"//xs:complexType[contains(@name, '{parent_type}')]//xs:element[@ref='{element_name}']"
                            elements = xsd_doc.xpath(complex_type_xpath_ref, namespaces=namespaces)
                            
                            # Also try with namespace prefix in ref
                            if not elements:
                                complex_type_xpath_ref_ns = f"//xs:complexType[contains(@name, '{parent_type}')]//xs:element[contains(@ref, ':{element_name}')]"
                                elements = xsd_doc.xpath(complex_type_xpath_ref_ns, namespaces=namespaces)
                        
                        # Try without namespace for broader compatibility
                        if not elements:
                            complex_type_xpath_no_ns = f"//*[local-name()='complexType' and contains(@name, '{parent_type}')]//*[local-name()='element' and @name='{element_name}']"
                            elements = xsd_doc.xpath(complex_type_xpath_no_ns)
                            
                            # Also try with @ref for no-namespace case
                            if not elements:
                                complex_type_xpath_no_ns_ref = f"//*[local-name()='complexType' and contains(@name, '{parent_type}')]//*[local-name()='element' and @ref='{element_name}']"
                                elements = xsd_doc.xpath(complex_type_xpath_no_ns_ref)
                        
                        # Only return if found in parent context
                        if elements:
                            return file_path
                        else:
                            continue  # Skip this file, element not found in parent context
                    else:
                        # No parent_type, search all elements
                        element_xpath = f"//xs:element[@name='{element_name}']"
                        elements = xsd_doc.xpath(element_xpath, namespaces=namespaces)
                        
                        # If not found, try without namespace
                        if not elements:
                            element_xpath_no_ns = f"//*[local-name()='element' and @name='{element_name}']"
                            elements = xsd_doc.xpath(element_xpath_no_ns)
                        
                        if elements:
                            return file_path
                        
                except Exception as e:
                    # Skip files that can't be parsed
                    continue
    
    return None


def find_best_xsd_path_match(xsd_path_info, xml_path, element_name):
    """Find the best matching XSD path for a given XML path and element name
    
    Args:
        xsd_path_info: The _paths dictionary from loaded XSD type info
        xml_path: The XML path from the template (e.g., 'stopPlaces/StopPlace/Name')
        element_name: The element name to match (for debugging/info)
        
    Returns:
        The best matching XSD metadata, or None if not found
    """
    if not xsd_path_info or not xml_path:
        return None
    
    # Try exact path match first (xml_path is the full path including element name)
    if xml_path in xsd_path_info:
        return xml_path, xsd_path_info[xml_path]
    
    # Try path variations by removing parts from the end
    path_parts = xml_path.split('/')
    for i in range(1, len(path_parts)):
        shortened_path = '/'.join(path_parts[:-i])
        if shortened_path in xsd_path_info:
            return shortened_path, xsd_path_info[shortened_path]
    
    # Try just the element name as fallback
    if '/' in xml_path:
        element_only = xml_path.rsplit('/', 1)[-1]
        if element_only in xsd_path_info:
            return element_only, xsd_path_info[element_only]
    
    return None
    
    # Try path variations by removing parts from the end
    path_parts = xml_path.split('/')
    for i in range(1, len(path_parts) + 1):
        shortened_path = '/'.join(path_parts[:-i])
        if shortened_path in xsd_path_info:
            elements = xsd_path_info[shortened_path]
            if element_name in elements:
                return shortened_path, elements[element_name]
    
    # Try path variations by replacing parts with wildcards (for type name variations)
    # For example, StopPlace might be StopPlace_VersionStructure in XSD
    parts = xml_path.split('/')
    for i in range(len(parts)):
        for pattern in ['_VersionStructure', '_Structure', '_Type']:
            test_parts = parts.copy()
            test_parts[i] = test_parts[i] + pattern
            test_path = '/'.join(test_parts)
            if test_path in xsd_path_info:
                elements = xsd_path_info[test_path]
                if element_name in elements:
                    return test_path, elements[element_name]
    
    # Try the element name alone as a fallback
    for path, elements in xsd_path_info.items():
        if element_name in elements:
            return path, elements[element_name]
    
    return None


def get_element_metadata(xsd_path, element_name, parent_type=None):
    """Extract detailed metadata for an element from XSD using XPath with substitution group support
    
    Args:
        xsd_path: Path to the XSD file
        element_name: Name of the element to find
        parent_type: Optional. The name of the parent complex type to search within.
                    If provided, will look for the element as a child of this type first.
    """
    try:
        # First try to find the element in the main XSD file
        parser = etree.XMLParser()
        xsd_doc = etree.parse(xsd_path, parser)
        namespaces = {'xs': 'http://www.w3.org/2001/XMLSchema'}
        
        element = None
        
        # If parent_type is specified, try to find the element within that complex type first
        if parent_type:
            # Clean parent_type by removing any special markers (e.g., "MULTILINGUAL_PARENT")
            # Split by | and get the first non-marker part
            clean_parent_type = None
            if parent_type:
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
            
            # Also try with ref attribute (for referenced elements)
            if not element:
                complex_type_xpath_ref = f"//xs:complexType[@name='{clean_parent_type}']//xs:element[@ref='{element_name}']"
                element = xsd_doc.xpath(complex_type_xpath_ref, namespaces=namespaces)
                if not element:
                    # Try with namespace prefix in ref (e.g., netex:PrivateCode)
                    complex_type_xpath_ref_ns = f"//xs:complexType[@name='{clean_parent_type}']//xs:element[contains(@ref, ':{element_name}')]"
                    element = xsd_doc.xpath(complex_type_xpath_ref_ns, namespaces=namespaces)
            
            # Also try without namespace prefix for broader compatibility
            if not element:
                complex_type_xpath_no_ns = f"//*[local-name()='complexType' and @name='{clean_parent_type}']//*[local-name()='element' and @name='{element_name}']"
                element = xsd_doc.xpath(complex_type_xpath_no_ns)
                
                # Also try with ref attribute for no-namespace case
                if not element:
                    complex_type_xpath_no_ns_ref = f"//*[local-name()='complexType' and @name='{clean_parent_type}']//*[local-name()='element' and @ref='{element_name}']"
                    element = xsd_doc.xpath(complex_type_xpath_no_ns_ref)
            
            # Try complex types that contain the parent_type name (e.g., StopPlace -> StopPlace_VersionStructure)
            if not element:
                complex_type_xpath_contains = f"//xs:complexType[contains(@name, '{clean_parent_type}')]//xs:element[@name='{element_name}']"
                element = xsd_doc.xpath(complex_type_xpath_contains, namespaces=namespaces)
                
                # Also try with ref attribute for contains case
                if not element:
                    complex_type_xpath_contains_ref = f"//xs:complexType[contains(@name, '{clean_parent_type}')]//xs:element[@ref='{element_name}']"
                    element = xsd_doc.xpath(complex_type_xpath_contains_ref, namespaces=namespaces)
                
            # Try common version structure patterns
            if not element:
                # Try parent_type + _VersionStructure pattern (e.g., StopPlace -> StopPlace_VersionStructure)
                version_patterns = [
                    f"{clean_parent_type}_VersionStructure",
                    f"{clean_parent_type}VesionStructure",  # Handle typo if present
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
            
            # NEW: Try _RelStructure pattern for parent_type
            # This handles containers like quays -> quays_RelStructure, stopPlaces -> stopPlaces_RelStructure
            if not element:
                rel_structure_parent = f"{clean_parent_type}_RelStructure"
                complex_type_xpath_rel = f"//xs:complexType[@name='{rel_structure_parent}']//xs:element[@ref='{element_name}']"
                element = xsd_doc.xpath(complex_type_xpath_rel, namespaces=namespaces)
                
                # Also try without exact name match (contains pattern)
                if not element:
                    complex_type_xpath_rel_contains = f"//xs:complexType[contains(@name, '{rel_structure_parent}')]//xs:element[@ref='{element_name}']"
                    element = xsd_doc.xpath(complex_type_xpath_rel_contains, namespaces=namespaces)
                    
                # Try with @name attribute as well
                if not element:
                    complex_type_xpath_rel_name = f"//xs:complexType[@name='{rel_structure_parent}']//xs:element[@name='{element_name}']"
                    element = xsd_doc.xpath(complex_type_xpath_rel_name, namespaces=namespaces)
                    
                if not element:
                    complex_type_xpath_rel_name_contains = f"//xs:complexType[contains(@name, '{rel_structure_parent}')]//xs:element[@name='{element_name}']"
                    element = xsd_doc.xpath(complex_type_xpath_rel_name_contains, namespaces=namespaces)
            
            if not element:
                complex_type_xpath_contains_no_ns = f"//*[local-name()='complexType' and contains(@name, '{clean_parent_type}')]//*[local-name()='element' and @name='{element_name}']"
                element = xsd_doc.xpath(complex_type_xpath_contains_no_ns)
            
            # If we have a parent_type but still haven't found the element, 
            # search in other XSD files with the parent context
            if not element:
                base_dir = os.path.dirname(os.path.abspath(xsd_path))
                found_in_file = search_xsd_files_for_element_with_parent(base_dir, element_name, clean_parent_type)
                if found_in_file is not None:
                    # Parse the file where the element was found
                    xsd_doc = etree.parse(found_in_file, parser)
                    namespaces = {'xs': 'http://www.w3.org/2001/XMLSchema'}
                    # Find the element in this document using parent_type context
                    # Try with @name first
                    complex_type_xpath = f"//xs:complexType[contains(@name, '{clean_parent_type}')]//xs:element[@name='{element_name}']"
                    element = xsd_doc.xpath(complex_type_xpath, namespaces=namespaces)
                    
                    # Also try with @ref attribute
                    if not element:
                        complex_type_xpath_ref = f"//xs:complexType[contains(@name, '{clean_parent_type}')]//xs:element[@ref='{element_name}']"
                        element = xsd_doc.xpath(complex_type_xpath_ref, namespaces=namespaces)
                        
                        # Also try with namespace prefix in ref
                        if not element:
                            complex_type_xpath_ref_ns = f"//xs:complexType[contains(@name, '{clean_parent_type}')]//xs:element[contains(@ref, ':{element_name}')]"
                            element = xsd_doc.xpath(complex_type_xpath_ref_ns, namespaces=namespaces)
                    
                    # Try without namespace for broader compatibility
                    if not element:
                        complex_type_xpath_no_ns = f"//*[local-name()='complexType' and contains(@name, '{clean_parent_type}')]//*[local-name()='element' and @name='{element_name}']"
                        element = xsd_doc.xpath(complex_type_xpath_no_ns)
                        
                        # Also try with @ref for no-namespace case
                        if not element:
                            complex_type_xpath_no_ns_ref = f"//*[local-name()='complexType' and contains(@name, '{clean_parent_type}')]//*[local-name()='element' and @ref='{element_name}']"
                            element = xsd_doc.xpath(complex_type_xpath_no_ns_ref)
                    # If found in parent context, use it
                    if element:
                        xsd_path = found_in_file  # Update xsd_path for later use
                        
            # IMPORTANT: If parent_type was specified but we still haven't found the element in that context,
            # DO NOT fall back to a generic search. Return None to avoid using the wrong element's metadata.
            # This prevents issues where e.g. StopPlace/Name gets the description from Traveller/Name.
            if not element:
                return None
        else:
            # No parent_type specified, do a generic search
            # Try to find the element in the main file first
            element_xpath = f"//xs:element[@name='{element_name}']"
            element = xsd_doc.xpath(element_xpath, namespaces=namespaces)
            
            # If not found in main file, search all XSD files
            if not element:
                base_dir = os.path.dirname(os.path.abspath(xsd_path))
                found_in_file = search_xsd_files_for_element_with_parent(base_dir, element_name, None)
                if found_in_file is not None:
                    # Parse the file where the element was found
                    xsd_doc = etree.parse(found_in_file, parser)
                    namespaces = {'xs': 'http://www.w3.org/2001/XMLSchema'}
                    # Find the element in this document
                    element_xpath = f"//xs:element[@name='{element_name}']"
                    element = xsd_doc.xpath(element_xpath, namespaces=namespaces)
                    
                    # If not found, try without namespace
                    if not element:
                        element_xpath_no_ns = f"//*[local-name()='element' and @name='{element_name}']"
                        element = xsd_doc.xpath(element_xpath_no_ns)
                    # If found, update xsd_doc for later use
                    if element:
                        xsd_path = found_in_file
            
            if not element:
                return None
        
        element = element[0]
        
        # Debug: print what we found (commented out by default)
        # print(f"DEBUG: Found element {element_name} with tag {element.tag}, attributes {element.attrib}")
        
        # Get cardinality - use element's own if available, otherwise traverse substitution group
        min_occurs = element.get('minOccurs', '1')
        max_occurs = element.get('maxOccurs', '1')
        cardinality = get_cardinality(min_occurs, max_occurs)
        
        # Check if parent is a _RelStructure type or has unbounded maxOccurs
        # This handles the case where elements are within a choice that we don't explicitly model
        # Check both the parent_type parameter and the actual parent complex type
        actual_parent_complex_type = None
        parent_elem = element.getparent()
        if parent_elem is not None:
            # Check if parent is a choice or sequence with maxOccurs="unbounded"
            parent_max_occurs = parent_elem.get('maxOccurs')
            if parent_max_occurs == 'unbounded':
                cardinality = '0..*'
            # Also check if parent is a complexType
            elif parent_elem.tag.endswith('complexType') or etree.QName(parent_elem).localname == 'complexType':
                # Get the name of the parent complex type
                actual_parent_complex_type = parent_elem.get('name')
        
        # Check in order of preference:
        # 1. parent_type parameter contains _RelStructure
        if parent_type and '_RelStructure' in parent_type:
            cardinality = '0..*'
        # 2. actual parent complex type contains _RelStructure
        elif actual_parent_complex_type and '_RelStructure' in actual_parent_complex_type:
            cardinality = '0..*'
        # 3. Check if there's a complex type matching parent_type that has _RelStructure
        elif parent_type:
            # For cases where parent_type is "quays" but the actual type is "quays_RelStructure"
            # Search for complex types containing parent_type and _RelStructure in current xsd_doc
            complex_types_with_pattern = xsd_doc.xpath(f"//xs:complexType[contains(@name, '{parent_type}') and contains(@name, '_RelStructure')]", namespaces=namespaces)
            if complex_types_with_pattern:
                cardinality = '0..*'
            else:
                # Also search all XSD files for matching complex type
                base_dir = os.path.dirname(os.path.abspath(xsd_path))
                for root, dirs, files in os.walk(base_dir):
                    for file in files:
                        if file.endswith('.xsd'):
                            file_path = os.path.join(root, file)
                            try:
                                doc = etree.parse(file_path, parser)
                                ct_match = doc.xpath(f"//xs:complexType[contains(@name, '{parent_type}') and contains(@name, '_RelStructure')]", namespaces=namespaces)
                                if ct_match:
                                    cardinality = '0..*'
                                    break
                            except:
                                continue
                    if cardinality == '1..*':
                        break
        
        # Get type - check substitution group chain recursively
        element_type = "unknown"
        current_element = element
        visited_elements = set()  # Prevent infinite loops
        
        # Handle elements with ref attribute - resolve to actual element for type extraction
        if current_element.get('ref') and not current_element.get('type'):
            ref_name = current_element.get('ref').split(':')[-1]  # Remove namespace prefix
            ref_element_xpath = f"//xs:element[@name='{ref_name}']"
            ref_element = xsd_doc.xpath(ref_element_xpath, namespaces=namespaces)
            if not ref_element:
                # Try without namespace
                ref_element_xpath_no_ns = f"//*[local-name()='element' and @name='{ref_name}']"
                ref_element = xsd_doc.xpath(ref_element_xpath_no_ns)
            if ref_element:
                current_element = ref_element[0]
        
        while current_element is not None and current_element.get('name') not in visited_elements:
            visited_elements.add(current_element.get('name'))
            
            # Check for direct type attribute
            type_attr = current_element.get('type')
            if type_attr:
                element_type = type_attr.split(':')[-1]  # Remove namespace prefix
                break
            
            # Check for inline types - try both with and without namespace
            simple_type = current_element.find('xs:simpleType', namespaces)
            complex_type = current_element.find('xs:complexType', namespaces)
            
            if simple_type is None:
                simple_type = current_element.find('simpleType')
            if complex_type is None:
                complex_type = current_element.find('complexType')
                
            if simple_type is not None:
                # Try to get the name of the simple type
                simple_type_name = simple_type.get('name')
                element_type = simple_type_name if simple_type_name else "inline simpleType"
                break
            elif complex_type is not None:
                # Try to get the name of the complex type
                complex_type_name = complex_type.get('name')
                element_type = complex_type_name if complex_type_name else element.get('name')
                break
            
            # Follow substitution group
            substitution_group = current_element.get('substitutionGroup')
            if substitution_group:
                # Find the head element
                head_name = substitution_group.split(':')[-1]
                head_xpath = f"//xs:element[@name='{head_name}']"
                head_element = xsd_doc.xpath(head_xpath, namespaces=namespaces)
                if head_element:
                    current_element = head_element[0]
                    continue
            
            break
        
        # Debug output (commented out by default)
        # print(f"DEBUG: Element {element_name} - type: {element_type}")
        # print(f"DEBUG: Element attributes: {element.attrib}")
        # print(f"DEBUG: Element children: {[child.tag for child in element]}")
        # simple_type = element.find('xs:simpleType', namespaces)
        # complex_type = element.find('xs:complexType', namespaces)
        # print(f"DEBUG: Has simpleType: {simple_type is not None}, Has complexType: {complex_type is not None}")
        # if complex_type is not None:
        #     print(f"DEBUG: complexType tag: {complex_type.tag}")
        
        # Get description - collect from entire substitution group chain
        description = ""
        current_element = element
        visited_elements = set()
        
        while current_element is not None and current_element.get('name') not in visited_elements:
            visited_elements.add(current_element.get('name'))
            
            # Check current element's annotation - try both with and without namespace
            annotation = current_element.find('xs:annotation', namespaces)
            if annotation is None:
                annotation = current_element.find('annotation')
                
            if annotation is not None:
                doc = annotation.find('xs:documentation', namespaces)
                if doc is None:
                    doc = annotation.find('documentation')
                    
                if doc is not None and doc.text:
                    if description:
                        description += " " + doc.text.strip()
                    else:
                        description = doc.text.strip()
            
            # Follow substitution group
            substitution_group = current_element.get('substitutionGroup')
            if substitution_group:
                head_name = substitution_group.split(':')[-1]
                head_xpath = f"//xs:element[@name='{head_name}']"
                head_element = xsd_doc.xpath(head_xpath, namespaces=namespaces)
                if head_element:
                    current_element = head_element[0]
                    continue
            
            break
        
        return {
            'cardinality': cardinality,
            'type': element_type,
            'description': sanitize_for_markdown(description or "")
        }
        
    except Exception as e:
        print(f"Warning: Could not extract metadata for {element_name}: {e}")
        return None


def parse_template_file(file_path, xsd_type_info):
    """Parse a single template file and extract documentation"""
    try:
        doc = etree.parse(file_path)
        root = doc.getroot()
        
        # Register namespace if present
        nsmap = root.nsmap
        ns = {}
        if None in nsmap:
            # Default namespace
            default_ns = nsmap[None]
            ns['default'] = default_ns
        
        # Find ch-root comments
        comments = root.xpath('//comment()', namespaces=ns)
        
        root_element = None
        
        for comment in comments:
            text = comment.text.strip() if comment.text else ''
            if 'ch-root' in text or 'ch-root' == text:
                # Find the parent element of this comment
                root_element = comment.getparent()
                break
        
        # If no ch-root found, check if this is a ch-profile template
        has_ch_see = any('ch-see' in (comment.text.strip() if comment.text else '')
                               for comment in comments)
        
        if root_element is None and has_ch_see:
            # If no ch-root found but has ch-see comments, use root as the element
            root_element = root
        
        if root_element is None:
            print(f"Warning: No ch-root found in {file_path}")
            return None
        
        # Get the elements from the root element
        elements_data = []
        
        # Use the root element we found
        common_ancestor = root_element
        
        # Process elements in the range
        processed_elements = set()
        
        def get_preceding_comments(element):
            """Get comments that appear immediately before this element (sibling comments)"""
            parent = element.getparent()
            if parent is None:
                return []
            
            comments = []
            # Get all children of parent
            children = list(parent)
            # Find the index of this element
            elem_index = -1
            for i, child in enumerate(children):
                if child is element:
                    elem_index = i
                    break
            
            # Collect comments immediately before this element
            if elem_index > 0:
                for i in range(elem_index - 1, -1, -1):
                    child = children[i]
                    if isinstance(child, etree._Comment):
                        comments.insert(0, child)
                    else:
                        # Stop if we hit a non-comment
                        break
            
            return comments
        
        def process_element(element, level=0, parent_type_context=None, xml_path=None):
            """Recursively process an element and its children
            
            Args:
                element: The XML element to process
                level: Indentation level for hierarchy
                parent_type_context: The name of the parent complex type for XSD lookup context
                xml_path: The XPath path from the root to this element
            """
            # Handle namespace properly
            if hasattr(element, 'tag'):
                elem_name = etree.QName(element).localname
            else:
                return  # Skip non-element nodes
            elem_id = element.get('id')
            
            # Build or use the XML path for this element
            if xml_path is None:
                xml_path = get_xml_element_path(element)
            
            # For children, we'll extend this path
            
            # Define multilingual element names early so we can use it in key generation
            multilingual_element_names = ['Text', 'Description', 'Name', 'ShortName', 'Label', 'Title', 'Subtitle']
            
            # Skip if already processed (avoid duplicates)
            # Include lang attribute in key for Text elements to avoid duplicates
            if elem_name in multilingual_element_names and element.get('lang'):
                elem_key = f"{elem_name}_{element.get('lang')}_{elem_id}" if elem_id else f"{elem_name}_{element.get('lang')}"
            else:
                # For elements without id, include ref or other attributes to make key unique
                elem_key = f"{elem_name}_{elem_id}" if elem_id else elem_name
            
            # Also include level in key to ensure uniqueness for nested elements
            # And include ref attribute if present (for StopPlaceRef, etc.)
            if element.get('ref'):
                elem_key = f"{elem_key}_ref={element.get('ref')}"
            elem_key = f"{elem_key}_L{level}"
            
            if elem_key in processed_elements:
                return
            processed_elements.add(elem_key)
            
            # Get comments for this element
            usage = 'ignored'
            note = ''
            is_referenced = False
            see_reference = None
            
            # Check if this element is a child of a MultilingualString parent
            is_multilingual_child = 'MULTILINGUAL_PARENT' in (parent_type_context or '')
            
            # Get comments that are direct children of this element (before any child elements)
            # These are the comments that describe the element itself
            child_comments = element.xpath('comment()')
            
            # NEW: Get preceding comments (sibling comments before this element)
            # This is important for elements like Text that may have ch-usage comments before them
            preceding_comments = get_preceding_comments(element)
            
            is_deprecated = False
            attrs_list = []
            has_ch_root = False
            
            # For Text and Description elements, also extract lang attribute from the element itself
            # Also check for other MultilingualString indicators
            if elem_name in multilingual_element_names and element.get('lang'):
                attrs_list.append('lang')
            
            # Process child comments first
            for comment in child_comments:
                if comment.text:
                    comment_text = comment.text.strip()
                    if comment_text == 'ch-root' or 'ch-root' in comment_text:
                        has_ch_root = True
                        # If this is the root element, use its name as the parent type context
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
                        # Extract attribute list
                        attrs_str = comment_text.replace('ch-attrs:', '').strip()
                        attrs_list = [attr.strip() for attr in attrs_str.split()]
            
            # NEW: Process preceding comments (for ch-usage, ch-note, etc. that appear before the element)
            # This is especially important for Text elements in MultilingualString contexts
            for comment in preceding_comments:
                if comment.text:
                    comment_text = comment.text.strip()
                    # Only process if we haven't already found a usage from child comments
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
                            # Extract attribute list and merge with existing
                            attrs_str = comment_text.replace('ch-attrs:', '').strip()
                            new_attrs = [attr.strip() for attr in attrs_str.split()]
                            for attr in new_attrs:
                                if attr not in attrs_list:
                                    attrs_list.append(attr)
            
            # Check if this element is a MultilingualString (has text content + child Text elements)
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
                    # This is a text node
                    if hasattr(child, 'strip') and child.strip():
                        has_text_content = True
            is_multilingual = has_text_content and has_child_text_elements
            
            # NEW: Also consider elements that are known MultilingualString types based on element name
            # Even if they don't have both text and child Text elements, they should be treated as multilingual
            if elem_name in multilingual_element_names:
                # Check if parent is also a multilingual element (nested Text case)
                parent = element.getparent()
                if parent is not None:
                    parent_name = etree.QName(parent).localname
                    if parent_name in multilingual_element_names:
                        # This is a nested Text element (e.g., Text inside Text)
                        is_multilingual = True
            
            # Get XSD type info
            xsd_info = xsd_type_info.get(elem_name, {})
            card = '1..1'
            xsd_type = 'unknown'
            
            if xsd_info:
                min_occurs = xsd_info.get('min_occurs', '1')
                max_occurs = xsd_info.get('max_occurs', '1')
                card = get_cardinality(min_occurs, max_occurs)
                xsd_type = xsd_info.get('type', 'unknown')
            else:
                # NEW: Check for container patterns when XSD info is not available
                # First, get the actual parent element name from the parent_type_context
                # The parent_type_context can contain markers like "MULTILINGUAL_PARENT"
                actual_parent_name = None
                if parent_type_context:
                    # Split by | and get the first non-marker part
                    parts = parent_type_context.split('|')
                    for part in parts:
                        if part and not part.startswith('MULTILINGUAL_'):
                            actual_parent_name = part
                            break
                
                # Check if current element contains multilingual children
                is_container_of_multilingual = False
                if elem_name in multilingual_element_names:
                    # Check if this element has child Text/Description/Name elements
                    for child in element:
                        if hasattr(child, 'tag'):
                            try:
                                child_name = etree.QName(child).localname
                                if child_name in multilingual_element_names:
                                    is_container_of_multilingual = True
                                    break
                            except:
                                pass
                
                # 1. Nested multilingual elements (Text inside Text, etc.) should be 0..*
                # Also, multilingual elements that are containers should have 0..* cardinality
                if elem_name in multilingual_element_names and (is_container_of_multilingual or (actual_parent_name and actual_parent_name in multilingual_element_names)):
                    # This is a multilingual element that either:
                    # - contains nested multilingual elements (container)
                    # - is nested inside another multilingual element
                    card = '0..*'
                
                # 2. Elements inside container elements (e.g., PrivateCode inside privateCodes)
                if actual_parent_name:
                    # Simple heuristic: if parent ends with 's' and is similar to child, it's likely a container
                    if actual_parent_name and elem_name and len(actual_parent_name) > len(elem_name):
                        # Check for common container patterns
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
            
            # Keep note separate from description
            # description = note  # REMOVED: This was incorrectly using note as description
            description = ''  # Start with empty description, will be filled from XSD or other sources
            
            # For multilingual elements (Text, Description, Name, etc.), description should be empty
            # and note should contain ch-note content if it exists
            # The text content of the element itself should not be in description
            if elem_name in multilingual_element_names:
                # Clear description for multilingual elements
                description = ''
                # Text content is NOT stored in description for multilingual elements
                # Instead, the lang attribute will be added to note
            
            # Add deprecated notice if needed
            if is_deprecated:
                if note:
                    note += ' NOTE: DEPRECATED'
                else:
                    note = 'NOTE: DEPRECATED'

            # Skip forbidden and ignored elements from the output
            # But NEVER skip the root element (the one with ch-root)
            # Also never skip MultilingualString elements or their child Text elements
            # Also never skip elements with lang attribute that are part of multilingual content
            is_multilingual_element = elem_name in multilingual_element_names and element.get('lang')
            

            
            # For multilingual elements, we only want to show them if they have explicit ch-usage
            # (optional, expected, or mandatory). Elements with usage='ignored' (default) should be skipped.
            is_multilingual_with_usage = elem_name in multilingual_element_names and usage.lower() in ['optional', 'expected', 'mandatory']
            
            # For nested Text elements (Text inside Text), mark them as multilingual children
            # But still only show them if they have explicit ch-usage
            if elem_name in multilingual_element_names:
                parent = element.getparent()
                if parent is not None:
                    parent_name = etree.QName(parent).localname
                    if parent_name in multilingual_element_names:
                        # This is a nested Text element, but only show if it has explicit ch-usage
                        # Don't mark as multilingual here since we want to respect the usage
                        pass
            
            # Skip elements with usage='ignored' or 'forbidden' unless:
            # - It's the root element (has_ch_root)
            # - It's a multilingual element with explicit usage (optional, expected, mandatory)
            if usage.lower() in ['forbidden', 'ignored'] and not has_ch_root and not is_multilingual_with_usage:
                # Process children anyway in case they have different usage
                if not is_referenced:
                    for child in element:
                        if isinstance(child, etree._Element) and not isinstance(child, etree._Comment):
                            # Extend the XML path for the child
                            child_name = etree.QName(child).localname
                            child_xml_path = f"{xml_path}/{child_name}" if xml_path else child_name
                            process_element(child, level + 1, parent_type_context, child_xml_path)
                return
            
            # For multilingual elements, keep the element name simple without lang in parentheses
            display_element_name = elem_name
            
            # For multilingual elements, Note should only contain ch-note content, not lang info
            # The lang attribute is already shown in the attributes section
            # So we don't need to add it to the note
            
            elements_data.append({
                'sub': sub_markers,
                'element': display_element_name,
                'usage': usage,
                'card': card,
                'type': xsd_type,
                'description': description,
                'note': note,  # Add note to data structure
                'is_referenced': is_referenced,
                'referenced_name': see_reference or elem_name,
                'level': level,
                'attributes': attrs_list,
                'is_deprecated': is_deprecated,
                'parent_type': parent_type_context,  # Add parent type context for XSD lookup
                'xml_path': xml_path  # Add XML path from root for path-based matching
            })
            
            # Process children ONLY if not referenced
            # When an element is referenced, its children are in a separate template file
            if not is_referenced:
                # Update parent_type_context for children based on current element's type
                # Use the current element's name as the base for parent type context
                # This ensures that children have the correct parent element name for container detection
                child_parent_type = elem_name
                # Try to enhance with XSD type if available, especially for _RelStructure containers
                if xsd_info and 'type' in xsd_info and xsd_info['type']:
                    xsd_type_name = xsd_info['type']
                    # If the XSD type ends with _RelStructure, use that as it helps with container detection
                    if xsd_type_name.endswith('_RelStructure'):
                        child_parent_type = xsd_type_name
                    # Also try to find the corresponding _RelStructure type for container elements
                    elif elem_name and elem_name[0].islower() and xsd_type_name:
                        # For container elements, try to find the _RelStructure variant
                        potential_rel_type = f"{elem_name}_RelStructure"
                        if potential_rel_type in xsd_type_info:
                            child_parent_type = potential_rel_type
                
                # NEW: Check if current element is a multilingual element (Text with lang attribute)
                # If so, mark it as a multilingual parent for its children
                is_current_multilingual_parent = elem_name in multilingual_element_names and element.get('lang')
                
                for child in element:
                    # Skip comments and text nodes, only process element nodes
                    if isinstance(child, etree._Comment):
                        continue
                    if not isinstance(child, etree._Element):
                        continue
                    
                    # For MultilingualString parents, force child Text elements to be included
                    child_name = etree.QName(child).localname
                    child_is_text = (child_name == 'Text')
                    child_is_multilingual_child = (is_multilingual or is_current_multilingual_parent) and child_is_text
                    
                    # NEW: Also mark as multilingual child if parent is a multilingual element name
                    if child_is_text and elem_name in multilingual_element_names:
                        child_is_multilingual_child = True
                    
                    # Pass parent multilingual status to child via parent_type_context
                    # We'll use a special marker to indicate this
                    if child_is_multilingual_child:
                        child_parent_type = f"{child_parent_type}|MULTILINGUAL_PARENT" if child_parent_type else "MULTILINGUAL_PARENT"
                    
                    # Extend the XML path for the child
                    child_name = etree.QName(child).localname
                    child_xml_path = f"{xml_path}/{child_name}" if xml_path else child_name
                    process_element(child, level + 1, child_parent_type, child_xml_path)
        
        # Start processing from the common ancestor
        # Process the common ancestor element itself
        # Get the root element name for parent type context
        root_element_name = None
        if hasattr(root_element, 'tag') and not isinstance(root_element, etree._Comment):
            root_element_name = etree.QName(root_element).localname
        
        if hasattr(common_ancestor, 'tag') and not isinstance(common_ancestor, etree._Comment):
            # Try to enhance root element name with XSD type if available
            enhanced_root_context = root_element_name
            if root_element_name:
                # Check if there's an XSD type for this root element
                root_xsd_info = xsd_type_info.get(root_element_name, {})
                if root_xsd_info and 'type' in root_xsd_info and root_xsd_info['type']:
                    # Use the XSD type as parent context for more accurate metadata lookup
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
    
    # Maintain original document order instead of sorting
    # child_elements.sort(key=lambda x: (x['level'], x['element']))
    
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
    
    # Add root ch-note as text before the caption
    if root_note:
        markdown += f"{root_note}\n\n"
    
    # Add table caption before the table
    if root_element_name:
        markdown += f"*Table: {root_element_name}*\n\n"
    
    markdown += "| Sub | Element | Usage | Card | Type | Description | Note |\n"
    markdown += "|-----|---------|-------|------|------|-------------|------|\n"
    
    # Add root element attributes if present (they should appear at the top of the table)
    if root_attributes:
        for attr in root_attributes:
            attr_usage = 'mandatory'  # Attributes from ch-attrs are always mandatory
            attr_card = '1..1'
            attr_type = 'xsd:string'  # Default type, could be enhanced with XSD lookup
            attr_desc = f"Attribute {attr}"
            # Sanitize description to prevent table breaks from newlines
            attr_desc = sanitize_for_markdown(attr_desc)
            markdown += f"|  | @{attr} | {attr_usage} | {attr_card} | {attr_type} | {attr_desc} | |\n"
    
    # Process top-level elements first
    for item in top_level_elements:
        # Skip root element (level 0) as it's now in the caption
        if item['level'] == 0:
            continue
        
        sub = item['sub']
        element = item['element']
        usage = item['usage']
        card = item['card']
        xsd_type = item['type']
        description = item['description']
        note = item.get('note', '')
        
        # Get XSD info for the element
        xsd_info = xsd_type_info.get(element, {})
        
        # Get parent_type and xml_path for context-aware metadata lookup
        parent_type = item.get('parent_type')
        xml_path = item.get('xml_path')
        
        # NEW: Try path-based XSD element lookup using the new function
        path_based_metadata = None
        if xsd_doc and xml_path:
            path_based_metadata = get_element_metadata_from_xsd_by_path(xsd_doc, xml_path)
        
        # Try path-based matching from pre-built paths as fallback
        xsd_paths = xsd_type_info.get('_paths', {})
        if not path_based_metadata and xml_path and xsd_paths:
            path_result = find_best_xsd_path_match(xsd_paths, xml_path, element)
            if path_result:
                path, path_metadata = path_result
                path_based_metadata = path_metadata
        
        # NEW: Use path-based metadata first if available
        if path_based_metadata:
            if not card or card == '1..1':
                card = get_cardinality(path_based_metadata.get('min_occurs', '1'), path_based_metadata.get('max_occurs', '1'))
            if not xsd_type or xsd_type == 'unknown':
                xsd_type = path_based_metadata.get('type', xsd_type)
            if not description:
                description = path_based_metadata.get('description', description)
        
        # Try enhanced metadata extraction first if we have XSD path and parent_type
        # This ensures we get context-specific metadata before falling back to generic info
        if xsd_path and (not path_based_metadata or (card == '1..1' and xsd_type == 'unknown' and not description)):
            metadata = get_element_metadata(xsd_path, element, parent_type)
            if metadata:
                if not card or card == '1..1':
                    card = metadata.get('cardinality', card)
                if not xsd_type or xsd_type == 'unknown':
                    xsd_type = metadata.get('type', xsd_type)
                if not description:
                    description = metadata.get('description', description)
            
            # If we didn't get metadata from parent_type context but have path-based metadata, use it
            if not metadata and path_based_metadata:
                metadata = path_based_metadata
                if not card or card == '1..1':
                    card = metadata.get('min_occurs', card)
                    max_occurs = metadata.get('max_occurs', '1')
                    if card == '1..1':
                        card = get_cardinality(metadata.get('min_occurs', '1'), metadata.get('max_occurs', '1'))
                if not xsd_type or xsd_type == 'unknown':
                    xsd_type = metadata.get('type', xsd_type)
                if not description:
                    description = metadata.get('description', description)
        
        # Only use generic xsd_type_info if we didn't get metadata from context-specific lookup
        # AND parent_type was not specified (for top-level elements)
        # If we have a parent_type but no metadata, don't use generic xsd_info to avoid wrong context
        if not parent_type and not path_based_metadata:
            # For elements without parent context, use generic xsd_info
            if xsd_info:
                # Use XSD description if available
                xsd_description = xsd_info.get('description', '')
                if xsd_description and not description:
                    description = xsd_description
                    note = xsd_description
                
                # Use XSD cardinality if available
                if 'min_occurs' in xsd_info and 'max_occurs' in xsd_info:
                    if card == '1..1' or not card:  # Only use if we don't have better info
                        card = get_cardinality(xsd_info['min_occurs'], xsd_info['max_occurs'])
                
                # Use XSD type if available
                if 'type' in xsd_info and (not xsd_type or xsd_type == 'unknown'):
                    xsd_type = xsd_info['type']
        # If we have parent_type but didn't get metadata from get_element_metadata,
        # and description is still empty, try generic xsd_info as fallback
        # BUT only for type, NOT for description (to avoid wrong context descriptions)
        elif not metadata and xsd_info:
            # Don't use xsd_info description for elements with parent_type to avoid wrong context
            # Only use type and cardinality from xsd_info
            if 'min_occurs' in xsd_info and 'max_occurs' in xsd_info:
                if card == '1..1' or not card:
                    card = get_cardinality(xsd_info['min_occurs'], xsd_info['max_occurs'])
            if 'type' in xsd_info and (not xsd_type or xsd_type == 'unknown'):
                xsd_type = xsd_info['type']
        
        # NEW: Override cardinality for container elements based on parent_type and element type
        # This handles cases where XSD says 0..1 but we need 0..* for multilingual/container elements
        multilingual_element_names = ['Text', 'Description', 'Name', 'ShortName', 'Label', 'Title', 'Subtitle']
        
        # Check for multilingual container patterns
        if element in multilingual_element_names:
            # Extract parent name from parent_type
            actual_parent_name = None
            if parent_type:
                parts = parent_type.split('|')
                for part in parts:
                    if part and not part.startswith('MULTILINGUAL_'):
                        actual_parent_name = part
                        break
            
            # Only set to 0..* if the parent is ALSO a multilingual element (nested Text, etc.)
            # NOT if xsd_type is MultilingualString - the cardinality should come from the XSD declaration
            if actual_parent_name in multilingual_element_names:
                # This is a nested multilingual element (e.g., Text inside Text), should be 0..*
                card = '0..*'
        
        # Check for known container patterns
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
                
                # NEW: Check if parent corresponds to a _RelStructure type
                # Containers like quays, stopPlaces, etc. have types like quays_RelStructure, stopPlaces_RelStructure
                # All such containers should have 0..* or 1..* cardinality for their child elements
                if not (card.startswith('0..*') or card.startswith('1..*')):
                    # Check if there's a complex type matching parent_type with _RelStructure
                    # This handles containers like quays, stopPlaces, etc.
                    if (parent_type and '_RelStructure' in parent_type) or (actual_parent_name and ('_RelStructure' in actual_parent_name or actual_parent_name.endswith('_RelStructure'))):
                        card = '0..*'
                    else:
                        # Also check if parent_type + _RelStructure exists as a complex type
                        # For example, parent_type="quays" should match complex type "quays_RelStructure"
                        # We'll do a simple string check - if parent_type looks like a container (lowercase first letter)
                        # and the element matches the singular form, assume it's a container
                        if actual_parent_name and actual_parent_name[0].islower():
                            # Check if element is the singular form of parent (e.g., quays -> Quay)
                            # Simple heuristic: parent ends with 's' and element is parent without 's'
                            if actual_parent_name.endswith('s') and element == actual_parent_name[:-1]:
                                card = '0..*'
                            # Also handle irregular plurals or other patterns
                            # Note: 'names' removed because Name should have its own cardinality from XSD
                            elif actual_parent_name in ['quays', 'stopPlaces', 'facilities', 'privateCodes', 
                                                        'alternativeNames', 'alternativeTexts',
                                                        'descriptions', 'texts', 'localServices']:
                                card = '0..*'
        
        # Handle versionRef -> version conversion for display
        if element.endswith('Ref') and 'versionRef=' in description:
            # Replace versionRef with version in the description
            description = description.replace('versionRef=', 'version=')
        
        # Create link if referenced
        if item['is_referenced']:
            link_name = item['referenced_name']
            element = f"[{element}]({link_name}.md)"
        
        # Use the note from the data structure (which contains ch-note content)
        display_note = item.get('note', '')
        # Ensure xsd_type is never None
        display_type = xsd_type if xsd_type and xsd_type != 'None' else 'unknown'
        # Sanitize description and note to prevent table breaks from newlines
        description = sanitize_for_markdown(description)
        display_note = sanitize_for_markdown(display_note)
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
        # Ensure xsd_type is never None for attributes
        display_type = xsd_type if xsd_type and xsd_type != 'None' else 'unknown'
        # Sanitize description and note to prevent table breaks from newlines
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
        
        # Get parent_type and xml_path for context-aware metadata lookup
        parent_type = item.get('parent_type')
        xml_path = item.get('xml_path')
        
        # NEW: Try path-based XSD element lookup using the new function first
        path_based_metadata = None
        if xsd_doc and xml_path:
            path_based_metadata = get_element_metadata_from_xsd_by_path(xsd_doc, xml_path)
        
        # Try path-based matching from pre-built paths as fallback
        xsd_paths = xsd_type_info.get('_paths', {})
        if not path_based_metadata and xml_path and xsd_paths:
            path_result = find_best_xsd_path_match(xsd_paths, xml_path, element)
            if path_result:
                path, path_metadata = path_result
                path_based_metadata = path_metadata
        
        # NEW: Use path-based metadata first if available
        if path_based_metadata:
            if not card or card == '1..1':
                card = get_cardinality(path_based_metadata.get('min_occurs', '1'), path_based_metadata.get('max_occurs', '1'))
            if not xsd_type or xsd_type == 'unknown':
                xsd_type = path_based_metadata.get('type', xsd_type)
            if not description:
                description = path_based_metadata.get('description', description)
        
        # Try enhanced metadata extraction first if we have XSD path and parent_type
        # This ensures we get context-specific metadata before falling back to generic info
        if xsd_path and (not path_based_metadata or (card == '1..1' and xsd_type == 'unknown' and not description)):
            metadata = get_element_metadata(xsd_path, element, parent_type)
            if metadata:
                if not card or card == '1..1':
                    card = metadata.get('cardinality', card)
                if not xsd_type or xsd_type == 'unknown':
                    xsd_type = metadata.get('type', xsd_type)
                if not description:
                    description = metadata.get('description', description)
            
            # If we didn't get metadata from parent_type context but have path-based metadata, use it
            if not metadata and path_based_metadata:
                metadata = path_based_metadata
                if not card or card == '1..1':
                    card = get_cardinality(metadata.get('min_occurs', '1'), metadata.get('max_occurs', '1'))
                if not xsd_type or xsd_type == 'unknown':
                    xsd_type = metadata.get('type', xsd_type)
                if not description:
                    description = metadata.get('description', description)
        
        # Get XSD info for the element
        xsd_info = xsd_type_info.get(element, {})
        
        # Only use generic xsd_type_info if we didn't get metadata from context-specific lookup
        # AND parent_type was not specified (for top-level elements)
        # If we have a parent_type but no metadata, don't use generic xsd_info to avoid wrong context
        if not parent_type and not path_based_metadata:
            # For elements without parent context, use generic xsd_info
            if xsd_info:
                # Use XSD description if available
                xsd_description = xsd_info.get('description', '')
                if xsd_description and not description:
                    description = xsd_description
                
                # Use XSD cardinality if available
                if 'min_occurs' in xsd_info and 'max_occurs' in xsd_info:
                    if card == '1..1' or not card:
                        card = get_cardinality(xsd_info['min_occurs'], xsd_info['max_occurs'])
                
                # Use XSD type if available
                if 'type' in xsd_info and (not xsd_type or xsd_type == 'unknown'):
                    xsd_type = xsd_info['type']
        # If we have parent_type but didn't get metadata from get_element_metadata,
        # and description is still empty, try generic xsd_info as fallback
        # BUT only for type, NOT for description (to avoid wrong context descriptions)
        elif not metadata and xsd_info:
            # Don't use xsd_info description for elements with parent_type to avoid wrong context
            # Only use type and cardinality from xsd_info
            if 'min_occurs' in xsd_info and 'max_occurs' in xsd_info:
                if card == '1..1' or not card:
                    card = get_cardinality(xsd_info['min_occurs'], xsd_info['max_occurs'])
            if 'type' in xsd_info and (not xsd_type or xsd_type == 'unknown'):
                xsd_type = xsd_info['type']
        
        # NEW: Override cardinality for container elements based on parent_type and element type
        # This handles cases where XSD says 0..1 but we need 0..* for multilingual/container elements
        multilingual_element_names = ['Text', 'Description', 'Name', 'ShortName', 'Label', 'Title', 'Subtitle']
        
        # Check for multilingual container patterns
        if element in multilingual_element_names:
            # Extract parent name from parent_type
            actual_parent_name = None
            if parent_type:
                parts = parent_type.split('|')
                for part in parts:
                    if part and not part.startswith('MULTILINGUAL_'):
                        actual_parent_name = part
                        break
            
            # Only set to 0..* if the parent is ALSO a multilingual element (nested Text, etc.)
            # NOT if xsd_type is MultilingualString - the cardinality should come from the XSD declaration
            if actual_parent_name in multilingual_element_names:
                # This is a nested multilingual element (e.g., Text inside Text), should be 0..*
                card = '0..*'
        
        # Check for known container patterns
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
                
                # NEW: Check if parent corresponds to a _RelStructure type
                # Containers like quays, stopPlaces, etc. have types like quays_RelStructure, stopPlaces_RelStructure
                # All such containers should have 0..* or 1..* cardinality for their child elements
                if not (card.startswith('0..*') or card.startswith('1..*')):
                    # Check if there's a complex type matching parent_type with _RelStructure
                    # This handles containers like quays, stopPlaces, etc.
                    if (parent_type and '_RelStructure' in parent_type) or (actual_parent_name and ('_RelStructure' in actual_parent_name or actual_parent_name.endswith('_RelStructure'))):
                        card = '0..*'
                    else:
                        # Also check if parent_type + _RelStructure exists as a complex type
                        # For example, parent_type="quays" should match complex type "quays_RelStructure"
                        # We'll do a simple string check - if parent_type looks like a container (lowercase first letter)
                        # and the element matches the singular form, assume it's a container
                        if actual_parent_name and actual_parent_name[0].islower():
                            # Check if element is the singular form of parent (e.g., quays -> Quay)
                            # Simple heuristic: parent ends with 's' and element is parent without 's'
                            if actual_parent_name.endswith('s') and element == actual_parent_name[:-1]:
                                card = '0..*'
                            # Also handle irregular plurals or other patterns
                            # Note: 'names' removed because Name should have its own cardinality from XSD
                            elif actual_parent_name in ['quays', 'stopPlaces', 'facilities', 'privateCodes', 
                                                        'alternativeNames', 'alternativeTexts',
                                                        'descriptions', 'texts', 'localServices']:
                                card = '0..*'
        
        # Handle versionRef -> version conversion for display
        if element.endswith('Ref') and 'versionRef=' in description:
            # Replace versionRef with version in the description
            description = description.replace('versionRef=', 'version=')
        
        # Create link if referenced
        if item['is_referenced']:
            link_name = item['referenced_name']
            element = f"[{element}]({link_name}.md)"
        
        # Use description for XSD/type info, note for ch-note content only
        display_note = note if note else ''
        # Ensure xsd_type is never None for child elements
        display_type = xsd_type if xsd_type and xsd_type != 'None' else 'unknown'
        # Sanitize description and note to prevent table breaks from newlines
        description = sanitize_for_markdown(description)
        display_note = sanitize_for_markdown(display_note)
        markdown += f"| {sub} | {element} | {usage} | {card} | {display_type} | {description} | {display_note} |\n"
        
        # Add attributes if present
        if item['attributes']:
            for attr in item['attributes']:
                attr_usage = 'mandatory'  # Attributes from ch-attrs are always mandatory
                attr_card = '1..1'
                attr_type = 'xsd:string'  # Default type, could be enhanced with XSD lookup
                attr_desc = f"Attribute {attr}"
                # Sanitize attribute description to prevent table breaks from newlines
                attr_desc = sanitize_for_markdown(attr_desc)
                
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


def process_ch_profile_templates(input_dir: str, output_dir: str, xsd_path: str, xsd_type_info):
    """Process ch-profile template files and generate MD files"""
    ch_profile_files = [f for f in os.listdir(input_dir) if f.startswith('ch-profile_') and f.endswith('.xml')]
    
    for xml_file in ch_profile_files:
        print(f"Processing ch-profile template: {xml_file}")
        file_path = os.path.join(input_dir, xml_file)
        
        # Parse template
        data = parse_template_file(file_path, xsd_type_info)
        
        if data:
            # Generate markdown filename (remove .xml, add .md)
            md_filename = os.path.splitext(xml_file)[0] + '.md'
            md_path = os.path.join(output_dir, md_filename)
            
            # Generate markdown content
            element_name = os.path.splitext(xml_file)[0]
            markdown_content = generate_markdown_table(data, element_name, xsd_path, xsd_type_info)
            
            # Write to file
            with open(md_path, 'w', encoding='utf-8') as f:
                f.write(markdown_content)
            
            print(f"Generated ch-profile MD: {md_path}")
        else:
            print(f"No data extracted from ch-profile template {xml_file}")


def build_markdown_tables(input_path: str, output_path: str, xsd_path: str):

    # Load XSD type information
    print(f"Loading XSD from {xsd_path}")
    xsd_type_info = load_xsd_type_info(xsd_path)
    print(f"Loaded {len(xsd_type_info)} type definitions")

    # Create output directory
    os.makedirs(output_path, exist_ok=True)
    
    # Process ch-profile templates first
    process_ch_profile_templates(input_path, output_path, xsd_path, xsd_type_info)
    
    # Process all XML files in input directory
    xml_files = [f for f in os.listdir(input_path) if f.endswith('.xml') and not f.startswith('ch-profile_')]
    
    for xml_file in xml_files:
        print(f"Processing {xml_file}")
        file_path = os.path.join(input_path, xml_file)
        
        # Parse template
        data = parse_template_file(file_path, xsd_type_info)
        
        if data:
            # Check for missing referenced files
            check_referenced_files_exist(data, input_path)
            
            # Generate markdown filename (remove .xml, add .md)
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
    
    print(f"Processed {len(xml_files)} files")

def parse_args():
    """Parse command line arguments"""
    parser = argparse.ArgumentParser(description='Generate markdown documentation from NeTEx templates')
    parser.add_argument('-i', '--input', default=TEMPLATES_DIR, help=f'Input folder containing XML templates (Default = {TEMPLATES_DIR})')
    parser.add_argument('-o', '--output', default=SITE_TABLES_DIR, help=f'Output folder for markdown files (Default = {SITE_TABLES_DIR})')
    parser.add_argument('-x', '--xsd', default=XSD_FILE_PATH, help=f'XSD schema file for type information (Default = {XSD_FILE_PATH})')
    return parser.parse_args()

def main():
    args = parse_args()
    build_markdown_tables(args.input, args.output, args.xsd)

if __name__ == '__main__':
    main()