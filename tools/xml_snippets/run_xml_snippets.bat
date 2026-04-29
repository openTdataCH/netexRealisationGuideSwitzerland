@echo off
setlocal

REM XML Snippets Tool - Usage Script
REM Processes XML templates and generates snippets

set TEMPLATES_DIR=..\..\templates
set OUTPUT_DIR=..\..\generated\xml-snippets

if not exist "%OUTPUT_DIR%" (
    mkdir "%OUTPUT_DIR%"
)

echo Processing all XML templates in %TEMPLATES_DIR%...
echo Output will be saved to %OUTPUT_DIR%...
echo.

python build_xml_snippets.py -i "%TEMPLATES_DIR%" -o "%OUTPUT_DIR%"

endlocal
