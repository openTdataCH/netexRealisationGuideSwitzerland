#!/usr/bin/env python3
"""
Expand documentation by including example snippets and markdown tables directly.
"""
import os
import shutil
import argparse
import re

def copy_media_folder(input_folder, output_folder):
    """Copy media folder from input to output."""
    media_src = os.path.join(input_folder, 'media')
    media_dst = os.path.join(output_folder, 'media')
    
    if os.path.exists(media_src):
        shutil.copytree(media_src, media_dst, dirs_exist_ok=True)

def include_xml_snippet(match, base_folder):
    """Include XML snippet content directly."""
    snippet_path = match.group(1)
    # Look for files in the main generated folder, not output folder
    # The generated folder is at the root of the project
    # base_folder is already the docs folder, so go up one level to project root
    project_root = os.path.abspath(os.path.join(base_folder, '..'))
    full_path = os.path.join(project_root, 'generated', 'xml-snippets', snippet_path)
    
    if os.path.exists(full_path):
        with open(full_path, 'r', encoding='utf-8') as f:
            return f"```xml\n{f.read()}\n```"
    return match.group(0)

def include_markdown_table(match, base_folder):
    """Include markdown table content directly."""
    table_path = match.group(1)
    # Look for files in the main generated folder, not output folder
    # The generated folder is at the root of the project
    # base_folder is already the docs folder, so go up one level to project root
    project_root = os.path.abspath(os.path.join(base_folder, '..'))
    full_path = os.path.join(project_root, 'generated', 'markdown-examples', table_path)
    
    if os.path.exists(full_path):
        with open(full_path, 'r', encoding='utf-8') as f:
            content = f.read()
            # Extract table content (between first two lines of ---)
            lines = content.split('\n')
            table_lines = []
            in_table = False
            for line in lines:
                if line.startswith('|') or line.startswith('---'):
                    in_table = True
                    table_lines.append(line)
                elif in_table:
                    break
            return '\n'.join(table_lines)
    return match.group(0)

def process_markdown_file(input_path, output_path, base_folder):
    """Process a single markdown file."""
    with open(input_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Process XML snippets - match the entire line prefix and link (flexible text)
    xml_pattern = r'- \[.*?\]\(\.\./generated/xml-snippets/([^)]+\.xml)\)'
    content = re.sub(xml_pattern, lambda m: '\n\n' + include_xml_snippet(m, base_folder) + '\n\n', content)
    
    # Process markdown tables - match the entire line prefix and link (flexible text)
    md_pattern = r'- \[.*?\]\(\.\./generated/markdown-examples/([^)]+\.md)\)'
    content = re.sub(md_pattern, lambda m: '\n\n' + include_markdown_table(m, base_folder) + '\n\n', content)
    
    # Write processed content
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(content)

def main():
    parser = argparse.ArgumentParser(description='Expand documentation by including examples and tables.')
    parser.add_argument('--docs', required=True, help='Input documentation folder')
    parser.add_argument('--out', required=True, help='Output folder')
    args = parser.parse_args()
    
    # Create output folder if it doesn't exist
    os.makedirs(args.out, exist_ok=True)
    
    # Copy media folder
    copy_media_folder(args.docs, args.out)
    
    # Process each markdown file
    for filename in os.listdir(args.docs):
        if filename.endswith('.md'):
            input_path = os.path.join(args.docs, filename)
            output_path = os.path.join(args.out, filename)
            process_markdown_file(input_path, output_path, args.docs)
    
    print(f"Documentation expanded successfully to {args.out}")

if __name__ == '__main__':
    main()