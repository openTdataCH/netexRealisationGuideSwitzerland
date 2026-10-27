"""Safe XML parsing helpers that disable external entity resolution (XXE protection)."""

from lxml import etree


def safe_parser():
    """Return an lxml XMLParser configured to prevent XXE attacks."""
    return etree.XMLParser(
        resolve_entities=False,
        no_network=True,
        load_dtd=False,
        huge_tree=False,
    )


def safe_parse(source):
    """Parse an XML file or file-like object with XXE protections enabled."""
    return etree.parse(source, safe_parser())


def safe_fromstring(data):
    """Parse an XML string/bytes with XXE protections enabled."""
    return etree.fromstring(data, safe_parser())
