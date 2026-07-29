# ch-profile_SITE_OFFER

*Table: PublicationDelivery*

| Sub | Element | Usage | Card | Type | Description | Note |
|-----|---------|-------|------|------|-------------|------|
|  | PublicationTimestamp | mandatory | 1..1 | xsd:dateTime | Time of output of data. |  |
|  | ParticipantRef | mandatory | 1..1 | siri:ParticipantCodeType | Identifier of system requesting Data. | Use here a distinctive name |
|  | dataObjects | mandatory | 0..1 | dataObjects |  |  |
| + | CompositeFrame | mandatory | 0..* | unknown |  |  |
| ++ | ValidBetween | expected | 0..1 | unknown | NeTEx Entities of any type. | This defines which timetable year is meant. We don't support partial delivery. |
| +++ | FromDate | expected | 0..1 | xsd:dateTime | Start date of AVAILABILITY CONDITION. |  |
| +++ | ToDate | expected | 0..1 | xsd:dateTime | End of AVAILABILITY CONDITION. Date is INCLUSIVE. |  |
| ++ | Description | optional | 0..1 | MultilingualString | NeTEx Entities of any type. | A description of the delivery can be provided. |
| ++ | [FrameDefaults](FrameDefaults.md) | expected | 0..1 | VersionFrameDefaultsStructure | NeTEx Entities of any type. |  |
| ++ | frames | mandatory | 0..1 | frames_RelStructure | NeTEx Entities of any type. |  |
| +++ | [ResourceFrame](ResourceFrame.md) | expected | 0..* | unknown | NeTEx Entities of any type. | Only if we really need it |
| +++ | [SiteFrame](SiteFrame.md) | mandatory | 0..* | unknown | NeTEx Entities of any type. |  |
| +++ | [ServiceCalendarFrame](ServiceCalendarFrame.md) | mandatory | 0..* | unknown | NeTEx Entities of any type. | Needed for the relevant AvailabilityConditions |
| +++ | [ServiceFrame](ServiceFrame_SITE_OFFER.xml.md) | expected | 0..* | unknown | NeTEx Entities of any type. | Used for DefaultConnections and SiteConnections |
