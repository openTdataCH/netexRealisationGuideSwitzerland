# TimetabledPassingTime_deprecated

Long-term planned time data concerning public transport vehicles passing a particular POINT IN JOURNEY PATTERN on a specified VEHICLE JOURNEY for a certain DAY TYPE.

*Table: TimetabledPassingTime*

| Sub | Element | Usage | Card | Type | Description | Note |
|-----|---------|-------|------|------|-------------|------|
|  | @id | mandatory | 1..1 | xsd:string | Attribute id | |
|  | @version | mandatory | 1..1 | xsd:string | Attribute version | |
| + | CheckConstraint | optional | 1..1 | unknown |  |  |
| + | IsFlexible | optional | 0..1 | xsd:boolean |  |  |
|  | AlightAndReboard | optional | 0..1 | boolean | Whether can alight and reboard at stop. |  |
|  | StopPointInJourneyPatternRef | mandatory | 1..1 | StopPointInJourneyPatternRefStructure | +v2.1 |  |
|  | ArrivalTime | expected | 0..1 | time | Timetabled arrival time. | Not used if departure only. |
|  | ArrivalDayOffset | optional | 0..1 | DayOffsetType | Number of days after the starting time of the journey if not same calendar day. Default is 0 for same day. |  |
|  | DepartureTime | expected | 0..1 | time | Timetabled departure time. | Not used if arrival only. |
|  | DepartureDayOffset | optional | 0..1 | DayOffsetType | Number of days after the starting time of the journey if not same calendar day. Default is 0 for same day. |  |
|  | WaitingTime | optional | 0..1 | duration | Timetabled waiting interval. |  |
|  | LatestArrivalTime | optional | 0..1 | time | Latest Arrival Time. |  |
|  | LatestArrivalDayOffset | optional | 0..1 | DayOffsetType | Number of days after the starting time of the journey if not same calendar day. Default is 0 for same day. |  |
|  | EarliestDepartureTime | optional | 0..1 | time | Earliest Timetabled departure time. |  |
|  | EarliestDepartureDayOffset | optional | 0..1 | DayOffsetType | Number of days after the starting time of the journey if not same calendar day. Default is 0 for same day. |  |
