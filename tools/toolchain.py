
import os
import shutil
from pathlib import Path

from tools.configuration import DOCS_DIR, SITE_DIR, XSD_FILE_PATH, SITE_TABLES_DIR, TEMPLATES_DIR, JEKYLL_DIR
from tools.expand_docs.expand_docs import expand_docs
from tools.md_builder.md_builder import build_markdown_tables


def clean(dir: str):
    dir_path = Path(dir)
    if dir_path.exists():
        shutil.rmtree(dir)
    os.makedirs(dir, exist_ok=True)

def copy_jekyll_files():
    src = Path(JEKYLL_DIR)
    dst = Path(SITE_DIR)
    shutil.copytree(src, dst, dirs_exist_ok=True)

def generate_docs():
    expand_docs(DOCS_DIR, SITE_DIR)
    # generate_html_files(SITE_DIR)

def generate_tables():
    build_markdown_tables(TEMPLATES_DIR, SITE_TABLES_DIR, XSD_FILE_PATH)
    # generate_html_files(SITE_TABLES_DIR)

def main():
    clean(SITE_DIR)
    copy_jekyll_files()
    generate_docs()
    generate_tables()

if __name__ == '__main__':
    main()
