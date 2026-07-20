# DayTypeAssignment

We currently use DayType to store the national holidays.

*Table: DayTypeAssignment*

| Sub | Element | Usage | Card | Type | Description | Note |
|-----|---------|-------|------|------|-------------|------|
|  | @id | mandatory | 1..1 | xsd:string | Attribute id | |
|  | @version | mandatory | 1..1 | xsd:string | Attribute version | |
|  | Date | mandatory | 0..1 | xsd:date | Date of the review |  |
|  | DayTypeRef | mandatory | 1..* | DayTypeRefStructure | The DAY TYPE of all the services in this group. |  |
