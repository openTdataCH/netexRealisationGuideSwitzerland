# DayTypeAssignment

| Sub | Element | Usage | Card | Type | Description | Note |
|-----|---------|-------|------|------|-------------|------|
|  | DayTypeAssignment | expected | 1..1 | unknown | Associates a DAY TYPE with an OPERATING DAY within a specific Calendar. A specification of a particular DAY TYPE which will be valid during a TIME BAND on an OPERATING DAY. | We currently use DayType to store the national holidays. |
| + | Date | mandatory | 0..1 | xsd:date | Date of the review |  |
| + | DayTypeRef | mandatory | 1..* | DayTypeRefStructure | The DAY TYPE of all the services in this group. |  |
