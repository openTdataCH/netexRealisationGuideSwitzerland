# Schematron Validator

This tool validates XML files against Schematron schemas and reports validation issues.

## Features

- Validates XML files against ISO Schematron schemas
- Prints detailed validation reports
- Option to dump the generated XSLT for debugging
- Works with Schematron files in the generated/schematrons directory

## Installation

Requires Python 3.6+ and the following packages:

```bash
pip install lxml pyschematron
```

## Usage

```bash
python check_schematron.py -i <xmlfile> -s <schematronfile> [--dump-xslt <xslfile>]
```

### Parameters

- `-i, --input`: Input XML file to validate
- `-s, --schematron`: Schematron file (ISO Schematron format)
- `-d, --dump-xslt`: Optional - write the internal/generated XSLT to this file for debugging

## Examples

### Basic validation
```bash
python check_schematron.py -i example.xml -s generated/schematrons/ch-profile_export_timetable_file.sch
```

### Validation with XSLT dump
```bash
python check_schematron.py -i example.xml -s generated/schematrons/ch-profile_export_timetable_file.sch --dump-xslt debug.xslt
```

## Output

The tool outputs:
- The validation report in SVRL format (Schematron Validation Report Language)
- A boolean indicating if the validation was successful (True/False)

## Typical Workflow

1. Generate Schematron files in the `generated/schematrons` directory
2. Run validation on your XML files:
   ```bash
   ./run.sh
   ```
3. For testing, use the test script:
   ```bash
   ./test_run.sh
   ```

## Notes

- The tool uses pyschematron library for validation
- Schematron files should be in ISO Schematron format
- XML files should be well-formed before validation