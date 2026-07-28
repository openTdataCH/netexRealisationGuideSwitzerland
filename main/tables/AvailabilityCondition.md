# AvailabilityCondition

*Table: AvailabilityCondition*

| Sub | Element | Usage | Card | Type | Description | Note |
|-----|---------|-------|------|------|-------------|------|
|  | @id | mandatory | 1..1 | xsd:string | Attribute id | |
|  | @version | mandatory | 1..1 | xsd:string | Attribute version | |
|  | FromDate | optional | 0..1 | xsd:dateTime |  | Is equal to the start date of the timetable year or, more generally, the period in which the ValidDayBits apply. |
|  | ToDate | optional | 0..1 | xsd:dateTime |  | Is equal to the end date of the timetable year or, more generally, the period in which the ValidDayBits apply. |
|  | ValidDayBits | mandatory | 0..1 | xsd:normalizedString |  |  |
|  | timebands | optional | 0..1 | timebandRefs_RelStructure |  | Can also be referenced |
| + | [Timeband](Timeband.md) | optional | 0..* | unknown |  |  |
| + | TimebandRef | optional | 0..* | TimebandRefStructure |  |  |
