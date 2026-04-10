# ServiceJourney

| Sub | Element | Usage | Card | Type | Description | Note |
|-----|---------|-------|------|------|-------------|------|
|  | PublicationDelivery | ignored | 1..1 | PublicationDeliveryStructure | A set of NeTEx objects as assembled by a publication request or other service. Provides a general purpose wrapper for NeTEx data content. |  |
| + | ParticipantRef | ignored | 1..1 | siri:ParticipantCodeType | Identifier of system requesting Data. |  |
| + | PublicationTimestamp | ignored | 1..1 | xsd:dateTime | Time of output of data. |  |
| + | dataObjects | ignored | 1..1 | unknown |  |  |
| ++ | CompositeFrame | ignored | 1..1 | unknown |  |  |
| +++ | frames | ignored | 1..1 | unknown |  |  |
| ++++ | TimetableFrame | ignored | 1..1 | unknown |  |  |
| +++++ | vehicleJourneys | ignored | 1..1 | unknown |  |  |
| ++++++ | ServiceJourney | ignored | 1..1 | unknown |  |  |
| +++++++ | DepartureTime | ignored | 1..1 | unknown |  |  |
| +++++++ | DirectionType | ignored | 1..1 | unknown |  |  |
| +++++++ | Extensions | ignored | 1..1 | unknown |  |  |
| +++++++ | LineRef | mandatory | 1..1 | unknown |  |  |
| +++++++ | PrivateCode | ignored | 1..1 | unknown |  |  |
| +++++++ | ServiceAlteration | ignored | 1..1 | unknown |  |  |
| +++++++ | TransportMode | ignored | 1..1 | unknown |  |  |
| +++++++ | TypeOfProductCategoryRef | ignored | 1..1 | unknown |  |  |
| +++++++ | TypeOfServiceRef | ignored | 1..1 | unknown |  |  |
| +++++++ | keyList | ignored | 1..1 | unknown |  |  |
| +++++++ | noticeAssignments | ignored | 1..1 | unknown |  |  |
| +++++++ | passingTimes | ignored | 1..1 | unknown |  |  |
| +++++++ | trainNumbers | ignored | 1..1 | unknown |  |  |
| +++++++ | validityConditions | ignored | 1..1 | unknown |  |  |
| ++++++++ | AvailabilityCondition | ignored | 1..1 | unknown |  |  |
| ++++++++ | KeyValue | ignored | 1..1 | unknown |  |  |
| ln++++++++ | [NoticeAssignment](NoticeAssignment.md) | ignored | 1..1 | unknown |  |  |
| ln++++++++ | [TimetabledPassingTime](TimetabledPassingTime.md) | ignored | 1..1 | unknown |  |  |
| ++++++++ | TrainNumberRef | mandatory | 1..1 | unknown |  |  |
| ++++++++ | facilities | ignored | 1..1 | unknown |  |  |
| +++++++++ | Facility | ignored | 1..1 | unknown |  |  |
| +++++++++ | FromDate | mandatory | 1..1 | unknown |  |  |
| +++++++++ | Key | ignored | 1..1 | unknown |  |  |
| +++++++++ | ToDate | mandatory | 1..1 | unknown |  |  |
| +++++++++ | ValidDayBits | mandatory | 1..1 | unknown |  |  |
| +++++++++ | Value | ignored | 1..1 | unknown |  |  |
| +++++++++ | timebands | ignored | 1..1 | unknown |  |  |
| ++++++++++ | ServiceFacilitySetRef | ignored | 1..1 | unknown |  |  |
| ln++++++++++ | [Timeband](Timeband.md) | ignored | 1..1 | unknown |  |  |
