# Schematron Builder for Swiss NeTEX

In this folder template2schematron.py allows you to build schematron files with the templates stored in the folder `templates` of this project.

There is a list of top-level template files available (starting with `ch-profile`).

## Parameters
* `-i` - the input folder for templates
* `-o` - the output file to be generated (should be in `generated/schematrons`)
* `-x` - the xsd file (currently not used)
* `-t` - the exact template to use


## Build all schema files
The script (started from the root of the project):
`tools/build_schemas.sh` builds all relevant schematron files.

## Supported functionality
For details on the functionality read [the documentation in the templates folder](../../templates/README.md).
