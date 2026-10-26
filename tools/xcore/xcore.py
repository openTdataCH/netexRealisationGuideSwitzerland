import argparse
import hashlib
import os
import subprocess
import tempfile
from pathlib import Path

import requests

from tools.configuration import NETEX_SITE_DIR, SITE_TABLES_DIR, XSD_FILE_PATH

JAVA_OPTS = ["-Xms4g", "-Xmx24g", "-XX:+UseG1GC", "-XX:+UseStringDeduplication"]
XCORE_XQ_PATH = "xquery/xcore.xq"

# URL to download the basex.jar
BASEX_JAR_URL = "https://files.basex.org/releases/10.6/BaseX106.jar"

# SHA-256 checksum of the expected BaseX 10.6 JAR (set to enable verification)
BASEX_JAR_SHA256 = "46e31dbd85e3f664d4a116b4a1aa8cde005ad211"

# Local path for basex.jar — user-specific to avoid /tmp race conditions
DEFAULT_BASEX_JAR_PATH = os.path.join(
    tempfile.gettempdir(), f"basex-{os.getuid()}.jar"
)

# Default report customization file
DEFAULT_CUSTOM_XML = "custom.xml"


def scan_tables(input_dir: Path, output_file_path: str):
    # Process each markdown file
    elements = ""
    for filename in os.listdir(input_dir):
        if filename.endswith(".md"):
            element_name = filename.replace(".md", "")
            elements = elements + "\n" + element_name

    with open(output_file_path, "w", encoding="utf-8") as f:
        f.write(elements)


def build_xcore_tables(
    output_dir_path: str,
    xsd_file_path: str,
    basex_jar_path: str,
    custom_xml_path: str,
    dry_run: bool,
):

    if not Path(basex_jar_path).exists():
        print(f"basex.jar not found at {basex_jar_path}")
        if not dry_run:
            print(
                f"Download of {basex_jar_path} prevented by argument dry_run={dry_run}"
            )
        else:
            download_basex_jar(basex_jar_path)

    print(f"> Using basex.jar at {basex_jar_path}")

    # Build command as an argument list — no shell=True, prevents command injection
    java_cmd = [
        "java",
        *JAVA_OPTS,
        "-cp",
        basex_jar_path,
        "org.basex.BaseX",
        "-b",
        "report=contab",
        "-b",
        f'uri="{xsd_file_path}"',
        "-b",
        f'odir="{output_dir_path}"',
        "-b",
        f'custom="{custom_xml_path}"',
        "-b",
        'dnamesExcluded=".git .github"',
        "-b",
        "htmlFilePerComplexType=true",
        XCORE_XQ_PATH,
    ]

    if not dry_run:
        result = subprocess.run(java_cmd, check=False)
        print(result)
    else:
        print(f"> Call of java command prevented by argument dry_run={dry_run}")
        print("> You may copy and run the following Java command:")
        print(" ".join(java_cmd))


def download_basex_jar(basex_jar_path: str):
    print(f"Downloading basex.jar to {basex_jar_path} ...")
    response = requests.get(BASEX_JAR_URL, timeout=120)
    response.raise_for_status()

    content = response.content

    # Verify checksum if a known-good hash is configured
    if BASEX_JAR_SHA256:
        digest = hashlib.sha256(content).hexdigest()
        if digest != BASEX_JAR_SHA256:
            raise ValueError(
                f"Checksum mismatch for downloaded JAR: "
                f"expected {BASEX_JAR_SHA256}, got {digest}"
            )
        print("Checksum verified OK.")
    else:
        print(
            "WARNING: BASEX_JAR_SHA256 not set — downloaded JAR integrity not verified."
        )

    # Write with restrictive permissions
    with open(basex_jar_path, "wb") as f:
        f.write(content)
    os.chmod(basex_jar_path, 0o600)


def parse_args():
    """Parse command line arguments"""
    parser = argparse.ArgumentParser(
        description="Generate html documentation from NeTEx XSD."
    )
    parser.add_argument(
        "-o",
        "--output",
        default=NETEX_SITE_DIR,
        help=f"Output folder for markdown files (Default = {NETEX_SITE_DIR})",
    )
    parser.add_argument(
        "-x",
        "--xsd",
        default=XSD_FILE_PATH,
        help=f"XSD schema file for type information (Default = {XSD_FILE_PATH})",
    )
    parser.add_argument(
        "-j",
        "--basex-jar",
        default=DEFAULT_BASEX_JAR_PATH,
        help=f"Path to the basex.jar (Default = {DEFAULT_BASEX_JAR_PATH})",
    )
    parser.add_argument(
        "-c",
        "--custom-xml",
        default=DEFAULT_CUSTOM_XML,
        help=f"Path to the report custom xml file (Default= {DEFAULT_CUSTOM_XML})",
    )
    parser.add_argument(
        "-d",
        "--dry-run",
        default=False,
        action="store_true",
        help="Dry run (Default = False)",
    )
    return parser.parse_args()


def main():
    args = parse_args()
    if args.dry_run:
        print("> Dry run ...")

    scan_tables(SITE_TABLES_DIR, "elements.txt")
    build_xcore_tables(
        args.output, args.xsd, args.basex_jar, args.custom_xml, args.dry_run
    )


if __name__ == "__main__":
    main()
