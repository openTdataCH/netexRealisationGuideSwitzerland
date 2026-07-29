# ch-profile_INTERCHANGE

*Table: PublicationDelivery*

| Sub | Element | Usage | Card | Type | Description | Note |
|-----|---------|-------|------|------|-------------|------|
|  | PublicationTimestamp | mandatory | 1..1 | xsd:dateTime | Time of output of data. |  |
|  | ParticipantRef | mandatory | 1..1 | siri:ParticipantCodeType | Identifier of system requesting Data. |  |
|  | dataObjects | mandatory | 0..1 | dataObjects |  |  |
| + | CompositeFrame | mandatory | 0..* | unknown |  |  |
| ++ | ValidBetween | expected | 0..1 | unknown | NeTEx Entities of any type. | This defines which timetable year is meant. We don't support partial delivery. |
| +++ | FromDate | expected | 0..1 | xsd:dateTime | Start date of AVAILABILITY CONDITION. |  |
| +++ | ToDate | expected | 0..1 | xsd:dateTime | End of AVAILABILITY CONDITION. Date is INCLUSIVE. |  |
| ++ | Description | optional | 0..1 | MultilingualString | NeTEx Entities of any type. | A description of the delivery can be provided. |
| ++ | [FrameDefaults](FrameDefaults.md) | expected | 0..1 | VersionFrameDefaultsStructure | NeTEx Entities of any type. |  |
| ++ | frames | mandatory | 0..1 | frames_RelStructure | NeTEx Entities of any type. |  |
| +++ | [ServiceCalendarFrame](ServiceCalendarFrame.md) | mandatory | 0..* | unknown | NeTEx Entities of any type. | Needed for the relevant AvailabilityConditions |
| +++ | TimetableFrame | mandatory | 0..* | unknown | NeTEx Entities of any type. |  |
| +++++ | [ServiceJourneyInterchange](ServiceJourneyInterchange.md) | mandatory | 0..1 | unknown | NeTEx Entities of any type. |  |
| +++++ | InterchangeRule | mandatory | 0..1 | unknown | NeTEx Entities of any type. |  |
