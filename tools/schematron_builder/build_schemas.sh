#!/bin/bash

# Schematron Builder Script
# Builds all Swiss NeTEX schematron files from templates

# Default configuration
INPUT_FOLDER="templates"
OUTPUT_FOLDER="generated/schematrons"
XSD_FILE="xsd/xsd/NeTEx_publication.xsd"
PYTHON_SCRIPT="tools/schematron_builder/template2schematron.py"
LOG_FILE="generated/schematrons/build.log"
CLEAN_OUTPUT=false
VALIDATE_OUTPUT=false
PARALLEL_JOBS=1

# Template files to process (format: template_file:output_file)
TEMPLATES=(
    "templates/ch-profile_export-timetable_file.xml:ch-profile_export_timetable_file.sch"
    "templates/ch-profile_export_resource_file.xml:ch-profile_export_resource_file.sch"
)

# Parse command line arguments
while getopts "i:o:x:t:clvp:h" opt; do
    case $opt in
        i) INPUT_FOLDER="$OPTARG" ;;
        o) OUTPUT_FOLDER="$OPTARG" ;;
        x) XSD_FILE="$OPTARG" ;;
        t) TEMPLATES=("$OPTARG") ;;
        c) CLEAN_OUTPUT=true ;;
        l) LOG_TO_FILE=true ;;
        v) VALIDATE_OUTPUT=true ;;
        p) PARALLEL_JOBS="$OPTARG" ;;
        h|*) 
            echo "Usage: $0 [options]"
            echo "Options:"
            echo "  -i INPUT_FOLDER    Input folder for templates (default: templates)"
            echo "  -o OUTPUT_FOLDER   Output folder for schematrons (default: generated/schematrons)"
            echo "  -x XSD_FILE        XSD file to use (default: xsd/xsd/NeTEx_publication.xsd)"
            echo "  -t TEMPLATE_SPEC   Template specification (template_file:output_file)"
            echo "  -c                 Clean output directory before building"
            echo "  -l                 Log output to file"
            echo "  -v                 Validate generated schematrons"
            echo "  -p JOBS            Number of parallel jobs (default: 1)"
            echo "  -h                 Show this help message"
            exit 0
            ;;
    esac
done

echo "=== Schematron Builder ==="
echo "Started: $(date)"
echo "Configuration:"
echo "  Input Folder: $INPUT_FOLDER"
echo "  Output Folder: $OUTPUT_FOLDER"
echo "  XSD File: $XSD_FILE"
echo "  Templates to process: ${#TEMPLATES[@]}"
echo "  Parallel Jobs: $PARALLEL_JOBS"
echo "  Clean Output: $CLEAN_OUTPUT"
echo "  Validate Output: $VALIDATE_OUTPUT"
echo ""

# Validate configuration
if [ ! -d "$INPUT_FOLDER" ]; then
    echo "ERROR: Input folder not found: $INPUT_FOLDER"
    exit 1
fi

if [ ! -f "$XSD_FILE" ]; then
    echo "ERROR: XSD file not found: $XSD_FILE"
    exit 1
fi

if [ ! -f "$PYTHON_SCRIPT" ]; then
    echo "ERROR: Python script not found: $PYTHON_SCRIPT"
    exit 1
fi

# Clean output directory if requested
if [ "$CLEAN_OUTPUT" = true ]; then
    echo "Cleaning output directory..."
    rm -rf "$OUTPUT_FOLDER"
fi

# Create output directory if it doesn't exist
mkdir -p "$OUTPUT_FOLDER"
if [ $? -ne 0 ]; then
    echo "ERROR: Failed to create output directory: $OUTPUT_FOLDER"
    exit 1
fi

# Start logging if requested
if [ "$LOG_TO_FILE" = true ]; then
    echo "Logging to: $LOG_FILE"
    exec > >(tee "$LOG_FILE") 2>&1
fi

# Function to process a single template
process_template() {
    local template_spec="$1"
    IFS=':' read -r template_file output_file <<< "$template_spec"
    
    if [ ! -f "$template_file" ]; then
        echo "WARNING: Template file not found, skipping: $template_file"
        return 1
    fi
    
    echo "Processing: $(basename "$template_file")..."
    
    python.exe "$PYTHON_SCRIPT" \
        -i "$INPUT_FOLDER" \
        -o "$OUTPUT_FOLDER/$output_file" \
        -x "$XSD_FILE" \
        -t "$template_file"
    
    local exit_code=$?
    
    if [ $exit_code -eq 0 ]; then
        echo "✓ Successfully built: $output_file"
        return 0
    else
        echo "✗ Failed to build: $output_file"
        return 1
    fi
}

# Function to validate a schematron file
validate_schematron() {
    local schematron_file="$1"
    # Simple validation: check if file exists and is not empty
    if [ -f "$schematron_file" ] && [ -s "$schematron_file" ]; then
        echo "✓ Validation passed: $(basename "$schematron_file")"
        return 0
    else
        echo "✗ Validation failed: $(basename "$schematron_file")"
        return 1
    fi
}

echo "Building ${#TEMPLATES[@]} schematron files..."
echo ""

success_count=0
total_count=${#TEMPLATES[@]}

# Process templates
if [ "$PARALLEL_JOBS" -gt 1 ]; then
    echo "Processing templates in parallel (jobs: $PARALLEL_JOBS)..."
    
    # Create temporary file for results
    temp_results=$(mktemp)
    
    # Process templates in parallel
    for template_spec in "${TEMPLATES[@]}"; do
        process_template "$template_spec" >> "$temp_results" 2>&1 &
        
        # Limit number of parallel jobs
        if [[ $(jobs -r -p | wc -l) -ge $PARALLEL_JOBS ]]; then
            wait -n
        fi
    done
    
    # Wait for all jobs to complete
    wait
    
    # Process results
    while read -r line; do
        if [[ "$line" == *"✓ Successfully built:"* ]]; then
            ((success_count++))
        fi
        echo "$line"
    done < "$temp_results"
    
    rm "$temp_results"
else
    # Sequential processing
    for template_spec in "${TEMPLATES[@]}"; do
        if process_template "$template_spec"; then
            ((success_count++))
        fi
        echo ""
    done
fi

# Validate output if requested
if [ "$VALIDATE_OUTPUT" = true ]; then
    echo ""
    echo "Validating generated schematron files..."
    echo ""
    
    validation_success=0
    validation_total=0
    
    for schematron_file in "$OUTPUT_FOLDER"/*.sch; do
        if [ -f "$schematron_file" ]; then
            ((validation_total++))
            if validate_schematron "$schematron_file"; then
                ((validation_success++))
            fi
        fi
    done
    
    echo ""
    echo "Validation Summary: $validation_success/$validation_total files validated"
fi

echo ""
echo "=== Summary ==="
echo "Completed: $(date)"
echo "Successfully built: $success_count/$total_count schematron files"

if [ $success_count -eq $total_count ]; then
    echo "All schematron files built successfully!"
    exit 0
else
    echo "Some schematron files failed to build."
    exit 1
fi