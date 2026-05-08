#!/usr/bin/env python3
"""
XML Validator Script
Validates XML files or folders against an XSD schema using lxml.
"""

import argparse
import os
import sys
from lxml import etree


def validate_xml(xml_path, xsd_path):
    """Validate an XML file against an XSD schema."""
    try:
        # Parse the XSD schema
        with open(xsd_path, 'rb') as xsd_file:
            schema_doc = etree.parse(xsd_file)
            schema = etree.XMLSchema(schema_doc)

        # Parse the XML file
        with open(xml_path, 'rb') as xml_file:
            xml_doc = etree.parse(xml_file)

        # Validate
        if schema.validate(xml_doc):
            print(f"✓ {xml_path} is valid.")
            return True
        else:
            print(f"✗ {xml_path} is invalid:")
            for error in schema.error_log:
                print(f"  - Line {error.line}: {error.message}")
            return False
    except Exception as e:
        print(f"✗ Error validating {xml_path}: {e}")
        return False


def validate_folder(folder_path, xsd_path):
    """Recursively validate all XML files in a folder."""
    validated_count = 0
    for root, _, files in os.walk(folder_path):
        for file in files:
            if file.lower().endswith('.xml'):
                xml_path = os.path.join(root, file)
                validate_xml(xml_path, xsd_path)
                validated_count += 1
    print(f"\nValidated {validated_count} XML files in {folder_path}.")


def main():
    parser = argparse.ArgumentParser(
        description="Validate XML files or folders against an XSD schema."
    )
    parser.add_argument(
        "--xml",
        required=True,
        help="Path to the XML file or folder containing XML files."
    )
    parser.add_argument(
        "--xsd",
        required=True,
        help="Path to the XSD schema file."
    )

    args = parser.parse_args()

    if not os.path.exists(args.xml):
        print(f"Error: XML path '{args.xml}' does not exist.")
        sys.exit(1)
    
    if not os.path.exists(args.xsd):
        print(f"Error: XSD path '{args.xsd}' does not exist.")
        sys.exit(1)

    if os.path.isdir(args.xml):
        validate_folder(args.xml, args.xsd)
    else:
        validate_xml(args.xml, args.xsd)


if __name__ == "__main__":
    main()