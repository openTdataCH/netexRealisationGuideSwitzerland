#!/usr/bin/env python3
"""
Debug script to test metadata extraction functionality
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from md_builder import get_element_metadata

def test_metadata_extraction():
    """Test the metadata extraction functionality"""
    
    xsd_path = "../../xsd/xsd/NeTEx_publication.xsd"
    
    # Test elements that should be found
    test_elements = [
        "CompositeFrame",
        "ResourceFrame", 
        "ServiceFrame",
        "FrameDefaults",
        "Operator",
        "PublicationDelivery"
    ]
    
    print("Testing metadata extraction functionality...")
    print("=" * 60)
    
    for element_name in test_elements:
        print(f"\nTesting: {element_name}")
        metadata = get_element_metadata(xsd_path, element_name)
        
        if metadata:
            print(f"  [OK] Found metadata:")
            print(f"    Cardinality: {metadata.get('cardinality', 'unknown')}")
            print(f"    Type: {metadata.get('type', 'unknown')}")
            desc = metadata.get('description', 'None')
            if desc:
                print(f"    Description: {desc[:100]}...")
            else:
                print(f"    Description: None")
        else:
            print(f"  [NOT FOUND] Not found in XSD")

if __name__ == "__main__":
    test_metadata_extraction()
