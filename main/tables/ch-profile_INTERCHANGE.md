# ch-profile_INTERCHANGE

*Table: PublicationDelivery*

| Sub | Element | Usage | Card | Type | Description | Note |
|-----|---------|-------|------|------|-------------|------|
|  | PublicationTimestamp | mandatory | 1..1 | xsd:dateTime |  |  |
|  | ParticipantRef | mandatory | 1..1 | siri:ParticipantCodeType |  |  |
|  | dataObjects | mandatory | 0..1 | dataObjects |  |  |
| + | CompositeFrame | mandatory | 1..* | unknown |  |  |
| ++ | ValidBetween | expected | 1..1 | unknown |  | This defines which timetable year is meant. We don't support partial delivery. |
| +++ | FromDate | expected | 0..1 | xsd:dateTime | Start date of AVAILABILITY CONDITION. |  |
| +++ | ToDate | expected | 0..1 | xsd:dateTime | End of AVAILABILITY CONDITION. Date is INCLUSIVE. |  |
| ++ | Description | optional | 0..1 | MultilingualString |  | A description of the delivery can be provided. |
| ++ | [FrameDefaults](FrameDefaults.md) | expected | 0..1 | VersionFrameDefaultsStructure |  |  |
| ++ | frames | mandatory | 0..1 | frames_RelStructure |  |  |
| +++ | [ServiceCalendarFrame](ServiceCalendarFrame.md) | mandatory | 1..1 | unknown |  | Needed for the relevant AvailabilityConditions |
| +++ | TimetableFrame | mandatory | 1..1 | unknown |  |  |
| +++++ | [ServiceJourneyInterchange](ServiceJourneyInterchange.md) | mandatory | 1..1 | unknown |  |  |
| +++++ | InterchangeRule | mandatory | 1..1 | unknown |  |  |
