#!/bin/bash

# Test script for Markdown Builder
# This script runs the markdown builder on test files and real templates

echo "=== Markdown Builder Test Run ==="
echo ""

# Test with our test files first
echo "1. Testing with test files..."
python md_builder.py -i "." -o "./test_output" -x "../../../xsd/xsd/NeTEx_publication.xsd"

echo ""
echo "2. Testing with real templates..."
python md_builder.py -i "../../templates" -o "../../generated/markdown-examples" -x "../../../xsd/xsd/NeTEx_publication.xsd"

echo ""
echo "3. Checking generated files..."
if [ -d "./test_output" ]; then
    echo "Test output directory: ./test_output"
    ls -la ./test_output/
else
    echo "No test output directory found"
fi

echo ""
echo "=== Test Run Complete ==="