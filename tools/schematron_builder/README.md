# Schematron Builder for Swiss NeTEX

This tool generates Schematron validation files from XML templates with special comment annotations. The generated schematron files can be used to validate NeTEX XML files against the Swiss profile.

## Overview

The `template2schematron.py` script processes XML templates containing special comment markers and generates Schematron (.sch) files that enforce the Swiss NeTEX profile rules.

## Features

- **Template Processing**: Extracts regions marked with `<!-- ch-start: -->` and `<!-- ch-stop: -->`
- **Rule Generation**: Creates Schematron rules based on comment annotations
- **Namespace Support**: Proper handling of NeTEX and Schematron namespaces
- **Modular Design**: Supports referenced templates for code reuse
- **Comprehensive Validation**: Generates rules for presence, absence, enumerations, and more

## Installation

Requires Python 3.6+ and lxml:

```bash
pip install lxml
```

## Usage

```bash
python template2schematron.py \
    -t TEMPLATE_FILE \
    -x XSD_FILE \
    -i INPUT_FOLDER \
    -o OUTPUT_FILE \
    [-v]
```

### Parameters

- `-t, --template`: Template XML file containing ch-start/ch-stop regions
- `-x, --xsd`: XSD file (path is stored but not currently used for validation)
- `-i, --input-folder`: Folder with referenced XML fragment files
- `-o, --output`: Output Schematron (.sch) file
- `-v, --verbose`: Enable verbose logging

### Example

```bash
python template2schematron.py \
    -t templates/ch-profile_export-timetable_file.xml \
    -x xsd/xsd/NeTEx_publication.xsd \
    -i templates \
    -o generated/schematrons/ch-profile_export_timetable_file.sch \
    -v
```

## Build Script

The `build_schemas.sh` script automates building all schematron files:

```bash
# Basic usage (default settings)
./build_schemas.sh

# Clean output and build with logging
./build_schemas.sh -c -l

# Process specific template with validation
./build_schemas.sh -t "templates/my_template.xml:my_output.sch" -v

# Parallel processing (4 jobs)
./build_schemas.sh -p 4

# Custom paths
./build_schemas.sh -i "my_templates" -o "my_output" -x "custom.xsd"
```

## Supported Comment Annotations

The script recognizes the following comment annotations in templates:

### Basic Annotations

- `<!-- ch-start: description -->`: Marks the beginning of a region to process
- `<!-- ch-stop: description -->`: Marks the end of a region to process
- `<!-- ch-note: text -->`: Adds descriptive notes (appears in schematron comments)
- `<!-- ch-notice: text -->`: Adds notices (treated like ch-note)

### Usage Control

- `<!-- ch-usage: mandatory -->`: Element must be present
- `<!-- ch-usage: forbidden -->`: Element must not be present
- `<!-- ch-usage: optional -->`: Element is optional
- `<!-- ch-usage: ignored -->`: Element is ignored
- `<!-- ch-usage: expected -->`: Element is expected but not required

### Advanced Features

- `<!-- ch-referenced -->`: References another template file with same name
- `<!-- ch-referenced: filename.xml -->`: References specific template file
- `<!-- ch-allowed-enums: value1 value2 value3 -->`: Restricts element to allowed values
- `<!-- ch-deprecated -->`: Marks element as deprecated
- `<!-- ch-class-id-must-exist -->`: Requires referenced element with ID to exist

### Attribute Control

- `<!-- ch-attrs: attr1 attr2 attr3 -->`: Specifies which attributes to include

## Template Structure

Templates should follow this structure:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<RootElement>
    <!-- ch-start: Example description -->
    <ChildElement>
        <!-- ch-usage: mandatory -->
        <!-- ch-note: This element is required -->
        Example content
    </ChildElement>
    <AnotherElement>
        <!-- ch-usage: forbidden -->
        <!-- ch-note: This element should not be used -->
    </AnotherElement>
    <!-- ch-stop: Example description -->
</RootElement>
```

## Generated Output

The script generates Schematron files with:

- **Assert rules**: For mandatory/forbidden elements and enumerations
- **Report rules**: For deprecated elements and cross-references
- **Comments**: Documentation from ch-note and ch-notice annotations
- **Proper namespaces**: NeTEX and Schematron namespaces

## Example Output

```xml
<?xml version="1.0" encoding="UTF-8"?>
<sch:schema xmlns:sch="http://purl.oclc.org/dsdl/schematron" 
            xmlns:netex="http://www.netex.org.uk/netex" 
            queryBinding="xslt2">
    <sch:ns prefix="netex" uri="http://www.netex.org.uk/netex"/>
    <sch:title>Generated schematron from template</sch:title>
    <sch:pattern id="p1">
        <sch:rule context="//netex:Element">
            <!-- Element must be present -->
            <sch:assert test="count(netex:ChildElement) > 0">
                ChildElement must be present
            </sch:assert>
        </sch:rule>
    </sch:pattern>
</sch:schema>
```

## Best Practices

1. **Modular Design**: Use `<!-- ch-referenced -->` to break complex templates into smaller files
2. **Clear Documentation**: Use `<!-- ch-note -->` to explain profile decisions
3. **Consistent Usage**: Apply `<!-- ch-usage -->` consistently across similar elements
4. **Validation**: Test generated schematron files with real data
5. **Version Control**: Keep templates under version control for traceability

## Troubleshooting

- **Missing lxml**: Install with `pip install lxml`
- **File not found**: Check paths and ensure template files exist
- **Invalid XML**: Validate your template XML before processing
- **Namespace issues**: Ensure proper namespace declarations in templates

## Test Templates

Comprehensive test templates and a working test script are available in the [`test_templates/`](test_templates/) folder. These demonstrate all supported ch-comment annotations and provide examples for testing the schematron builder.

### Quick Test

Run the simple test to verify everything works:

```bash
cd tools/schematron_builder/test_templates
python simple_test.py
```

See [`test_templates/README.md`](test_templates/README.md) for detailed documentation and usage examples.

## Related Tools

- `check_schematron.py`: Validates XML files against generated schematron files
- `md_builder.py`: Generates markdown documentation from the same templates
- `build_schemas.sh`: Automates building multiple schematron files

## See Also

- [Templates Documentation](../templates/README.md): Detailed template annotation guide
- [Markdown Builder](../md_builder/README.md): Documentation generation tool
- [Schematron Validator](../check_schematron/README.md): Validation tool