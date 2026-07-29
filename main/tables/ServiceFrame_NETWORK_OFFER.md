# ServiceFrame_NETWORK_OFFER

A minimal ServiceFrame must be present in all timetable files.

*Table: ServiceFrame*

| Sub | Element | Usage | Card | Type | Description | Note |
|-----|---------|-------|------|------|-------------|------|
|  | lines | mandatory | 0..1 | lineRefs_RelStructure | A coherent set of Service data to which the same frame VALIDITY CONDITIONs have been assigned. | Only Line is used and not FlexibleLine |
| + | [Line](Line.md) | mandatory | 0..* | unknown | A coherent set of Service data to which the same frame VALIDITY CONDITIONs have been assigned. |  |
|  | groupsOfLines | expected | 0..1 | groupsOfLinesInFrame_RelStructure | A coherent set of Service data to which the same frame VALIDITY CONDITIONs have been assigned. |  |
| + | [GroupOfLines](GroupOfLines.md) | expected | 0..* | unknown | A coherent set of Service data to which the same frame VALIDITY CONDITIONs have been assigned. | We use GroupOfLine for the modeling of mixed lines |
|  | destinationDisplays | expected | 0..1 | destinationDisplayRefs_RelStructure | A coherent set of Service data to which the same frame VALIDITY CONDITIONs have been assigned. | We only allow fully formed content of destinationDisplays |
| + | [DestinationDisplay](DestinationDisplay.md) | expected | 0..* | unknown | A coherent set of Service data to which the same frame VALIDITY CONDITIONs have been assigned. | We only allow fully formed content of destinationDisplays |
|  | scheduledStopPoints | mandatory | 0..1 | scheduledStopPointsInFrame_RelStructure | A coherent set of Service data to which the same frame VALIDITY CONDITIONs have been assigned. | Swiss ScheduledStopPoint are using the SLOID in the id if possible. |
| + | [ScheduledStopPoint](ScheduledStopPoint.md) | mandatory | 0..* | unknown | A coherent set of Service data to which the same frame VALIDITY CONDITIONs have been assigned. | The id of the ScheduledStopPoint is a SLOID if one exists. Otherwisse it contains a gen part. |
|  | stopAssignments | expected | 0..1 | stopAssignmentsInFrame_RelStructure | A coherent set of Service data to which the same frame VALIDITY CONDITIONs have been assigned. |  |
| + | [PassengerStopAssignment](PassengerStopAssignment.md) | expected | 0..* | unknown | A coherent set of Service data to which the same frame VALIDITY CONDITIONs have been assigned. | are only used in a special PSA file in the export. |
|  | timingLinks | expected | 0..1 | timingLinksInFrame_RelStructure | A coherent set of Service data to which the same frame VALIDITY CONDITIONs have been assigned. | We use TimingLink as the time behaviour between two ScheduledStopPoints |
| + | [TimingLink](TimingLink.md) | expected | 0..* | unknown | A coherent set of Service data to which the same frame VALIDITY CONDITIONs have been assigned. | every different handling of the link needs a different timing link e.g. bus vs tram |
|  | journeyPatterns | mandatory | 0..1 | journeyPatternRefs_RelStructure | A coherent set of Service data to which the same frame VALIDITY CONDITIONs have been assigned. |  |
| + | [ServiceJourneyPattern](ServiceJourneyPattern.md) | mandatory | 0..* | unknown | A coherent set of Service data to which the same frame VALIDITY CONDITIONs have been assigned. |  |
|  | timeDemandTypes | expected | 0..1 | timeDemandTypeRefs_RelStructure | A coherent set of Service data to which the same frame VALIDITY CONDITIONs have been assigned. |  |
| + | [TimeDemandType](TimeDemandType.md) | expected | 0..* | unknown | A coherent set of Service data to which the same frame VALIDITY CONDITIONs have been assigned. |  |
|  | notices | expected | 0..1 | noticesInFrame_RelStructure | A coherent set of Service data to which the same frame VALIDITY CONDITIONs have been assigned. | notices may be present or not |
| + | [Notice](Notice.md) | expected | 0..* | unknown | A coherent set of Service data to which the same frame VALIDITY CONDITIONs have been assigned. | if notices are present, one Notice must be. |
