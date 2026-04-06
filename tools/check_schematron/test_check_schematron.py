#!/usr/bin/env python3
"""
Test script for check_schematron.py
Tests the schematron validation functionality
"""

import os
import sys
import tempfile
import subprocess
from pathlib import Path

def test_basic_validation():
    """Test basic validation with existing schematron files"""
    print("Testing basic validation...")
    
    # Find a schematron file
    schematron_dir = Path("../../generated/schematrons")
    if not schematron_dir.exists():
        print("ERROR: Schematron directory not found")
        return False
    
    sch_files = list(schematron_dir.glob("*.sch"))
    if not sch_files:
        print("ERROR: No schematron files found")
        return False
    
    # Create a simple test XML
    test_xml = """<?xml version="1.0" encoding="UTF-8"?>
<TestRoot>
    <TestElement>Test Content</TestElement>
</TestRoot>"""
    
    with tempfile.NamedTemporaryFile(mode='w', suffix='.xml', delete=False) as f:
        f.write(test_xml)
        xml_file = f.name
    
    try:
        # Run validation
        result = subprocess.run([
            sys.executable, "check_schematron.py",
            "-i", xml_file,
            "-s", str(sch_files[0])
        ], capture_output=True, text=True)
        
        print(f"Return code: {result.returncode}")
        print(f"Output length: {len(result.stdout)} characters")
        print("Validation completed successfully")
        return True
        
    except Exception as e:
        print(f"ERROR: {e}")
        return False
    finally:
        os.unlink(xml_file)

def test_xslt_dump():
    """Test XSLT dump functionality"""
    print("\nTesting XSLT dump...")
    
    schematron_dir = Path("../../generated/schematrons")
    sch_files = list(schematron_dir.glob("*.sch"))
    if not sch_files:
        print("ERROR: No schematron files found")
        return False
    
    # Create test files
    test_xml = """<?xml version="1.0" encoding="UTF-8"?>
<TestRoot>
    <TestElement>Test Content</TestElement>
</TestRoot>"""
    
    with tempfile.NamedTemporaryFile(mode='w', suffix='.xml', delete=False) as f:
        f.write(test_xml)
        xml_file = f.name
    
    xslt_file = "test_dump.xslt"
    
    try:
        # Run with XSLT dump
        result = subprocess.run([
            sys.executable, "check_schematron.py",
            "-i", xml_file,
            "-s", str(sch_files[0]),
            "-d", xslt_file
        ], capture_output=True, text=True)
        
        # Check if XSLT file was created
        if os.path.exists(xslt_file):
            xslt_size = os.path.getsize(xslt_file)
            print(f"XSLT file created: {xslt_file}")
            print(f"XSLT file size: {xslt_size} bytes")
            os.unlink(xslt_file)
            print("XSLT dump test passed")
            return True
        else:
            print("ERROR: XSLT file was not created")
            return False
            
    except Exception as e:
        print(f"ERROR: {e}")
        return False
    finally:
        os.unlink(xml_file)
        if os.path.exists(xslt_file):
            os.unlink(xslt_file)

def test_help():
    """Test help functionality"""
    print("\nTesting help functionality...")
    
    try:
        result = subprocess.run([
            sys.executable, "check_schematron.py", "--help"
        ], capture_output=True, text=True)
        
        if result.returncode == 0 and "Check an XML file against a Schematron schema" in result.stdout:
            print("Help test passed")
            return True
        else:
            print("ERROR: Help output not as expected")
            return False
            
    except Exception as e:
        print(f"ERROR: {e}")
        return False

def main():
    """Run all tests"""
    print("=== Schematron Validator Tests ===")
    print("=" * 40)
    
    tests = [
        test_basic_validation,
        test_xslt_dump,
        test_help
    ]
    
    passed = 0
    total = len(tests)
    
    for test in tests:
        if test():
            passed += 1
        else:
            print(f"FAILED: {test.__name__}")
    
    print("\n" + "=" * 40)
    print(f"Tests passed: {passed}/{total}")
    
    if passed == total:
        print("All tests passed!")
        return 0
    else:
        print("Some tests failed!")
        return 1

if __name__ == '__main__':
    sys.exit(main())
