#!/usr/bin/env python3
"""
check_schematron.py

Usage:
  check_schematron.py -i <xmlfile_or_folder> -s <schematronfile> [--dump-xslt <xslfile>] [--fail-on-first-error]
  check_schematron.py --help

Checks XML file(s) against a Schematron schema and prints all reported problems.
If -i points to a folder, all XML files in that folder (recursively) will be validated.
If --dump-xslt is provided the internal/generated XSLT is written to that file.

Requires: lxml
Install: pip install -U lxml
"""

import sys
import argparse
import os
from concurrent.futures import ProcessPoolExecutor, as_completed
from multiprocessing import cpu_count
from pathlib import Path
from lxml import etree
from lxml.isoschematron import Schematron


def parse_args(argv):
    p = argparse.ArgumentParser(description="Check XML file(s) against a Schematron schema.")
    p.add_argument('-i', '--input', required=True, 
                   help='Input XML file or folder containing XML files')
    p.add_argument('-s', '--schematron', dest='schematron', required=True, 
                   help='Schematron file (ISO Schematron)')
    p.add_argument('-d', '--dump-xslt', dest='dump_xslt', 
                   help='Write the internal/generated XSLT to this file')
    p.add_argument('-f', '--fail-on-first-error', action='store_true', default=False,
                   help='Stop processing after the first validation error (default: False)')
    p.add_argument('-j', '--workers', type=int, default=None,
                   help='Number of parallel workers (default: CPU count)')
    p.add_argument('--sequential', action='store_true', default=False,
                   help='Process files sequentially (no parallel processing)')
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


def create_schematron_validator(schematron_path):
    """
    Create and compile a Schematron validator from the schematron file.
    Uses lxml's native Schematron support for better performance.
    """
    schematron_path = Path(schematron_path)
    
    # Validate file exists
    if not schematron_path.exists():
        raise FileNotFoundError(f"Schematron file not found: {schematron_path}")
    
    # Create and compile the validator using lxml's native support
    try:
        # lxml.isoschematron accepts ElementTree, file-like objects, or filenames
        # We use the path directly as it's most reliable
        schematron_doc = etree.parse(str(schematron_path))
        validator = Schematron(schematron_doc)
    except Exception as e:
        error_msg = f"Failed to compile Schematron {schematron_path}: {e}"
        # Check for common issues
        if "xslt2" in str(e).lower():
            error_msg += "\n\nHINT: lxml.isoschematron only supports queryBinding=\"xslt\" (XSLT 1.0)."
            error_msg += "\nThe Schematron file has queryBinding=\"xslt2\" which is not supported."
            error_msg += "\nRegenerate the Schematron file with queryBinding=\"xslt\"."
        raise ValueError(error_msg)
    
    return validator


def get_validation_report(validator):
    """
    Get validation report from lxml.isoschematron validator.
    lxml.isoschematron uses error_log (an _ListErrorLog object) instead of validation_report.
    """
    # First try validation_report
    svrl = validator.validation_report
    if svrl is not None:
        return svrl
    
    # If validation_report is None, try error_log
    # error_log is an _ListErrorLog object in lxml.isoschematron
    error_log = getattr(validator, 'error_log', None)
    if error_log is not None:
        # error_log is a list-like object containing _LogEntry objects
        # Each entry's string representation contains SVRL fragments prefixed with file:line info
        try:
            # Create a proper SVRL document root with namespace
            SVRL_NS = 'http://purl.oclc.org/dsdl/svrl'
            svrl_root = etree.Element('{' + SVRL_NS + '}schematron-output', nsmap={'svrl': SVRL_NS})
            
            # Process each error in the error_log
            for error in error_log:
                error_str = str(error)
                # Find where the actual SVRL XML starts (after the error message prefix)
                xml_start = error_str.find('<svrl:')
                if xml_start >= 0:
                    xml_part = error_str[xml_start:]
                    # Parse the SVRL fragment
                    try:
                        fragment = etree.fromstring(xml_part.encode('utf-8'))
                        svrl_root.append(fragment)
                    except Exception:
                        # If parsing fails, skip this error
                        pass
            
            # If we found any SVRL fragments, return the document
            if len(svrl_root) > 0:
                return svrl_root
        except Exception:
            pass
    
    return None


def validate_single_file(args_tuple):
    """
    Validate a single XML file against a pre-compiled Schematron validator.
    This function is designed to be called from a ProcessPoolExecutor.
    
    args_tuple: (xml_file_path, schematron_path, fail_on_first_error)
    Returns: (xml_file_path, is_valid, svrl_string, error_message)
    """
    xml_file_path, schematron_path, fail_on_first_error = args_tuple
    
    try:
        xml_file_path = Path(xml_file_path)
        schematron_path = Path(schematron_path)
        
        # Create validator for this process (each process gets its own)
        # Note: We compile once per process, not per file
        validator = create_schematron_validator(schematron_path)
        
        # Read file in binary mode for efficiency
        with open(xml_file_path, 'rb') as f:
            xml_content = f.read()
        
        # Parse XML
        try:
            doc = etree.fromstring(xml_content)
        except etree.XMLSyntaxError as e:
            return (str(xml_file_path), False, None, f"XML syntax error: {e}")
        
        # Validate
        is_valid = validator.validate(doc)
        
        # Get validation report (SVRL) - use helper to handle lxml.isoschematron API
        svrl = get_validation_report(validator)
        if svrl is not None:
            # Disable pretty printing for speed
            svrl_str = etree.tostring(svrl, pretty_print=False).decode('utf-8')
        else:
            svrl_str = ""
        
        return (str(xml_file_path), is_valid, svrl_str, None)
        
    except Exception as e:
        return (str(xml_file_path), False, None, str(e))


def get_xslt_from_validator(validator):
    """
    Extract XSLT from a compiled Schematron validator.
    lxml.isoschematron compiles to XSLT internally.
    """
    # The validator has a schema attribute which is an XMLSchema
    # The XMLSchema has an xslt attribute with the compiled stylesheet
    if hasattr(validator, 'schema') and hasattr(validator.schema, 'xslt'):
        return etree.tostring(validator.schema.xslt, pretty_print=True).decode('utf-8')
    return None


def main(argv=None):
    try:
        args = parse_args(argv)

        # Validate input path and schematron file
        validate_files(args.input, args.schematron)

        # Get all XML files to validate
        xml_files = get_xml_files(args.input)
        
        print(f"Found {len(xml_files)} XML file(s) to validate against {args.schematron}")

        overall_success = True
        
        # Determine number of workers
        if args.sequential:
            num_workers = 1
        elif args.workers is not None:
            num_workers = args.workers
        else:
            num_workers = cpu_count()
        
        print(f"Using {num_workers} worker(s) for validation")
        
        # Handle XSLT dump if requested
        if args.dump_xslt:
            try:
                validator = create_schematron_validator(args.schematron)
                xslt_content = get_xslt_from_validator(validator)
                if xslt_content:
                    with open(args.dump_xslt, 'w', encoding='utf-8') as f:
                        f.write(xslt_content)
                    print(f"XSLT dumped to: {args.dump_xslt}")
                else:
                    print(f"Warning: XSLT not available from lxml.isoschematron validator", file=sys.stderr)
            except Exception as e:
                print(f"Warning: Could not dump XSLT: {e}", file=sys.stderr)

        # Sequential processing (simple, for small number of files or debugging)
        if args.sequential or num_workers == 1:
            # Create validator once for sequential processing
            validator = create_schematron_validator(args.schematron)
            
            for xml_file in xml_files:
                print(f"\nValidating {xml_file}...")
                
                try:
                    # Read file efficiently
                    with open(xml_file, 'rb') as f:
                        xml_content = f.read()
                    
                    doc = etree.fromstring(xml_content)
                    is_valid = validator.validate(doc)
                    
                    # Get SVRL report - use helper to handle lxml.isoschematron API
                    svrl = get_validation_report(validator)
                    if svrl is not None:
                        report_str = etree.tostring(svrl, pretty_print=False).decode('utf-8')
                        print("Validation Report:")
                        print(report_str)
                    else:
                        print("No validation report generated")
                    
                    print(f"Validation Result: {'SUCCESS' if is_valid else 'FAILED'}")
                    
                    if not is_valid:
                        overall_success = False
                        if args.fail_on_first_error:
                            print(f"\nStopping after first error due to --fail-on-first-error")
                            break
                            
                except Exception as e:
                    print(f"ERROR validating {xml_file}: {e}")
                    overall_success = False
                    if args.fail_on_first_error:
                        break

        else:
            # Parallel processing
            print(f"Processing {len(xml_files)} files in parallel...")
            
            # Prepare arguments for parallel processing
            # Note: We pass the schematron path to each worker, which will compile it once per process
            work_args = [(str(f), args.schematron, args.fail_on_first_error) 
                         for f in xml_files]
            
            with ProcessPoolExecutor(max_workers=num_workers) as executor:
                # Submit all tasks
                futures = {executor.submit(validate_single_file, arg): arg[0] 
                           for arg in work_args}
                
                # Process results as they complete
                results_processed = 0
                for future in as_completed(futures):
                    results_processed += 1
                    xml_file_path, is_valid, svrl_str, error = future.result()
                    
                    print(f"\n[{results_processed}/{len(xml_files)}] Validating {xml_file_path}...")
                    
                    if error:
                        print(f"ERROR: {error}")
                        overall_success = False
                        if args.fail_on_first_error:
                            # Cancel remaining futures
                            for f in futures:
                                f.cancel()
                            print(f"\nStopping after first error due to --fail-on-first-error")
                            break
                    else:
                        if svrl_str:
                            print("Validation Report:")
                            print(svrl_str)
                        print(f"Validation Result: {'SUCCESS' if is_valid else 'FAILED'}")
                        
                        if not is_valid:
                            overall_success = False
                            if args.fail_on_first_error:
                                # Cancel remaining futures
                                for f in futures:
                                    f.cancel()
                                print(f"\nStopping after first error due to --fail-on-first-error")
                                break
        
        return 0 if overall_success else 1

    except Exception as e:
        print(f"ERROR: {e}", file=sys.stderr)
        import traceback
        traceback.print_exc(file=sys.stderr)
        return 1


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))