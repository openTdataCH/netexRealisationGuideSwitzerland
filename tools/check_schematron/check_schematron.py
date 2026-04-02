#!/usr/bin/env python3
"""
check_schematron.py

Usage:
  check_schematron.py -i <xmlfile> --s <schematronfile> [--dump-xslt <xslfile>]
  check_schematron.py --help

Checks an XML file against a Schematron schema and prints all reported problems.
If --dump-xslt is provided the internal/generated XSLT is written to that file.

Requires: lxml
Install: pip install -U lxml
"""

import sys
import argparse
from lxml import etree
from pathlib import Path

from pyschematron import validate_document

def parse_args(argv):
    p = argparse.ArgumentParser(description="Check an XML file against a Schematron schema.")
    p.add_argument('-i', '--input', required=True, help='Input XML file')
    p.add_argument('-s', '-schematron', dest='schematron', required=True, help='Schematron file (ISO Schematron)')
    p.add_argument('-d', '-dump-xslt', dest='dump_xslt', help='Write the internal/generated XSLT to this file')
    return p.parse_args(argv)



def main(argv):
    args = parse_args(argv)
    result=validate_document(Path(args.input),Path(args.schematron))

    svrl = result.get_svrl()
    svrl = result.get_svrl()

    report_str = etree.tostring(svrl, pretty_print=True).decode('utf-8')
    print(report_str)
    print(result.is_valid())

if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
