# ch-profile_SITE_OFFER

*Table: PublicationDelivery*

| Sub | Element | Usage | Card | Type | Description | Note |
|-----|---------|-------|------|------|-------------|------|
|  | PublicationTimestamp | mandatory | 1..1 | xsd:dateTime |  |  |
|  | ParticipantRef | mandatory | 1..1 | siri:ParticipantCodeType |  | Use here a distinctive name |
|  | dataObjects | mandatory | 0..1 | dataObjects |  |  |
| + | CompositeFrame | mandatory | 0..* | unknown |  |  |
| ++ | ValidBetween | expected | 1..1 | unknown |  | This defines which timetable year is meant. We don't support partial delivery. |
| +++ | FromDate | expected | 0..1 | xsd:dateTime | Start date of AVAILABILITY CONDITION. |  |
| +++ | ToDate | expected | 0..1 | xsd:dateTime | End of AVAILABILITY CONDITION. Date is INCLUSIVE. |  |
| ++ | Description | optional | 0..1 | MultilingualString |  | A description of the delivery can be provided. |
| ++ | [FrameDefaults](FrameDefaults.md) | expected | 0..1 | VersionFrameDefaultsStructure |  |  |
| ++ | frames | mandatory | 0..1 | frames_RelStructure |  |  |
| +++ | [ResourceFrame](ResourceFrame.md) | expected | 0..* | unknown |  | Only if we really need it |
| +++ | [SiteFrame](SiteFrame.md) | mandatory | 0..* | unknown |  |  |
| +++ | [ServiceCalendarFrame](ServiceCalendarFrame.md) | mandatory | 0..* | unknown |  | Needed for the relevant AvailabilityConditions |
| +++ | [ServiceFrame](ServiceFrame_SITE_OFFER.xml.md) | expected | 0..* | unknown |  | Used for DefaultConnections and SiteConnections |
