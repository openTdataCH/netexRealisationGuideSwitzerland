from importlib.resources import files

PROJECT_DIR=files()

# Source documents
DOCS_DIR = PROJECT_DIR.joinpath("../docs")
TEMPLATES_DIR = PROJECT_DIR.joinpath("../templates")

JEKYLL_DIR = PROJECT_DIR.joinpath("../jekyll")

XSD_FILE_PATH = PROJECT_DIR.joinpath("../xsd/xsd/NeTEx_publication.xsd")

# Generated documents
SITE_DIR = PROJECT_DIR.joinpath("../site")
SITE_TABLES_DIR = SITE_DIR.joinpath("tables")


