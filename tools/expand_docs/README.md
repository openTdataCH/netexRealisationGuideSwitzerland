# Documentation Expander

This tool expands markdown documentation by:
1. Including XML snippet examples directly in the markdown
2. Including markdown table content directly in the markdown
3. Copying the media folder to the output location

## Installation

### Build tools with uv

The recommended way is to [build the tools with uv](../README.md#how-to-setup-and-run-the-build).

#### Tools script

The tools build installs a wrapper script `expand-docs` to `.venv/bin`.

### Individual Installation

Requires python 3.6+.

## Usage

In order to get a detailed usage message, Run the tool with option `-h` or `--help`:
```bash
python expand_docs.py -h
```
Or, with installed script:
```bash
expand-docs -h
```

See [the tools README](../README.md#how-to-run-a-tool) about how to run a tool.

### Usage Example
```bash
python expand_docs.py --docs src --out site
```

## Features

- **XML Snippet Inclusion**: Links like `- [Example snippet](../site/xml-snippets/ServiceFrame.xml)` are replaced with the actual XML content wrapped in code blocks
- **Markdown Table Inclusion**: Links like `- [Swiss profile NeTEx definition](../generated/markdown-examples/ServiceFrame.md)` are replaced with the table content from the referenced markdown file
- **Media Folder Copy**: The entire `media` folder from the input directory is copied to the output directory



