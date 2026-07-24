import argparse
import subprocess
from pathlib import Path

import requests

from tools.configuration import XSD_FILE_PATH, NETEX_SITE_DIR

JAVA_OPTS="-Xms4g -Xmx24g -XX:+UseG1GC -XX:+UseStringDeduplication"
XCORE_XQ_PATH="xquery/xcore.xq"

# URL to download the basex.jar
BASEX_JAR_URL="https://files.basex.org/releases/10.6/BaseX106.jar"

# Local path for basex.jar
DEFAULT_BASEX_JAR_PATH="/tmp/basex.jar"

# Default report customization file
DEFAULT_CUSTOM_XML="custom.xml"

def build_xcore_tables(output_dir_path: str, xsd_file_path: str, basex_jar_path: str, custom_xml_path: str):

    if not Path(basex_jar_path).exists():
        print(f"basex.jar not found at {basex_jar_path}")
        download_basex_jar(basex_jar_path)

    print(f"Using basex.jar at {basex_jar_path}")

    xcore_opts = f'-b report=contab -b uri="{xsd_file_path}" -b odir="{output_dir_path}" -b custom="{custom_xml_path}" -b dnamesExcluded=".git .github" -b htmlFilePerComplexType=true'

    java_cmd = f'java {JAVA_OPTS} -cp {basex_jar_path} org.basex.BaseX {xcore_opts} {XCORE_XQ_PATH}'

    print(java_cmd)
    result = subprocess.run(java_cmd, shell=True)
    print(result)

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
    return parser.parse_args()

def main():
    args = parse_args()
    build_xcore_tables(args.output, args.xsd, args.basex_jar, args.custom_xml)

if __name__ == '__main__':
    main()