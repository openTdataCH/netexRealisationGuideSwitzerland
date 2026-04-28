echo "check validity of templates and examples"
cd validation
rem call run.bat
cd ..

echo "build all schematron files"
cd  schematron_builder
call process_all_ch_profiles.bat
cd ..

echo "checking if all ch-see files exist"
cd md_builder
call run_check_ch_see_references.bat

echo  "build all md example files"
call run.bat
cd ..

echo "build xml snippets"
cd xml_snippets
call run_xml_snippets.bat
cd ..

echo "to be build xcore html files"

echo "check links in docs"
cd check_links
call run.bat
cd ..

echo "generate the included docs"
cd expand_docs
call run.bat
cd ..