# CompositeFrame

*Table: CompositeFrame*

| Sub | Element | Usage | Card | Type | Description | Note |
|-----|---------|-------|------|------|-------------|------|
|  | ValidBetween | expected | 1..1 | ValidBetween | OPTIMISATION. Simple version of a VALIDITY CONDITION. Comprises a simple period. NO UNIQUENESS CONSTRAINT. | This defines which timetable year is meant. We don't support partial delivery. |
| + | FromDate | expected | 0..1 | xsd:dateTime | Start date of AVAILABILITY CONDITION. |  |
| + | ToDate | expected | 0..1 | xsd:dateTime | End of AVAILABILITY CONDITION. Date is INCLUSIVE. |  |
|  | Description | optional | 0..* | MultilingualString | Description of contents. | A description of the delivery can be provided. |
|  | [FrameDefaults](FrameDefaults.md) | expected | 0..1 | VersionFrameDefaultsStructure | Default values to use on elements in the frame that do not explicitly state a value. |  |
|  | frames | mandatory | 0..1 | frames_RelStructure | Content frames in COMPOSITE FRAME. |  |
| + | [ResourceFrame](ResourceFrame.md) | expected | 1..1 | ResourceFrame | A coherent set of reference values for TYPE OF VALUEs , ORGANISATIONs, VEHICLE TYPEs etc that have a common validity, as specified by a set of frame VALIDITY CONDITIONs. Used to define common resources that will be referenced by other types of FRAME. |  |
| + | [SiteFrame](SiteFrame.md) | expected | 1..1 | SiteFrame | A coherent set of SITE data to which the same frame VALIDITY CONDITIONs have been assigned. |  |
| + | [ServiceFrame](ServiceFrame.md) | expected | 1..1 | ServiceFrame | A coherent set of Service data to which the same frame VALIDITY CONDITIONs have been assigned. |  |
| + | [ServiceCalendarFrame](ServiceCalendarFrame.md) | expected | 1..1 | ServiceCalendarFrame | A SERVICE CALENDAR. A coherent set of OPERATING DAYS and DAY TYPES comprising a Calendar. That may be used to state the temporal VALIDITY of other NeTEx entities such as Timetables, STOP PLACEs, etc. Covers a PERIOD with a collection of assignments of OPERATING DAYS to DAY TYPES. |  |
| + | [TimetableFrame](TimetableFrame.md) | expected | 1..1 | TimetableFrame | A coherent set of timetable data (VEHICLE JOURNEYs and BLOCKs) to which the same VALIDITY CONDITIONs have been assigned. |  |
