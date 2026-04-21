#!/usr/bin/env python3
"""
check_schematron.py

Usage:
  check_schematron.py -i <xmlfile_or_folder> -s <schematronfile> [--dump-xslt <xslfile>]
  check_schematron.py --help

Checks XML file(s) against a Schematron schema and prints all reported problems.
If -i points to a folder, all XML files in that folder (recursively) will be validated.
If --dump-xslt is provided the internal/generated XSLT is written to that file.

Requires: lxml, pyschematron
Install: pip install -U lxml pyschematron
"""

import sys
import argparse
from lxml import etree
from pathlib import Path

from pyschematron import validate_document

def parse_args(argv):
    p = argparse.ArgumentParser(description="Check XML file(s) against a Schematron schema.")
    p.add_argument('-i', '--input', required=True, help='Input XML file or folder containing XML files')
    p.add_argument('-s', '--schematron', dest='schematron', required=True, help='Schematron file (ISO Schematron)')
    p.add_argument('-d', '--dump-xslt', dest='dump_xslt', help='Write the internal/generated XSLT to this file')
    return p.parse_args(argv)

def validate_files(input_path, schematron_file):
    """Validate that input path and schematron file exist and are readable"""
    if not Path(schematron_file).exists():
        raise FileNotFoundError(f"Schematron file not found: {schematron_file}")
    
    if not Path(input_path).exists():
        raise FileNotFoundError(f"Input path not found: {input_path}")

def get_xml_files(input_path):
    """Get all XML files from input path (file or folder)"""
    input_path = Path(input_path)
    
    if input_path.is_file():
        # Single file
        if input_path.suffix.lower() == '.xml':
            return [input_path]
        else:
            raise ValueError(f"Input file must be an XML file: {input_path}")
    elif input_path.is_dir():
        # Folder - find all XML files recursively
        xml_files = list(input_path.rglob('*.xml'))
        if not xml_files:
            raise ValueError(f"No XML files found in folder: {input_path}")
        return xml_files
    else:
        raise ValueError(f"Invalid input path: {input_path}")

def main(argv):
    try:
        args = parse_args(argv)

        # Validate input path and schematron file
        validate_files(args.input, args.schematron)

        # Get all XML files to validate
        xml_files = get_xml_files(args.input)
        
        print(f"Found {len(xml_files)} XML file(s) to validate against {args.schematron}")
        
        overall_success = True
        
        # Handle XSLT dump if requested (only once)
        if args.dump_xslt:
            # Use first file to generate XSLT
            first_file = xml_files[0]
            result = validate_document(first_file, Path(args.schematron))
            xslt_content = result.get_xslt()
            with open(args.dump_xslt, 'w', encoding='utf-8') as f:
                f.write(xslt_content)
            print(f"XSLT dumped to: {args.dump_xslt}")

        # Validate each XML file
        for xml_file in xml_files:
            print(f"\nValidating {xml_file}...")
            result = validate_document(xml_file, Path(args.schematron))

            # Get and display validation results
            svrl = result.get_svrl()
            report_str = etree.tostring(svrl, pretty_print=True).decode('utf-8')
            print("Validation Report:")
            print(report_str)

            is_valid = result.is_valid()
            print(f"Validation Result: {'SUCCESS' if is_valid else 'FAILED'}")
            
            if not is_valid:
                overall_success = False

        return 0 if overall_success else 1

    except Exception as e:
        print(f"ERROR: {e}", file=sys.stderr)
        return 1

if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))