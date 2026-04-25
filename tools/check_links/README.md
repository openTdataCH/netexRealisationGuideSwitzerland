# Markdown Link Checker

This tool checks all relative links in markdown files and warns if the target files don't exist.

## Usage

```bash
python check_links.py --docs docs --main .
```

## Features

- Checks all markdown files (`*.md`, `*.MD`, `*.markdown`, `*.Markdown`) in the specified folder and subfolders
- Validates relative links (ignores absolute URLs and anchor links)
- Handles links relative to the main folder (`../` paths)
- Handles links relative to the current file
- Provides detailed warnings for broken links

## Parameters

- `--docs`: Documentation folder to process (default: `docs`)
- `--main`: Main project folder (default: current directory)

## Example Output

```
WARNING: Broken link in docs/06_stops.md
  Link text: 'Swiss profile NeTEx definition'
  Link URL: '../generated/markdown-examples/StopPlace.md'
  Expected at: D:\development\github\netexRealisationGuideSwitzerland\generated\markdown-examples\StopPlace.md

All other links are valid!
```