# TimetabledPassingTime

| Sub | Element | Usage | Card | Type | Description | Note |
|-----|---------|-------|------|------|-------------|------|
| ++ | CheckConstraint | optional | 1..1 | unknown | Characteristics of a SITE COMPONENT representing a process, such as check-in, security
screening, ticket control or immigration, that may potentially incur a time penalty that should be allowed for when journey planning. Used to mark PATH LINKs to determine transit routes through interchanges. | **TODO - Planned for V2.1** Allows for specifying delays due to longer boarding times. |
| ++ | IsFlexible | optional | 0..1 | xsd:boolean | Whether use of stop is flexible, i.e. requires phoning to arrange. Must be a FLEXIBLE LINE. Default is false. | **TODO - Planned for V2.1** Stop is only served upon prior request (e.g., booking by phone). |
| + | AlightAndReboard | optional | 0..1 | xsd:boolean | Whether can alight and reboard at stop. |  |
| + | StopPointInJourneyPatternRef | mandatory | 1..1 | StopPointInJourneyPatternRefStructure | Reference to a STOP POINT IN SEQUENCE. If given by context does not need to be stated. |  |
| + | ArrivalTime | expected | 0..1 | xsd:time | Timetabled Arrival time. | Not used if departure only. |
| + | ArrivalDayOffset | optional | 0..1 | DayOffsetType | Arrival Day Offset from start of JOURNEY. +v1.1 |  |
| + | DepartureTime | expected | 0..1 | xsd:time | Departure time. | Not used if arrival only. |
| + | DepartureDayOffset | optional | 0..1 | DayOffsetType | Departure Time Day Offset. |  |
| + | WaitingTime | optional | 0..1 | xsd:duration | Timetabled waiting interval. |  |
| + | LatestArrivalTime | optional | 0..1 | xsd:time | Latest Arrival Time. |  |
| + | LatestArrivalDayOffset | optional | 0..1 | DayOffsetType | Number of days after the starting time of the journey if not same calendar day. Default is 0 for same day. |  |
| + | EarliestDepartureTime | optional | 0..1 | xsd:time | Earliest Timetabled departure time. |  |
| + | EarliestDepartureDayOffset | optional | 0..1 | DayOffsetType | Number of days after the starting time of the journey if not same calendar day. Default is 0 for same day. |  |
| + | occupancies | optional | 0..1 | OccupancyView_RelStructure | OCCUPANCYs associated with this journey. +v2.0 |  |
| ++ | [OccupancyView](OccupancyView.md) | optional | 1..1 | OccupancyView_VersionStructure |  |  |
