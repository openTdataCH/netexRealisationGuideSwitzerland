#!/bin/bash

# Schematron Validator Execution Script
# This script runs the schematron validator with default parameters

# Default parameters - adjust these as needed
XML_INPUT="../../test_data/example.xml"  # Path to your test XML file or folder containing XML files
SCHEMATRON_FILE="../../generated/schematrons/ch-profile_export_timetable_file.sch"

# Check if files exist
echo "Schematron Validator"
echo "===================="
echo ""

if [ ! -e "$XML_INPUT" ]; then
    echo "Error: XML input not found at $XML_INPUT"
    echo "Please create a test XML file or folder, or update the XML_INPUT variable in run.sh"
    exit 1
fi

if [ ! -f "$SCHEMATRON_FILE" ]; then
    echo "Error: Schematron file not found at $SCHEMATRON_FILE"
    echo "Available schematron files in generated/schematrons:"
    ls -la ../../generated/schematrons/
    exit 1
fi

# Determine if input is file or directory
if [ -f "$XML_INPUT" ]; then
    echo "Input XML file: $XML_INPUT"
elif [ -d "$XML_INPUT" ]; then
    echo "Input XML folder: $XML_INPUT"
    echo "Will validate all XML files recursively in this folder"
else
    echo "Error: Invalid input type at $XML_INPUT"
    exit 1
fi

echo "Schematron: $SCHEMATRON_FILE"
echo ""

# Run the Python script
python check_schematron.py -i "$XML_INPUT" -s "$SCHEMATRON_FILE"

echo ""
echo "Validation complete!"
