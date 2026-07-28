# ch-profile_NETWORK_OFFER

*Table: PublicationDelivery*

| Sub | Element | Usage | Card | Type | Description | Note |
|-----|---------|-------|------|------|-------------|------|
|  | PublicationTimestamp | mandatory | 1..1 | xsd:dateTime |  |  |
|  | ParticipantRef | mandatory | 1..1 | siri:ParticipantCodeType |  |  |
|  | dataObjects | mandatory | 0..1 | dataObjects |  |  |
| + | CompositeFrame | mandatory | 0..* | unknown |  |  |
| ++ | ValidBetween | expected | 1..1 | unknown |  | This defines which timetable year is meant. We don't support partial delivery. |
| +++ | FromDate | expected | 0..1 | xsd:dateTime | Start date of AVAILABILITY CONDITION. |  |
| +++ | ToDate | expected | 0..1 | xsd:dateTime | End of AVAILABILITY CONDITION. Date is INCLUSIVE. |  |
| ++ | Description | optional | 0..1 | MultilingualString |  | A description of the delivery can be provided. |
| ++ | [FrameDefaults](FrameDefaults.md) | expected | 0..1 | VersionFrameDefaultsStructure |  |  |
| ++ | frames | mandatory | 0..1 | frames_RelStructure |  |  |
| +++ | [ResourceFrame](ResourceFrame.md) | mandatory | 0..* | unknown |  |  |
| +++ | [SiteFrame](SiteFrame.md) | optional | 0..* | unknown |  | Only for elements that are NOT in the SITE_OFFER and only during importation. |
| +++ | [ServiceFrame](ServiceFrame_NETWORK_OFFER.xml.md) | mandatory | 0..* | unknown |  | Doesn't contain DefaultConnection and SiteConnection. |
| +++ | [ServiceCalendarFrame](ServiceCalendarFrame.md) | mandatory | 0..* | unknown |  |  |
| +++ | [TimetableFrame](TimetableFrame.md) | mandatory | 0..* | unknown |  |  |
