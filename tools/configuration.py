from importlib.resources import files

PROJECT_DIR=files()

# Source documents
DOCS_DIR = PROJECT_DIR.joinpath("../src")
TEMPLATES_DIR = DOCS_DIR.joinpath("templates")
TEMPLATES_PREFIX =  "ch-profile-"

JEKYLL_DIR = PROJECT_DIR.joinpath("../jekyll")
JEKYLL_DEFAULT_BASE_URL= "netexRealisationGuideSwitzerland/main"
JEKYLL_CONFIG = "_config.yml"

XSD_FILE_PATH = PROJECT_DIR.joinpath("../xsd/xsd/NeTEx_publication.xsd")

# Generated documents
SITE_DIR = PROJECT_DIR.joinpath("../site")
SITE_TABLES_DIR = SITE_DIR.joinpath("tables")
SITE_XML_SNIPPETS_DIR = SITE_DIR.joinpath("xml-snippets")
SITE_TEMPLATES_DIR = SITE_DIR.joinpath("templates")
SITE_SCHEMATRON_DIR = SITE_DIR.joinpath("schematron")

# Generated NeTEx HTML
NETEX_SITE_DIR = PROJECT_DIR.joinpath("../netex-site")

