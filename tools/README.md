# Tools for the Swiss NeTEx RG

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

Run the following following commands in the project root directory:

``` shell
uv venv
.venv\bin\activate.bat
uv sync
```
### Install build module

> This can be skipped as the `build` module is now part of the build dependencies.

Make sure you have an up-to-date version of `pip` and of module `build` used to run the build:
```
python -m ensurepip
python -m pip install --upgrade pip build
```
### Run the build

If everything is setup correctly, you should be able to the build from your project root directory:

```
python -m build
```

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

| Name | Description                                                                                                                                                | 
| --- |------------------------------------------------------------------------------------------------------------------------------------------------------------| 
| check-links | **Checks relative links** in Markdown files and warns if the target files doesn't exist.                                                                   
| check-schematron | **Validates XML** files against Schematron schemas and reports validation issues.                                                                          |
| expand-docs | **Expands Markdown** documentation: Includes XML snippets and Markdown tables directly in the Markdown and copies the media folder to the output location. 
| md-builder | **Generates Markdown tables** from annotated NeTEx XML templates, using XSD schemas for type and cardinality information.                                  | 
| pycore | **Generates Markdown tables** from a XSD schema.                                                                                                           | 
| schematron-builder | **Generates Schematron files** from XML templates with special comment annotations.                                                                        | 
| xml-validator | **Validates XML** files or folders against an XSD schema.                                                                                                  | 
| xml-snippets | **Extracts XML Snippets** from templates.                                                                                                                  | 

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
- `setup.py` in the root project acts as the interface for the build
  - here we can add tools to be run during the build.
- The build writes all output to directory `site`, excluded from git

### Github Action

The Github Action [pages.yaml](../.github/pages.yaml) runs the script [build.sh](./build.sh) (can also be tested locally) 
  - triggered after commits to main branch (e.g. after the merge of a branch)
  - runs the build via the `python -m build` mechanism 
  - uploads generated docs to GitHub Pages
