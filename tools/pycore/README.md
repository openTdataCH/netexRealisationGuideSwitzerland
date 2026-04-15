# pycore Documentation

Creates Markdown tables from a XSD.

## Usage

Run `python3 pycore.py --help` to get help output.

### Test with StopPlace.md

`python3 pycore.py -o ../../generated/pycore ../../experimental/StopPlace.xsd`

### Create NeTEx tables:

`python3 pycore.py -o ../../generated/pycore ../../xsd/xsd/NeTEx_publication.xsd`

## Known Issues

- Many links are invalid or shouldn't be links
- Markdown of many Elements written to wrong path (like AccessMode)
- All type tables are empty
- All group tables are empty