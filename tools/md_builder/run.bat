@echo off
setlocal enabledelayedexpansion

REM Markdown Builder Tool - Run Script
REM This script demonstrates how to use the md_builder.py tool

echo Markdown Builder Tool - Run Script
REM ==================================
echo.

REM Configuration
set TEMPLATES_DIR=..\..\templates
set XSD_FILE=..\..\xsd\xsd\NeTEx_publication.xsd
set OUTPUT_DIR=..\..\generated\markdown-examples

REM Create output directory if it doesn't exist
if not exist "%OUTPUT_DIR%" (
    mkdir "%OUTPUT_DIR%"
)

echo Processing all XML templates in %TEMPLATES_DIR%...
echo Output will be saved to %OUTPUT_DIR%...
echo.

REM Process all XML files in the templates directory
for %%f in ("%TEMPLATES_DIR%\*.xml") do (
    set filename=%%~nf
    echo Processing: !filename!
    python md_builder.py -i "%TEMPLATES_DIR%" -o "%OUTPUT_DIR%" -x "%XSD_FILE%"
    
    if !ERRORLEVEL! == 0 (
        echo ✓ Generated: !filename!.md
    ) else (
        echo ✗ Failed to process: !filename!
    )
    echo.
)

echo Markdown generation completed!
echo.
echo Generated files:
dir /b "%OUTPUT_DIR%\*.md" 2>nul || echo No markdown files found in %OUTPUT_DIR%

echo.
echo For more information, see README.md

endlocal