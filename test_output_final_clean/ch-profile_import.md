# ch-profile_import

| Sub | Element | Usage | Card | Type | Description | Note |
|-----|---------|-------|------|------|-------------|------|
|  | PublicationDelivery | ignored | 1..1 | PublicationDeliveryStructure | A set of NeTEx objects as assembled by a publication request or other service. Provides a general purpose wrapper for NeTEx data content. |  |
| + | ParticipantRef | ignored | 1..1 | siri:ParticipantCodeType | Identifier of system requesting Data. |  |
| + | PublicationTimestamp | ignored | 1..1 | xsd:dateTime | Time of output of data. |  |
| + | dataObjects | ignored | 1..1 | unknown |  |  |
| ++ | CompositeFrame | ignored | 1..1 | unknown |  |  |
| +++ | frames | ignored | 1..1 | unknown |  |  |
| ln++++ | [ResourceFrame](ResourceFrame.md) | ignored | 1..1 | unknown |  |  |
| ln++++ | [ServiceCalendarFrame](ServiceCalendarFrame.md) | ignored | 1..1 | unknown |  |  |
| ln++++ | [ServiceFrame](ServiceFrame.md) | ignored | 1..1 | unknown |  |  |
| ++++ | TimetableFrame | ignored | 1..1 | unknown |  |  |
