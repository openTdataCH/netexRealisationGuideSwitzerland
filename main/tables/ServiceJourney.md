# ServiceJourney

*Table: ServiceJourney*

| Sub | Element | Usage | Card | Type | Description | Note |
|-----|---------|-------|------|------|-------------|------|
|  | @id | mandatory | 1..1 | xsd:string | Attribute id | |
|  | @version | mandatory | 1..1 | xsd:string | Attribute version | |
|  | @responsibilitySetRef | mandatory | 1..1 | xsd:string | Attribute responsibilitySetRef | |
|  | validityConditions | mandatory | 1..1 | validityConditions_RelStructure |  | Used to specify a set of temporal conditions that can be associated with the ServiceJourney, for example that the corresponding journey only applies on particular days of a period (indicated by ValidDayBits, “Verkehrstagebitfeld”). |
| + | AvailabilityConditionRef | mandatory | 1..1 | AvailabilityConditionRefStructure |  | Only a single AvailabilityConditionRef is allowed. |
|  | keyList | expected | 1..1 | KeyListStructure |  | KEY LIST with the KEY VALUEs belonjing to the SERVICE JOURNEY. Will contain the SJYID. |
| + | KeyValue | mandatory | 1..* | KeyValueStructure |  | A KeyValue pair with the Key SJYID must exist. The Value contains a valid Swiss Journey ID. |
| ++ | Key | mandatory | 1..1 | xsd:normalizedString | Identifier of value e.g. System. |  |
| ++ | Value | mandatory | 0..1 | xsd:anyType | Value for alternative key. |  |
|  | privateCodes | expected | 1..1 | PrivateCodesStructure |  |  |
| + | PrivateCode | expected | 0..* | PrivateCodeStructure |  | The following types are possible: sjyid and rn. rn is the type used for the Postauto region. |
| ++ | @type | mandatory | 1..1 | xsd:string | Attribute type | |
|  | TransportMode | optional | 0..1 | AllModesEnumeration |  |  |
|  | TypeOfProductCategoryRef | mandatory | 1..1 | TypeOfProductCategoryRefStructure |  | Relevant elements are defined in the mapping excel. |
|  | TypeOfServiceRef | optional | 1..1 | TypeOfServiceRefStructure |  | Should always be ch:1:TypeOfService:1 |
|  | noticeAssignments | optional | 0..1 | noticeAssignments_RelStructure | NOTICEs of an interchange. | The complete set of all applicable Notices. Attention: Notices may be restricted to a a part of the journey (by defining the first and last stop). |
| + | [NoticeAssignment](NoticeAssignment.md) | optional | 1..1 | unknown |  |  |
|  | occupancies | optional | 0..1 | OccupancyView_RelStructure |  |  |
| + | [OccupancyView](OccupancyView.md) | optional | 1..1 | OccupancyView_VersionStructure |  | Currently not available |
|  | ServiceAlteration | mandatory | 0..1 | ServiceAlterationEnumeration |  | Only the value planned is allowed. We might add the others, like cancelled, later. |
|  | DepartureTime | expected | 0..1 | xsd:time | Time of Departure. |  |
|  | DepartureDayOffset | optional | 0..1 | DayOffsetType |  | 0 for current operating day. Could also be negative. |
|  | JourneyPatternRef | mandatory | 1..* | JourneyPatternRefStructure | Reference to a JOURNEY PATTERN. | The reference to the ServiceJourneyPattern. |
| + | @nameOfRefClass | mandatory | 1..1 | xsd:string | Attribute nameOfRefClass | |
|  | TimeDemandTypeRef | mandatory | 0..1 | TimeDemandTypeRefStructure |  | The timing behaviour is defined here. We allow only one TimeDemandType per ServiceJourney. |
|  | VehicleTypeRef | expected | 1..1 | VehicleTypeRefStructure |  | Mostly used for accessibility information like NF. Relevant definitions in the mapping excel. |
|  | LineRef | mandatory | 1..1 | LineRefStructure |  |  |
|  | DirectionType | mandatory | 0..1 | RelativeDirectionEnumeration |  | Allowed are: inbound, outbound |
|  | trainNumbers | mandatory | 0..1 | trainNumbersInFrame_RelStructure |  |  |
| + | TrainNumberRef | mandatory | 1..* | TrainNumberRefStructure |  |  |
|  | [Destination](Destination.md) | expected | 0..1 | TravelSpecificationSummaryEndpointStructure |  |  |
|  | parts | optional | 0..1 | blockParts_RelStructure |  | For some use cases e.g. change of Facilities during ServiceJourney |
| + | JourneyPartRef | expected | 1..1 | JourneyPartRefStructure |  |  |
|  | checkConstraints | optional | 0..1 | checkConstraints_RelStructure |  |  |
| + | CheckConstraint | optional | 1..* | unknown | Process associated with a Place, typically giving rise to a delay to the traveller. | CheckConstraints are used for different use cases |
