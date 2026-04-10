#!/bin/bash

# Markdown Builder Execution Script
# This script runs the markdown builder with the specified parameters

# Default parameters
INPUT_FOLDER="../../templates"
OUTPUT_FOLDER="../../generated/markdown-examples"
XSD_FILE="../../xsd/xsd/NeTEx_publication.xsd"

# Create output directory if it doesn't exist
mkdir -p "$OUTPUT_FOLDER"

# Run the Python script
echo "Running Markdown Builder..."
echo "Input: $INPUT_FOLDER"
echo "Output: $OUTPUT_FOLDER"
echo "XSD: $XSD_FILE"
echo ""

python md_builder.py -i "$INPUT_FOLDER" -o "$OUTPUT_FOLDER" -x "$XSD_FILE"

echo ""
echo "Markdown generation complete!"