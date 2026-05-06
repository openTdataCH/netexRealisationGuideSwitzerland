# ServiceFrame

| Sub | Element | Usage | Card | Type | Description | Note |
|-----|---------|-------|------|------|-------------|------|
| + | lines | mandatory | 0..1 | lineRefs_RelStructure | Lines for FLEXIBLE STOP PLACE. | Only Line is used and not FlexibleLine |
| ++ | [Line](Line.md) | mandatory | 1..1 | unknown | A group of ROUTEs which is generally known to the public by a similar name or number. |  |
| + | destinationDisplays | expected | 0..1 | destinationDisplayRefs_RelStructure | Destinations associated with this GROUP OF SERVICEs, including via points. | We only allow fully formed content of destinationDisplays |
| ++ | [DestinationDisplay](DestinationDisplay.md) | expected | 1..1 | unknown | An advertised destination of a specific JOURNEY PATTERN, usually displayed on a head sign or at other on-board locations. | We only allow fully formed content of destinationDisplays |
| + | scheduledStopPoints | mandatory | 0..1 | scheduledStopPointsInFrame_RelStructure | SCHEDULED STOP POINTs in frame. | Swiss ScheduledStopPoint are using the sloid in the id, when possible. |
| ++ | [SiteConnection](SiteConnection.md) | expected | 1..1 | unknown | The physical (spatial) possibility to connect from one point to another in a SITE. | SiteConnection are used only in the main file and not in timetable files. |
| ++ | [DefaultConnection](DefaultConnection.md) | expected | 1..1 | unknown | Specifies the default transfer times to transfer between MODEs and / or OPERATORs within a region. | DefaultConnection is only used in the site file |
| + | stopAssignments | expected | 0..1 | stopAssignmentsInFrame_RelStructure | STOP ASSIGNMENTs in frame. |  |
| ++ | [PassengerStopAssignment](PassengerStopAssignment.md) | expected | 1..1 | unknown | The default allocation of a SCHEDULED STOP POINT to a specific STOP PLACE, and also possibly a QUAY and BOARDING POSITION. | are only used in a special PSA file in the export. |
| + | journeyPatterns | mandatory | 0..1 | journeyPatternRefs_RelStructure | JourneyPatternsequivalent to the series. |  |
| ++ | [ServiceJourneyPattern](ServiceJourneyPattern.md) | mandatory | 1..1 | unknown | The JOURNEY PATTERN for a (passenger carrying) SERVICE JOURNEY. |  |
| + | notices | expected | 0..1 | noticesInFrame_RelStructure | NOTICEs in frame. | notices may be present or not |
| ++ | [Notice](Notice.md) | expected | 1..1 | unknown | A note or footnote about any aspect of a service, e.g. an announcement, notice, etc. May have different DELIVERY VARIANTs for different media. | if notices are present, one Notice must be. |
