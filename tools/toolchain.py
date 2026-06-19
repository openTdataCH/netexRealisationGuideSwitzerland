import os
import shutil
from pathlib import Path

from tools.configuration import DOCS_DIR, SITE_DIR, XSD_FILE_PATH, SITE_TABLES_DIR, TEMPLATES_DIR, JEKYLL_DIR, SITE_XML_SNIPPETS_DIR
from tools.expand_docs.expand_docs import expand_docs
from tools.md_builder.md_builder import build_markdown_tables
from tools.xml_snippets.build_xml_snippets import generate_all_snippets

def clean(dir: str):
    dir_path = Path(dir)
    if dir_path.exists():
        shutil.rmtree(dir)
    os.makedirs(dir, exist_ok=True)

def copy_jekyll_files():
    src = Path(JEKYLL_DIR)
    dst = Path(SITE_DIR)
    shutil.copytree(src, dst, dirs_exist_ok=True)

def generate_tables():
    build_markdown_tables(TEMPLATES_DIR, SITE_TABLES_DIR, XSD_FILE_PATH)

def generate_xml_snippets():
    generate_all_snippets(TEMPLATES_DIR, SITE_XML_SNIPPETS_DIR)

def generate_docs():
    expand_docs(DOCS_DIR, SITE_DIR)

def main():
    clean(SITE_DIR)
    copy_jekyll_files()
    generate_tables()
    generate_xml_snippets()
    generate_docs()

if __name__ == '__main__':
    main()
