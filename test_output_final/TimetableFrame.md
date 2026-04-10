# TimetableFrame

| Sub | Element | Usage | Card | Type | Description | Note |
|-----|---------|-------|------|------|-------------|------|
|  | PublicationDelivery | ignored | 1..1 | PublicationDeliveryStructure | A set of NeTEx objects as assembled by a publication request or other service. Provides a general purpose wrapper for NeTEx data content. |  |
| + | ParticipantRef | ignored | 1..1 | siri:ParticipantCodeType | Identifier of system requesting Data. |  |
| + | PublicationTimestamp | ignored | 1..1 | xsd:dateTime | Time of output of data. |  |
| + | dataObjects | ignored | 1..1 | unknown |  |  |
| ++ | CompositeFrame | ignored | 1..1 | unknown |  |  |
| +++ | frames | ignored | 1..1 | unknown |  |  |
| ++++ | TimetableFrame | ignored | 1..1 | unknown |  |  |
| +++++ | trainNumbers | ignored | 1..1 | unknown |  |  |
| +++++ | typesOfService | ignored | 1..1 | unknown |  |  |
| +++++ | vehicleJourneys | ignored | 1..1 | unknown |  |  |
| ln++++++ | [TemplateServiceJourney](TemplateServiceJourney.md) | ignored | 1..1 | unknown |  |  |
| ++++++ | TemplateServiceJourney | ignored | 1..1 | unknown |  |  |
| ln++++++ | [TrainNumber](TrainNumber.md) | ignored | 1..1 | unknown |  |  |
| ++++++ | TypeOfService | ignored | 1..1 | unknown | This is exactly how the TypeOfService should be defined for Switzerland. Attention: Only once per file. |  |
| ln++++++ | [VehicleJourney](VehicleJourney.md) | ignored | 1..1 | unknown |  |  |
| +++++++ | Name | ignored | 1..1 | unknown |  |  |
| +++++++ | PrivateCode | ignored | 1..1 | unknown |  |  |
| +++++++ | ShortName | ignored | 1..1 | unknown |  |  |
