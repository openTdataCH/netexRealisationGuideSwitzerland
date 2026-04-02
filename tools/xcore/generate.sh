#!/bin/bash
# Generate the documentation tables in docs/generated/ from the .xsd schema files
#
# You need the binary `java`
# apt-get install default-jre

# The -e flag causes the script to exit as soon as one command returns a non-zero exit code
set -e

usage() {
  echo "Usage: $(basename "$0") <path-to-custom-file> <path-to-xsd>"
  echo "Example: $(basename "$0") custom.xml ../../xsd/xsd/NeTEx_publication.xsd"
}

# Print usage if no arguments or if -h/--help is requested
if [ $# -le 1 ] || [ "${1:-}" = "-h" ] || [ "${1:-}" = "--help" ]; then
  usage
  exit 1
fi

CUSTOM_XML=$1
if [ ! -f "$CUSTOM_XML" ]; then
  echo "Error: $CUSTOM_XML is not a regular file or does not exist." >&2
  exit 2
fi

XSD_URI=$2
GENERATOR_DIR="xquery"
GENERATED_DIR="../../generated/xcore"
BASEX_JAR="/tmp/basex.jar"

if [ ! -e ${BASEX_JAR} ]; then
	echo "Downloading BaseX ..."
	wget --output-document=${BASEX_JAR} https://files.basex.org/releases/10.6/BaseX106.jar
fi

echo "Generating documentation tables ..."

# prepare GENERATED_DIR
# mkdir -p "${GENERATED_DIR}"
# rm -f "${GENERATED_DIR}"/docs

# cd "${GENERATOR_DIR}"
JAVA_OPTS="-Xms4g -Xmx24g -XX:+UseG1GC -XX:+UseStringDeduplication"

java $JAVA_OPTS -cp ${BASEX_JAR} org.basex.BaseX \
 -b report=contab \
 -b uri="${XSD_URI}" \
 -b odir="${GENERATED_DIR}" \
 -b custom=$CUSTOM_XML \
 -b dnamesExcluded=".git .github" \
 -b htmlFilePerComplexType=true \
 ${GENERATOR_DIR}/xcore.xq

# Remove interim edesc files
# rm -rf "${GENERATED_DIR}"/edesc

# move to speaking name
# mv "${GENERATED_DIR}"/contab "${GENERATED_DIR}"/docs
# mv "${GENERATED_DIR}"/docs/contab-index.html "${GENERATED_DIRECTORY}"/docs/index.html

echo -e '\033[0;32mFinished generating documentation tables\033[0m'
