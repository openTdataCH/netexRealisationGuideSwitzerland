#!/usr/bin/env python3
"""
Test script for build_xml_snippets.py

Tests the XML snippets extraction functionality.
"""

import os
import sys
import tempfile
import shutil
from pathlib import Path

# Add the parent directory to Python path to import the module
sys.path.append(str(Path(__file__).parent))

from build_xml_snippets import extract_snippet_from_template, remove_ch_annotations

def test_remove_ch_annotations():
    """Test the remove_ch_annotations function"""
    print("Testing remove_ch_annotations...")
    
    # Test input with various ch-annotations
    test_input = """<!-- ch-note: This should be preserved -->
<Element>
    <!-- ch-usage: mandatory -->
    <Child>content</Child>
    <!-- ch-notice: Another note to preserve -->
    <!-- usage: forbidden -->
    <Forbidden>excluded</Forbidden>
</Element>
<!-- ch-stop: example stops here -->"""
    
    expected_output = """<!-- This should be preserved -->
<Element>
    <Child>content</Child>
    <!-- Another note to preserve -->
</Element>"""
    
    result = remove_ch_annotations(test_input)
    
    # Check that ch-note and ch-notice are preserved (converted to regular comments)
    assert "<!-- This should be preserved -->" in result
    assert "<!-- Another note to preserve -->" in result
    
    # Check that other ch-annotations are removed
    assert "<!-- ch-usage:" not in result
    assert "<!-- usage:" not in result
    assert "<!-- ch-stop:" not in result
    
    print("[OK] remove_ch_annotations test passed")

def test_simple_snippet_extraction():
    """Test snippet extraction from a simple template"""
    print("Testing simple snippet extraction...")
    
    # Create a temporary test file
    with tempfile.NamedTemporaryFile(mode='w', suffix='.xml', delete=False) as f:
        f.write("""<?xml version="1.0" encoding="UTF-8"?>
<Root>
    <!-- ch-root -->
    <TestElement id="test">
        <!-- ch-note: Important note -->
        <Child>Value</Child>
        <!-- usage: forbidden -->
        <ForbiddenChild>Should be excluded</ForbiddenChild>
    </TestElement>
</Root>""")
        temp_file = f.name
    
    try:
        # Extract snippet
        result = extract_snippet_from_template(temp_file)
        
        # Check that the result is not None
        assert result is not None, "Snippet extraction failed"
        

        
        # Check that the main element is present
        assert "<TestElement" in result
        # The pretty-printer may change the format, so check for Child element in any form
        assert ("<Child>" in result or "<Child/>") in result
        
        # Check that ch-note is preserved as regular comment
        assert "<!-- Important note -->" in result
        
        # Check that forbidden element is excluded
        assert "<ForbiddenChild>" not in result
        
        print("[OK] Simple snippet extraction test passed")
        
    finally:
        # Clean up
        os.unlink(temp_file)

def test_no_ch_markers():
    """Test behavior when ch-start/ch-stop markers are missing"""
    print("Testing behavior with missing ch-markers...")
    
    # Create a temporary test file without markers
    with tempfile.NamedTemporaryFile(mode='w', suffix='.xml', delete=False) as f:
        f.write("""<?xml version="1.0" encoding="UTF-8"?>
<Root>
    <Element>No markers here</Element>
</Root>""")
        temp_file = f.name
    
    try:
        # Extract snippet (should return None)
        result = extract_snippet_from_template(temp_file)
        
        # Should return None when no markers found
        assert result is None, "Expected None for file without ch-markers"
        
        print("[OK] Missing ch-markers test passed")
        
    finally:
        # Clean up
        os.unlink(temp_file)

def test_malformed_xml():
    """Test behavior with malformed XML"""
    print("Testing behavior with malformed XML...")
    
    # Create a temporary test file with malformed XML
    with tempfile.NamedTemporaryFile(mode='w', suffix='.xml', delete=False) as f:
        f.write("""<?xml version="1.0" encoding="UTF-8"?>
<Root>
    <!-- ch-root -->
    <Element>Unclosed element
</Root>""")
        temp_file = f.name
    
    try:
        # Extract snippet (should handle gracefully)
        result = extract_snippet_from_template(temp_file)
        
        # Should return None for malformed XML
        assert result is None, "Expected None for malformed XML"
        
        print("[OK] Malformed XML test passed")
        
    finally:
        # Clean up
        os.unlink(temp_file)

def run_all_tests():
    """Run all tests"""
    print("Running XML Snippets Tool tests...\n")
    
    try:
        test_remove_ch_annotations()
        test_simple_snippet_extraction()
        test_no_ch_markers()
        test_malformed_xml()
        
        print("\n[SUCCESS] All tests passed!")
        return True
        
    except Exception as e:
        print(f"\n[FAILED] Test failed: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == '__main__':
    success = run_all_tests()
    sys.exit(0 if success else 1)