#!/usr/bin/env python3
"""
Simple debug script to test element finding
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from lxml import etree

def test_simple_element_finding():
    """Test simple element finding"""
    
    # Test with CompositeFrame
    file_path = "../../xsd/xsd/netex_framework/netex_frames/netex_compositeFrame_version.xsd"
    element_name = "CompositeFrame"
    
    print(f"Testing element finding for {element_name} in {file_path}")
    
    # Parse the file
    parser = etree.XMLParser()
    xsd_doc = etree.parse(file_path, parser)
    namespaces = {'xs': 'http://www.w3.org/2001/XMLSchema'}
    
    # Try to find the element
    element_xpath = f"//xs:element[@name='{element_name}']"
    elements = xsd_doc.xpath(element_xpath, namespaces=namespaces)
    
    print(f"Found {len(elements)} elements")
    
    if elements:
        element = elements[0]
        print(f"Element tag: {element.tag}")
        print(f"Element attributes: {element.attrib}")
        print(f"Element text: {element.text}")
        
        # Check for child elements
        for child in element:
            print(f"Child: {child.tag}")
        
        # Check for complexType
        complex_type = element.find('xs:complexType', namespaces)
        if complex_type is not None:
            print(f"Found complexType: {complex_type.tag}")
        else:
            print("No complexType found")
            
        # Try without namespace
        complex_type_no_ns = element.find('complexType')
        if complex_type_no_ns is not None:
            print(f"Found complexType (no ns): {complex_type_no_ns.tag}")
    else:
        print("No elements found")

if __name__ == "__main__":
    test_simple_element_finding()
