# ServiceFrame

A minimal ServiceFrame must be present in all timetable files.

*Table: ServiceFrame*

| Sub | Element | Usage | Card | Type | Description | Note |
|-----|---------|-------|------|------|-------------|------|
|  | @id | mandatory | 1..1 | xsd:string | Attribute id | |
|  | @version | mandatory | 1..1 | xsd:string | Attribute version | |
|  | lines | mandatory | 0..1 | lineRefs_RelStructure |  | Only Line is used and not FlexibleLine |
| + | [Line](Line.md) | mandatory | 0..* | unknown |  |  |
|  | groupsOfLines | expected | 0..1 | groupsOfLinesInFrame_RelStructure |  |  |
| + | [GroupOfLines](GroupOfLines.md) | expected | 0..* | unknown |  | We use GroupOfLine for the modeling of mixed lines |
|  | destinationDisplays | expected | 0..1 | destinationDisplayRefs_RelStructure |  |  |
| + | [DestinationDisplay](DestinationDisplay.md) | expected | 0..* | unknown |  | We only allow DestinationDisplay based on Name and not on reference to a ScheduledStopPoint |
|  | scheduledStopPoints | expected | 0..1 | scheduledStopPointsInFrame_RelStructure |  | Swiss ScheduledStopPoint are using the SLOID in the id, when possible. |
| + | [ScheduledStopPoint](ScheduledStopPoint.md) | mandatory | 0..* | unknown |  | The id of the ScheduledStopPoint is a SLOID if one exists. Otherwisse it contains a gen part. |
|  | connections | expected | 0..1 | transfersInFrame_RelStructure |  | connections is used in SITE_OFFER, but not in NETWORK_OFER |
| + | [SiteConnection](SiteConnection.md) | expected | 0..* | unknown |  | SiteConnection are used only in the SITE_OFFER file and not in NETWORK_OFFER files. |
| + | [DefaultConnection](DefaultConnection.md) | expected | 0..* | unknown |  | DefaultConnection is only used in the SITE_OFFER file |
|  | stopAssignments | expected | 0..1 | stopAssignmentsInFrame_RelStructure |  |  |
| + | [PassengerStopAssignment](PassengerStopAssignment.md) | expected | 0..* | unknown |  | Make the link between timetables and site model. |
|  | timingLinks | expected | 0..1 | timingLinksInFrame_RelStructure |  | We use TimingLink as the time behaviour between two ScheduledStopPoints |
| + | [TimingLink](TimingLink.md) | expected | 0..* | unknown |  | every different handling of the link needs a different timing link e.g. bus vs tram |
|  | journeyPatterns | mandatory | 0..1 | journeyPatternRefs_RelStructure |  |  |
| + | [ServiceJourneyPattern](ServiceJourneyPattern.md) | mandatory | 0..* | unknown |  |  |
|  | timeDemandTypes | expected | 0..1 | timeDemandTypeRefs_RelStructure |  |  |
| + | [TimeDemandType](TimeDemandType.md) | expected | 0..* | unknown |  | TimeDemandType is now the core concept to use for the timing behaviour of ServiceJourney. |
|  | notices | expected | 0..1 | noticesInFrame_RelStructure |  | notices may be present or not |
| + | [Notice](Notice.md) | expected | 0..* | unknown |  | if notices are present, one Notice must be. |
