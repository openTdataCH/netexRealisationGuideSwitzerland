# Introduction
The primary purpose of the NeTEx interface in Switzerland is the transmission of timetable data to one or more partners. The data transmitted via this interface is also required for the provision of timetable data in information systems. 
This document sets out the Swiss-wide standard for the implementation of the NeTEx interface and of individual data structures with regard to the mutual exchange of timetable information for modes of transport (e.g. train, bus) between public transport companies. This information is then made available on the OpenData platform.

The document specifically describes:
-	which data may be exchanged between public transport partners
-	which NeTEx elements are supported within public transport in Switzerland
-	the format of individual data elements
-	data flows in terms of content and time
-	necessary agreements regarding metadata
-	what needs to be taken into account when operating the interface
-	how data is to be interpreted


# How to use the document
This document shows all elements of the standard deemed necessary for exchanging public transport timetable data in Switzerland. Each description is grounded in the text of the official standard, but enriched to simplify implementation. We use the following structure:
- A link to the definition in official NeTEx and Transmodel terminology.
- **Purpose**: Introducing the element, its purpose and how it relates to other elements
- **Table**: Basically the XSD definition of the element in tabular form, tailored to the Swiss profile and enriched by profile-specific notes.
- **Example**: A detailed XML example.

The **Table** sections are based on the original XSD schema documentation and/or descriptions from the standard (whenever the XSD documentation is insufficient), but also adapted to the needs of public transport in Switzerland. In some cases  cardinality may change and fields may become mandatory or optional. A column **Usage** indicates whether a contained element is mandatory, almost always expected, or optional, while the column **Notes** provides profile-specific additions. Elements that are not used/important are not shown.

The **Notes** column also specifies value transformations and mapping tables in some cases. Only the provided functions and values are to be used, no deviations are allowed.

In some cases there are references to the HRDF format currently used in the data exchange of timetables in Switzerland. This is also to help implementers  understand how concepts map between the formats.

# Roadmap

| Date    | Milestone                                        |
|---------|--------------------------------------------------|
| 2026-07 | First draft for discussion of RG 2.0 (0.7 level) |
| 2026-09 | Review 1 done (0.8 level)                        |
| 2026-12 | RG 2.0 ready (1.0 level)                         |
| tbd     | RG 2.0 based NeTEx output                        |
| tbd     | Input accepted in version 2.0 format by SKI      |

