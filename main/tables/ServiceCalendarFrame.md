# ServiceCalendarFrame

A minimal ServiceCalendarFrame must be present in all timetable files.

*Table: ServiceCalendarFrame*

| Sub | Element | Usage | Card | Type | Description | Note |
|-----|---------|-------|------|------|-------------|------|
|  | @id | mandatory | 1..1 | xsd:string | Attribute id | |
|  | @version | mandatory | 1..1 | xsd:string | Attribute version | |
|  | validityConditions | mandatory | 1..1 | validityConditions_RelStructure |  |  |
| + | [AvailabilityCondition](AvailabilityCondition.md) | mandatory | 0..* | unknown |  | Our main mechanism for validity and operating days |
|  | [ServiceCalendar](ServiceCalendar.md) | expected | 1..1 | unknown |  | We only have one ServiceCalendar for the whole timetable year. It is not referenced. |
|  | dayTypes | optional | 0..1 | unknown |  |  |
| + | [DayType](DayType.md) | optional | 1..1 | unknown |  | Used for holidays only |
|  | timebands | expected | 0..1 | timebandRefs_RelStructure |  |  |
| + | [Timeband](Timeband.md) | expected | 0..* | unknown |  | Mainly used for frequency-based lines. |
|  | dayTypeAssignments | optional | 0..1 | dayTypeAssignments_RelStructure |  |  |
| + | [DayTypeAssignment](DayTypeAssignment.md) | optional | 0..* | unknown | An operating period. | Used for holidays only |
