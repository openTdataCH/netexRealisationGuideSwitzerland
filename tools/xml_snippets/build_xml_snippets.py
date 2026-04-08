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
            continue
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
    print(f"DEBUG: process_element called with: {type(element)}")
    if parent_excluded:
        # If parent is excluded, all children are excluded too
        return None
    
    # Check if this element should be excluded
    if should_exclude_element(element):
        return None
    
    # Create a copy of the element to avoid modifying the original
    if not hasattr(element, 'tag'):
        print(f"DEBUG: Element is not a proper element: {type(element)}")
        return None
    
    print(f"DEBUG: Creating element {element.tag}")
    new_element = etree.Element(element.tag, attrib=element.attrib)
    
def process_element_with_cleanup(element, parent_excluded=False):
    """Process an element and its children, excluding forbidden/ignored elements and removing ch-annotations"""
    # Skip comments
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
    
    return new_element

def extract_snippet_from_template(file_path):
    """Extract snippet from a template file between ch-start and ch-stop markers"""
    try:
        # Read the file content
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Find ch-start and ch-stop markers (both old and new formats)
        start_marker_old = '<!-- ch-start:'
        start_marker_new = '<!-- ch-start -->'
        end_marker_old = '<!-- ch-stop:'
        end_marker_new = '<!-- ch-stop -->'
        
        start_idx = content.find(start_marker_old)
        if start_idx == -1:
            start_idx = content.find(start_marker_new)
            
        end_idx = content.find(end_marker_old)
        if end_idx == -1:
            end_idx = content.find(end_marker_new)
        
        if start_idx == -1 or end_idx == -1:
            print(f"Warning: No ch-start or ch-stop found in {file_path}")
            return None
        
        # Extract the region between markers (including the markers)
        # Determine which marker format was found
        if end_idx != -1:
            if content.find(end_marker_old, end_idx) == end_idx:
                snippet_content = content[start_idx:end_idx + len(end_marker_old)]
            else:
                snippet_content = content[start_idx:end_idx + len(end_marker_new)]
        else:
            snippet_content = ""
        
        # Find the end of the ch-stop comment
        stop_comment_end = content.find('-->', end_idx)
        if stop_comment_end != -1:
            snippet_content = content[start_idx:stop_comment_end + 3]  # Include -->
        
        # Remove ch-start and ch-stop comments to avoid parsing issues (both formats)
        snippet_content = re.sub(r'<!-- ch-start:[^>]*-->', '', snippet_content)
        snippet_content = re.sub(r'<!-- ch-start -->', '', snippet_content)
        snippet_content = re.sub(r'<!-- ch-stop:[^>]*-->', '', snippet_content)
        snippet_content = re.sub(r'<!-- ch-stop -->', '', snippet_content)
        snippet_content = snippet_content.strip()
        
        # Parse the XML while preserving namespace information
        try:
            # Extract namespace information from the original snippet
            # Look for xmlns in the snippet content itself
            ns_match = re.search(r'<([^>]+)\s+xmlns="([^"]+)"', snippet_content)
            default_ns = None
            if ns_match:
                default_ns = ns_match.group(2)
            else:
                # If not found in snippet, look in the full template content
                full_ns_match = re.search(r'<([^>]+)\s+xmlns="([^"]+)"', content)
                if full_ns_match:
                    default_ns = full_ns_match.group(2)
            
            # Wrap in a root element with the same namespace for parsing
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
            
            if processed_root is None:
                print(f"Warning: All content excluded in {file_path}")
                return None
            
            # Convert back to XML string
            xml_string = etree.tostring(processed_root, encoding='unicode', pretty_print=True)
            
            # Fix namespace prefixes to make the default namespace truly default
            if default_ns:
                # Replace ns0: prefixes with no prefix and add xmlns declaration
                xml_string = xml_string.replace(f'ns0:', '')
                xml_string = xml_string.replace(f'xmlns:ns0="{default_ns}"', f'xmlns="{default_ns}"')
                
                # If xmlns declaration is missing, add it to the root element
                if 'xmlns="' not in xml_string:
                    # Find the root element opening tag
                    root_tag_match = re.match(r'<([^>\s]+)(\s+[^>]*)?>', xml_string.strip())
                    if root_tag_match:
                        tag_name = root_tag_match.group(1)
                        tag_attrs = root_tag_match.group(2) if root_tag_match.group(2) else ''
                        if tag_attrs:
                            new_tag = f'<{tag_name} xmlns="{default_ns}" {tag_attrs.strip()}'
                        else:
                            new_tag = f'<{tag_name} xmlns="{default_ns}"'
                        xml_string = xml_string.replace(f'<{tag_name}{tag_attrs}>', new_tag + '>')
            
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