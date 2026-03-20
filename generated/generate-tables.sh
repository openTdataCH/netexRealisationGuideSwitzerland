#!/bin/bash
# Generate the documentation tables as docs/generated/OJP.html from the .xsd schema files
#
# You need the binary `java`
# apt-get install default-jre

# The -e flag causes the script to exit as soon as one command returns a non-zero exit code
set -e

base_dir="$(readlink -f $(dirname "$0")/..)"
xsl_dir=$base_dir/xsd/
generated_dir="${base_dir}/generated/docs"
basex="${generated_dir}/basex.jar"

if [ ! -e ${basex} ]; then
	echo "Download BaseX ..."
	wget --output-document=${basex} https://files.basex.org/releases/10.6/BaseX106.jar	
fi

echo "Generating documentation tables ..."

# prepare generated_dir
mkdir -p "${generated_dir}"
rm -f "${generated_dir}"/contab/*.html
cd ${xsl_dir}
java -cp ${basex} org.basex.BaseX -b report=contab -b dir=${base_dir} -b odir=${generated_dir} -b custom=custom-netex-perxsd.xml -b dnamesExcluded=".git .github" xcore.xq
rm -fr "${generated_dir}"/edesc

echo -e '\033[0;32mFinished generating documentation tables\033[0m'
