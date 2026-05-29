from importlib.resources import files

PROJECT_DIR=files()

# Source documents
DOCS_DIR = PROJECT_DIR.joinpath("../docs")
TEMPLATES_DIR = PROJECT_DIR.joinpath("../templates")

# Generated documents
GENERATED_DIR = PROJECT_DIR.joinpath("../site")
GENERATED_DOCS_DIR = GENERATED_DIR.joinpath("docs")

XSD_FILE_PATH = PROJECT_DIR.joinpath("../xsd/xsd/NeTEx_publication.xsd")
