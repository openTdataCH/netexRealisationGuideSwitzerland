# XML Validator

This tool validates XML files or folders against an XSD schema using `lxml`.

## Installation

### Build tools with uv

The recommended way is to [build the tools with uv](../README.md#how-to-setup-and-run-the-build).

#### Tools script

The tools build installs a wrapper script `xml-validator` to `.venv/bin`.

### Individual Installation

Requires Python 3.x and the `lxml` library (install with `pip install lxml`).

## Usage

In order to get a detailed usage message, run the tool with option `-h` or `--help`:
```bash
python xml_validator.py -h
```
Or, with installed script:
```bash
xml-validator -h
```

### Usage Examples

#### Validate a Single XML File
```bash
python xml_validator.py --xml path/to/file.xml --xsd path/to/schema.xsd
```

#### Validate All XML Files in a Folder
```bash
python xml_validator.py --xml path/to/folder --xsd path/to/schema.xsd
```

## Output

- For valid XML files, the tool prints a success message.
- For invalid XML files, the tool prints the validation errors with line numbers.
- If validating a folder, the tool continues to the next file after encountering an error.
