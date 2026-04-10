# Xcore - Generate documentation tables from XSD

Xcore is a script/application implemented in `xquery`.

The `xquery` code to generate the `html` Documentation of a XSD is copied from here:
https://github.com/VDVde/OJP/tree/develop/docs

It can be run with the `generate.sh` script - all output is written to a `generated` subfolder excluded from git. 

## Usage Examples

### StopPlace Example 

A small example I use for testing...
``` shell
./generate.sh custom_test.xml ../../experimental/StopPlace.xsd      
```
### The Big NeTEx

Generating the reports for the full NeTEx XSD may need many hours and some resouces ...

``` shell
./generate.sh ./custom.xml ../../xsd/xsd/NeTEx_publication.xsd
```

## Customization Files

Customization files (`stop_place_custom`.xml or `netex_custom.xml`) are a place, where the reports can be configured.

## Changes to the original code

Changes in the `xquery` code are marked with `(: NeTEx ... :)` comments, mainly in the following files of the `xcore` directory:
- `xco-html.xqm`
- `xcore.xq`

The shell script `generate.sh` is adapted from original `generate_tables.sh`.