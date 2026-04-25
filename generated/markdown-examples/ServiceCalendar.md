# ServiceCalendar

| Sub | Element | Usage | Card | Type | Description | Note |
|-----|---------|-------|------|------|-------------|------|
|  | ServiceCalendar | expected | 1..1 | unknown | A SERVICE CALENDAR. A collection of DAY TYPE ASSIGNMENTs. |  |
| + | Name | mandatory | 0..1 | MultilingualString | Name of Traveller | timetable year |
| + | FromDate | mandatory | 0..1 | xsd:dateTime | Start date of AVAILABILITY CONDITION. | Beginning of timetable year |
| + | ToDate | mandatory | 0..1 | xsd:dateTime | End of AVAILABILITY CONDITION. Date is INCLUSIVE. | End of timetable year |
