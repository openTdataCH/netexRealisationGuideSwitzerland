# XML Validator

This tool validates XML files or folders against an XSD schema using `lxml`.

## Usage

### Validate a Single XML File
```bash
python xml-validator.py --xml path/to/file.xml --xsd path/to/schema.xsd
```

### Validate All XML Files in a Folder
```bash
python xml-validator.py --xml path/to/folder --xsd path/to/schema.xsd
```

### Help
```bash
python xml-validator.py --help
```

## Parameters

- `--xml`: Path to the XML file or folder containing XML files.
- `--xsd`: Path to the XSD schema file.

## Output

- For valid XML files, the tool prints a success message.
- For invalid XML files, the tool prints the validation errors with line numbers.
- If validating a folder, the tool continues to the next file after encountering an error.

## Example

```bash
# Validate all XML files in the templates folder
python xml-validator.py --xml templates --xsd xsd/xsd/NeTEx_Publication.xsd
```

## Dependencies

- Python 3.x
- `lxml` library (install with `pip install lxml`)