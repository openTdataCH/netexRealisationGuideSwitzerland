#!/usr/bin/env python3
"""
Simple test to verify the schematron builder works
"""

import subprocess
import sys
import os

def main():
    print("Testing Schematron Builder...")
    
    # Test 1: Generate schematron
    print("1. Generating schematron from test_simple.xml...")
    cmd = (
        f"{sys.executable} ../template2schematron.py "
        "-t test_simple.xml "
        "-x ../../xsd/xsd/NeTEx_publication.xsd "
        "-i . "
        "-o test_simple_output.sch"
    )
    
    result = subprocess.run(cmd, shell=True, capture_output=True)
    if result.returncode == 0:
        print("   + Schematron generation successful")
    else:
        print(f"   - Schematron generation failed: {result.stderr}")
        return 1
    
    # Test 2: Check if schematron file was created
    if os.path.exists("test_simple_output.sch"):
        print("   + Schematron file created successfully")
        
        # Read a few lines to verify content
        with open("test_simple_output.sch", "r", encoding="utf-8") as f:
            lines = f.readlines()[:5]
            print(f"   + Schematron file contains {len(lines)} lines (showing first few):")
            for line in lines:
                print(f"     {line.strip()}")
    else:
        print("   - Schematron file not created")
        return 1
    
    print("\nSUCCESS: All basic tests passed!")
    return 0

if __name__ == "__main__":
    sys.exit(main())