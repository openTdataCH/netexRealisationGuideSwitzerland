# CompositeFrame

*Table: CompositeFrame*

| Sub | Element | Usage | Card | Type | Description | Note |
|-----|---------|-------|------|------|-------------|------|
|  | ValidBetween | expected | 1..1 | unknown |  | This defines which timetable year is meant. We don't support partial delivery. |
| + | FromDate | expected | 0..1 | xsd:dateTime | Start date of AVAILABILITY CONDITION. |  |
| + | ToDate | expected | 0..1 | xsd:dateTime | End of AVAILABILITY CONDITION. Date is INCLUSIVE. |  |
|  | Description | optional | 0..1 | MultilingualString |  | A description of the delivery can be provided. |
|  | [FrameDefaults](FrameDefaults.md) | expected | 0..1 | VersionFrameDefaultsStructure |  |  |
|  | frames | mandatory | 0..1 | frames_RelStructure |  |  |
| + | [ResourceFrame](ResourceFrame.md) | expected | 0..* | unknown |  |  |
| + | [SiteFrame](SiteFrame.md) | expected | 0..* | unknown |  |  |
| + | [ServiceFrame](ServiceFrame.md) | expected | 0..* | unknown |  |  |
| + | [ServiceCalendarFrame](ServiceCalendarFrame.md) | expected | 0..* | unknown |  |  |
| + | [TimetableFrame](TimetableFrame.md) | expected | 0..* | unknown |  |  |
