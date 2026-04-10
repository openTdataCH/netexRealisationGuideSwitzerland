@echo off
setlocal enabledelayedexpansion

REM Process all ch-profile templates and generate schematron files
set TEMPLATES_DIR=..\..\templates
set XSD_FILE=..\..\xsd\xsd\NeTEx_publication.xsd
set OUTPUT_DIR=..\..\generated\schematrons

if not exist "%OUTPUT_DIR%" (
    mkdir "%OUTPUT_DIR%"
)

echo Processing all ch-profile templates...

for %%f in ("%TEMPLATES_DIR%\ch-profile_*.xml") do (
    set TEMPLATE_FILE=%%f
    set TEMPLATE_NAME=%%~nf
    set OUTPUT_FILE=%OUTPUT_DIR%\!TEMPLATE_NAME!.sch
    
    echo Processing: !TEMPLATE_NAME!
    python template2schematron.py -t "!TEMPLATE_FILE!" -x "%XSD_FILE%" -i "%TEMPLATES_DIR%" -o "!OUTPUT_FILE!"
    
    if exist "!OUTPUT_FILE!" (
        echo Generated: !OUTPUT_FILE!
    ) else (
        echo Failed to generate: !OUTPUT_FILE!
    )
)

echo Done processing all ch-profile templates.