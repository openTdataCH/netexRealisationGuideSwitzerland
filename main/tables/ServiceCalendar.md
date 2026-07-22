# ServiceCalendar

*Table: ServiceCalendar*

| Sub | Element | Usage | Card | Type | Description | Note |
|-----|---------|-------|------|------|-------------|------|
|  | @id | mandatory | 1..1 | xsd:string | Attribute id | |
|  | @version | mandatory | 1..1 | xsd:string | Attribute version | |
|  | Name | expected | 0..* | MultilingualString | Name of Traveller | timetable year |
|  | FromDate | mandatory | 0..1 | xsd:dateTime | Start date of AVAILABILITY CONDITION. | Beginning of timetable year |
|  | ToDate | mandatory | 0..1 | xsd:dateTime | End of AVAILABILITY CONDITION. Date is INCLUSIVE. | End of timetable year |
