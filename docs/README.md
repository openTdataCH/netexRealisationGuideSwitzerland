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
This profile is based on NeTEx 2.0 xxxlink **TODO**.

The relevant specification documents are **TODO**

## Binding nature
This document describes the way in which the NeTEx standard is specifically applied and interpreted in Switzerland. It forms the basis for agreements concerning the connection between the individual public transport partners for exchanging timetables. 

## Chapters
- [Introduction & Roadmap](01_intro_roadmap.md)
- [Basic concepts of NeTEx](02_basic_concepts.md)
- [Guiding principles for the profile](03_guiding_principles.md)
- [File structure, encoding etc](04_files.md)
- [Frames used in the profile](05_frames.md)
- [Site model](06_stops.md)
- [Service model](07_service.md)
- [Service Calendar model](07_service.md)
- [Timetables](09_timetable.md)
- [Common elements](10_common.md)
- Special use cases:
  - ["Durchbindung"](uc01_durchbindung.md)
  - [Joining / splitting](uc02_joining_splitting.md)
  - [Transfers](uc03_transfers.md)
  - [Service facilities](uc04_service_facilities.md)
  - [Usage of JourneyParts](uc05_journey_parts.md)
  - **TODO**
  - [Direct carriages ("Kurswagen")](uc08_kurswagen.md)
  - [Accessibility](uc09_accessibility.md)
  - [Journeys passing midnight](uc10_midnight_passing.md)
  - Modes  and the ["KI Branchenstandard"](https://www.oev-info.ch/de/branchenstandard/branchenstandard-kundeninformation-bs-ki/branchenstandard-kundeninformation-bs-ki)
- Mapping tables
  - Modes
  - ServiceAttribute 
- Annexes:
  - [Resources and references](A1_annex_resources_references.md)
  - [Differences between Swiss profile and EPIP/EPIAP and how they could be amended](A2_annex_comparison_EPIP_EPIAP.md)
  - [Differences to the French and nordic profile](A3_annex_comparison_France_Norway.md)
  - [Glossary](A4_annex_glossary)
  - [Changelog andmigration from Swiss profile 1.0 to 2.0)](A5_changelog_migration.md)


## Examples
We have a [set of examples](../examples/README.md) that show how to create use cases with the realisation guide.

## Impressum
* Authors: **TODO**
* Status: Draft
* Last change: **TODO**
* Contact: info.fachbus@sbb.ch

## Copyright
The document is free. Proliferation in unchanged form is explicitly supported.
All toolings are - when nothing else is mentioned - available as AGPL 3.0.

