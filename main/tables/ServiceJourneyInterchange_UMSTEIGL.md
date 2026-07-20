# ServiceJourneyInterchange_UMSTEIGL

ChangeWithinVehicle is not applicable when StaySeated=false

*Table: ServiceJourneyInterchange*

| Sub | Element | Usage | Card | Type | Description | Note |
|-----|---------|-------|------|------|-------------|------|
|  | @id | mandatory | 1..1 | xsd:string | Attribute id | |
|  | @version | mandatory | 1..1 | xsd:string | Attribute version | |
|  | validityConditions | expected | 1..1 | validityConditions_RelStructure | VALIDITY CONDITIONs conditioning entity. |  |
| + | AvailabilityConditionRef | expected | 1..* | AvailabilityConditionRefStructure | Reference to an AVAILABILITY CONDITION. A VALIDITY CONDITION defined in terms of temporal attributes. |  |
|  | Description | optional | 0..1 | MultilingualString | Description of contents. |  |
|  | StaySeated | mandatory | 0..1 | xsd:boolean | Whether the passenger can remain in vehicle (i.e. block linking). Default is false: the passenger must change vehicles for this INTERCHANGE. Default is false. |  |
|  | CrossBorder | optional | 0..1 | xsd:boolean | Whether interchanging crosses a border. |  |
|  | Planned | mandatory | 0..1 | xsd:boolean | Whether INTERCHANGE is planned in a timetable. Default is true. |  |
|  | Guaranteed | mandatory | 0..1 | xsd:boolean | Whether INTERCHANGE is guaranteed. Default is false. |  |
|  | MaximumWaitTime | optional | 0..1 | xsd:duration | Maximum wait time for JOURNEY MEETING. | If not set or PT0M, connection is considered guaranteed. |
|  | MinimumTransferTime | expected | 0..1 | xsd:duration | Maximum transfer duration for INTERCHANGE. |  |
|  | FromPointRef | mandatory | 1..1 | VehicleMeetingPointRefStructure | Identifier of VEHICLE MEETING POINT from which Link starts. | ScheduledStopPoint at which the feeder journey arrives. Replaces StopPlaceRef+FeederFilter from InterchangeRule. |
| + | @nameOfRefClass | mandatory | 1..1 | xsd:string | Attribute nameOfRefClass | |
|  | ToPointRef | mandatory | 1..1 | VehicleMeetingPointRefStructure | Identifier of VEHICLE MEETING POINT at which Link ends. | ScheduledStopPoint at which the distributor journey departs. Same stop as FromPointRef for same-stop transfers. |
| + | @nameOfRefClass | mandatory | 1..1 | xsd:string | Attribute nameOfRefClass | |
|  | FromServiceJourneyRef | mandatory | 1..1 | ServiceJourneyRefStructure | SERVICE JOURNEY that feeds the INTERCHANGE. +v2.0 | Reference to the specific feeder ServiceJourney. Replaces FeederFilter/LineInDirectionRef from InterchangeRule. One element per journey pair required. |
|  | ToServiceJourneyRef | mandatory | 1..1 | ServiceJourneyRefStructure | SERVICE JOURNEY that distributes from the INTERCHANGE. +v2.0 | Reference to the specific distributor ServiceJourney. Replaces DistributorFilter/LineInDirectionRef from InterchangeRule. |
