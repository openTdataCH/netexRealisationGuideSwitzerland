
# Work in Progress: NeTEx realisation guide 2.0 for Switzerland
We work here to create the next NeTEX realisation guide.

## Profile 2.0 draft
[Start the document](docs/README.md)

## Repo structure
The current relevant folder/files in the repo:
* .github: scripts and workflows
* docs: The profile
  * docs/include: the images and other files that are used for the md as well
* examples: all XML examples
* mgmt: Handling of this repo
* README.md: the starting file

## Provisional Roadmap for profile 2.0
* 2026-4: repo ready, moved to MD
* 2026-7: first draft ready
* 2026-12: ready for release, discussed with KI ADM and KIDS AG Solldaten

## Folders

| Folder                 | Content                                                           |
|------------------------|-------------------------------------------------------------------|
| docs                   | The realisation guide itself.                                     |
| examples               | Valid XML examples based on use cases                             |
| generated              | all generated elements. Some we still publish.                    |
| generated/schematrons  | schematron files to be used to validate Swiss data files          |
| generated/elements.xml | Simple element examples XML.                                      |
| generated/xcore        | xcore documentation of the NeTEX XSD.                             |
| generated/elements.md  | markdowns of the relevant elements                                |
| templates              | template files to generade schematrons and elements in elemnts.md |
| tools                  | relevant tools to build everything                                |
| tools/schematron_builder | pyhton program to build the schematrons in generated/schematrons  |
| tools/md_builder | python program to build the elements.md                           |
| tools/xcore            | Tool to generate elemnts.xml from the XSD                         |
| xsd                    | the NeTEx 2.0 XSD                                                 |

## Changelog from version 1.0.1
tbd

## Generate a local copy
* check out the project
* check out the xsd
* build schematrons
* build elements.xml
* build elemnts.md
## Contact
Contact: info.fachbus@sbb.ch
