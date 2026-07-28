# ServiceJourneyInterchange

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
|  | ChangeWithinVehicle | optional | 0..1 | xsd:boolean |  | Set to true for train splitting (Flügelzug) when the passenger may have to move to a different coach. Default is false. |
|  | Planned | optional | 0..1 | xsd:boolean |  |  |
|  | Guaranteed | optional | 0..1 | xsd:boolean |  |  |
|  | MaximumWaitTime | optional | 0..1 | xsd:duration |  | If not set or PT0M, it is guaranteed. |
|  | FromPointRef | mandatory | 1..1 | VehicleMeetingPointRefStructure |  |  |
| + | @nameOfRefClass | mandatory | 1..1 | xsd:string | Attribute nameOfRefClass | |
|  | FromVisitNumber | optional | 0..1 | xsd:nonNegativeInteger |  |  |
|  | ToPointRef | mandatory | 1..1 | VehicleMeetingPointRefStructure |  |  |
| + | @nameOfRefClass | mandatory | 1..1 | xsd:string | Attribute nameOfRefClass | |
|  | FromServiceJourneyRef | mandatory | 1..1 | ServiceJourneyRefStructure |  |  |
|  | ToServiceJourneyRef | mandatory | 1..1 | ServiceJourneyRefStructure |  |  |
