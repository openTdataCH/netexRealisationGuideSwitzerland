# AvailabilityCondition

| Sub | Element | Usage | Card | Type | Description | Note |
|-----|---------|-------|------|------|-------------|------|
| + | FromDate | optional | 0..1 | xsd:dateTime | Start date of AVAILABILITY CONDITION. | Is equal to the start date of the timetable year or, more generally, the period in which the ValidDayBits apply. |
| + | ToDate | optional | 0..1 | xsd:dateTime | End of AVAILABILITY CONDITION. Date is INCLUSIVE. | Is equal to the end date of the timetable year or, more generally, the period in which the ValidDayBits apply. |
| + | ValidDayBits | mandatory | 0..1 | xsd:normalizedString | For UIC style encoding of day types String of bits, one for each day in period: whether valid or not valid on the day. Normally there will be a bit for every day between start and end date. If bit is missing, assume available. |  |
| + | timebands | optional | 0..1 | timebandRefs_RelStructure | TIMEBANDS associated with JOURNEY FREQUENCY GROUP. | Can also be referenced |
| ++ | [Timeband](Timeband.md) | optional | 1..1 | unknown | A period in a day, significant for some aspect of public transport, e.g. similar traffic conditions or fare category. |  |
| ++ | TimebandRef | optional | 1..1 | TimebandRefStructure | Reference to a TIME BAND. |  |
