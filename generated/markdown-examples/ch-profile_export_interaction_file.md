# ch-profile_export_interaction_file

| Sub | Element | Usage | Card | Type | Description | Note |
|-----|---------|-------|------|------|-------------|------|
|  | PublicationDelivery | mandatory | 1..1 | PublicationDeliveryStructure | A set of NeTEx objects as assembled by a publication request or other service. Provides a general purpose wrapper for NeTEx data content. |  |
| + | PublicationTimestamp | mandatory | 1..1 | xsd:dateTime | Time of output of data. |  |
| + | ParticipantRef | mandatory | 1..1 | siri:ParticipantCodeType | Identifier of system requesting Data. |  |
| + | dataObjects | mandatory | 0..1 | unknown | NeTEx Entities of any type. |  |
| ++ | CompositeFrame | mandatory | 1..1 | unknown | A container VERSION FRAME that groups a set of content VERSION FRAMsE to which the same VALIDITY CONDITIONs have been assigned. |  |
| +++ | frames | mandatory | 0..1 | frames_RelStructure | Content frames in COMPOSITE FRAME. |  |
| ++++ | TimetableFrame | mandatory | 1..1 | unknown | A coherent set of timetable data (VEHICLE JOURNEYs and BLOCKs) to which the same VALIDITY CONDITIONs have been assigned. |  |
| +++++ | interchangeRules | mandatory | 0..1 | interchangeRules_RelStructure | INTERCHANGE RULEs for visit. |  |
| ++++++ | InterchangeRule | mandatory | 1..1 | unknown | Conditions for considering journeys to meet or not to meet, specified indirectly: by a particular MODE, DIRECTION or LINE. Such conditions may alternatively be specified directly, indicating the corresponding services. In this case they are either a SERVICE JOURNEY PATTERN INTERCHANGE or a SERVICE JOURNEY INTERCHANGE. |  |
| ++++++ | InterchangeRule | optional | 1..1 | unknown | Conditions for considering journeys to meet or not to meet, specified indirectly: by a particular MODE, DIRECTION or LINE. Such conditions may alternatively be specified directly, indicating the corresponding services. In this case they are either a SERVICE JOURNEY PATTERN INTERCHANGE or a SERVICE JOURNEY INTERCHANGE. | transfer times between ServiceJourneys (UMSTEIGZ) |
