# TimetabledPassingTime

| Sub | Element | Usage | Card | Type | Description | Note |
|-----|---------|-------|------|------|-------------|------|
| + | PointInJourneyPatternRef | mandatory | 0..1 | PointInJourneyPatternRefStructure | Point in JOURNEY PATTERN upon which this DEAD RUN CALL is based. Can be used to obtain full association sets. |  |
| + | AlightAndReboard | optional | 0..1 | xsd:boolean | Whether can alight and reboard at stop. |  |
| + | ArrivalTime | expected | 0..1 | xsd:time | Timetabled Arrival time. | Not used if departure only. |
| + | ArrivalDateOffset | optional | 1..1 | unknown |  |  |
| + | DepartureTime | expected | 0..1 | xsd:time | Departure time. | Not used if arrival only. |
| + | DepartureDateOffset | optional | 1..1 | unknown |  |  |
| + | WaitingTime | optional | 0..1 | xsd:duration | Timetabled waiting interval. |  |
| + | LatestArrivalTime | optional | 0..1 | xsd:time | Latest Arrival Time. |  |
| + | LatestArrivalDayOffset | optional | 0..1 | DayOffsetType | Number of days after the starting time of the journey if not same calendar day. Default is 0 for same day. |  |
| + | EarliestDepartureTime | optional | 0..1 | xsd:time | Earliest Timetabled departure time. |  |
| + | EarliestDepartureDayOffset | optional | 0..1 | DayOffsetType | Number of days after the starting time of the journey if not same calendar day. Default is 0 for same day. |  |
| + | CheckConstraint | optional | 1..1 | None | Characteristics of a SITE COMPONENT representing a process, such as check-in, security
screening, ticket control or immigration, that may potentially incur a time penalty that should be allowed for when journey planning. Used to mark PATH LINKs to determine transit routes through interchanges. | **TODO - Planned for V2.1** Allows for specifying delays due to longer boarding times. |
| + | IsFlexible | optional | 0..1 | xsd:boolean | Whether use of stop is flexible, i.e. requires phoning to arrange. Must be a FLEXIBLE LINE. Default is false. | **TODO - Planned for V2.1** Stop is only served upon prior request (e.g., booking by phone). |
| + | occupancies | optional | 0..1 | OccupancyView_RelStructure | OCCUPANCYs associated with this journey. +v2.0 |  |
| ++ | [OccupancyView](OccupancyView.md) | optional | 1..1 | OccupancyView_VersionStructure |  |  |
