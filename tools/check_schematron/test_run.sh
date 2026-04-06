#!/bin/bash

# Test script for Schematron Validator
# This script tests the schematron validator with various schematron files

echo "=== Schematron Validator Test Run ==="
echo ""

# Check if we have any schematron files
SCHEMATRON_DIR="../../generated/schematrons"
if [ ! -d "$SCHEMATRON_DIR" ]; then
    echo "Error: Schematron directory not found at $SCHEMATRON_DIR"
    exit 1
fi

# Check if we have test XML files
TEST_XML="../../test_data/example.xml"
if [ ! -f "$TEST_XML" ]; then
    echo "Warning: Test XML file not found at $TEST_XML"
    echo "Creating a simple test XML file..."
    mkdir -p ../../test_data
    cat > "$TEST_XML" << 'EOF'
<?xml version="1.0" encoding="UTF-8"?>
<TestRoot>
    <TestElement>Test Content</TestElement>
</TestRoot>
EOF
fi

echo "1. Testing with available schematron files..."
echo ""

# Test with each schematron file found
for SCH_FILE in "$SCHEMATRON_DIR"/*.sch; do
    if [ -f "$SCH_FILE" ]; then
        echo "Testing with: $(basename "$SCH_FILE")"
        python check_schematron.py -i "$TEST_XML" -s "$SCH_FILE"
        echo ""
    fi
done

echo "2. Testing with XSLT dump feature..."
echo ""
# Test XSLT dump with first schematron file
FIRST_SCH="$SCHEMATRON_DIR"/$(ls "$SCHEMATRON_DIR"/*.sch | head -n 1 | xargs basename)
if [ -n "$FIRST_SCH" ]; then
    python check_schematron.py -i "$TEST_XML" -s "$FIRST_SCH" --dump-xslt "./test_output.xslt"
    if [ -f "./test_output.xslt" ]; then
        echo "XSLT successfully dumped to test_output.xslt"
        echo "File size: $(wc -c < ./test_output.xslt) bytes"
    fi
else
    echo "No schematron files found for XSLT dump test"
fi

echo ""
echo "=== Test Run Complete ==="
