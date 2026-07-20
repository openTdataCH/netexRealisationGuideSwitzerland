# ServiceCalendarFrame

A minimal ServiceCalendarFrame must be present in all timetable files.

*Table: ServiceCalendarFrame*

| Sub | Element | Usage | Card | Type | Description | Note |
|-----|---------|-------|------|------|-------------|------|
|  | @id | mandatory | 1..1 | xsd:string | Attribute id | |
|  | @version | mandatory | 1..1 | xsd:string | Attribute version | |
|  | validityConditions | mandatory | 1..1 | validityConditions_RelStructure | VALIDITY CONDITIONs conditioning entity. |  |
| + | [AvailabilityCondition](AvailabilityCondition.md) | mandatory | 1..* | AvailabilityCondition | VALIDITY CONDITION stated in terms of DAY TYPES and PROPERTIES OF DAYs. | Our main mechanism for validity and operating days |
|  | [ServiceCalendar](ServiceCalendar.md) | expected | 1..1 | ServiceCalendar | A SERVICE CALENDAR. A collection of DAY TYPE ASSIGNMENTs. | We only have one ServiceCalendar for the whole timetable year. It is not referenced. |
|  | dayTypes | optional | 0..1 | dayTypeRefs_RelStructure | DAY TYPEs for BLOCK. |  |
| + | [DayType](DayType.md) | optional | 1..1 | DayType | A type of day characterized by one or more properties which affect public transport operation. For example: weekday in school holidays. | Used for holidays only |
|  | timebands | expected | 0..1 | timebandRefs_RelStructure | TIMEBANDS associated with JOURNEY FREQUENCY GROUP. |  |
| + | [Timeband](Timeband.md) | expected | 1..* | Timeband_VersionedChildStructure | A period in a day, significant for some aspect of public transport, e.g. similar traffic conditions or fare category. | Mainly used for frequency-based lines. |
|  | dayTypeAssignments | optional | 0..1 | dayTypeAssignments_RelStructure | Assignments of DAY TYPEs to specific OPERATING DAYs. The same DAY TYPE may be assigned to multiple Operating dates, and vice versa. |  |
| + | [DayTypeAssignment](DayTypeAssignment.md) | optional | 1..* | DayTypeAssignment | Associates a DAY TYPE with an OPERATING DAY within a specific Calendar. A specification of a particular DAY TYPE which will be valid during a TIME BAND on an OPERATING DAY. | Used for holidays only |
