@echo off
setlocal enabledelayedexpansion

REM XML Snippets Tool - Usage Script
REM This script demonstrates how to use the build_xml_snippets.py tool

echo XML Snippets Tool Usage Demo
echo ==========================

echo.
echo 1. Basic usage - Process all templates in a directory
echo.

set TEMPLATES_DIR=..\..\templates
set OUTPUT_DIR=..\..\generated\xml-snippets

if not exist "%OUTPUT_DIR%" (
    mkdir "%OUTPUT_DIR%"
)

echo Processing all XML templates in %TEMPLATES_DIR%...
echo Output will be saved to %OUTPUT_DIR%...
echo.

python build_xml_snippets.py -i "%TEMPLATES_DIR%" -o "%OUTPUT_DIR%"

echo.
echo 2. Process a single template file
echo.

set SINGLE_TEMPLATE=%TEMPLATES_DIR%\ServiceFacilitySet.xml
set SINGLE_OUTPUT=%OUTPUT_DIR%\ServiceFacilitySet_single_test.xml

echo Processing single template: %SINGLE_TEMPLATE%
echo Output: %SINGLE_OUTPUT%
echo.

python build_xml_snippets.py -i "%TEMPLATES_DIR%" -o "%OUTPUT_DIR%"

echo.
echo 3. Show generated files
echo.

echo Files generated in %OUTPUT_DIR%:
dir /b "%OUTPUT_DIR%\*.xml"

echo.
echo 4. Show content of a sample output file
echo.

set SAMPLE_FILE=%OUTPUT_DIR%\ServiceFacilitySet.xml

if exist "%SAMPLE_FILE%" (
    echo Content of %SAMPLE_FILE%:
    echo.
    type "%SAMPLE_FILE%"
) else (
    echo Sample file not found: %SAMPLE_FILE%
)

echo.
echo Demo completed!
echo.
echo For more information, see README.md

endlocal