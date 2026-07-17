import argparse
import os
import shutil
from pathlib import Path

from tools.configuration import DOCS_DIR, SITE_DIR, XSD_FILE_PATH, SITE_TABLES_DIR, TEMPLATES_DIR, JEKYLL_DIR, \
<<<<<<< HEAD
    SITE_XML_SNIPPETS_DIR, SITE_TEMPLATES_DIR, SITE_SCHEMATRON_DIR, TEMPLATES_PREFIX, JEKYLL_DEFAULT_BASE_URL, \
    JEKYLL_CONFIG
=======
    SITE_XML_SNIPPETS_DIR, SITE_TEMPLATES_DIR, SITE_SCHEMATRON_DIR, TEMPLATES_PREFIX
>>>>>>> upstream/main
from tools.expand_docs.expand_docs import expand_docs
from tools.md_builder.md_builder import build_markdown_tables
from tools.schematron_builder.schematron_builder import generate_all_schematrons
from tools.xml_snippets.xml_snippets import generate_all_snippets

def clean(dir: str):
    dir_path = Path(dir)
    if dir_path.exists():
        shutil.rmtree(dir)
    os.makedirs(dir, exist_ok=True)

def copy_jekyll_files():
    src = Path(JEKYLL_DIR)
    dst = Path(SITE_DIR)
    shutil.copytree(src, dst, dirs_exist_ok=True)

def apply_base_url(base_url: str):
    """
    Sets the base URL in the Jekyll config file.
    """
    if base_url is None:
        print(f'Failed to set base url - Base url not given.')
        return
    else:
        config_file_path = os.path.join(SITE_DIR, JEKYLL_CONFIG)
        if os.path.exists(config_file_path):
            with open(config_file_path, 'a', encoding='utf-8') as f:
                f.write(f'baseurl: "{base_url}" \n')
        else:
            print(f'Failed to set base url - No config file found: "{config_file_path}"')

def copy_templates():
    src = Path(TEMPLATES_DIR)
    dst = Path(SITE_TEMPLATES_DIR)
    shutil.copytree(src, dst, dirs_exist_ok=True)

def generate_tables():
    build_markdown_tables(TEMPLATES_DIR, SITE_TABLES_DIR, XSD_FILE_PATH)

def generate_xml_snippets():
    generate_all_snippets(TEMPLATES_DIR, SITE_XML_SNIPPETS_DIR)

def generate_schematrons():
    generate_all_schematrons(TEMPLATES_DIR, TEMPLATES_PREFIX, SITE_SCHEMATRON_DIR, XSD_FILE_PATH, 'PublicationDelivery')

def generate_docs():
    expand_docs(DOCS_DIR, SITE_DIR)

def main():
    parser = argparse.ArgumentParser(description='Runs tools in particular order to prepare the site sources.')
    parser.add_argument('-b', '--base-url', default=JEKYLL_DEFAULT_BASE_URL,
                        help=f'Base URL for the Jekyll page (Default = {JEKYLL_DEFAULT_BASE_URL})')
    args = parser.parse_args()
    clean(SITE_DIR)
    copy_jekyll_files()
    apply_base_url(args.base_url)
    copy_templates()
    generate_tables()
    generate_xml_snippets()
    generate_schematrons()
    generate_docs()

if __name__ == '__main__':
    main()
