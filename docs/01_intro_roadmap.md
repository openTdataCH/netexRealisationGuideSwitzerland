# Introduction
The task performed by the NeTEx interface in Switzerland is the transmission of timetable data to one or more partners. The data transmitted via this interface is also required for the provision of timetable data in information systems. 
This document sets out the Swiss-wide standard for the implementation of the NeTEx inter-face and of individual data structures with regard to the mutual exchange of timetable infor-mation for modes of transport ( train, bus, … ) between public transport companies. This in-formation is then made available on the OpenData platform.

The document specifically describes:
•	which data may be exchanged between public transport partners
•	which NeTEx elements are supported within public transport in Switzerland
•	explicit deviations from the corresponding NeTEx
•	the format of individual data elements
•	the data flows in terms of content and time
•	what agreements are necessary with respect to metadata
•	what needs to be taken into account when operating the interface
•	how data is to be interpreted


# How to use the document
This document shows all elements of the norm that are deemed necessary for data exchange for public transport timetables in Switzerland. Each description is based on the text in the standard. However, we tried to enrich the information to simplify implementation. We use fol-lowing sections:
•	Business Requirements: Telling the business story of the element and how it is used in public transportation in Switzerland
•	Structure: Contains the detailed physical structure of the element with examples and more information about the business level 
•	Example: A detailed XML example

The tables in the structure section are based on the original XSD schema documentation and/or descriptions from the standard (whenever the XSD documentation is insufficient), but also adapted to the needs of public transport in Switzerland. In some cases the cardinality may change and fields may become mandatory or optional. An additional row is introduced for the specification of such business requirements. Elements that are not used/important, are not shown.

Additionally we use the following information in the business requirement row (following each elment description):
•	NOT TO BE USED: This element or field is not used in Switzerland. When the data is present, the file will be rejected during import. This element is not ignored, but rejected.
•	IGNORED AT IMPORT: This element or field may be provided, but it will not be loaded and removed from the data.

The business requirement row also specifies value transformations and mapping tables in some cases. Only the provided functions and values are to be used, no deviations are al-lowed.

In some cases there are references to the HRDF format currently used in the data exchange of timetables in Switzerland. This is also to help implementers to understand how to work with it.

# Roadmap

| Date | Milestone|
|--|--|
|2026-07 |First draft for discussion of RG 2.0 (0.7 level)|
|2026-09 |Review 1 done (0.8 level) |
|2026-12|RG 2.0 ready (1.0 level |
|tbd |RG 2.0 based NeTEx output |
|tbd| Input accepted in version 2.0 format by SKI|

**TODO** Needs to be updated.
