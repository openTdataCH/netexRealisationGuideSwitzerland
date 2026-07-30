# ServiceFrame_NETWORK_OFFER

A minimal ServiceFrame must be present in all timetable files.

*Table: ServiceFrame*

| Sub | Element | Usage | Card | Type | Description | Note |
|-----|---------|-------|------|------|-------------|------|
|  | lines | mandatory | 0..1 | lineRefs_RelStructure | LINEs in frame. | Only Line is used and not FlexibleLine |
| + | [Line](Line.md) | mandatory | 0..* | Line_VersionStructure | A group of ROUTEs which is generally known to the public by a similar name or number. |  |
|  | groupsOfLines | expected | 0..1 | groupsOfLinesInFrame_RelStructure | GROUPs of LINEs in frame. |  |
| + | [GroupOfLines](GroupOfLines.md) | expected | 1..* | GroupOfLines_VersionStructure | A grouping of LINEs which will be commonly referenced for a specific purpose. | We use GroupOfLine for the modeling of mixed lines |
|  | destinationDisplays | expected | 0..1 | destinationDisplayRefs_RelStructure | DESTINATION DISPLAYs in frame. | We only allow fully formed content of destinationDisplays |
| + | [DestinationDisplay](DestinationDisplay.md) | expected | 1..* | DestinationDisplay_VersionStructure | An advertised destination of a specific JOURNEY PATTERN, usually displayed on a head sign or at other on-board locations. | We only allow fully formed content of destinationDisplays |
|  | scheduledStopPoints | mandatory | 0..1 | scheduledStopPointsInFrame_RelStructure | SCHEDULED STOP POINTs in frame. | Swiss ScheduledStopPoint are using the SLOID in the id if possible. |
| + | [ScheduledStopPoint](ScheduledStopPoint.md) | mandatory | 0..* | unknown | A POINT where passengers can board or alight from vehicles. It is open, which hierarchical level such a point has. It can represent a single door (BoardingPosition) or a whole ZONE. The association to the physical model is done with STOP ASSIGNMENTs. | The id of the ScheduledStopPoint is a SLOID if one exists. Otherwisse it contains a gen part. |
|  | stopAssignments | expected | 0..1 | stopAssignmentsInFrame_RelStructure | STOP ASSIGNMENTs in frame. |  |
| + | [PassengerStopAssignment](PassengerStopAssignment.md) | expected | 0..* | PassengerStopAssignment_VersionStructure | The default allocation of a SCHEDULED STOP POINT to a specific STOP PLACE, and also possibly a QUAY and BOARDING POSITION. | are only used in a special PSA file in the export. |
|  | timingLinks | expected | 0..1 | timingLinksInFrame_RelStructure | TIMING LINKs in frame. | We use TimingLink as the time behaviour between two ScheduledStopPoints |
| + | [TimingLink](TimingLink.md) | expected | 1..* | TimingLink_VersionStructure | An ordered pair of TIMING POINTs for which run times may be recorded. Timing links are directional - there will be separate links for each direction of a route. | every different handling of the link needs a different timing link e.g. bus vs tram |
|  | journeyPatterns | mandatory | 0..1 | journeyPatternRefs_RelStructure | JOURNEY PATTERNs in frame. |  |
| + | [ServiceJourneyPattern](ServiceJourneyPattern.md) | mandatory | 0..* | ServiceJourneyPattern_VersionStructure | The JOURNEY PATTERN for a (passenger carrying) SERVICE JOURNEY. |  |
|  | timeDemandTypes | expected | 0..1 | timeDemandTypeRefs_RelStructure | TIME DEMAND TYPEs in frame. |  |
| + | [TimeDemandType](TimeDemandType.md) | expected | 1..* | TimeDemandType_VersionStructure | An indicator of traffic conditions or other factors which may affect vehicle run or wait times. It may be entered directly by the scheduler or defined by the use of TIME BANDs. |  |
|  | notices | expected | 0..1 | noticesInFrame_RelStructure | NOTICEs in frame. | notices may be present or not |
| + | [Notice](Notice.md) | expected | 1..* | Notice_VersionStructure | A note or footnote about any aspect of a service, e.g. an announcement, notice, etc. May have different DELIVERY VARIANTs for different media. | if notices are present, one Notice must be. |
