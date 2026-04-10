#!/usr/bin/env python3
"""
Test script for debugging metadata extraction from XSD

This script tests the get_element_metadata function and helps identify
issues with XSD parsing and substitution group traversal.
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from md_builder import get_element_metadata, load_xsd_type_info

def test_metadata_extraction():
    """Test metadata extraction for specific elements"""
    
    # Test with the NeTEx publication XSD
    xsd_path = "../../xsd/xsd/NeTEx_publication.xsd"
    
    if not os.path.exists(xsd_path):
        print(f"Error: XSD file not found at {xsd_path}")
        return
    
    print("Testing metadata extraction from NeTEx XSD")
    print("=" * 50)
    
    # Test elements that should be found in the schema
    test_elements = [
        "PublicationDelivery",
        "FrameDefaults",
        "CompositeFrame",
        "ResourceFrame",
        "ServiceFrame",
        "TypeOfProductCategory",
        "Operator",
        "SiteFrame",
        "TimetableFrame"
    ]
    
    # Also test the basic XSD loading
    print("\n1. Testing basic XSD loading...")
    xsd_type_info = load_xsd_type_info(xsd_path)
    print(f"Loaded {len(xsd_type_info)} type definitions")
    print("Type definitions found:")
    for name, info in list(xsd_type_info.items())[:10]:  # Show first 10
        print(f"  - {name}: {info.get('type', 'unknown')}")
    if len(xsd_type_info) > 10:
        print(f"  ... and {len(xsd_type_info) - 10} more")
    
    # Test metadata extraction for each element
    print("\n2. Testing metadata extraction for specific elements...")
    for element_name in test_elements:
        print(f"\nTesting: {element_name}")
        metadata = get_element_metadata(xsd_path, element_name)
        
        if metadata:
            print(f"  [OK] Found metadata:")
            print(f"    Cardinality: {metadata.get('cardinality', 'unknown')}")
            print(f"    Type: {metadata.get('type', 'unknown')}")
            print(f"    Description: {metadata.get('description', 'None')[:100]}..." if metadata.get('description') else "    Description: None")
        else:
            print(f"  [NOT FOUND] Not found in XSD")
    
    # Test substitution group traversal
    print("\n3. Testing substitution group traversal...")
    # These elements might be in substitution groups
    substitution_elements = [
        "VehicleJourney",
        "ServiceJourney",
        "TimingLink",
        "StopPoint"
    ]
    
    for element_name in substitution_elements:
        print(f"\nTesting substitution group for: {element_name}")
        metadata = get_element_metadata(xsd_path, element_name)
        
        if metadata:
            print(f"  [OK] Found (may be via substitution group):")
            print(f"    Cardinality: {metadata.get('cardinality', 'unknown')}")
            print(f"    Type: {metadata.get('type', 'unknown')}")
        else:
            print(f"  [NOT FOUND] Not found (even via substitution groups)")
    
    print("\n" + "=" * 50)
    print("Debugging complete!")

if __name__ == "__main__":
    test_metadata_extraction()