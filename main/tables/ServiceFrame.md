# ServiceFrame

A minimal ServiceFrame must be present in all timetable files.

*Table: ServiceFrame*

| Sub | Element | Usage | Card | Type | Description | Note |
|-----|---------|-------|------|------|-------------|------|
|  | @id | mandatory | 1..1 | xsd:string | Attribute id | |
|  | @version | mandatory | 1..1 | xsd:string | Attribute version | |
|  | lines | mandatory | 0..1 | lineRefs_RelStructure | A coherent set of Service data to which the same frame VALIDITY CONDITIONs have been assigned. | Only Line is used and not FlexibleLine |
| + | [Line](Line.md) | mandatory | 0..* | unknown | A coherent set of Service data to which the same frame VALIDITY CONDITIONs have been assigned. |  |
|  | groupsOfLines | expected | 0..1 | groupsOfLinesInFrame_RelStructure | A coherent set of Service data to which the same frame VALIDITY CONDITIONs have been assigned. |  |
| + | [GroupOfLines](GroupOfLines.md) | expected | 0..* | unknown | A coherent set of Service data to which the same frame VALIDITY CONDITIONs have been assigned. | We use GroupOfLine for the modeling of mixed lines |
|  | destinationDisplays | expected | 0..1 | destinationDisplayRefs_RelStructure | A coherent set of Service data to which the same frame VALIDITY CONDITIONs have been assigned. |  |
| + | [DestinationDisplay](DestinationDisplay.md) | expected | 0..* | unknown | A coherent set of Service data to which the same frame VALIDITY CONDITIONs have been assigned. | We only allow DestinationDisplay based on Name and not on reference to a ScheduledStopPoint |
|  | scheduledStopPoints | expected | 0..1 | scheduledStopPointsInFrame_RelStructure | A coherent set of Service data to which the same frame VALIDITY CONDITIONs have been assigned. | Swiss ScheduledStopPoint are using the SLOID in the id, when possible. |
| + | [ScheduledStopPoint](ScheduledStopPoint.md) | mandatory | 0..* | unknown | A coherent set of Service data to which the same frame VALIDITY CONDITIONs have been assigned. | The id of the ScheduledStopPoint is a SLOID if one exists. Otherwisse it contains a gen part. |
|  | connections | expected | 0..1 | transfersInFrame_RelStructure | A coherent set of Service data to which the same frame VALIDITY CONDITIONs have been assigned. | connections is used in SITE_OFFER, but not in NETWORK_OFER |
| + | [SiteConnection](SiteConnection.md) | expected | 0..* | unknown | A coherent set of Service data to which the same frame VALIDITY CONDITIONs have been assigned. | SiteConnection are used only in the SITE_OFFER file and not in NETWORK_OFFER files. |
| + | [DefaultConnection](DefaultConnection.md) | expected | 0..* | unknown | A coherent set of Service data to which the same frame VALIDITY CONDITIONs have been assigned. | DefaultConnection is only used in the SITE_OFFER file |
|  | stopAssignments | expected | 0..1 | stopAssignmentsInFrame_RelStructure | A coherent set of Service data to which the same frame VALIDITY CONDITIONs have been assigned. |  |
| + | [PassengerStopAssignment](PassengerStopAssignment.md) | expected | 0..* | unknown | A coherent set of Service data to which the same frame VALIDITY CONDITIONs have been assigned. | Make the link between timetables and site model. |
|  | timingLinks | expected | 0..1 | timingLinksInFrame_RelStructure | A coherent set of Service data to which the same frame VALIDITY CONDITIONs have been assigned. | We use TimingLink as the time behaviour between two ScheduledStopPoints |
| + | [TimingLink](TimingLink.md) | expected | 0..* | unknown | A coherent set of Service data to which the same frame VALIDITY CONDITIONs have been assigned. | every different handling of the link needs a different timing link e.g. bus vs tram |
|  | journeyPatterns | mandatory | 0..1 | journeyPatternRefs_RelStructure | A coherent set of Service data to which the same frame VALIDITY CONDITIONs have been assigned. |  |
| + | [ServiceJourneyPattern](ServiceJourneyPattern.md) | mandatory | 0..* | unknown | A coherent set of Service data to which the same frame VALIDITY CONDITIONs have been assigned. |  |
|  | timeDemandTypes | expected | 0..1 | timeDemandTypeRefs_RelStructure | A coherent set of Service data to which the same frame VALIDITY CONDITIONs have been assigned. |  |
| + | [TimeDemandType](TimeDemandType.md) | expected | 0..* | unknown | A coherent set of Service data to which the same frame VALIDITY CONDITIONs have been assigned. | TimeDemandType is now the core concept to use for the timing behaviour of ServiceJourney. |
|  | notices | expected | 0..1 | noticesInFrame_RelStructure | A coherent set of Service data to which the same frame VALIDITY CONDITIONs have been assigned. | notices may be present or not |
| + | [Notice](Notice.md) | expected | 0..* | unknown | A coherent set of Service data to which the same frame VALIDITY CONDITIONs have been assigned. | if notices are present, one Notice must be. |
