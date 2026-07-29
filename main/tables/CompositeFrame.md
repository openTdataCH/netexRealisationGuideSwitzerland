# CompositeFrame

*Table: CompositeFrame*

| Sub | Element | Usage | Card | Type | Description | Note |
|-----|---------|-------|------|------|-------------|------|
|  | ValidBetween | expected | 1..1 | unknown |  | This defines which timetable year is meant. We don't support partial delivery. |
| + | FromDate | expected | 0..1 | xsd:dateTime | Start date of AVAILABILITY CONDITION. |  |
| + | ToDate | expected | 0..1 | xsd:dateTime | End of AVAILABILITY CONDITION. Date is INCLUSIVE. |  |
|  | Description | optional | 0..1 | MultilingualString |  | A description of the delivery can be provided. |
|  | [FrameDefaults](FrameDefaults.md) | expected | 0..1 | VersionFrameDefaultsStructure | Default values to use on elements in the frame that do not explicitly state a value. |  |
|  | frames | mandatory | 0..1 | frames_RelStructure | Content frames in COMPOSITE FRAME. |  |
| + | [ResourceFrame](ResourceFrame.md) | expected | 0..* | frames_RelStructure | Content frames in COMPOSITE FRAME. |  |
| + | [SiteFrame](SiteFrame.md) | expected | 0..* | frames_RelStructure | Content frames in COMPOSITE FRAME. |  |
| + | [ServiceFrame](ServiceFrame.md) | expected | 0..* | frames_RelStructure | Content frames in COMPOSITE FRAME. |  |
| + | [ServiceCalendarFrame](ServiceCalendarFrame.md) | expected | 0..* | frames_RelStructure | Content frames in COMPOSITE FRAME. |  |
| + | [TimetableFrame](TimetableFrame.md) | expected | 0..* | frames_RelStructure | Content frames in COMPOSITE FRAME. |  |
