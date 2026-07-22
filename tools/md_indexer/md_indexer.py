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


def check_template_exists(term, templates_folder):
    """Check if a template file exists for the given term"""
    # Try different case variations
    filename_patterns = [
        f'{term}.xml',
        f'{term}.XML',
        f'{term.lower()}.xml',
        f'{term.upper()}.xml',
    ]
    
    for pattern in filename_patterns:
        filepath = os.path.join(templates_folder, pattern)
        if os.path.exists(filepath):
            return True
    return False


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


def generate_index(glossary_terms, md_files, source_folder, output_file, templates_folder=None):
    """Generate the index markdown file"""
    # If templates_folder is not provided, try to find it
    if templates_folder is None:
        templates_folder = os.path.join(source_folder, 'templates')
    
    # Exclude the output file from md_files to avoid self-reference
    output_basename = os.path.basename(output_file)
    filtered_md_files = [f for f in md_files if f != output_basename]
    
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write('# Index\n\n')
        f.write('Cross-reference index of NeTEx profile elements.\n\n')
        f.write('---\n\n')
        
        for term in sorted(glossary_terms):
            # Build list of links
            links = []
            
            # 1. Check if template exists and the corresponding site/tables file exists
            if check_template_exists(term, templates_folder):
                # Check if the site/tables/{term}.md file would exist
                tables_file = os.path.join(source_folder, '..', 'site', 'tables', f'{term}.md')
                # Normalize the path
                tables_file = os.path.normpath(tables_file)
                # For now, assume it exists if template exists
                # (we can't check if it exists because it might be in a different location)
                links.append(f'[{term}](site/tables/{term}.md)')
            
            # 2. Add other references
            references = find_term_references(term, filtered_md_files, source_folder)
            if references:
                sorted_refs = sort_references(references)
                for ref in sorted_refs:
                    # Create link without .md extension
                    link_name = os.path.basename(ref).replace('.md', '')
                    links.append(f'[{link_name}]({ref})')
            
            # 3. Add glossary link last (only if there are other links)
            if links:
                lowercase_term = term.lower()
                links.append(f'[A4_annex_glossary](A4_annex_glossary.md#{lowercase_term})')
                
                f.write(f'- {term}: {(", ").join(links)}\n')
    
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
    parser.add_argument(
        '-t', '--templates',
        default=None,
        help='Templates folder (default: <input>/templates)'
    )
    return parser.parse_args()


def main():
    args = parse_args()
    
    source_folder = args.input
    output_file = args.output
    templates_folder = args.templates
    
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
    generate_index(terms, md_files, source_folder, output_file, templates_folder)


if __name__ == '__main__':
    main()
