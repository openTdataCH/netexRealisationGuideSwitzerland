#!/usr/bin/env python3
"""
Markdown Indexer

Generates an index file from glossary terms found in markdown files.
Extracts all ## headers from the glossary file (e.g., A4_annex_glossary.md),
then searches all other markdown files to find which pages reference each term.

Usage:
    python md_indexer.py -i INPUT_FOLDER -o OUTPUT_FILE

Example:
    python md_indexer.py -i src -o src/A5_index.md
"""

import argparse
import os
import re


def extract_glossary_terms(glossary_file):
    """Extract all ## headers from the glossary file"""
    terms = []
    
    with open(glossary_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Find all ## headers
    pattern = r'^##\s+(.+)$'
    for line in content.split('\n'):
        match = re.match(pattern, line.strip())
        if match:
            term = match.group(1).strip()
            terms.append(term)
    
    return terms


def find_term_references(term, md_files, source_folder):
    """Find all markdown files that reference a given term"""
    references = []
    
    for md_file in md_files:
        # Skip the glossary file itself
        if os.path.basename(md_file) == 'A4_annex_glossary.md':
            continue
        
        filepath = os.path.join(source_folder, md_file)
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Check if the term appears in the content (case insensitive)
        # Match the term as a whole word or in link format
        patterns = [
            rf'\b{re.escape(term)}\b',  # Whole word
            rf'\[{re.escape(term)}\]',  # In link text
            rf'\[.*?\]\({re.escape(term)}\.md\)',  # Link to term.md
        ]
        
        for pattern in patterns:
            if re.search(pattern, content, re.IGNORECASE):
                references.append(md_file)
                break
    
    return references


def sort_references(references):
    """
    Sort references with priority:
    1. Files matching 01_xx.md to 10_common.md (in numerical order)
    2. Files matching uc_*.md (alphabetically)
    3. All other files (alphabetically)
    """
    # Define priority groups
    numbered_files = []
    uc_files = []
    other_files = []
    
    # Pattern for numbered files: starts with digits and underscore
    numbered_pattern = re.compile(r'^\d+_')
    # Pattern for uc files: starts with uc followed by digits and underscore
    uc_pattern = re.compile(r'^uc\d+_')
    
    for ref in references:
        basename = os.path.basename(ref)
        if numbered_pattern.match(basename):
            numbered_files.append(ref)
        elif uc_pattern.match(basename):
            uc_files.append(ref)
        else:
            other_files.append(ref)
    
    # Sort numbered files numerically then alphabetically
    def get_numeric_key(filename):
        basename = os.path.basename(filename)
        # Extract the number part
        match = re.match(r'^(\d+)', basename)
        if match:
            return (int(match.group(1)), basename)
        return (999, basename)
    
    numbered_files.sort(key=get_numeric_key)
    
    # Sort uc files alphabetically
    uc_files.sort()
    
    # Sort other files alphabetically
    other_files.sort()
    
    return numbered_files + uc_files + other_files


def generate_index(glossary_terms, md_files, source_folder, output_file):
    """Generate the index markdown file"""
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write('# Index\n\n')
        f.write('Cross-reference index of NeTEx profile elements.\n\n')
        f.write('---\n\n')
        
        for term in sorted(glossary_terms):
            references = find_term_references(term, md_files, source_folder)
            if references:
                sorted_refs = sort_references(references)
                ref_links = []
                for ref in sorted_refs:
                    # Create link without .md extension
                    link_name = os.path.basename(ref).replace('.md', '')
                    ref_links.append(f'[{link_name}]({ref})')
                
                f.write(f'## {term}\n\n')
                f.write(f'{term}: {(", ").join(ref_links)}\n\n')
    
    print(f'Index generated: {output_file}')


def get_md_files(folder):
    """Get all markdown files in the folder (non-recursive)"""
    md_files = []
    for filename in os.listdir(folder):
        if filename.endswith('.md'):
            md_files.append(filename)
    return md_files


def parse_args():
    """Parse command line arguments"""
    parser = argparse.ArgumentParser(
        description='Generate markdown index from glossary terms'
    )
    parser.add_argument(
        '-i', '--input',
        required=True,
        help='Input folder containing markdown files'
    )
    parser.add_argument(
        '-o', '--output',
        required=True,
        help='Output file path for the index (e.g., src/A5_index.md)'
    )
    return parser.parse_args()


def main():
    args = parse_args()
    
    source_folder = args.input
    output_file = args.output
    
    # Get all markdown files in source folder
    md_files = get_md_files(source_folder)
    
    if not md_files:
        print(f'No markdown files found in {source_folder}')
        return
    
    # Find the glossary file
    glossary_file = None
    for filename in md_files:
        if 'glossary' in filename.lower():
            glossary_file = os.path.join(source_folder, filename)
            break
    
    if not glossary_file:
        print('No glossary file found (expected A4_annex_glossary.md or similar)')
        return
    
    # Extract terms from glossary
    terms = extract_glossary_terms(glossary_file)
    
    if not terms:
        print('No terms found in glossary file')
        return
    
    print(f'Found {len(terms)} terms in glossary')
    
    # Generate index
    generate_index(terms, md_files, source_folder, output_file)


if __name__ == '__main__':
    main()
