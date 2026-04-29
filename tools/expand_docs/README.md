# Documentation Expander

This tool expands markdown documentation by:
1. Including XML snippet examples directly in the markdown
2. Including markdown table content directly in the markdown
3. Copying the media folder to the output location

## Usage

```bash
python expand_docs.py --docs docs --out generated/docs
```

## Features

- **XML Snippet Inclusion**: Links like `- [Example snippet](../generated/xml-snippets/ServiceFrame.xml)` are replaced with the actual XML content wrapped in code blocks
- **Markdown Table Inclusion**: Links like `- [Swiss profile NeTEx definition](../generated/markdown-examples/ServiceFrame.md)` are replaced with the table content from the referenced markdown file
- **Media Folder Copy**: The entire `media` folder from the input directory is copied to the output directory

## Requirements

- Python 3.6+
- No external dependencies

## Default Parameters

- Input folder: `docs`
- Output folder: `generated/docs`