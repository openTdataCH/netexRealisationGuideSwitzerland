#!/bin/bash

# Schematron Validator Execution Script
# This script runs the schematron validator with default parameters

# Default parameters - adjust these as needed
XML_FILE="../../test_data/example.xml"  # Path to your test XML file
SCHEMATRON_FILE="../../generated/schematrons/ch-profile_export_timetable_file.sch"

# Check if files exist
echo "Schematron Validator"
echo "===================="
echo ""

if [ ! -f "$XML_FILE" ]; then
    echo "Error: XML file not found at $XML_FILE"
    echo "Please create a test XML file or update the XML_FILE variable in run.sh"
    exit 1
fi

if [ ! -f "$SCHEMATRON_FILE" ]; then
    echo "Error: Schematron file not found at $SCHEMATRON_FILE"
    echo "Available schematron files in generated/schematrons:"
    ls -la ../../generated/schematrons/
    exit 1
fi

echo "Input XML: $XML_FILE"
echo "Schematron: $SCHEMATRON_FILE"
echo ""

# Run the Python script
python check_schematron.py -i "$XML_FILE" -s "$SCHEMATRON_FILE"

echo ""
echo "Validation complete!"
