# ch-see Reference Checker for NeTEx Templates

This tool checks if XML files referenced by `ch-see` annotations in NeTEx templates exist.

## Purpose

The `ch-see` reference checker is a simplified validation tool that:
- Processes XML template files in a folder (non-recursively)
- Finds all `ch-see` annotations (both explicit and implicit)
- Checks if the referenced XML files exist
- Reports valid and invalid references with detailed information

## Usage

```bash
python check_ch_see_references.py -i templates/
```

## Features

- **Implicit reference handling**: `<!-- ch-see -->` looks for `<ElementName>.xml` in the same folder
- **Explicit reference handling**: `<!-- ch-see: filename.xml -->` checks the specified file
- **Cross-platform**: Works with both forward and backward slashes, outputs forward slashes
- **Clear output**: Shows `[VALID]`/`[INVALID]` indicators with detailed information
- **Comprehensive summary**: Counts total, valid, and invalid references
- **Missing files list**: Detailed list of all missing files and where they're expected
- **Warning collection**: Gathers and displays all processing warnings
- **No emojis**: Uses plain text output for compatibility

## Example Output

```
Checking ch-see references in XML templates from: /path/to/templates
[VALID] Implicit reference in ServiceFrame.xml for <Line>: Line.xml
[VALID] Reference in ServiceFrame.xml: DestinationDisplay.xml
[INVALID] Implicit reference in TemplateServiceJourney.xml for <Destination>: Destination.xml
   Expected at: templates/Destination.xml

============================================================
ch-see reference checking summary:
  Total ch-see references found: 62
  Valid references: 58
  Invalid references: 4
  Status: Found 4 invalid references

Missing files (4):
  - TemplateServiceJourney.xml: <Destination> expects templates/Destination.xml
  - ServiceFrame.xml: <Connection> expects templates/Connection.xml
  - TimetableFrame.xml: <InterchangeRule> expects templates/InterchangeRule.xml
  - InterchangeRule_UMSTEIGZ.xml: <InterchangeRuleTiming> expects templates/InterchangeRuleTiming.xml

Warnings (2):
  1. XML syntax error in broken.xml: Expected '>' at line 10
  2. Error processing malformed.xml: UnboundLocalError: local variable 'root' referenced before assignment
```

## Parameters

- `-i, --input`: Input folder containing XML templates (required)

## Reference Types

### Implicit References
```xml
<Line id="example">
    <!-- ch-see -->
    <Name>Example Line</Name>
</Line>
```
This looks for `Line.xml` in the same folder as the template.

### Explicit References
```xml
<ServiceFrame id="example">
    <!-- ch-see: ServiceJourney.xml -->
    <Name>Example Service Frame</Name>
</ServiceFrame>
```
This looks for `ServiceJourney.xml` relative to the template file.

## Notes

- This tool does NOT recursively process files - it only checks templates in the specified folder
- It does NOT generate markdown - it only validates references
- **Implicit references**: `<!-- ch-see -->` means look for `<parent-element-name>.xml`
- **Explicit references**: `<!-- ch-see: filename.xml -->` means look for the specified file
- References are resolved relative to the template file's location
- The tool handles both absolute and relative paths in `ch-see` annotations
- All output paths use forward slashes for cross-platform compatibility
- Missing files and warnings are listed in detail at the end of the output

## Integration

This tool can be used as a validation step before running the main `md_builder.py` tool to ensure all referenced templates exist and are properly linked.