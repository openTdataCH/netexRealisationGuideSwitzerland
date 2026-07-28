# OccupancyView

*Table: OccupancyView*

| Sub | Element | Usage | Card | Type | Description | Note |
|-----|---------|-------|------|------|-------------|------|
|  | @id | mandatory | 1..1 | xsd:string | Attribute id | |
|  | @version | mandatory | 1..1 | xsd:string | Attribute version | |
|  | dayTypeRefs | optional | 0..1 | unknown |  |  |
| + | DayTypeRef | optional | 1..* | DayTypeRefStructure |  |  |
|  | dayTypes | expected | 0..1 | unknown |  |  |
| + | [DayType](DayType.md) | expected | 1..1 | unknown |  |  |
|  | FareClass | expected | 0..1 | FareClassEnumeration |  |  |
|  | OccupancyLevel | expected | 0..1 | OccupancyEnumeration |  | Niedrige Belegung: empty; mittlere Belegung: manySeatsAvailable; hohe Belegung: fewSeatsAvailable |
|  | GroupReservation | optional | 0..* | GroupReservationStructure |  |  |
| + | NameOfGroup | expected | 1..1 | MultilingualString | Name for which the travel group has made the reservation. |  |
| + | NumberOfReservedSeats | expected | 1..1 | NumberOfPassengers | Number of seats that the group has booked. |  |
