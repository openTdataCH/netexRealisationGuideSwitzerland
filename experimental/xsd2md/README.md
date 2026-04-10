# XSD to Markdown Example with Python

It is relatively easy to generate Markdown documentation from XSD with Python.

This example script generates a Markdown table for an element, in this case `StopPlace`:

``` shell
python xsd2md.py ../StopPlace.xsd StopPlace > StopPlace.md
```

#### Included Files

| File | Description                                                     |
| ---  |-----------------------------------------------------------------| 
| `xsd2md.py` | Python script                                                   | 
| `../StopPlace.xsd` | Sample Schema for `StopPlace`                                   | 
| `StopPlace.md` | Markdown document with table documenting the `StopPlace` element. | 

The script extracts additional documentation from `documentation` elements inside the elements of the XSD.

