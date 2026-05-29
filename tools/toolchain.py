from tools.configuration import DOCS_DIR, GENERATED_DOCS_DIR, XSD_FILE_PATH, GENERATED_TABLES_DIR, TEMPLATES_DIR
from tools.expand_docs.expand_docs import expand_docs
from tools.md2html.md2html import generate_html_files
from tools.md_builder.md_builder import build_markdown_tables

def generate_docs():
    expand_docs(DOCS_DIR, GENERATED_DOCS_DIR)
    generate_html_files(GENERATED_DOCS_DIR)

def generate_tables():
    build_markdown_tables(TEMPLATES_DIR, GENERATED_TABLES_DIR, XSD_FILE_PATH)
    generate_html_files(GENERATED_TABLES_DIR)

def main():
    generate_docs()
    generate_tables()

if __name__ == '__main__':
    main()
