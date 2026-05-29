import argparse
import shutil

from tools.configuration import DOCS_DIR, GENERATED_DOCS_DIR
from tools.expand_docs.expand_docs import expand_docs
from tools.md2html.md2html import generate_html_files


def main():
    parser = argparse.ArgumentParser(description='Run tools to generate documents.')
    parser.add_argument('--target', default="docs", help=f"Target to generate (default: docs)")
    args = parser.parse_args()
    expand_docs(DOCS_DIR, GENERATED_DOCS_DIR)
    generate_html_files(GENERATED_DOCS_DIR)

if __name__ == '__main__':
    main()
