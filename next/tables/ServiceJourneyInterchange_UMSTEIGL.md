# ServiceJourneyInterchange_UMSTEIGL

ChangeWithinVehicle is not applicable when StaySeated=false

*Table: ServiceJourneyInterchange*

| Sub | Element | Usage | Card | Type | Description | Note |
|-----|---------|-------|------|------|-------------|------|
|  | @id | mandatory | 1..1 | xsd:string | Attribute id | |
|  | @version | mandatory | 1..1 | xsd:string | Attribute version | |
|  | validityConditions | expected | 1..1 | validityConditions_RelStructure | VALIDITY CONDITIONs conditioning entity. |  |
| + | AvailabilityConditionRef | expected | 0..* | AvailabilityConditionRefStructure | Reference to an AVAILABILITY CONDITION. A VALIDITY CONDITION defined in terms of temporal attributes. |  |
|  | Description | optional | 0..1 | MultilingualString | Description of SCHEDULED STOP POINT feeding INTERCHANGE. |  |
|  | StaySeated | mandatory | 0..1 | xsd:boolean | Whether the passenger can remain in vehicle (i.e. block linking). Default is false: the passenger must change vehicles for this INTERCHANGE. Default is false. |  |
|  | CrossBorder | optional | 0..1 | xsd:boolean | Whether INTERCHANGE involves crossing an international border. Default is false. |  |
|  | Planned | mandatory | 0..1 | xsd:boolean | Whether INTERCHANGE is planned in a timetable. Default is true. |  |
|  | Guaranteed | mandatory | 0..1 | xsd:boolean | Whether INTERCHANGE is guaranteed. Default is false. |  |
|  | StandardWaitTime | optional | 0..1 | xsd:duration | Standard wait time for INTERCHANGE. | Used for joining/splitting and waiting in vehicle |
|  | StandardTransferTime | expected | 0..1 | xsd:duration | Standard transfer duration for INTERCHANGE. |  |
|  | FromPointRef | mandatory | 1..1 | VehicleMeetingPointRefStructure | Start POINT of LINK. | ScheduledStopPoint at which the feeder journey arrives. Replaces StopPlaceRef+FeederFilter from InterchangeRule. |
| + | @nameOfRefClass | mandatory | 1..1 | xsd:string | Attribute nameOfRefClass | |
|  | ToPointRef | mandatory | 1..1 | VehicleMeetingPointRefStructure | End POINT of LINK. | ScheduledStopPoint at which the distributor journey departs. Same stop as FromPointRef for same-stop transfers. |
| + | @nameOfRefClass | mandatory | 1..1 | xsd:string | Attribute nameOfRefClass | |
|  | FromServiceJourneyRef | mandatory | 1..1 | ServiceJourneyRefStructure | SERVICE JOURNEY that feeds JOURNEY MEETING. +v2.0 | Reference to the specific feeder ServiceJourney. Replaces FeederFilter/LineInDirectionRef from InterchangeRule. One element per journey pair required. |
|  | ToServiceJourneyRef | mandatory | 1..1 | ServiceJourneyRefStructure | SERVICE JOURNEY that distributes from JOURNEY MEETING. +v2.0 | Reference to the specific distributor ServiceJourney. Replaces DistributorFilter/LineInDirectionRef from InterchangeRule. |
