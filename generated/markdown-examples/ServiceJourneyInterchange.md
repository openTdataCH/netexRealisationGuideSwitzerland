# ServiceJourneyInterchange

| Sub | Element | Usage | Card | Type | Description | Note |
|-----|---------|-------|------|------|-------------|------|
|  | ServiceJourneyInterchange | mandatory | 1..1 | unknown | The scheduled possibility for transfer of passengers between two SERVICE JOURNEYs at the same or different STOP POINTs. |  |
| + | validityConditions | expected | 1..1 | validityConditions_RelStructure | VALIDITY CONDITIONs conditioning entity. |  |
| ++ | AvailabilityConditionRef | expected | 1..1 | AvailabilityConditionRefStructure | Reference to an AVAILABILITY CONDITION. A VALIDITY CONDITION defined in terms of temporal attributes. |  |
| + | Description | optional | 0..1 | MultilingualString | Description of contents. |  |
| + | StaySeated | mandatory | 0..1 | xsd:boolean | Whether the passenger can remain in vehicle (i.e. block linking). Default is false: the passenger must change vehicles for this INTERCHANGE.
Default is false. |  |
| + | CrossBorder | optional | 0..1 | xsd:boolean | Whether interchanging crosses a border. |  |
| + | Planned | optional | 0..1 | xsd:boolean | Whether INTERCHANGE is planned in a timetable. Default is true. |  |
| + | Guaranteed | optional | 0..1 | xsd:boolean | Whether INTERCHANGE is guaranteed. Default is false. |  |
| + | MaximumWaitTime | optional | 0..1 | xsd:duration | Maximum wait time for JOURNEY MEETING. | If not set or PT0M, it is guaranteed. |
| + | FromPointRef | mandatory | 1..1 | VehicleMeetingPointRefStructure | Identifier of VEHICLE MEETING POINT from which Link starts. |  |
| + | FromVisitNumber | optional | 0..1 | xsd:nonNegativeInteger | Visit number to distinguish which visit to FROM SCHEDULED STOP POINT this is. Default is one. Only needed for circular routes with connections at the same stop on different visits. |  |
| + | ToPointRef | mandatory | 1..1 | VehicleMeetingPointRefStructure | Identifier of VEHICLE MEETING POINT at which Link ends. |  |
| + | FromServiceJourneyRef | mandatory | 1..1 | ServiceJourneyRefStructure | SERVICE JOURNEY that feeds the INTERCHANGE. +v2.0 |  |
| + | ToServiceJourneyRef | mandatory | 1..1 | ServiceJourneyRefStructure | SERVICE JOURNEY that distributes from the INTERCHANGE. +v2.0 |  |
