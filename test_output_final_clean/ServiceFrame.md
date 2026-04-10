# ServiceFrame

| Sub | Element | Usage | Card | Type | Description | Note |
|-----|---------|-------|------|------|-------------|------|
|  | PublicationDelivery | ignored | 1..1 | PublicationDeliveryStructure | A set of NeTEx objects as assembled by a publication request or other service. Provides a general purpose wrapper for NeTEx data content. |  |
| + | ParticipantRef | ignored | 1..1 | siri:ParticipantCodeType | Identifier of system requesting Data. |  |
| + | PublicationTimestamp | ignored | 1..1 | xsd:dateTime | Time of output of data. |  |
| + | dataObjects | ignored | 1..1 | unknown |  |  |
| ++ | CompositeFrame | ignored | 1..1 | unknown |  |  |
| +++ | frames | ignored | 1..1 | unknown |  |  |
| ++++ | ServiceFrame | ignored | 1..1 | unknown | TODO how would we describe additional id and which ones are mandatory? |  |
| +++++ | connections | ignored | 1..1 | unknown |  |  |
| +++++ | destinationDisplays | ignored | 1..1 | unknown | We only allow fully formed content of destinationDisplays |  |
| +++++ | directions | forbidden | 1..1 | unknown | We don't use directions, but only direction type |  |
| +++++ | groupsOfLines | forbidden | 1..1 | unknown |  |  |
| +++++ | lines | mandatory | 1..1 | unknown | Only Line is used and not FlexibleLine |  |
| +++++ | notices | ignored | 1..1 | unknown | notices may be present or not |  |
| +++++ | scheduledStopPoints | ignored | 1..1 | unknown | Swiss ScheduledStopPoint are using the sloid in the id, when possible. |  |
| +++++ | stopAssignments | ignored | 1..1 | unknown |  |  |
| ++++++ | Access | forbidden | 1..1 | unknown |  |  |
| ln++++++ | [Connection](Connection.md) | ignored | 1..1 | unknown | Connection is used only used in the site file |  |
| ln++++++ | [DefaultConnection](DefaultConnection.md) | ignored | 1..1 | unknown | DefaultConnection is only used in the site file |  |
| ln++++++ | [DestinationDisplay](DestinationDisplay.md) | ignored | 1..1 | unknown | We only allow fully formed content of destinationDisplays |  |
| ++++++ | Direction | forbidden | 1..1 | unknown |  |  |
| ++++++ | FlexibleLine | forbidden | 1..1 | unknown | We work with Line only. |  |
| ++++++ | GroupOfLines | forbidden | 1..1 | unknown |  |  |
| ln++++++ | [Line](Line.md) | mandatory | 1..1 | unknown |  |  |
| ln++++++ | [Notice](Notice.md) | ignored | 1..1 | unknown | if notices are present, one Notice must be. |  |
| ln++++++ | [PassengerStopAssignment](PassengerStopAssignment.md) | ignored | 1..1 | unknown | are only ued in a special PSA file in the export. |  |
| ++++++ | ScheduledStopPoint | ignored | 1..1 | unknown | TODO full or not |  |
| ln++++++ | [SiteConnection](SiteConnection.md) | ignored | 1..1 | unknown | SiteConnection are used only in the main file and not in timetable files. |  |
| +++++++ | From | ignored | 1..1 | unknown |  |  |
| +++++++ | Name | ignored | 1..1 | unknown |  |  |
| +++++++ | To | ignored | 1..1 | unknown |  |  |
