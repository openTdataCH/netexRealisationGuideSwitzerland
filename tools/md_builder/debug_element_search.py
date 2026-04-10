#!/usr/bin/env python3
"""
Debug script to test element search functionality
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from md_builder import search_xsd_files_for_element

def test_element_search():
    """Test the element search functionality"""
    
    base_dir = "../../xsd/xsd"
    
    # Test elements that should be found
    test_elements = [
        "CompositeFrame",
        "ResourceFrame", 
        "ServiceFrame",
        "FrameDefaults",
        "Operator"
    ]
    
    print("Testing element search functionality...")
    print("=" * 50)
    
    for element_name in test_elements:
        print(f"\nSearching for: {element_name}")
        element_found, found_in_file = search_xsd_files_for_element(base_dir, element_name)
        
        if element_found is not None:
            print(f"  [FOUND] in {found_in_file}")
            print(f"    Tag: {element_found.tag}")
            print(f"    Attributes: {element_found.attrib}")
            
            # Check for inline types
            namespaces = {'xs': 'http://www.w3.org/2001/XMLSchema'}
            complex_type = element_found.find('xs:complexType', namespaces)
            simple_type = element_found.find('xs:simpleType', namespaces)
            
            if complex_type is not None:
                print(f"    Has inline complexType: Yes")
            elif simple_type is not None:
                print(f"    Has inline simpleType: Yes")
            else:
                type_attr = element_found.get('type')
                print(f"    Type attribute: {type_attr}")
        else:
            print(f"  [NOT FOUND]")

if __name__ == "__main__":
    test_element_search()
