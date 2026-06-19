
# Work in Progress: NeTEx realisation guide 2.0 for Switzerland
We work here to create the next NeTEX realisation guide.

## Profile 2.0 draft

The finalised version (as HTML) can be found here: [https://opentdatach.github.io/netexRealisationGuideSwitzerland/](https://opentdatach.github.io/netexRealisationGuideSwitzerland/).

The original markdown sources can be found here: [markdown folder](docs/README.md)

## Released version
none

## Provisional Roadmap for profile 2.0
* 2026-04: repo ready, moved to MD
* 2026-07: first draft ready (v0.7)
* 2026-09: input from review incorporated (v0.8)
* 2026-12: ready for release, discussed with KI ADM and KIDS AG Solldaten (v1.0)

## Folders

### Source Folders

Source folders added to git:

| Folder            | Content                                                                                                                   |
|-------------------|---------------------------------------------------------------------------------------------------------------------------|
| docs              | The document sources of the realisation guide (with links)                                                                |
| examples          | Valid XML examples based on use cases                                                                                     |
| jekyll            | jekyll template folder (is copied to the site folder during the build). Jekyll is used to generate html for GitHub pages. |
| mgmt              | governance and organisation                                                                                               |
| templates         | template files to generade schematrons and elements in elements.md                                                        |
| tools             | Python tools to build everything ([see](./tools/README.md))                                                               |
| xsd               | the NeTEx 2.0 XSD                                                                                                         |

### Generated Folders

The ([build automation framework](./tools/README.md#build-automation-framework)) generates target documents from source documents.  
These target documents are written to `site` and according subfolders, excluded from git:

| Folder            | Content                                                                                       |
|-------------------|-----------------------------------------------------------------------------------------------|
| site              | Destination folder for generated docs. The content of this older is deployed to github pages. |
| site/schematrons  | Schematron files to be used to validate Swiss data files                                      |
| site/xml-snippets | Simple element examples XML.                                                                  |
| site/netex-html   | xcore documentation of the NeTEX XSD.                                                         |
| site/tables       | markdown tables of the relevant elements                                                      |

## Governance of the realisation guide and this repository.
[see here](mgmt/README.md)

## Changelog from version 1.0.1
[see here](docs/A5_changelog_migration.md)

## Contact
Contact: info.fachbus@sbb.ch
