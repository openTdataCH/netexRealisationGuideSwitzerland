# XML Snippets Tool

A tool for extracting XML snippets from NeTEx templates with special comment annotations.

## Overview

The `xml_snippets.py` tool extracts XML snippets from templates that contain special comment markers (`<!-- ch-root -->`). 

It removes most ch-annotations while preserving important documentation and excluding elements marked 
as forbidden or ignored.

## Features

- **Extracts snippets** containing `<!-- ch-root -->` markers
- **Removes ch-annotations** except for `ch-note:` and `ch-notice:` (converted to regular comments)
- **Excludes forbidden/ignored elements** marked with `ch-usage: forbidden`, `ch-usage: ignored`, `usage: forbidden`, or `usage: ignored`
- **Converts versionRef to version** for reference elements (e.g., `<ElementRef versionRef="1">` becomes `<ElementRef version="1">`)
- **Preserves XML structure** and generates well-formed XML output
- **Handles nested elements** and maintains proper hierarchy

## Installation

### Build tools with uv

The recommended way is to [build the tools with uv](../README.md#how-to-setup-and-run-the-build).

#### Tools script

The tools build installs a wrapper script `xml-snippets` to `.venv/bin`.

### Individual installation

The tool requires Python 3 and the `lxml` library:

```bash
pip install lxml
```

## Usage

In order to get a detailed usage message, run the tool with option `-h` or `--help`:
```bash
python xml_snippets.py -h
```
Or, with installed script:
```bash
xml-snippets -h
```
See [the tools README](../README.md#how-to-run-a-tool) about how to run a tool.

### Usage Example

```bash
python build_xml_snippets.py -i ../../templates -o ../../site/xml-snippets
```

Or, with installed tool script, just:
```bash
xml-snippets
```

This will process all XML files in the `templates` folder and generate cleaned XML snippets in the `site/xml-snippets` folder.

## Input Format

The tool expects XML templates with the following structure:

```xml
<Element><!-- ch-root -->
    <!-- ch-note: Important documentation to preserve -->
    <ChildElement>content</ChildElement>
    
    <!-- usage: forbidden -->
    <ForbiddenElement>this will be excluded</ForbiddenElement>
    
    <AnotherElement><!-- ch-usage: ignored -->also excluded</AnotherElement>
</Element>
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

## Example Files

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
- Missing ch-root markers
- XML parsing errors
- Files with no valid XML content
- Cases where all content is excluded

## Limitations

- Only processes the first ch-start/ch-stop region in each file
- Does not validate XML against schemas
- Preserves original whitespace and formatting

## Development

To modify the tool:

1. Edit `xml_snippets.py`
2. Test with sample templates
3. Add new features as needed

## License

This tool is part of the NeTEx Realisation Guide Switzerland project.