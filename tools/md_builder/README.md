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

### Build tools with uv

The recommended way is to [build the tools with uv](../README.md#how-to-setup-and-run-the-build).

#### Tools script

The tools build installs a wrapper script `md-builder` to `.venv/bin`.

### Individual installation
Requires Python 3.6+ and `lxml`:

```bash
pip install lxml
```

## Usage

In order to get a detailed usage message, run the tool with option `-h` or `--help`:
```bash
python md_builder.py -h
```
Or, with installed script:
```bash
md-builder -h
```

See [the tools README](../README.md#how-to-run-a-tool) about how to run a tool.

### Usage Example

```bash
python md_builder.py -i src -o site
```
## Template Annotation Tags

The tool recognizes the following comment tags in XML templates:

- `<!-- ch-root -->`: Marks the element to process (placed within the element)
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

## Template Example

Given a template like:

```xml
<StopPlace id="ch:1:StopPlace" version="1"><!-- ch-root -->
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