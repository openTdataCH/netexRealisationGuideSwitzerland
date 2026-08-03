# Journeys passing midnight

## Case 1: Journey start belongs to the previous OperatingDay

The time format consists only of the hour, minutes (and seconds) of a 24-hour
clock, e.g. '23:55:00'. If a `ServiceJourney`'s `DepartureTime` falls after
midnight but the journey still belongs to the previous day's schedule (e.g.
the last-mile S1 departing at 00:11, counted as part of yesterday's service),
`DepartureDayOffset` must be set to `1`.

## Case 2: Journey crosses midnight during its course

`TimeDemandType`/`TimingLink` hold only relative durations (`RunTime`,
`WaitTime`) — there is no per-stop `DayOffset` element in this model. Consequently, a midnight
crossing partway through a journey is not explicitly flagged anywhere — it
follows implicitly from cumulating `DepartureTime` with the `RunTime`/`WaitTime`
values of the `TimeDemandType`. No additional element is needed or available
for this case.
