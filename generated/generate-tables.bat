@echo off
:: Generate the documentation tables as docs/generated/OJP.html from the .xsd schema files
::
:: You need the binary `java`
:: Ensure Java is installed and in the PATH

setlocal enabledelayedexpansion

set "base_dir=%~dp0.."
set "xsl_dir=%base_dir%\xsd\"
set "generated_dir=%base_dir%\generated\docs"
set "basex=%TEMP%\basex.jar"

if not exist "%basex%" (
    echo Download BaseX ...
    powershell -Command "Invoke-WebRequest -Uri 'https://files.basex.org/releases/10.6/BaseX106.jar' -OutFile '%basex%'"
)

echo Generating documentation tables ...

:: prepare generated_dir
mkdir "%generated_dir%" 2>nul
if exist "%generated_dir%\contab\*.html" del "%generated_dir%\contab\*.html"

cd /d "%xsl_dir%"

:: Use Java to run BaseX
java -cp "%basex%" org.basex.BaseX -b report=contab -b dir="%base_dir%" -b odir="%generated_dir%" -b custom=custom-netex-perxsd.xml -b dnamesExcluded=".git .github" xcore.xq

if exist "%generated_dir%\edesc" rmdir /s /q "%generated_dir%\edesc"

echo Finished generating documentation tables
