# Markdown Builder for NeTEx Templates

This tool generates markdown documentation tables from annotated NeTEx XML templates, using XSD schemas for type and cardinality information.

## Features

- Extracts documentation from XML templates with special comment tags
- Generates markdown tables with element information
- Uses XSD schemas for type and cardinality data
- Supports element referencing and linking between markdown files
- Handles nested elements with proper indentation markers
- Converts versionRef to version in element descriptions (e.g., `versionRef="1"` becomes `version="1"`)

## Installation

Requires Python 3.6+ and the following packages:

```bash
pip install lxml
```

## Usage

```bash
python md_builder.py -i <input_folder> -o <output_folder> -x <xsd_file>
```

### Parameters

- `-i, --input`: Input folder containing XML template files
- `-o, --output`: Output folder for generated markdown files
- `-x, --xsd`: XSD schema file for type information

### Convenience Scripts

The tool includes convenience scripts for batch processing:

**Windows:**
```bash
run.bat
```

**Linux/Mac:**
```bash
./run.sh
```

These scripts process all XML templates in the templates directory and generate markdown files in the output directory.

## Template Annotation Tags

The tool recognizes the following comment tags in XML templates:

- `<!-- ch-start: ... -->`: Marks the beginning of the section to process
- `<!-- ch-stop: ... -->`: Marks the end of the section to process
- `<!-- ch-usage: mandatory|forbidden|optional|ignored|expected -->`: Specifies usage requirement
- `<!-- ch-note: ... -->`: Adds a note/description for the element
- `<!-- ch-notice: ... -->`: Adds a notice for the element
- `<!-- ch-see -->`: Marks element as referenced (creates link to element.md)
- `<!-- ch-see: <name> -->`: Marks element as referenced with custom filename

## Output Format

The generated markdown files contain tables with the following columns:

- **Sub**: Indentation markers (`>` for nested, `<` for referenced)
- **Element**: Element name (with link if referenced)
- **Usage**: Usage requirement (mandatory, forbidden, etc.)
- **Card**: Cardinality (e.g., 1..1, 0..*, 1..*)
- **Type**: Element type from XSD
- **Description**: Description from template notes
- **Note**: Additional notes from template

## Example

Given a template like:

```xml
<StopPlace id="ch:1:StopPlace" version="1">
    <!-- ch-start: StopPlace example -->
    <Name>
        <!-- ch-usage: mandatory -->
        <!-- ch-note: The name of the StopPlace -->
        Bern
    </Name>
    <PrivateCode>
        <!-- ch-usage: mandatory -->
        <!-- ch-note: DiDok number -->
        8500001
    </PrivateCode>
    <!-- ch-stop: StopPlace example -->
</StopPlace>
```

The tool generates a markdown table with proper type information from the XSD.

## Generated Files

For each XML template file `ElementName.xml`, the tool generates `ElementName.md` in the output folder.

## Notes

- The tool processes all `.xml` files in the input directory
- XSD parsing extracts type and cardinality information for elements
- Referenced elements create relative links to other markdown files
- Nested elements are shown with indentation markers