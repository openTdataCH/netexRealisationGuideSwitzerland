import argparse
import os
import re
import markdown
from pygments.formatters import HtmlFormatter

from tools.configuration import SITE_DIR

MD_LINK_PATTERN = re.compile(r'(\[.*\])(\(.*\.)(md)(.*\))')
MD_LINK_REPLACEMENT = r'\1\2html\4'

def generate_html(md: str) -> str:

    md_with_html_links = MD_LINK_PATTERN.sub(MD_LINK_REPLACEMENT, md)
    body = generate_html_body(md_with_html_links)

    # Generate CSS for code highlighting
    code_css = HtmlFormatter().get_style_defs(".codehilite")

    # Wrap in a simple HTML template
    return f"""<!doctype html>
     <html lang="en">
     <head>
       <meta charset="utf-8">
       <title>Title</title>
       <meta name="viewport" content="width=device-width, initial-scale=1">
       <style>
       body {{ max-width: 800px; margin: 2rem auto; padding: 0 1rem; font-family: system-ui, sans-serif; }}
       pre {{ overflow: auto; }}
       {code_css}
       </style>
     </head>
     <body>
       {body}
     </body>
     </html>"""

def generate_html_body(md: str) -> str:
    """Convert Markdown to HTML fragment."""
    body = markdown.markdown(
        md,
        extensions=[
            "extra",  # tables, footnotes, etc.
            "fenced_code",  # triple-backtick code blocks
            "codehilite"  # Pygments-based syntax highlighting
        ],
        extension_configs={
            "codehilite": {"guess_lang": True, "noclasses": False}
        },
    )
    return body

def generate_html_files(src_dir: str):
    """Generate HTML files from all markdown files in src_dir."""
    for filename in os.listdir(src_dir):
        if filename.endswith('.md'):
            md_path = os.path.join(src_dir, filename)
            with open(md_path, 'r', encoding='utf-8') as f:
                md = f.read()
            html = generate_html(md)
            html_path = md_path.replace('.md', '.html')
            with open(html_path, 'w', encoding='utf-8') as f:
                f.write(html)
    print(f"Generated HTML files in {src_dir}")

def main():
    parser = argparse.ArgumentParser(description='Generate HTML files from Markdown files.')
    parser.add_argument('--dir', default=SITE_DIR, help=f"Folder to search for md files (default = {SITE_DIR})")
    args = parser.parse_args()
    generate_html_files(args.dir)

if __name__ == '__main__':
    main()