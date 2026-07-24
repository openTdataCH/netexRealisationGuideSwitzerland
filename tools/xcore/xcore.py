import argparse
import os
import subprocess
from pathlib import Path

import requests

from tools.configuration import XSD_FILE_PATH, NETEX_SITE_DIR, DOCS_DIR, SITE_TABLES_DIR

JAVA_OPTS="-Xms4g -Xmx24g -XX:+UseG1GC -XX:+UseStringDeduplication"
XCORE_XQ_PATH="xquery/xcore.xq"

# URL to download the basex.jar
BASEX_JAR_URL="https://files.basex.org/releases/10.6/BaseX106.jar"

# Local path for basex.jar
DEFAULT_BASEX_JAR_PATH="/tmp/basex.jar"

# Default report customization file
DEFAULT_CUSTOM_XML="custom.xml"

def scan_tables(input_dir: Path, output_file_path: str):
    # Process each markdown file
    elements = ""
    for filename in os.listdir(input_dir):
        if filename.endswith('.md'):
            element_name = filename.replace('.md', '')
            elements = elements + "\n" + element_name

    with open(output_file_path, 'w', encoding='utf-8') as f:
        f.write(elements)

def build_xcore_tables(output_dir_path: str, xsd_file_path: str, basex_jar_path: str, custom_xml_path: str, dry_run: bool):

    if not Path(basex_jar_path).exists():
        print(f"basex.jar not found at {basex_jar_path}")
        if not dry_run:
            print(f'Download of {basex_jar_path} prevented by argument dry_run={dry_run}')
        else:
            download_basex_jar(basex_jar_path)

    print(f"> Using basex.jar at {basex_jar_path}")

    xcore_opts = f'-b report=contab -b uri="{xsd_file_path}" -b odir="{output_dir_path}" -b custom="{custom_xml_path}" -b dnamesExcluded=".git .github" -b htmlFilePerComplexType=true'

    java_cmd = f'java {JAVA_OPTS} -cp {basex_jar_path} org.basex.BaseX {xcore_opts} {XCORE_XQ_PATH}'

    if not dry_run:
        result = subprocess.run(java_cmd, shell=True)
        print(result)
    else:
        print(f'> Call of java command prevented by argument dry_run={dry_run}')
        print("> You may copy and run the following Java command:")
        print(java_cmd)

def download_basex_jar(basex_jar_path: str):
    print(f"Downloading basex.jar to {basex_jar_path} ...")
    response = requests.get(BASEX_JAR_URL)
    if response.status_code == 200:
        with open(f'{basex_jar_path}', 'wb') as f:
            f.write(response.content)

def parse_args():
    """Parse command line arguments"""
    parser = argparse.ArgumentParser(description='Generate html documentation from NeTEx XSD.')
    parser.add_argument('-o', '--output', default=NETEX_SITE_DIR, help=f'Output folder for markdown files (Default = {NETEX_SITE_DIR})')
    parser.add_argument('-x', '--xsd', default=XSD_FILE_PATH, help=f'XSD schema file for type information (Default = {XSD_FILE_PATH})')
    parser.add_argument('-j', '--basex-jar', default=DEFAULT_BASEX_JAR_PATH, help=f'Path to the basex.jar (Default = {DEFAULT_BASEX_JAR_PATH})')
    parser.add_argument('-c', '--custom-xml', default=DEFAULT_CUSTOM_XML, help=f'Path to the report custom xml file (Default= {DEFAULT_CUSTOM_XML})')
    parser.add_argument('-d','--dry-run',default=False, action='store_true', help=f'Dry run (Default = False)')
    return parser.parse_args()

def main():
    args = parse_args()
    if args.dry_run:
        print("> Dry run ...")

    scan_tables(SITE_TABLES_DIR,"elements.txt")
    build_xcore_tables(args.output, args.xsd, args.basex_jar, args.custom_xml, args.dry_run)

if __name__ == '__main__':
    main()