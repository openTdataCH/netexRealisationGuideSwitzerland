# OccupancyView

| Sub | Element | Usage | Card | Type | Description | Note |
|-----|---------|-------|------|------|-------------|------|
| + | dayTypeRefs | optional | 0..1 | unknown | DAY TYPEs for BLOCK. |  |
| ++ | DayTypeRef | optional | 1..* | DayTypeRefStructure | The DAY TYPE of all the services in this group. | **TODO** Profile should be clear about DayType vs. DayTypeRef usage |
| + | dayTypes | expected | 0..1 | unknown | DAY TYPEs for BLOCK. | **TODO** Superfluous? DAY TYPEs should be the same as for the VEHICLE JOURNEY. |
| ++ | [DayType](DayType.md) | expected | 1..1 | unknown | A type of day characterized by one or more properties which affect public transport operation. For example: weekday in school holidays. |  |
| + | FareClass | expected | 0..1 | FareClassEnumeration | Fare class in VEHICLE for which occupancy or capacities are specified. |  |
| + | OccupancyLevel | expected | 0..1 | OccupancyEnumeration | An approximate figure of how occupied or full a VEHICLE and its parts are, e.g. 'manySeatsAvailable' or 'standingRoomOnly'.  
More accurate data can be provided by the individual occupancies or capacities below. | Niedrige Belegung: empty; mittlere Belegung: manySeatsAvailable; hohe Belegung: fewSeatsAvailable |
| + | GroupReservation | optional | 0..* | GroupReservationStructure | Reservations of travel groups, i.e., name of group and number of seats booked. |  |
| ++ | NameOfGroup | expected | 1..1 | MultilingualString | Name for which the travel group has made the reservation. |  |
| ++ | NumberOfReservedSeats | expected | 1..1 | NumberOfPassengers | Number of seats that the group has booked. |  |
