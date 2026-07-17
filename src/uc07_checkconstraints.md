# CheckConstraints

Check constraints are very broad elements within NeTEx. A lot of things can be expressed with it.
In Switzerland, we use the following use cases:
- Special delays in alighting or boarding.
- Doors closed already before departure.
- Waiting times (e.g. for carTransportRail and touristic offers)

CheckConstraints can apply while boarding or alighting.

We can have `CheckConstraint`s on [`ServiceJourney`](09_timetable.md#servicejourney) and [`ServiceJourneyPattern`](07_service.md#servicejourneypattern)
