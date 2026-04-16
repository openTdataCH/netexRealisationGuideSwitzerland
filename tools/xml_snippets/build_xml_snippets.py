#!/usr/bin/env python3
"""
build_xml_snippets.py

Parses XML templates and extracts snippets between ch-start and ch-stop comments.
Removes ch-annotations except for ch-note and ch-notice (keeping only the content).
Excludes elements marked with ch-usage: forbidden or ch-usage: ignored.

Usage:
    python build_xml_snippets.py -i INPUT_FOLDER -o OUTPUT_FOLDER

Example:
    python build_xml_snippets.py -i templates -o generated/xml-snippets
"""

import os
import sys
import argparse
import re
from lxml import etree

def parse_args():
    """Parse command line arguments"""
    parser = argparse.ArgumentParser(
        description='Extract XML snippets from templates with ch-start/ch-stop markers'
    )
    parser.add_argument(
        '-i', '--input', 
        required=True, 
        help='Input folder containing XML templates'
    )
    parser.add_argument(
        '-o', '--output',
        required=True,
        help='Output folder for XML snippet files'
    )
    return parser.parse_args()

def remove_ch_annotations(text):
    """Remove ch-annotations except for ch-note and ch-notice content"""
    if not isinstance(text, str):
        text = str(text)
    
    # Remove all ch-comments except ch-note and ch-notice
    lines = text.split('\n')
    cleaned_lines = []
    
    for line in lines:
        stripped = line.strip()

        
        # Keep ch-note content (remove the prefix)
        if stripped.startswith('<!-- ch-note:'):
            # Extract the content after the prefix
            content = re.sub(r'<!--\s*ch-note:\s*', '<!-- ', stripped)
            # Remove trailing --> and add it back
            content = re.sub(r'\s*-->$', ' -->', content)
            cleaned_lines.append(content)
        # Also keep comments that look like notes but might be missing ch- prefix
        elif re.match(r'<!--\s*(note|Notice):\s*.*-->$', stripped):
            # Keep these as regular comments
            cleaned_lines.append(line)
        # Remove all other ch-comments
        elif stripped.startswith('<!-- ch-') or re.match(r'<!--\s*usage:', stripped):
            # Check if there's text content after the comment on the same line
            comment_end_match = re.search(r'-->', stripped)
            if comment_end_match:
                comment_end = comment_end_match.end()
                text_after_comment = stripped[comment_end:].strip()
                if text_after_comment:
                    # Preserve the text content after the comment
                    cleaned_lines.append(text_after_comment)
            # Don't append the comment itself
        else:
            cleaned_lines.append(line)
    
    return '\n'.join(cleaned_lines)

def should_exclude_element(element):
    """Check if element should be excluded based on ch-usage annotations"""
    # Safety check
    if not hasattr(element, 'xpath'):
        return False
    
    # Check for forbidden/ignored usage in comments
    try:
        # Check preceding sibling comments
        for comment in element.xpath('preceding-sibling::comment()[1]'):
            if comment.text and ('usage: forbidden' in comment.text or 'usage: ignored' in comment.text):
                return True
        
        # Check child comments
        for comment in element.xpath('comment()[1]'):
            if comment.text and ('usage: forbidden' in comment.text or 'usage: ignored' in comment.text):
                return True
        
        # Check parent's comments (immediate preceding sibling)
        parent = element.getparent()
        if parent is not None:
            prev = element.getprevious()
            if isinstance(prev, etree._Comment) and prev.text:
                if 'usage: forbidden' in prev.text or 'usage: ignored' in prev.text:
                    return True
    except Exception:
        pass  # Silently ignore any errors
    
    return False

def process_element(element, parent_excluded=False):
    """Process an element and its children, excluding forbidden/ignored elements"""

    if parent_excluded:
        # If parent is excluded, all children are excluded too
        return None
    
    # Check if this element should be excluded
    if should_exclude_element(element):
        return None
    
    # Create a copy of the element to avoid modifying the original
    if not hasattr(element, 'tag'):

        return None
    

    new_element = etree.Element(element.tag, attrib=element.attrib)
    
def process_element_with_cleanup(element, parent_excluded=False):
    """Process an element and its children, excluding forbidden/ignored elements and removing ch-annotations"""
    # Skip comments (but preserve their tail text if they're children of an element)
    if isinstance(element, etree._Comment):
        return None
    
    if parent_excluded:
        # If parent is excluded, all children are excluded too
        return None
    
    # Check if this element should be excluded
    if should_exclude_element(element):
        return None
    
    # Create a copy of the element to avoid modifying the original
    if not hasattr(element, 'tag'):
        return None
    
    # Handle versionRef -> version attribute conversion
    attrib = dict(element.attrib)
    if 'versionRef' in attrib and 'version' not in attrib:
        # Convert versionRef to version
        attrib['version'] = attrib['versionRef']
        del attrib['versionRef']
    
    new_element = etree.Element(element.tag, attrib=attrib)
    
    # Preserve the element's own text content
    if element.text and element.text.strip():
        new_element.text = element.text.strip()
    
    # Process children
    for child in element:
        if isinstance(child, etree._Comment):
            # Handle comments - keep only ch-note content
            if child.text:
                comment_text = child.text.strip()
                if comment_text.startswith('ch-note:'):
                    # Convert to regular comment
                    content = re.sub(r'ch-note:\s*', '', comment_text)
                    new_comment = etree.Comment(f' {content} ')
                    new_element.append(new_comment)
                # Preserve tail text of ALL comments (not just ch-note)
                if child.tail and child.tail.strip():
                    # Add the tail text as text content of the new element
                    if new_element.text:
                        new_element.text += ' ' + child.tail.strip()
                    else:
                        new_element.text = child.tail.strip()
            continue
        elif isinstance(child, etree._Element):
            processed_child = process_element_with_cleanup(child, parent_excluded=False)
            if processed_child is not None:
                new_element.append(processed_child)
        else:
            # Preserve text content from text nodes
            if child.text and child.text.strip():
                if new_element.text:
                    new_element.text += ' ' + child.text.strip()
                else:
                    new_element.text = child.text.strip()
            if child.tail and child.tail.strip():
                if len(new_element) > 0 and hasattr(new_element[-1], 'tail'):
                    if new_element[-1].tail:
                        new_element[-1].tail += ' ' + child.tail.strip()
                    else:
                        new_element[-1].tail = child.tail.strip()
    

    
    # Preserve the element's own tail text (text after the element's closing tag)
    if hasattr(element, 'tail') and element.tail and element.tail.strip():
        new_element.tail = element.tail.strip()

    return new_element

def customize_xml_serialization(element, default_ns=None):
    """Custom XML serialization that handles ch-note comments appropriately"""
    # First get the standard pretty-printed XML
    xml_string = etree.tostring(element, encoding='unicode', pretty_print=True)
    
    # Remove namespace declarations
    if default_ns:
        xml_string = xml_string.replace(f'ns0:', '')
        xml_string = xml_string.replace(f'xmlns:ns0="{default_ns}"', '')
        xml_string = xml_string.replace(f'xmlns="{default_ns}"', '')
    
    # Post-process to move inline comments to separate lines for simple elements
    lines = xml_string.split('\n')
    processed_lines = []
    
    for line in lines:
        # Check if this line has an inline comment in a simple element
        # Pattern: <Element>content<!-- comment --></Element>
        if '<!--' in line and '-->' in line and '<' in line and '>' in line:
            # Try to match the pattern
            pattern = r'^(\s*)<([^>\s]+)([^>]*)>([^<]*)<!--\s*(.*?)\s*-->([^<]*)</\2>\s*$'
            match = re.match(pattern, line)
            
            if match:
                indent = match.group(1)
                element_name = match.group(2)
                element_attrs = match.group(3)
                text_content = match.group(4).strip()
                comment_content = match.group(5).strip()
                trailing = match.group(6).strip()
                
                # Reconstruct the element without inline comment
                if text_content or trailing:
                    element_content = text_content
                    if trailing:
                        element_content += ' ' + trailing
                    element_line = f'{indent}<{element_name}{element_attrs}>{element_content}</{element_name}>'
                else:
                    element_line = f'{indent}<{element_name}{element_attrs}/>'
                
                # Add comment on separate line
                comment_line = f'{indent}<!-- {comment_content} -->'
                
                # Add both lines
                processed_lines.append(element_line)
                processed_lines.append(comment_line)
                continue
        
        processed_lines.append(line)
    
    return '\n'.join(processed_lines)

def extract_snippet_from_template(file_path):
    """Extract snippet from a template file using ch-root marker"""
    try:
        # Read the file content
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Find ch-root marker
        root_marker = '<!-- ch-root -->'
        root_idx = content.find(root_marker)
        
        if root_idx == -1:
            print(f"Warning: No ch-root found in {file_path}")
            return None
        
        # Find the parent element of the ch-root comment
        # Parse the content to find the element containing the comment
        try:
            # Remove XML declaration if present to avoid parsing issues
            content_no_decl = re.sub(r'^\s*<\?xml\s+[^>]+>\s*', '', content, flags=re.IGNORECASE | re.MULTILINE)
            

            
            # Wrap content in a temporary root for parsing
            wrapped_content = f'<__temp_root__>{content_no_decl}</__temp_root__>'
            temp_root = etree.fromstring(wrapped_content.encode('utf-8'))
            
            # Find the comment with ch-root
            root_comment = None
            for comment in temp_root.xpath('//comment()'):
                if comment.text and 'ch-root' in comment.text:
                    root_comment = comment
                    break
            
            if root_comment is None:
                print(f"Warning: Could not find ch-root comment in {file_path}")
                return None
            
            # Get the parent element of the comment
            parent_element = root_comment.getparent()
            if parent_element is None:
                print(f"Warning: ch-root comment has no parent element in {file_path}")
                return None
            
            # Convert the parent element to XML string
            snippet_content = etree.tostring(parent_element, encoding='unicode')
            
        except Exception as e:
            print(f"Warning: Error parsing XML in {file_path}: {e}")
            return None
        
        # Process the element tree to exclude forbidden/ignored elements and remove ch-annotations
        try:
            # Extract namespace information from the snippet content
            ns_match = re.search(r'<([^>]+)\s+xmlns="([^"]+)"', snippet_content)
            default_ns = None
            if ns_match:
                default_ns = ns_match.group(2)
            else:
                # If not found in snippet, look in the full template content
                full_ns_match = re.search(r'<([^>]+)\s+xmlns="([^"]+)"', content)
                if full_ns_match:
                    default_ns = full_ns_match.group(2)
            
            # Parse the snippet content
            if default_ns:
                wrapped = f'<__root__ xmlns="{default_ns}">{snippet_content}</__root__>'
            else:
                wrapped = f'<__root__>{snippet_content}</__root__>'
            root = etree.fromstring(wrapped.encode('utf-8'))
            
            # Find the actual content (first element child)
            snippet_root = None
            for child in root:
                if isinstance(child, etree._Element):
                    snippet_root = child
                    break
            
            if snippet_root is None:
                print(f"Warning: No valid XML content found in snippet from {file_path}")
                return None
            
            # Process the element tree to exclude forbidden/ignored elements and remove ch-annotations
            processed_root = process_element_with_cleanup(snippet_root)
            
            # Handle tail text of the root element
            # Check if the root element has text content that should be preserved
            if snippet_root.text and snippet_root.text.strip():
                # The root element has direct text content
                direct_text = snippet_root.text.strip()

            
            # Also check for tail text (text after the element's closing tag)
            root_tag_name = snippet_root.tag
            if f'</{root_tag_name}>' in snippet_content:
                # Find the position after the root element's closing tag
                closing_tag_end = snippet_content.find(f'</{root_tag_name}>') + len(f'</{root_tag_name}>')
                tail_text = snippet_content[closing_tag_end:].strip()
                if tail_text:

                    processed_root.tail = tail_text
            
            if processed_root is None:
                print(f"Warning: All content excluded in {file_path}")
                return None
            
            # Convert back to XML string
            xml_string = etree.tostring(processed_root, encoding='unicode', pretty_print=True)
            

            # Custom XML serialization to handle ch-note placement correctly
            xml_string = customize_xml_serialization(processed_root, default_ns)
            
            return xml_string
            
        except etree.XMLSyntaxError as e:
            print(f"Warning: XML parsing error in {file_path}: {e}")
            return None
    
    except Exception as e:
        print(f"Error processing {file_path}: {e}")
        return None

def main():
    args = parse_args()
    
    # Create output directory
    os.makedirs(args.output, exist_ok=True)
    
    # Process all XML files in input directory
    xml_files = [f for f in os.listdir(args.input) if f.endswith('.xml')]
    
    for xml_file in xml_files:
        print(f"Processing {xml_file}")
        file_path = os.path.join(args.input, xml_file)
        
        # Extract snippet
        snippet = extract_snippet_from_template(file_path)
        
        if snippet:
            # Generate output filename
            output_filename = os.path.splitext(xml_file)[0] + '.xml'
            output_path = os.path.join(args.output, output_filename)
            
            # Write to file
            with open(output_path, 'w', encoding='utf-8') as f:
                # Add XML declaration
                f.write('<?xml version="1.0" encoding="UTF-8"?>\n')
                f.write(snippet)
            
            print(f"Generated {output_path}")
        else:
            print(f"No snippet extracted from {xml_file}")
    
    print(f"Processed {len(xml_files)} files")

if __name__ == '__main__':
    main()