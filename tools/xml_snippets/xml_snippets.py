#!/usr/bin/env python3
"""
build_xml_snippets.py

Parses XML templates and extracts snippets between ch-start and ch-stop comments.
Removes ch-annotations except for ch-note and ch-notice (keeping only the content).
Excludes elements marked with ch-usage: forbidden or ch-usage: ignored.

Usage:
    python build_xml_snippets.py -i INPUT_FOLDER_OR_FILE -o OUTPUT_FOLDER

Example:
    python build_xml_snippets.py -i templates -o site/xml-snippets
    python build_xml_snippets.py -i single_template.xml -o site/xml-snippets
"""

import os
import sys
import argparse
import re
from lxml import etree


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
    children_to_add = []
    pending_ch_notes = []  # ch-note comments that should appear before the next element
    
    for child in element:
        if isinstance(child, etree._Comment):
            # Handle comments - keep only ch-note content as comment elements
            if child.text:
                comment_text = child.text.strip()
                if comment_text.startswith('ch-note:'):
                    # Extract the note content (remove ch-note: prefix)
                    content = re.sub(r'ch-note:\s*', '', comment_text)
                    pending_ch_notes.append(content)
            # Preserve tail text of ALL comments (not just ch-note)
            if child.tail and child.tail.strip():
                # This tail text belongs to the parent element's text content
                # Add it to new_element.text
                if new_element.text:
                    new_element.text += ' ' + child.tail.strip()
                else:
                    new_element.text = child.tail.strip()
            continue
        elif isinstance(child, etree._Element):
            # If we have pending ch-note comments, add them as comment elements before this child
            for note_content in pending_ch_notes:
                comment_elem = etree.Comment(f' {note_content} ')
                children_to_add.append(comment_elem)
            pending_ch_notes = []
            
            processed_child = process_element_with_cleanup(child, parent_excluded=False)
            if processed_child is not None:
                children_to_add.append(processed_child)
        else:
            # Text nodes - preserve their content
            if child.text and child.text.strip():
                if new_element.text:
                    new_element.text += ' ' + child.text.strip()
                else:
                    new_element.text = child.text.strip()
            if child.tail and child.tail.strip():
                if new_element.text:
                    new_element.text += ' ' + child.tail.strip()
                else:
                    new_element.text = child.tail.strip()
    
    # Handle any remaining ch-note comments (these belong to the parent element itself)
    if pending_ch_notes:
        for note_content in pending_ch_notes:
            comment_elem = etree.Comment(f' {note_content} ')
            children_to_add.append(comment_elem)

    # Add all collected children to the new element
    for child_to_add in children_to_add:
        new_element.append(child_to_add)

    # Preserve the element's own tail text (text after the element's closing tag)
    if hasattr(element, 'tail') and element.tail and element.tail.strip():
        new_element.tail = element.tail.strip()

    return new_element


def has_element_children(element):
    """Check if an element has any child elements (not just text or comments)"""
    for child in element:
        if isinstance(child, etree._Element):
            return True
    return False


def get_tag_name(tag):
    """Extract the tag name without namespace"""
    if '}' in tag:
        return tag.split('}')[1]
    return tag


def format_element_with_mixed_content(element, indent='', default_ns=None):
    """Format an element that has both text content and child elements"""
    lines = []
    child_indent = indent + '  '
    
    # Get tag name without namespace
    tag_name = get_tag_name(element.tag)
    
    # Opening tag with text content
    tag_str = f'<{tag_name}'
    if element.attrib:
        tag_str += ' ' + ' '.join(f'{k}="{v}"' for k, v in element.attrib.items())
    tag_str += '>'
    
    if element.text and element.text.strip():
        # Add text content on the same line as opening tag
        lines.append(f'{indent}{tag_str}{element.text.strip()}')
    else:
        lines.append(f'{indent}{tag_str}')
    
    # Handle children
    for child in element:
        if isinstance(child, etree._Comment):
            # Comments on their own line
            lines.append(f'{child_indent}{etree.tostring(child, encoding="unicode").strip()}')
        elif isinstance(child, etree._Element):
            # Recursively format child elements using serialize_element_tree
            child_str = serialize_element_tree(child, indent_level=len(indent.split('  ')), default_ns=default_ns)
            # Add proper indentation to each line
            for line in child_str.split('\n'):
                if line.strip():
                    lines.append(f'{child_indent}{line.strip()}')
                else:
                    lines.append(line)
        else:
            # Text nodes
            text = child.text if child.text else ''
            if text.strip():
                lines.append(f'{child_indent}{text.strip()}')
    
    # Closing tag
    lines.append(f'{indent}</{tag_name}>')
    
    return '\n'.join(lines)


def serialize_element_tree(element, indent_level=0, default_ns=None):
    """Recursively serialize element tree with custom formatting"""
    indent = '  ' * indent_level
    
    # Get tag name without namespace
    tag_name = get_tag_name(element.tag) if hasattr(element, 'tag') else str(type(element))
    
    # Check if this element has both text and child elements
    has_text = element.text and element.text.strip()
    has_children = has_element_children(element)
    
    if has_text and has_children:
        # Special formatting for elements with both text and children
        return format_element_with_mixed_content(element, indent, default_ns)
    
    # Use standard pretty print but with recursive handling of children
    # Build the serialization manually
    lines = []
    
    # Opening tag
    tag_str = f'<{tag_name}'
    if element.attrib:
        tag_str += ' ' + ' '.join(f'{k}="{v}"' for k, v in element.attrib.items())
    
    if has_children:
        # Element has children
        tag_str += '>'
        lines.append(f'{indent}{tag_str}')
        
        # Process children
        child_indent = indent + '  '
        for child in element:
            if isinstance(child, etree._Comment):
                # Comments
                comment_str = etree.tostring(child, encoding='unicode').strip()
                lines.append(f'{child_indent}{comment_str}')
            elif isinstance(child, etree._Element):
                # Recursively serialize child elements
                child_xml = serialize_element_tree(child, indent_level + 1, default_ns)
                for line in child_xml.split('\n'):
                    if line.strip():
                        lines.append(f'{child_indent}{line.strip()}')
                    else:
                        lines.append(line)
            else:
                # Text nodes - shouldn't happen at this level
                pass
        
        # Closing tag
        lines.append(f'{indent}</{tag_name}>')
    else:
        # Self-closing or empty element
        if element.text and element.text.strip():
            tag_str += '>' + element.text.strip() + f'</{tag_name}>'
            lines.append(f'{indent}{tag_str}')
        else:
            tag_str += '/>'
            lines.append(f'{indent}{tag_str}')
    
    # Remove namespace declarations from the serialized string
    xml_string = '\n'.join(lines)
    if default_ns:
        xml_string = xml_string.replace(f'ns0:', '')
        xml_string = xml_string.replace(f'xmlns:ns0="{default_ns}"', '')
        xml_string = xml_string.replace(f'xmlns="{default_ns}"', '')
    
    return xml_string


def customize_xml_serialization(element, default_ns=None):
    """Custom XML serialization that handles ch-note comments appropriately"""
    return serialize_element_tree(element, default_ns=default_ns)


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


def generate_all_snippets(input_dir: str, output_dir: str):
    """
    Generates all XML snippets from templates in input_dir.

    :param input_dir: Input directory
    :param output_dir: Output directory where the XML snippets will be generated.
    """

    xml_files = [os.path.join(input_dir, f) for f in os.listdir(input_dir) if f.endswith('.xml')]

    for file_path in xml_files:
        generate_snippet(file_path, output_dir)
    print(f"Processed {len(xml_files)} files")


def generate_snippet(template_path: str, output_dir: str):
    """
    Generates a XML snippet from a single template.

    :param template_path: Path to the template file.
    :param output_dir: Output directory where the XML snippet will be generated.
    """
    print(f"Processing {os.path.basename(template_path)}")

    # Extract snippet
    snippet = extract_snippet_from_template(template_path)

    if snippet:

        # Create output directory
        os.makedirs(output_dir, exist_ok=True)

        # Generate output filename
        output_filename = os.path.splitext(os.path.basename(template_path))[0] + '.xml'
        output_path = os.path.join(output_dir, output_filename)

        # Write to file
        with open(output_path, 'w', encoding='utf-8') as f:
            # Add XML declaration
            f.write('<?xml version="1.0" encoding="UTF-8"?>\n')
            f.write(snippet)

        print(f"Generated {output_path}")
    else:
        print(f"No snippet extracted from {os.path.basename(template_path)}")


def parse_args():
    """Parse command line arguments"""
    parser = argparse.ArgumentParser(
        description='Extract XML snippets from templates with ch-start/ch-stop markers'
    )
    parser.add_argument(
        '-i', '--input',
        required=True,
        help='Input folder or single XML file containing templates'
    )
    parser.add_argument(
        '-o', '--output',
        required=True,
        help='Output folder for XML snippet files'
    )
    return parser.parse_args()

def main():
    args = parse_args()

    # Determine if input is a file or directory
    if os.path.isfile(args.input):
        generate_snippet(args.input, args.output)
    else:
        # Directory mode - process all XML files in input directory
        generate_all_snippets(args.input, args.output)

if __name__ == '__main__':
    main()
