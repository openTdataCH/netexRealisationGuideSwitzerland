# TimetabledPassingTime_deprecated

Long-term planned time data concerning public transport vehicles passing a particular POINT IN JOURNEY PATTERN on a specified VEHICLE JOURNEY for a certain DAY TYPE.

*Table: TimetabledPassingTime*

| Sub | Element | Usage | Card | Type | Description | Note |
|-----|---------|-------|------|------|-------------|------|
|  | @id | mandatory | 1..1 | xsd:string | Attribute id | |
|  | @version | mandatory | 1..1 | xsd:string | Attribute version | |
| + | CheckConstraint | optional | 1..1 | unknown | A coherent set of timetable data (VEHICLE JOURNEYs and BLOCKs) to which the same VALIDITY CONDITIONs have been assigned. |  |
| + | IsFlexible | optional | 0..1 | xsd:boolean | A coherent set of timetable data (VEHICLE JOURNEYs and BLOCKs) to which the same VALIDITY CONDITIONs have been assigned. |  |
|  | AlightAndReboard | optional | 0..1 | xsd:boolean | A coherent set of timetable data (VEHICLE JOURNEYs and BLOCKs) to which the same VALIDITY CONDITIONs have been assigned. |  |
|  | StopPointInJourneyPatternRef | mandatory | 1..1 | StopPointInJourneyPatternRefStructure | A coherent set of timetable data (VEHICLE JOURNEYs and BLOCKs) to which the same VALIDITY CONDITIONs have been assigned. |  |
|  | ArrivalTime | expected | 0..1 | xsd:time | A coherent set of timetable data (VEHICLE JOURNEYs and BLOCKs) to which the same VALIDITY CONDITIONs have been assigned. | Not used if departure only. |
|  | ArrivalDayOffset | optional | 0..1 | DayOffsetType | A coherent set of timetable data (VEHICLE JOURNEYs and BLOCKs) to which the same VALIDITY CONDITIONs have been assigned. |  |
|  | DepartureTime | expected | 0..1 | xsd:time | A coherent set of timetable data (VEHICLE JOURNEYs and BLOCKs) to which the same VALIDITY CONDITIONs have been assigned. | Not used if arrival only. |
|  | DepartureDayOffset | optional | 0..1 | DayOffsetType | A coherent set of timetable data (VEHICLE JOURNEYs and BLOCKs) to which the same VALIDITY CONDITIONs have been assigned. |  |
|  | WaitingTime | optional | 0..1 | xsd:duration | A coherent set of timetable data (VEHICLE JOURNEYs and BLOCKs) to which the same VALIDITY CONDITIONs have been assigned. |  |
|  | LatestArrivalTime | optional | 0..1 | xsd:time | A coherent set of timetable data (VEHICLE JOURNEYs and BLOCKs) to which the same VALIDITY CONDITIONs have been assigned. |  |
|  | LatestArrivalDayOffset | optional | 0..1 | DayOffsetType | A coherent set of timetable data (VEHICLE JOURNEYs and BLOCKs) to which the same VALIDITY CONDITIONs have been assigned. |  |
|  | EarliestDepartureTime | optional | 0..1 | xsd:time | A coherent set of timetable data (VEHICLE JOURNEYs and BLOCKs) to which the same VALIDITY CONDITIONs have been assigned. |  |
|  | EarliestDepartureDayOffset | optional | 0..1 | DayOffsetType | A coherent set of timetable data (VEHICLE JOURNEYs and BLOCKs) to which the same VALIDITY CONDITIONs have been assigned. |  |
