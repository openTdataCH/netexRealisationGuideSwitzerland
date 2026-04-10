# XML Snippets Tool

A tool for extracting XML snippets from NeTEx templates with special comment annotations.

## Overview

The `build_xml_snippets.py` tool extracts XML snippets from templates that contain special comment markers (`<!-- ch-start: -->` and `<!-- ch-stop: -->`). It removes most ch-annotations while preserving important documentation and excluding elements marked as forbidden or ignored.

## Features

- **Extracts snippets** between `<!-- ch-start: -->` and `<!-- ch-stop: -->` markers
- **Removes ch-annotations** except for `ch-note:` and `ch-notice:` (converted to regular comments)
- **Excludes forbidden/ignored elements** marked with `ch-usage: forbidden`, `ch-usage: ignored`, `usage: forbidden`, or `usage: ignored`
- **Converts versionRef to version** for reference elements (e.g., `<ElementRef versionRef="1">` becomes `<ElementRef version="1">`)
- **Preserves XML structure** and generates well-formed XML output
- **Handles nested elements** and maintains proper hierarchy

## Installation

No special installation required. The tool requires Python 3 and the `lxml` library:

```bash
pip install lxml
```

## Usage

### Basic Usage

```bash
python build_xml_snippets.py -i INPUT_FOLDER -o OUTPUT_FOLDER
```

### Example

```bash
python build_xml_snippets.py -i ../../templates -o ../../generated/xml-snippets
```

This will process all XML files in the `templates` folder and generate cleaned XML snippets in the `generated/xml-snippets` folder.

### Batch Processing

To process all templates in a directory:

```bash
# On Windows
for %%f in (templates\*.xml) do (
    python build_xml_snippets.py -i templates -o generated/xml-snippets
)

# On Linux/Mac
for f in templates/*.xml; do
    python build_xml_snippets.py -i templates -o generated/xml-snippets
 done
```

## Command Line Arguments

- `-i, --input` (required): Input folder containing XML templates
- `-o, --output` (required): Output folder for XML snippet files

## Input Format

The tool expects XML templates with the following structure:

```xml
<!-- ch-start: Example description -->
<Element>
    <!-- ch-note: Important documentation to preserve -->
    <ChildElement>content</ChildElement>
    
    <!-- usage: forbidden -->
    <ForbiddenElement>this will be excluded</ForbiddenElement>
    
    <AnotherElement><!-- ch-usage: ignored -->also excluded</AnotherElement>
</Element>
<!-- ch-stop: example stops here -->
```

## Output Format

The tool generates cleaned XML snippets:

```xml
<Element>
  <!-- Important documentation to preserve -->
  <ChildElement>content</ChildElement>
  <!-- Forbidden and ignored elements are removed -->
</Element>
```

## Example

**Input template:**
```xml
<ServiceFacilitySet id="generated" version="1">
    <!-- ch-note: List of ServiceFacility. Be careful: not all are supported. -->
    <NuisanceFacilityList>animalsAllowed</NuisanceFacilityList>
    <accommodations>
        <!-- usage: forbidden -->
        <AccommodationRef ref="notUsed" versionRef="none"/>
    </accommodations>
</ServiceFacilitySet>
```

**Output snippet:**
```xml
<ServiceFacilitySet id="generated" version="1">
  <!-- List of ServiceFacility. Be careful: not all are supported. -->
  <NuisanceFacilityList>animalsAllowed</NuisanceFacilityList>
  <!-- Forbidden accommodations element removed -->
</ServiceFacilitySet>
```

## Error Handling

The tool provides informative error messages for:
- Missing ch-start/ch-stop markers
- XML parsing errors
- Files with no valid XML content
- Cases where all content is excluded

## Limitations

- Only processes the first ch-start/ch-stop region in each file
- Does not validate XML against schemas
- Preserves original whitespace and formatting

## Development

To modify the tool:

1. Edit `build_xml_snippets.py`
2. Test with sample templates
3. Add new features as needed

## License

This tool is part of the NeTEx Realisation Guide Switzerland project.