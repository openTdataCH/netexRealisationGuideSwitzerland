#!/usr/bin/env python3
"""
Expand documentation by including example snippets and markdown tables directly.
"""
import os
import shutil
import argparse
import re
from tools.configuration import DOCS_DIR, SITE_DIR, SITE_TABLES_DIR, SITE_XML_SNIPPETS_DIR

TABLE_MD_LINK_TARGET_PATTERN = re.compile(r'(\[.*])\((.*(\.)md).*\)')
TABLE_MD_LINK_TARGET_REPLACEMENT = r'\1(./tables/\2)'

def copy_media_folder(input_folder, output_folder):
    """Copy media folder from input to output."""
    media_src = os.path.join(input_folder, 'media')
    media_dst = os.path.join(output_folder, 'media')

    if os.path.exists(media_src):
        shutil.copytree(media_src, media_dst, dirs_exist_ok=True)


def include_xml_snippet(snippet_file_name: str, base_folder: str):
    """
    Include XML snippet content directly.

    param: snippet_file_name: Snippet file name
    param: base_folder: Path to the documents base folder

    """
    # Look for files in the main generated folder, not output folder
    # The generated folder is at the root of the project
    # base_folder is already the docs folder, so go up one level to project root
    project_root = os.path.abspath(os.path.join(base_folder, '..'))
    full_path = os.path.join(project_root, 'site', 'xml-snippets', snippet_file_name)

    if os.path.exists(full_path):
        with open(full_path, 'r', encoding='utf-8') as f:
            return f"```xml\n{f.read()}\n```"
    return snippet_file_name

def include_markdown_table(table_file_name: str, base_folder: str):
    """
    Include markdown table content directly.

    param: table_file_name: Path to the markdown table file
    param: base_folder: Path to the documents base folder
    """

    # Look for files in the main generated folder, not output folder
    # The generated folder is at the root of the project
    # base_folder is already the docs folder, so go up one level to project root
    project_root = os.path.abspath(os.path.join(base_folder, '..'))
    full_path = os.path.join(project_root, 'site', 'tables', table_file_name)

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
                    # correct md link target
                    line = TABLE_MD_LINK_TARGET_PATTERN.sub(TABLE_MD_LINK_TARGET_REPLACEMENT,line)
                    table_lines.append(line)
                elif line.startswith("#"):
                    # we ignore heading
                    continue
                else:
                    # just add everything else
                    table_lines.append(line)
                    in_table = False

            return '\n'.join(table_lines)
    return table_file_name


def expand_markdown_file(input_file_path, output_file_path, base_folder):
    """
        Expands a single markdown file: integrates/expands xml snippets and markdown tables.

        param: input_file_path: Path to the input markdown file
        param: output_file_path: Path to the output markdown file
        param: base_folder: Path to the documents base folder
    """
    with open(input_file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Process XML snippets - match the entire line prefix and link (flexible text)
    xml_pattern = r'(?:- )?\[.*?\]\(\.\./site/xml-snippets/([^)]+\.xml)\)'
    content = re.sub(xml_pattern, lambda m: '\n\n' + include_xml_snippet(m.group(1), base_folder) + '\n\n', content)

    # Process markdown tables - match the entire line prefix and link (flexible text)
    md_pattern = r'(?:- )?\[.*?\]\(\.\./site/tables/([^)]+\.md)\)'
    content = re.sub(md_pattern, lambda m: '\n\n' + include_markdown_table(m.group(1), base_folder) + '\n\n', content)

    # Write processed content
    with open(output_file_path, 'w', encoding='utf-8') as f:
        f.write(content)


def expand_docs(input_dir: str, output_dir: str):
    """
        Expands all markdown files in input_dir: integrates/expands xml snippets and markdown tables.

        param: input_file_path: Path to the input dir to search for input markdown files
        param: output_file_path: Path to the output dir
        param: xml_snippets_path: Path to the folder to look for xml snippets
        param: table_path: Path to the folder to look for markdown tables
    """

    # Create output folder if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)

    # Copy media folder
    copy_media_folder(input_dir, output_dir)

    # Process each markdown file
    for filename in os.listdir(input_dir):
        if filename.endswith('.md'):
            input_md = os.path.join(input_dir, filename)
            output_md = os.path.join(output_dir, filename)
            expand_markdown_file(input_md, output_md, input_dir)

    print(f"Documentation expanded successfully to {output_dir}")

def main():
    parser = argparse.ArgumentParser(description='Expand documentation by including examples and tables.')
    parser.add_argument('--docs', default=DOCS_DIR, help=f"Input documentation folder (default = {DOCS_DIR})")
    parser.add_argument('--out', default=SITE_DIR, help=f"Output folder (default = {SITE_DIR})")
    args = parser.parse_args()
    expand_docs(args.docs, args.out)

if __name__ == '__main__':
    main()
