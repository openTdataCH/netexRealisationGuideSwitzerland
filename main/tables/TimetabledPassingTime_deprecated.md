# TimetabledPassingTime_deprecated

Long-term planned time data concerning public transport vehicles passing a particular POINT IN JOURNEY PATTERN on a specified VEHICLE JOURNEY for a certain DAY TYPE.

*Table: TimetabledPassingTime*

| Sub | Element | Usage | Card | Type | Description | Note |
|-----|---------|-------|------|------|-------------|------|
|  | @id | mandatory | 1..1 | xsd:string | Attribute id | |
|  | @version | mandatory | 1..1 | xsd:string | Attribute version | |
| + | CheckConstraint | optional | 1..1 | unknown |  |  |
| + | IsFlexible | optional | 0..1 | xsd:boolean |  |  |
|  | AlightAndReboard | optional | 0..1 | xsd:boolean |  |  |
|  | StopPointInJourneyPatternRef | mandatory | 1..1 | StopPointInJourneyPatternRefStructure |  |  |
|  | ArrivalTime | expected | 0..1 | xsd:time | Timetabled Arrival time. | Not used if departure only. |
|  | ArrivalDayOffset | optional | 0..1 | DayOffsetType | Arrival Day Offset from Start of Journey. |  |
|  | DepartureTime | expected | 0..1 | xsd:time | Timetabled departure time. | Not used if arrival only. |
|  | DepartureDayOffset | optional | 0..1 | DayOffsetType | Number of days after the starting departure time of the journey if not same calendar day. Default is 0 for same day. |  |
|  | WaitingTime | optional | 0..1 | xsd:duration | Timetabled waiting interval. |  |
|  | LatestArrivalTime | optional | 0..1 | xsd:time |  |  |
|  | LatestArrivalDayOffset | optional | 0..1 | DayOffsetType |  |  |
|  | EarliestDepartureTime | optional | 0..1 | xsd:time |  |  |
|  | EarliestDepartureDayOffset | optional | 0..1 | DayOffsetType |  |  |
