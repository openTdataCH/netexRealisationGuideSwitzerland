# Tools for the Swiss NeTEx RG

## Tools Overview

### Validation Tools

The following validation tools are used to validate sources (links and xml):

| Name                                           | Type   | Default Input | Description                                                                                                                                                 | 
|------------------------------------------------|--------|---------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------| 
| [check_links](check_links/README.md)           | Python | `docs`        | **Checks relative links** in Markdown files and warns if the target files doesn't exist.                                                                    
| [check_schematron](check_schematron/README.md) | Python | -             |  **Validates XML** files against Schematron schemas and reports validation issues.                                                                           |
| [xml_validator](validation/README.md)          | Python | -             |  **Validates XML** files or folders against an XSD schema.                                                                                                   | 

### Docs Generation Tools

The following tools are used to generate target files from sources:

| Name                                               | Type   | Default Input | Default Output      | Description                                                                                                                                                 | 
|----------------------------------------------------|--------|---------------|---------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------| 
| [expand_docs](expand_docs/README.md)               | Python | `docs`        | `site`              | **Expands Markdown** documentation: Includes XML snippets and Markdown tables directly in the Markdown and copies the media folder to the output location.  
| [md_builder](md_builder/README.md)                 | Python | `templates`   | `site/tables`       | **Generates Markdown tables** from annotated NeTEx XML templates, using XSD schemas for type and cardinality information.                                   |
| [schematron_builder](schematron_builder/README.md) | Python | -             | -                   | **Generates Schematron files** from XML templates with special comment annotations.                                                                         |
| [xml_snippets](xml_snippets/README.md)             | Python | `templates`   | `site/xml-snippets` | **Extracts XML Snippets** from templates.                                                                                                                   |
| [pycore](pycore/README.md)                         | xquery | -             | -                   | **Generates Markdown tables** from a XSD schema.                                                                                                            |

## General rules applying to all tools

- Default input folders and/or output folders are used if folders are not explicitly given (not all tools yet).
- The default output folder of the tools is `site`, or an according subdirectory of `site`, excluded from git. See also [Folders](../README.md#folders).
- Option `-h` or `--help` prints the usage text.

In general, the NeTEx RG python tools use the `argparse` library. Thus, you should allways be able to get a usage description by providing the option `-h` or `--help`, e.g. with:
```
uv run md_builder.py --help 
```
The example above requires `uv`, see [How to setup and run the build](#how-to-setup-and-run-the-build).

The [tool scripts](#install-tool-scripts), provide another possibility to run tools from the command line, e.g. by running `md-builder`.

## The toolchain script toolchain.py

The script `tools/toolchain.py` is used to run tools (xml_snippets, md_builder, expand_docs etc.) in sequence in order to generate the `site` target docs.

## How to setup and run the build

The build builds the tools and runs them to create the generated documents in the directory `site`.

### Steps involved to setup and run the build

1. Install the [uv package manager](#install-the-uv-package-manager)
2. Initialize the [virtual environment](#initialize-the-virtual-environment)
3. Install the [build module](#install-build-module)
4. [Run the build]()

For more information about the build framework, see [Build Automation](#build-automation).

### Install the uv package manager

Install the uv package manager:
- See [uv package manager](https://docs.astral.sh/uv/)
- if you have pip installed, you can run `pip install uv`

### Initialize the virtual environment

#### Mac/Linux

Run the following following commands in the project root directory:
```sh
uv venv
source .venv/bin/activate
uv sync
```

#### Windows

Create the virtual environment directory `venv` running the following command in the project root directory (needs `uv`, see [Install the uv package manager](#install-the-uv-package-manager) above):

``` shell
uv venv
```

It may respond like this, or similar:
```
Using CPython 3.14.6
Creating virtual environment at: .venv
Activate with: .venv\Scripts\activate
```

Run the activation script to activate the virtual environment as proposed in the output above. Then, do the sync to download 
the project dependencies:

``` shell
uv sync
```

### Install build module

> This can be skipped as the `build` module is now part of the build dependencies.

Make sure you have an up-to-date version of `pip` and of module `build` used to run the build:
``` shell
python -m ensurepip
python -m pip install --upgrade pip build
```
### Run the build

If everything is setup correctly, you should be able to the build from your project root directory:

``` shell
uv run python -m build
```

### Configure PyCharm with uv Python Interpreter

In the PyCharm settings you may configure the Python interpreter with `uv` based on the `.venv` directory of the project. 

## Tool Scripts

The `pyproject.toml` is configured to generate scripts for the tools.
These tool scripts are not required for the build, but they may be useful for running tools locally.

### Prerequisites: Set PYTHONPATH and PATH

The following environment variables shall be set accordingly:

| Environment Variable | Value                                                                                                                                                                           |
|----------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `PYTHONPATH`         | Add the project root path, where you checked out this repository.                                                                                                   |
| `PATH`               | Add the path to the installed scripts to the `PATH` variable. On Linux, Mac, this may be like `${project-root}/.venv/bin:$PATH`, on Windows like `${project-root}\.venv\Scripts` | |

> On Linux or Mac, this can be achieved by adding something like this to your `.zshrc` or `.bashrc` file:
> ```
> NETEX_RG_HOME=~/path/to/project-root
> export PYTHONPATH="$NETEX_RG_HOME:$PYTHONPATH"
> export PATH="$NETEX_RG_HOME/.venv/bin:$PATH"
> ```

### Install Tool Scripts

The scripts can be installed with the following command (executed from the project root):
```
uv pip install -e .
```
This generates executable scripts for Linux/Mac and Windows in subdirectories of `.venv`.

### Tool Scripts Overview

The following tool scripts are available after installation:
- check-links
- check-schematron
- expand-docs
- md-builder
- pycore
- schematron-builder
- xml-validator
- xml-snippets

See also [Tools Overview](#tools-overview) for more information about the tools.

### How to add a new Script

- Add a new entry in the `[project.scripts]` section of `pyproject.toml`.
- If the script requires another package, use `uv add` to added to the environment.

## Build Automation Framework

### Package Manager

The package manager `uv` simplifies the build and installation of scripts for the tools.

- Dependencies are managed by `uv`, as configured in `pyproject.toml` and more detailed in `uv.lock`. 
- `uv` provides an os-independent interface for scripts
  - Generated tool scripts run on Windows, Mac or Linux

### Project build

Components of the build automation:
- [pyproject.toml](../pyproject.toml) is configured with `setuptools` (https://setuptools.pypa.io/en/latest/)
  - docs can be generated running `python -m build`
- `setup.py` in the root project acts as the interface for the build system
  - runs `tools.toolchain` from `tools/toolchain.py` to generate the docs
    - here we can add tools to be run during the build.
- The build writes all output to directory `site`, excluded from git

### Github Action

The Github Action [pages.yaml](../.github/pages.yaml) runs the script [build.sh](./build.sh) (can also be tested locally) 
  - triggered after commits to main branch (e.g. after the merge of a branch)
  - runs the build via the `python -m build` mechanism 
  - uploads generated docs to GitHub Pages


