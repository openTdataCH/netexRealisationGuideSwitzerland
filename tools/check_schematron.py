#!/usr/bin/env python3
"""
check_schematron.py

Usage:
  check_schematron.py -i <xmlfile> --s <schematronfile>
  check_schematron.py --help

Checks an XML file against a Schematron schema and prints all reported problems.
If no problems are found prints "OK".

Requires: lxml
Install: pip install lxml
"""

import sys
import argparse
from lxml import etree, isoschematron

def parse_args(argv):
    p = argparse.ArgumentParser(description="Check an XML file against a Schematron schema.")
    p.add_argument('-i', '--input', required=True, help='Input XML file')
    p.add_argument('--s', '--schematron', dest='schematron', required=True, help='Schematron file (ISO Schematron)')
    return p.parse_args(argv)

def load_xml(path):
    try:
        return etree.parse(path)
    except (OSError, etree.XMLSyntaxError) as e:
        print(f"Error reading/parsing XML '{path}': {e}", file=sys.stderr)
        return None

def load_schematron(path):
    try:
        sch_doc = etree.parse(path)
        return isoschematron.Schematron(sch_doc)
    except (OSError, etree.XMLSyntaxError, etree.SchematronError) as e:
        print(f"Error reading/parsing Schematron '{path}': {e}", file=sys.stderr)
        return None

def extract_asserts_from_report(report_root):
    """
    Given an lxml element returned by schematron.validation_report (Schematron validation output),
    collect assert/report messages, their context and diagnostic info if present.
    """
    # Schematron report uses the namespace: http://purl.oclc.org/dsdl/schematron
    ns = {'sch': 'http://purl.oclc.org/dsdl/schematron'}
    results = []
    # look for failed-assert and successful-report (depending on schema rules)
    for tag in ('failed-assert', 'successful-report'):
        for node in report_root.findall('.//sch:' + tag, namespaces=ns):
            location = node.get('location') or ''
            role = tag  # or node.get('role')
            test = node.get('test') or ''
            # find human readable message: the <text> element inside
            text_el = node.find('.//sch:text', namespaces=ns)
            message = (text_el.text or '').strip() if text_el is not None else ''.join(node.itertext()).strip()
            # severity/flag could be on the parent <rule> or on the assert element (role/test)
            results.append({
                'type': tag,
                'location': location,
                'test': test,
                'message': message
            })
    return results

def main(argv):
    args = parse_args(argv)
    xml_tree = load_xml(args.input)
    if xml_tree is None:
        return 2

    schematron = load_schematron(args.schematron)
    if schematron is None:
        return 2

    # Validate: schematron.assert_ returns True/False, schematron.validate is alias in some versions.
    try:
        ok = schematron.validate(xml_tree)
    except Exception as e:
        print(f"Error during Schematron validation: {e}", file=sys.stderr)
        return 2

    # If the Schematron object has a validation report, extract details.
    report = None
    # lxml stores the report in schematron.validation_report (ElementTree) or schematron.validation_report.getroot()
    if hasattr(schematron, 'validation_report') and schematron.validation_report is not None:
        report = schematron.validation_report
    elif hasattr(schematron, 'validation_report_str') and schematron.validation_report_str:
        try:
            report = etree.fromstring(schematron.validation_report_str.encode('utf-8'))
        except Exception:
            report = None

    problems = []
    if report is not None:
        # ensure we have an Element (root)
        if isinstance(report, etree._ElementTree):
            root = report.getroot()
        else:
            root = report
        problems = extract_asserts_from_report(root)

    # If lxml's Schematron didn't produce report nodes (some implementations), but validate returned False,
    # we still need to indicate failure.
    if not ok:
        if not problems:
            # generic failure without detailed nodes
            print("Schematron validation failed, but no assertion details were found in the report.")
            return 1
        else:
            # print each problem
            for idx, p in enumerate(problems, start=1):
                print(f"[{idx}] {p['type']} at '{p['location']}' - {p['message']}")
            return 1
    else:
        # ok == True
        if not problems:
            print("OK")
            return 0
        else:
            # Some Schematrons may produce successful-report nodes even when overall OK.
            # Print them as informational.
            for idx, p in enumerate(problems, start=1):
                print(f"[{idx}] {p['type']} at '{p['location']}' - {p['message']}")
            print("OK")
            return 0

if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
