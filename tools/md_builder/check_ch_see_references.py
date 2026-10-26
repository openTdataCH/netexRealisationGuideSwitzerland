#!/usr/bin/env python3
"""
Simple ch-see reference checker for NeTEx templates
Checks if XML files referenced by ch-see annotations exist.
"""

import argparse
import os

from tools.safe_path import safe_join
from tools.safe_xml import safe_parse

# Global counters
total_references = 0
valid_references = 0
invalid_references = 0
# List of (filename, element_name, expected_path) tuples
missing_files: list[tuple] = []
# List of warning messages
warnings_list: list[str] = []


def get_element_name(element):
    """Get the local name of an XML element"""
    if hasattr(element, "tag"):
        from lxml import etree
        return etree.QName(element).localname
    return None


def process_ch_see_reference(comment_text, filename, file_path, input_folder):
    """Process a single ch-see reference with explicit filename"""
    global total_references, valid_references, invalid_references

    total_references += 1
    see_reference = comment_text.replace("ch-see:", "").strip()

    # Check if the referenced file exists
    # The reference could be just a filename or a relative path
    if os.path.isabs(see_reference):
        # Absolute path — verify it stays within input_folder
        ref_path = os.path.realpath(see_reference)
        input_real = os.path.realpath(input_folder)
        if not ref_path.startswith(input_real + os.sep) and ref_path != input_real:
            invalid_references += 1
            display_ref = see_reference.replace("\\", "/")
            print(f"[BLOCKED] Path traversal attempt in {filename}: {display_ref}")
            missing_files.append((filename, None, display_ref))
            return
    else:
        # Relative path — resolve within input_folder using safe_join
        try:
            ref_path = safe_join(input_folder, see_reference)
        except ValueError:
            invalid_references += 1
            display_ref = see_reference.replace("\\", "/")
            print(f"[BLOCKED] Path traversal attempt in {filename}: {display_ref}")
            missing_files.append((filename, None, display_ref))
            return

    # Normalize path for display (use forward slashes)
    display_ref = see_reference.replace("\\", "/")

    if os.path.exists(ref_path):
        valid_references += 1
        print(f"[VALID] Reference in {filename}: {display_ref}")
    else:
        invalid_references += 1
        print(f"[INVALID] Reference in {filename}: {display_ref}")
        print(f"   Expected at: {ref_path.replace('\\', '/')}")
        missing_files.append((filename, None, ref_path.replace("\\", "/")))


def process_constructed_reference(
    constructed_reference, filename, file_path, elem_name, input_folder
):
    """Process a constructed reference from ch-see without filename"""
    global total_references, valid_references, invalid_references

    total_references += 1

    # Look for elem_name.xml in the same folder as the template
    # Use safe_join to prevent path traversal
    try:
        ref_path = safe_join(input_folder, constructed_reference)
    except ValueError:
        invalid_references += 1
        display_ref = constructed_reference.replace("\\", "/")
        print(
            f"[BLOCKED] Path traversal attempt in {filename} for <{elem_name}>: {display_ref}"
        )
        missing_files.append((filename, elem_name, display_ref))
        return

    # Normalize path for display (use forward slashes)
    display_ref = constructed_reference.replace("\\", "/")

    if os.path.exists(ref_path):
        valid_references += 1
        print(
            f"[VALID] Implicit reference in {filename} for <{elem_name}>: {display_ref}"
        )
    else:
        invalid_references += 1
        print(
            f"[INVALID] Implicit reference in {filename} for <{elem_name}>: {display_ref}"
        )
        print(f"   Expected at: {ref_path.replace('\\', '/')}")
        missing_files.append((filename, elem_name, ref_path.replace("\\", "/")))


def check_ch_see_references(input_folder):
    """Check ch-see references in XML template files."""

    global total_references, valid_references, invalid_references, warnings_list
    total_references = 0
    valid_references = 0
    invalid_references = 0
    missing_files = []
    warnings_list = []

    # Process each XML file in the input folder
    for filename in os.listdir(input_folder):
        if filename.endswith(".xml"):
            file_path = os.path.join(input_folder, filename)

            try:
                # Parse the XML file with XXE protections
                tree = safe_parse(file_path)
                root = tree.getroot()

                # Find all comments in the file
                all_comments = root.xpath("//comment()")

                # Check for ch-see references (both <!-- ch-see --> and <!-- ch-see: file.xml -->)
                for comment in all_comments:
                    if comment.text:
                        comment_text = comment.text.strip()
                        if comment_text.startswith("ch-see:"):
                            # Format: <!-- ch-see: filename.xml -->
                            process_ch_see_reference(comment_text, filename, file_path, input_folder)
                        elif comment_text == "ch-see":
                            # Format: <!-- ch-see --> (no specific file reference)
                            # This means look for a file with the same name as the parent element + .xml
                            parent_element = comment.getparent()
                            if parent_element is not None:
                                elem_name = get_element_name(parent_element)
                                if elem_name:
                                    # Construct reference: elem_name.xml
                                    constructed_reference = f"{elem_name}.xml"
                                    process_constructed_reference(
                                        constructed_reference,
                                        filename,
                                        file_path,
                                        elem_name,
                                        input_folder,
                                    )

            except Exception as e:
                from lxml import etree
                if isinstance(e, etree.XMLSyntaxError):
                    warning_msg = f"XML syntax error in {filename}: {e}"
                else:
                    warning_msg = f"Error processing {filename}: {e}"
                warnings_list.append(warning_msg)
                print(f"WARNING: {warning_msg}")

    # Print summary
    print(f"\n{'='*60}")
    print("ch-see reference checking summary:")
    print(f"  Total ch-see references found: {total_references}")
    print(f"  Valid references: {valid_references}")
    print(f"  Invalid references: {invalid_references}")

    if warnings_list:
        print(f"  Warnings found: {len(warnings_list)}")

    if invalid_references == 0 and not warnings_list:
        print("  Status: All references are valid")
    else:
        status_messages = []
        if invalid_references > 0:
            status_messages.append(f"Found {invalid_references} invalid references")
        if warnings_list:
            status_messages.append(f"Found {len(warnings_list)} warnings")
        print(f"  Status: {', '.join(status_messages)}")

    # Print detailed list of missing files
    if missing_files:
        print(f"\nMissing files ({len(missing_files)}):")
        for filename, elem_name, expected_path in missing_files:
            if elem_name:
                print(f"  - {filename}: <{elem_name}> expects {expected_path}")
            else:
                print(f"  - {filename}: expects {expected_path}")

    # Print detailed list of warnings
    if warnings_list:
        print(f"\nWarnings ({len(warnings_list)}):")
        for i, warning in enumerate(warnings_list, 1):
            print(f"  {i}. {warning}")


def main():
    parser = argparse.ArgumentParser(
        description="Check ch-see references in NeTEx XML templates"
    )
    parser.add_argument(
        "-i", "--input", required=True, help="Input folder containing XML templates"
    )
    args = parser.parse_args()

    # Convert to absolute path
    input_folder = os.path.abspath(args.input)

    if not os.path.isdir(input_folder):
        print(f"Error: Input folder '{input_folder}' does not exist")
        return

    print(f"Checking ch-see references in XML templates from: {input_folder}")
    check_ch_see_references(input_folder)


if __name__ == "__main__":
    main()
