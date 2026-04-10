#!/usr/bin/env python3
"""
Test script to verify that the starting element issue has been fixed
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from md_builder import get_element_metadata

def test_starting_elements():
    """Test that we can find the correct starting elements"""
    
    xsd_path = "../../xsd/xsd/NeTEx_publication.xsd"
    
    # Test elements that should be found as starting elements
    test_elements = [
        "CompositeFrame",
        "ResourceFrame", 
        "ServiceFrame",
        "FrameDefaults",
        "TimetableFrame",
        "SiteFrame"
    ]
    
    print("Testing starting element metadata extraction...")
    print("=" * 50)
    
    all_found = True
    for element_name in test_elements:
        print(f"\nTesting: {element_name}")
        metadata = get_element_metadata(xsd_path, element_name)
        
        if metadata:
            print(f"  [OK] Found metadata:")
            print(f"    Cardinality: {metadata.get('cardinality', 'unknown')}")
            print(f"    Type: {metadata.get('type', 'unknown')}")
            desc = metadata.get('description', 'None')
            if desc and len(desc) > 0:
                print(f"    Description: {desc[:80]}...")
            else:
                print(f"    Description: None")
        else:
            print(f"  [NOT FOUND] Not found in XSD")
            all_found = False
    
    print("\n" + "=" * 50)
    if all_found:
        print("SUCCESS: All starting elements found with metadata!")
    else:
        print("PARTIAL: Some elements not found")
    
    return all_found

if __name__ == "__main__":
    test_starting_elements()
