# Swiss profile 2.0 for NeTEx 2.0 - Realisation directive for public transport in Switzerland

This document describes the realisation specifications for the data transfer between SKI and the public transport in Switzerland, based on the official NeTEx standard.
It provides detailed clarifications and describes deviations from the official standard, with the aim of achieving consistent use throughout public transport in Switzerland.

The realisation specifications in this document will be agreed by the KIDS (“Kundeninfor-mationsdaten-Schnittstellen im öV-Schweiz”) working group.

The realisation specifications will be officially released by the National Commission Customer Information (Nationale Kommission Kundeninformation (KKI)) . 

The realisation specifications mainly concern: 
•	detailed clarifications about points which have abstract and open definitions in the standard. 
•	detailed clarifications about points which have hitherto been handled inconsistently within public transport in Switzerland. 
•	intentional deviations from the official standard within public transport in Switzerland.

## Supported NeTEx version
This profile is based on NeTEx 2.0 xxxlink tbd.

The relevant specification documents are xxxtbd

## Binding nature
This document describes the way in which the NeTEx standard is specifically applied and interpreted in Switzerland. It forms the basis for agreements concerning the connection between the individual public transport partners for exchanging timetables. 

## Chapters
- [Introduction & Roadmap](01_intro_roadmap.md)
- [Basic concepts of NeTEx](02_basic_concepts.md)
- [Guiding principles for the profile](03_guiding_principles.md)
- [File structure, encoding etc](04_files.md)
- [Frames used in the profile](05_frames.md)
- [Site model](06_stops.md)
- [Service](07_service.md)
- [Timetables](08_timetable.md)
- [Common elements](09_common.md)
- Special use cases
  - Joining / Splitting und "Durchbindung"
  - ServiceFacilities
  - JourneyParts
  - [Transfers / transfer times](uc_transfers.md)
  - [Journeys passing midnight](uc_midnight_passing.md)
  - Modes  and the ["KI Branchenstandard"](https://www.oev-info.ch/de/branchenstandard/branchenstandard-kundeninformation-bs-ki/branchenstandard-kundeninformation-bs-ki)
- Mapping tables
  - Modes
  - ServiceAttribute 
- Other profiles
  - Migration from RG 1.01 to RG 2.0 in Switzerland
  - Differences between Swiss profile and EPIP/EPIAP and how they could be amended
  - Differences to the French profile 
- [Resources and references](Annex_resources_references.md)

## Examples
We have a [set of examples](../examples/README.md) that show how to create use cases with the realisation guide.

## Tools
The basics:
- [How to use and build the templates?](../templates/README.md)

Building stuff:
- [Building markdown tables for the documentation of the Swiss profile](../tools/md_builder/README.md)
- [Building XML snippets as example for individual sections in the Swiss profile](..tools/xml_snippet/README.md)
- [Building schematron files for each input/output XML file in the Swiss profile](../tools/schematron_builder/README.md)
- We will do an xcore implementation that produces a HTML of the original NeTEx XSD tables into single files to be linked into the md, too.


We may in future also update the way we have things done here in the docs folder: We may use it to create a series of md files, where the tables and examples are included in the md files.

Testing stuff:
- [Checking XML files with schematron](../tools/check_schematron/README.md)
- The XSD validation is to be done in a separate step.

## Impressum
* Authors: tbd
* Status: tbd
* Last change: tbd
* Contact: info.fachbus@sbb.ch

## Copyright
The document is free. Proliferation in unchanged form is explicitly supported.
All toolings are - when nothing else is mentioned - available as AGPL 3.0.

