from importlib.resources import files

PROJECT_DIR=files()

# Source documents
DOCS_DIR = PROJECT_DIR.joinpath("../docs")
TEMPLATES_DIR = PROJECT_DIR.joinpath("templates")

# Generated documents
GENERATED_DIR = PROJECT_DIR.joinpath("generated")
