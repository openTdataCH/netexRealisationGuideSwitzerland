#!/usr/bin/env python3
"""
Markdown Builder for NeTEx templates
Extracts documentation from annotated XML templates and generates markdown tables
with type information from XSD schemas.
"""

import os
import sys
import argparse
from lxml import etree
from collections import defaultdict
import re


def parse_args():
    """Parse command line arguments"""
    parser = argparse.ArgumentParser(description='Generate markdown documentation from NeTEx templates')
    parser.add_argument('-i', '--input', required=True, help='Input folder containing XML templates')
    parser.add_argument('-o', '--output', required=True, help='Output folder for markdown files')
    parser.add_argument('-x', '--xsd', required=True, help='XSD schema file for type information')
    return parser.parse_args()


def load_xsd_type_info(xsd_path):
    """Load type and cardinality information from XSD"""
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


def _process_xsd_file(xsd_path, base_dir, processed_files=None):
    """Process an XSD file and all its imports/includes recursively"""
    if processed_files is None:
        processed_files = set()
    
    # Avoid circular processing
    if xsd_path in processed_files:
        return {}
    processed_files.add(xsd_path)
    
    type_info = {}
    
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
                else:
                    print(f"Import not found: {import_path}")
        
        # Process includes
        for include_elem in xsd_root.findall('xs:include', namespaces={'xs': 'http://www.w3.org/2001/XMLSchema'}):
            schema_location = include_elem.get('schemaLocation')
            if schema_location:
                # Resolve relative paths relative to the current file's directory
                include_path = os.path.normpath(os.path.join(current_dir, schema_location))
                if os.path.exists(include_path):
                    print(f"Processing include: {include_path}")
                    included_types = _process_xsd_file(include_path, base_dir, processed_files)
                    type_info.update(included_types)
                else:
                    print(f"Include not found: {include_path}")
        
        # Extract complex types
        for complex_type in xsd_root.findall('.//xs:complexType', namespaces=ns):
            name = complex_type.get('name')
            if name:
                type_info[name] = {'type': 'complex', 'elements': {}, 'description': ''}
                
                # Extract documentation/description
                annotation = complex_type.find('xs:annotation', namespaces=ns)
                if annotation is not None:
                    doc = annotation.find('xs:documentation', namespaces=ns)
                    if doc is not None and doc.text:
                        type_info[name]['description'] = doc.text.strip()
                
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
                                elem_description = elem_doc.text.strip()
                        
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
                        type_info[name]['description'] = doc.text.strip()
        
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
                        elem_description = doc.text.strip()
                
                type_info[name] = {
                    'type': elem_type,
                    'min_occurs': min_occurs,
                    'max_occurs': max_occurs,
                    'element_type': 'top_level',
                    'description': elem_description
                }
        
        return type_info
    except Exception as e:
        print(f"Error processing {xsd_path}: {e}")
        return {}
    
    except Exception as e:
        print(f"Error loading XSD: {e}")
        return {}


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


def search_xsd_files_for_element(base_dir, element_name):
    """Search all XSD files in the directory structure for a specific element"""
    namespaces = {'xs': 'http://www.w3.org/2001/XMLSchema'}
    
    # Search through all XSD files in the directory tree
    for root, dirs, files in os.walk(base_dir):
        for file in files:
            if file.endswith('.xsd'):
                file_path = os.path.join(root, file)
                try:
                    parser = etree.XMLParser()
                    xsd_doc = etree.parse(file_path, parser)
                    
                    # Look for the element - try both with and without namespace
                    element_xpath = f"//xs:element[@name='{element_name}']"
                    elements = xsd_doc.xpath(element_xpath, namespaces=namespaces)
                    
                    # If not found, try without namespace
                    if not elements:
                        element_xpath_no_ns = f"//*[local-name()='element' and @name='{element_name}']"
                        elements = xsd_doc.xpath(element_xpath_no_ns)
                    
                    if elements:
                        return file_path  # Return the file path where element was found
                        
                except Exception as e:
                    # Skip files that can't be parsed
                    continue
    
    return None


def get_element_metadata(xsd_path, element_name):
    """Extract detailed metadata for an element from XSD using XPath with substitution group support"""
    try:
        # First try to find the element in the main XSD file
        parser = etree.XMLParser()
        xsd_doc = etree.parse(xsd_path, parser)
        namespaces = {'xs': 'http://www.w3.org/2001/XMLSchema'}
        
        # Try to find the element in the main file
        element_xpath = f"//xs:element[@name='{element_name}']"
        element = xsd_doc.xpath(element_xpath, namespaces=namespaces)
        
        # If not found in main file, search all XSD files in the directory
        if not element:
            base_dir = os.path.dirname(os.path.abspath(xsd_path))
            found_in_file = search_xsd_files_for_element(base_dir, element_name)
            if found_in_file is not None:
                # Parse the file where the element was found
                xsd_doc = etree.parse(found_in_file, parser)
                # Find the element in this document
                element_xpath = f"//xs:element[@name='{element_name}']"
                element = xsd_doc.xpath(element_xpath, namespaces=namespaces)
                
                # If not found, try without namespace
                if not element:
                    element_xpath_no_ns = f"//*[local-name()='element' and @name='{element_name}']"
                    element = xsd_doc.xpath(element_xpath_no_ns)
        
        if not element:
            return None
        
        element = element[0]
        
        # Debug: print what we found (commented out by default)
        # print(f"DEBUG: Found element {element_name} with tag {element.tag}, attributes {element.attrib}")
        
        # Get cardinality - use element's own if available, otherwise traverse substitution group
        min_occurs = element.get('minOccurs', '1')
        max_occurs = element.get('maxOccurs', '1')
        cardinality = get_cardinality(min_occurs, max_occurs)
        
        # Get type - check substitution group chain recursively
        element_type = "unknown"
        current_element = element
        visited_elements = set()  # Prevent infinite loops
        
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
                element_type = "inline simpleType"
                break
            elif complex_type is not None:
                element_type = "inline complexType"
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
                        description += " \n" + doc.text.strip()
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
            'description': description or ""
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
        # ch-profile templates may have comments at root level
        has_ch_see = any('ch-see' in (comment.text.strip() if comment.text else '') 
                               for comment in comments)
        
        if not root_element and has_ch_see:
            # This is a ch-profile template, use root as the element
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
        
        def process_element(element, level=0):
            """Recursively process an element and its children"""
            # Handle namespace properly
            if hasattr(element, 'tag'):
                elem_name = etree.QName(element).localname
            else:
                return  # Skip non-element nodes
            elem_id = element.get('id')
            
            # Skip if already processed (avoid duplicates)
            elem_key = f"{elem_name}_{elem_id}" if elem_id else elem_name
            if elem_key in processed_elements:
                return
            processed_elements.add(elem_key)
            
            # Get comments for this element
            usage = 'ignored'
            note = ''
            is_referenced = False
            see_reference = None
            
            # Get comments that are direct children of this element (before any child elements)
            # These are the comments that describe the element itself
            child_comments = element.xpath('comment()')
            is_deprecated = False
            attrs_list = []
            
            for comment in child_comments:
                if comment.text:
                    comment_text = comment.text.strip()
                    if comment_text.startswith('ch-usage:'):
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
            
            # Get XSD type info
            xsd_info = xsd_type_info.get(elem_name, {})
            card = '1..1'
            xsd_type = 'unknown'
            
            if xsd_info:
                min_occurs = xsd_info.get('min_occurs', '1')
                max_occurs = xsd_info.get('max_occurs', '1')
                card = get_cardinality(min_occurs, max_occurs)
                xsd_type = xsd_info.get('type', 'unknown')
            
            # Determine sub level markers - use + for indentation
            sub_markers = ''
            if level > 0:
                sub_markers = '+' * level
            
            # Keep note separate from description
            # description = note  # REMOVED: This was incorrectly using note as description
            description = ''  # Start with empty description, will be filled from XSD or other sources
            
            # Add deprecated notice if needed
            if is_deprecated:
                if note:
                    note += ' NOTE: DEPRECATED'
                else:
                    note = 'NOTE: DEPRECATED'

            # Skip forbidden and ignored elements from the output
            if usage.lower() in ['forbidden', 'ignored']:
                # Process children anyway in case they have different usage
                if not is_referenced:
                    for child in element:
                        if isinstance(child, etree._Element) and not isinstance(child, etree._Comment):
                            process_element(child, level + 1)
                return
            
            elements_data.append({
                'sub': sub_markers,
                'element': elem_name,
                'usage': usage,
                'card': card,
                'type': xsd_type,
                'description': description,
                'note': note,  # Add note to data structure
                'is_referenced': is_referenced,
                'referenced_name': see_reference or elem_name,
                'level': level,
                'attributes': attrs_list,
                'is_deprecated': is_deprecated
            })
            
            # Process children ONLY if not referenced
            # When an element is referenced, its children are in a separate template file
            if not is_referenced:
                for child in element:
                    # Only process actual elements, skip comments and text nodes
                    if isinstance(child, etree._Element) and not isinstance(child, etree._Comment):
                        process_element(child, level + 1)
        
        # Start processing from the common ancestor
        # Process the common ancestor element itself
        if hasattr(common_ancestor, 'tag') and not isinstance(common_ancestor, etree._Comment):
            process_element(common_ancestor)
        
        return elements_data
    
    except Exception as e:
        print(f"Error processing {file_path}: {e}")
        return None


def generate_markdown_table(data, filename, xsd_type_info):
    """Generate markdown table from parsed data"""
    if not data:
        return ''
    
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
    
    markdown = f"# {filename}\n\n"
    markdown += "| Sub | Element | Usage | Card | Type | Description | Note |\n"
    markdown += "|-----|---------|-------|------|------|-------------|------|\n"
    
    # Process top-level elements first
    for item in top_level_elements:
        sub = item['sub']
        element = item['element']
        usage = item['usage']
        card = item['card']
        xsd_type = item['type']
        description = item['description']
        note = item.get('note', '')
        
        # Get XSD info for the element
        xsd_info = xsd_type_info.get(element, {})
        if xsd_info:
            # Use XSD description if available
            xsd_description = xsd_info.get('description', '')
            if xsd_description and not description:
                description = xsd_description
                note = xsd_description
            
            # Use XSD cardinality if available
            if 'min_occurs' in xsd_info and 'max_occurs' in xsd_info:
                card = get_cardinality(xsd_info['min_occurs'], xsd_info['max_occurs'])
            
            # Use XSD type if available
            if 'type' in xsd_info:
                xsd_type = xsd_info['type']
        
        # Try enhanced metadata extraction if still unknown and we have XSD path
        if xsd_type == 'unknown' and 'xsd_path' in globals():
            metadata = get_element_metadata(xsd_path, element)
            if metadata:
                if not card or card == '1..1':
                    card = metadata.get('cardinality', card)
                if xsd_type == 'unknown':
                    xsd_type = metadata.get('type', xsd_type)
                if not description:
                    description = metadata.get('description', description)
        
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
        markdown += f"| {sub} | {element} | {usage} | {card} | {xsd_type} | {description} | {display_note} |\n"
    
    # Process attributes
    for item in attributes:
        sub = item['sub']
        element = item['element']
        usage = item['usage']
        card = item['card']
        xsd_type = item['type']
        description = item['description']
        note = item.get('note', '')
        
        markdown += f"| {sub} | {element} | {usage} | {card} | {xsd_type} | {description} | {note} |\n"
    
    # Process child elements
    for item in child_elements:
        sub = item['sub']
        element = item['element']
        usage = item['usage']
        card = item['card']
        xsd_type = item['type']
        description = item['description']
        note = item.get('note', '')
        
        # Get XSD info for the element
        xsd_info = xsd_type_info.get(element, {})
        if xsd_info:
            # Use XSD description if available
            xsd_description = xsd_info.get('description', '')
            if xsd_description and not description:
                description = xsd_description
                # Don't overwrite note with XSD description - keep the ch-note content
            
            # Use XSD cardinality if available
            if 'min_occurs' in xsd_info and 'max_occurs' in xsd_info:
                card = get_cardinality(xsd_info['min_occurs'], xsd_info['max_occurs'])
            
            # Use XSD type if available
            if 'type' in xsd_info:
                xsd_type = xsd_info['type']
        
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
        markdown += f"| {sub} | {element} | {usage} | {card} | {xsd_type} | {description} | {display_note} |\n"
        
        # Add attributes if present
        if item['attributes']:
            for attr in item['attributes']:
                attr_usage = 'mandatory'  # Attributes from ch-attrs are always mandatory
                attr_card = '1..1'
                attr_type = 'xsd:string'  # Default type, could be enhanced with XSD lookup
                attr_desc = f"Attribute {attr}"
                
                markdown += f"| {sub} | @{attr} | {attr_usage} | {attr_card} | {attr_type} | {attr_desc} | |\n"
    
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


def process_ch_profile_templates(input_dir, output_dir, xsd_type_info):
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
            markdown_content = generate_markdown_table(data, element_name, xsd_type_info)
            
            # Write to file
            with open(md_path, 'w', encoding='utf-8') as f:
                f.write(markdown_content)
            
            print(f"Generated ch-profile MD: {md_path}")
        else:
            print(f"No data extracted from ch-profile template {xml_file}")


def main():
    args = parse_args()
    
    # Load XSD type information
    print(f"Loading XSD from {args.xsd}")
    xsd_type_info = load_xsd_type_info(args.xsd)
    print(f"Loaded {len(xsd_type_info)} type definitions")
    
    # Store XSD path for metadata extraction
    xsd_path = args.xsd
    
    # Create output directory
    os.makedirs(args.output, exist_ok=True)
    
    # Process ch-profile templates first
    process_ch_profile_templates(args.input, args.output, xsd_type_info)
    
    # Process all XML files in input directory
    xml_files = [f for f in os.listdir(args.input) if f.endswith('.xml') and not f.startswith('ch-profile_')]
    
    for xml_file in xml_files:
        print(f"Processing {xml_file}")
        file_path = os.path.join(args.input, xml_file)
        
        # Parse template
        data = parse_template_file(file_path, xsd_type_info)
        
        if data:
            # Check for missing referenced files
            check_referenced_files_exist(data, args.input)
            
            # Generate markdown filename (remove .xml, add .md)
            md_filename = os.path.splitext(xml_file)[0] + '.md'
            md_path = os.path.join(args.output, md_filename)
            
            # Generate markdown content
            element_name = os.path.splitext(xml_file)[0]
            markdown_content = generate_markdown_table(data, element_name, xsd_type_info)
            
            # Write to file
            with open(md_path, 'w', encoding='utf-8') as f:
                f.write(markdown_content)
            
            print(f"Generated {md_path}")
        else:
            print(f"No data extracted from {xml_file}")
    
    print(f"Processed {len(xml_files)} files")


if __name__ == '__main__':
    main()