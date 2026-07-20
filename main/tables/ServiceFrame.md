# ServiceFrame

A minimal ServiceFrame must be present in all timetable files.

*Table: ServiceFrame*

| Sub | Element | Usage | Card | Type | Description | Note |
|-----|---------|-------|------|------|-------------|------|
|  | @id | mandatory | 1..1 | xsd:string | Attribute id | |
|  | @version | mandatory | 1..1 | xsd:string | Attribute version | |
|  | ServiceCalendarFrameRef | optional | 1..1 | ServiceCalendarFrameRef | Reference to a SERVICE CALENDAR FRAME. | We can have a reference to other Frames if necessary. However, we believe that the id/version (together with the NameOfClass) should always be unique. If they are the same, it is the same "object"). |
|  | lines | mandatory | 0..1 | lineRefs_RelStructure | Lines for FLEXIBLE STOP PLACE. | Only Line is used and not FlexibleLine |
| + | [Line](Line.md) | mandatory | 1..* | Line | A group of ROUTEs which is generally known to the public by a similar name or number. |  |
|  | groupsOfLines | expected | 0..1 | groupsOfLinesInFrame_RelStructure | Groups of LINEs in NETWORK. |  |
| + | [GroupOfLines](GroupOfLines.md) | expected | 1..* | GroupOfLines | A grouping of LINEs which will be commonly referenced for a specific purpose. | We use GroupOfLine for the modeling of mixed lines |
|  | destinationDisplays | expected | 0..1 | destinationDisplayRefs_RelStructure | Destinations associated with this GROUP OF SERVICEs, including via points. | We only allow fully formed content of destinationDisplays |
| + | [DestinationDisplay](DestinationDisplay.md) | expected | 1..* | DestinationDisplay | An advertised destination of a specific JOURNEY PATTERN, usually displayed on a head sign or at other on-board locations. | We only allow fully formed content of destinationDisplays |
|  | scheduledStopPoints | expected | 0..1 | scheduledStopPointsInFrame_RelStructure | SCHEDULED STOP POINTs in frame. | Swiss ScheduledStopPoint are using the SLOID in the id, when possible. |
| + | [ScheduledStopPoint](ScheduledStopPoint.md) | mandatory | 1..* | ScheduledStopPoint | A POINT where passengers can board or alight from vehicles. It is open, which hierarchical level such a point has. It can represent a single door (BoardingPosition) or a whole ZONE. The association to the physical model is done with STOP ASSIGNMENTs. | The id of the ScheduledStopPoint is a SLOID if one exists. Otherwisse it contains a gen part. |
|  | connections | expected | 0..1 | transfersInFrame_RelStructure | CONNECTIONs in frame. |  |
| + | [SiteConnection](SiteConnection.md) | expected | 1..* | SiteConnection | The physical (spatial) possibility to connect from one point to another in a SITE. | SiteConnection are used only in the SITE_OFFER file and not in NETWORK_OFFER files. |
| + | [DefaultConnection](DefaultConnection.md) | expected | 1..* | DefaultConnection | Specifies the default transfer times to transfer between MODEs and / or OPERATORs within a region. | DefaultConnection is only used in the SITE_OFFER file |
|  | stopAssignments | expected | 0..1 | stopAssignmentsInFrame_RelStructure | STOP ASSIGNMENTs in frame. |  |
| + | [PassengerStopAssignment](PassengerStopAssignment.md) | expected | 1..* | PassengerStopAssignment | The default allocation of a SCHEDULED STOP POINT to a specific STOP PLACE, and also possibly a QUAY and BOARDING POSITION. | are only used in a special PSA file in the export. |
|  | timingLinks | expected | 0..1 | timingLinksInFrame_RelStructure | TIMING LINKs in frame. | We use TimingLink as the time behaviour between two ScheduledStopPoints |
| + | [TimingLink](TimingLink.md) | expected | 1..* | TimingLink | An ordered pair of TIMING POINTs for which run times may be recorded. Timing links are directional - there will be separate links for each direction of a route. | every different handling of the link needs a different timing link e.g. bus vs tram |
|  | journeyPatterns | mandatory | 0..1 | journeyPatternRefs_RelStructure | JourneyPatternsequivalent to the series. |  |
| + | [ServiceJourneyPattern](ServiceJourneyPattern.md) | mandatory | 1..* | ServiceJourneyPattern | The JOURNEY PATTERN for a (passenger carrying) SERVICE JOURNEY. |  |
|  | timeDemandTypes | expected | 0..1 | timeDemandTypeRefs_RelStructure | Other TIME DEMAND TYPEs used in journey. |  |
| + | [TimeDemandType](TimeDemandType.md) | expected | 1..* | TimeDemandType | An indicator of traffic conditions or other factors which may affect vehicle run or wait times. It may be entered directly by the scheduler or defined by the use of TIME BANDs. | TimeDemandType is now the core concept to use for the timing behaviour of ServiceJourney. |
|  | notices | expected | 0..1 | noticesInFrame_RelStructure | NOTICEs in frame. | notices may be present or not |
| + | [Notice](Notice.md) | expected | 1..* | Notice | A note or footnote about any aspect of a service, e.g. an announcement, notice, etc. May have different DELIVERY VARIANTs for different media. | if notices are present, one Notice must be. |
