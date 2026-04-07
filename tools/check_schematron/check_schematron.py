#!/usr/bin/env python3
"""
check_schematron.py

Usage:
  check_schematron.py -i <xmlfile> -s <schematronfile> [--dump-xslt <xslfile>]
  check_schematron.py --help

Checks an XML file against a Schematron schema and prints all reported problems.
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
    p = argparse.ArgumentParser(description="Check an XML file against a Schematron schema.")
    p.add_argument('-i', '--input', required=True, help='Input XML file')
    p.add_argument('-s', '--schematron', dest='schematron', required=True, help='Schematron file (ISO Schematron)')
    p.add_argument('-d', '--dump-xslt', dest='dump_xslt', help='Write the internal/generated XSLT to this file')
    return p.parse_args(argv)

def validate_files(input_file, schematron_file):
    """Validate that input files exist and are readable"""
    if not Path(input_file).exists():
        raise FileNotFoundError(f"Input XML file not found: {input_file}")
    if not Path(schematron_file).exists():
        raise FileNotFoundError(f"Schematron file not found: {schematron_file}")

def main(argv):
    try:
        args = parse_args(argv)

        # Validate input files
        validate_files(args.input, args.schematron)

        print(f"Validating {args.input} against {args.schematron}...")
        result = validate_document(Path(args.input), Path(args.schematron))

        # Handle XSLT dump if requested
        if args.dump_xslt:
            xslt_content = result.get_xslt()
            with open(args.dump_xslt, 'w', encoding='utf-8') as f:
                f.write(xslt_content)
            print(f"XSLT dumped to: {args.dump_xslt}")

        # Get and display validation results
        svrl = result.get_svrl()
        report_str = etree.tostring(svrl, pretty_print=True).decode('utf-8')
        print("\nValidation Report:")
        print(report_str)

        is_valid = result.is_valid()
        print(f"\nValidation Result: {'SUCCESS' if is_valid else 'FAILED'}")

        return 0 if is_valid else 1

    except Exception as e:
        print(f"ERROR: {e}", file=sys.stderr)
        return 1

if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))