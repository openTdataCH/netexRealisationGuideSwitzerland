# OccupancyView

*Table: OccupancyView*

| Sub | Element | Usage | Card | Type | Description | Note |
|-----|---------|-------|------|------|-------------|------|
|  | @id | mandatory | 1..1 | xsd:string | Attribute id | |
|  | @version | mandatory | 1..1 | xsd:string | Attribute version | |
|  | dayTypeRefs | optional | 0..1 | dayTypeRefs_RelStructure | DAY TYPEs for BLOCK. |  |
| + | DayTypeRef | optional | 1..* | DayTypeRefStructure | Reference to a DAY TYPE. |  |
|  | dayTypes | expected | 0..1 | dayTypesInFrame_RelStructure | Reusable DAY TYPE in SERVICE CALENDAR FRAME. |  |
| + | [DayType](DayType.md) | expected | 1..1 | DayType_VersionStructure | A type of day characterized by one or more properties which affect public transport operation. For example: weekday in school holidays. |  |
|  | FareClass | expected | 0..1 | FareClassEnumeration | Fixed class associated with this CLASS OF USE. |  |
|  | OccupancyLevel | expected | 0..1 | OccupancyEnumeration | An approximate figure of how occupied or full a VEHICLE and its parts are, e.g. 'manySeatsAvailable' or 'standingRoomOnly'. More accurate data can be provided by the individual occupancies or capacities below. | Niedrige Belegung: empty; mittlere Belegung: manySeatsAvailable; hohe Belegung: fewSeatsAvailable |
|  | GroupReservation | optional | 0..* | GroupReservationStructure | Reservations of travel groups, i.e., name of group and number of seats booked. |  |
| + | NameOfGroup | expected | 1..1 | MultilingualString | Name for which the travel group has made the reservation. |  |
| + | NumberOfReservedSeats | expected | 1..1 | NumberOfPassengers | Number of seats that the group has booked. |  |
