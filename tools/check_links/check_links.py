#!/usr/bin/env python3
"""
Check relative links in markdown files and warn if target files don't exist.
"""
import os
import re
import argparse
from pathlib import Path

def check_markdown_links(docs_folder, main_folder):
    """Check all relative links in markdown files."""
    markdown_extensions = ('.md', '.MD', '.markdown', '.Markdown')
    link_pattern = r'\[([^\]]+)\]\(([^)]+)\)'
    
    total_links = 0
    working_links = 0
    broken_links = 0
    backslash_warnings = 0
    
    # Convert to absolute paths for consistent resolution
    docs_folder = os.path.abspath(docs_folder)
    main_folder = os.path.abspath(main_folder)
    
    for root, dirs, files in os.walk(docs_folder):
        for file in files:
            if file.endswith(markdown_extensions):
                file_path = os.path.join(root, file)
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # Find all markdown links
                for match in re.finditer(link_pattern, content):
                    link_text = match.group(1)
                    link_url = match.group(2)
                    
                    # Skip absolute URLs and anchor links
                    if link_url.startswith(('http://', 'https://', '#')):
                        continue
                    
                    # Check for backslashes and warn
                    if '\\' in link_url:
                        backslash_warnings += 1
                        print(f"WARNING: Backslash found in link in {os.path.relpath(file_path, docs_folder)}")
                        print(f"  Link text: '{link_text}'")
                        print(f"  Link URL: '{link_url}'")
                        print(f"  Please use forward slashes (/) for cross-platform compatibility")
                        print()
                    
                    total_links += 1
                    
                    # Convert relative link to absolute path
                    # The link is relative to the current markdown file's location
                    file_dir = os.path.dirname(file_path)
                    
                    if link_url.startswith('../'):
                        # Relative path - resolve from the file's directory
                        target_path = os.path.normpath(os.path.join(file_dir, link_url))
                    else:
                        # Local relative path
                        target_path = os.path.normpath(os.path.join(file_dir, link_url))
                    
                    # Convert absolute path back to relative path for display (using forward slashes)
                    rel_target_path = os.path.relpath(target_path, docs_folder)
                    rel_target_path = rel_target_path.replace(os.sep, '/')
                    
                    # Check if target exists
                    if not os.path.exists(target_path):
                        broken_links += 1
                        print(f"WARNING: Broken link in {os.path.relpath(file_path, docs_folder)}")
                        print(f"  Link text: '{link_text}'")
                        print(f"  Link URL: '{link_url}'")
                        print(f"  Expected at: {rel_target_path}")
                        print()
                    else:
                        working_links += 1
    
    print(f"\nLink checking summary:")
    print(f"  Total relative links checked: {total_links}")
    print(f"  Working links: {working_links}")
    print(f"  Broken links: {broken_links}")
    if backslash_warnings > 0:
        print(f"  Backslash warnings: {backslash_warnings}")
    
    if broken_links == 0 and backslash_warnings == 0:
        print("  Status: All links are valid! :)")
    else:
        status_messages = []
        if broken_links > 0:
            status_messages.append(f"Found {broken_links} broken links")
        if backslash_warnings > 0:
            status_messages.append(f"Found {backslash_warnings} backslash warnings")
        print(f"  Status: {', '.join(status_messages)} :(")

def main():
    parser = argparse.ArgumentParser(description='Check relative links in markdown files.')
    parser.add_argument('--docs', required=True, help='Documentation folder to process')
    parser.add_argument('--main', required=True, help='Main project folder')
    args = parser.parse_args()
    
    check_markdown_links(args.docs, args.main)

if __name__ == '__main__':
    main()