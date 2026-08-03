# ServiceJourneyInterchange

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
|  | ChangeWithinVehicle | optional | 0..1 | xsd:boolean | In case of train splitting, the passenger may have to change to a different part of the train to continue the journey. Default is false. +v2.1 | Set to true for train splitting (Flügelzug) when the passenger may have to move to a different coach. Default is false. |
|  | Planned | optional | 0..1 | xsd:boolean | Whether INTERCHANGE is planned in a timetable. Default is true. |  |
|  | Guaranteed | optional | 0..1 | xsd:boolean | Whether INTERCHANGE is guaranteed. Default is false. |  |
|  | StandardWaitTime | optional | 0..1 | xsd:duration | Standard wait time for INTERCHANGE. | Used for joining/splitting and waiting in vehicle |
|  | StandardTransferTime | expected | 0..1 | xsd:duration | Standard transfer duration for INTERCHANGE. |  |
|  | FromPointRef | mandatory | 1..1 | VehicleMeetingPointRefStructure | Start POINT of LINK. |  |
| + | @nameOfRefClass | mandatory | 1..1 | xsd:string | Attribute nameOfRefClass | |
|  | FromVisitNumber | optional | 0..1 | xsd:nonNegativeInteger | Visit number to distinguish which visit to FROM SCHEDULED STOP POINT this is. Default is one. Only needed for circular routes with connections at the same stop on different visits. |  |
|  | ToPointRef | mandatory | 1..1 | VehicleMeetingPointRefStructure | End POINT of LINK. |  |
| + | @nameOfRefClass | mandatory | 1..1 | xsd:string | Attribute nameOfRefClass | |
|  | FromServiceJourneyRef | mandatory | 1..1 | ServiceJourneyRefStructure | SERVICE JOURNEY that feeds JOURNEY MEETING. +v2.0 |  |
|  | ToServiceJourneyRef | mandatory | 1..1 | ServiceJourneyRefStructure | SERVICE JOURNEY that distributes from JOURNEY MEETING. +v2.0 |  |
