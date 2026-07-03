# Markdown Link Checker

This tool checks all relative links in markdown files and warns if the target files don't exist.

## Installation

### Build tools with uv

The recommended way is to [build the tools with uv](../README.md#how-to-setup-and-run-the-build).

#### Tools script

The tools build installs a wrapper script `check-links` to `.venv/bin`.

## Usage

In order to get a detailed usage message, run the tool with option `-h` or `--help`:
```bash
python check_links.py -h
```
Or, with installed script:
```bash
check-links -h
```
See [the tools README](../README.md#how-to-run-a-tool) about how to run a tool.

### Usage Example

```bash
python check_links.py --docs src
```

## Features

- Checks all markdown files (`*.md`, `*.MD`, `*.markdown`, `*.Markdown`) in the specified folder and subfolders
- Validates relative links (ignores absolute URLs and anchor links)
- Handles links relative to the main folder (`../` paths)
- Handles links relative to the current file
- Provides detailed warnings for broken links

## Example Output

```
WARNING: Broken link in docs/06_stops.md
  Link text: 'Swiss profile NeTEx definition'
  Link URL: '../generated/markdown-examples/StopPlace.md'
  Expected at: D:\development\github\netexRealisationGuideSwitzerland\generated\markdown-examples\StopPlace.md

All other links are valid!
```