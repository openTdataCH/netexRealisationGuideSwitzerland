# ServiceJourneyInterchange_UMSTEIGZ

Transfer time between two specific ServiceJourneys at a given stop (UMSTEIGZ). StaySeated=false: passenger must change vehicles. Replaces InterchangeRule in RG 2.0. One element per journey pair required.

*Table: ServiceJourneyInterchange*

| Sub | Element | Usage | Card | Type | Description | Note |
|-----|---------|-------|------|------|-------------|------|
|  | @id | mandatory | 1..1 | xsd:string | Attribute id | |
|  | @version | mandatory | 1..1 | xsd:string | Attribute version | |
|  | validityConditions | expected | 1..1 | validityConditions_RelStructure |  |  |
| + | AvailabilityConditionRef | expected | 1..1 | AvailabilityConditionRefStructure |  |  |
|  | Description | optional | 0..1 | MultilingualString | Description of SCHEDULED STOP POINT feeding INTERCHANGE. |  |
|  | StaySeated | mandatory | 0..1 | xsd:boolean |  |  |
|  | CrossBorder | optional | 0..1 | xsd:boolean |  |  |
|  | Planned | mandatory | 0..1 | xsd:boolean |  |  |
|  | Guaranteed | optional | 0..1 | xsd:boolean |  |  |
|  | MaximumWaitTime | optional | 0..1 | xsd:duration |  | If not set or PT0M, connection is considered guaranteed. |
|  | MinimumTransferTime | expected | 0..1 | xsd:duration |  |  |
|  | MaximumTransferTime | expected | 0..1 | xsd:duration |  |  |
|  | FromPointRef | mandatory | 1..1 | VehicleMeetingPointRefStructure |  | ScheduledStopPoint at which the feeder journey arrives. Replaces StopPlaceRef+FeederFilter from InterchangeRule. |
| + | @nameOfRefClass | mandatory | 1..1 | xsd:string | Attribute nameOfRefClass | |
|  | ToPointRef | mandatory | 1..1 | VehicleMeetingPointRefStructure |  | ScheduledStopPoint at which the distributor journey departs. Same stop as FromPointRef for same-stop transfers. |
| + | @nameOfRefClass | mandatory | 1..1 | xsd:string | Attribute nameOfRefClass | |
|  | FromServiceJourneyRef | mandatory | 1..1 | ServiceJourneyRefStructure |  | Reference to the specific feeder ServiceJourney. Replaces FeederFilter/ServiceJourneyRef from InterchangeRule. |
|  | ToServiceJourneyRef | mandatory | 1..1 | ServiceJourneyRefStructure |  | Reference to the specific distributor ServiceJourney. Replaces DistributorFilter/ServiceJourneyRef from InterchangeRule. |
