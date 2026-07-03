# Schematron Validator

This tool validates XML files against Schematron schemas and reports validation issues.

## Features

- Validates XML files against ISO Schematron schemas
- Prints detailed validation reports
- Option to dump the generated XSLT for debugging
- Works with Schematron files in the generated/schematrons directory

## Installation

### Build tools with uv

The recommended way is to [build the tools with uv](../README.md#how-to-setup-and-run-the-build).

#### Tools script

The tools build installs a wrapper script `check-schematron` to `.venv/bin`.

### Individual installation

Requires Python 3.6+ and the following packages:

```bash
pip install lxml pyschematron
```

## Usage

In order to get a detailed usage message, Run the tool with option `-h` or `--help`:
```bash
python check_schematron.py -h
```
Or, with installed script:
```bash
check-schematron -h
```

See [the tools README](../README.md#how-to-run-a-tool) about how to run a tool.

### Usage Examples

#### Basic validation

```bash
python check_schematron.py -i example.xml -s site/schematrons/ch-profile_export_timetable_file.sch
```

#### Validation with XSLT dump
```bash
python check_schematron.py -i example.xml -s site/schematrons/ch-profile_export_timetable_file.sch --dump-xslt debug.xslt
```

## Output

The tool outputs:
- The validation report in SVRL format (Schematron Validation Report Language)
- A boolean indicating if the validation was successful (True/False)

## Typical Workflow

1. Run `schematron_builder.py` to generate Schematron files in the `site/schematrons` directory
2. Run `check_schematron.py` to validate your XML files
3. For testing, use the test script:
   ```bash
   ./test_run.sh
   ```

## Notes

- The tool uses pyschematron library for validation
- Schematron files should be in ISO Schematron format
- XML files should be well-formed before validation