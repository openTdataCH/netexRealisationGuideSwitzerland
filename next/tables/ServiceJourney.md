# ServiceJourney

*Table: ServiceJourney*

| Sub | Element | Usage | Card | Type | Description | Note |
|-----|---------|-------|------|------|-------------|------|
|  | @id | mandatory | 1..1 | xsd:string | Attribute id | |
|  | @version | mandatory | 1..1 | xsd:string | Attribute version | |
|  | @responsibilitySetRef | mandatory | 1..1 | xsd:string | Attribute responsibilitySetRef | |
|  | validityConditions | mandatory | 1..1 | validityConditions_RelStructure |  | Used to specify the temporal conditions for the ServiceJourney, for example that the corresponding journey only applies on particular days of a period (indicated by ValidDayBits, “Verkehrstagebitfeld”). |
| + | AvailabilityConditionRef | mandatory | 0..* | AvailabilityConditionRefStructure |  | Only a single AvailabilityConditionRef is allowed. |
|  | keyList | optional | 1..1 | KeyListStructure |  | KEY LIST with the KEY VALUEs belonging to the SERVICE JOURNEY. We don't use it for sjyid! |
| + | KeyValue | optional | 1..* | KeyValueStructure | Key value pair for Entity. | We use it for tariff codes and region codes PAG mostly. |
| ++ | Key | optional | 1..1 | normalizedString | Identifier of value e.g. System. |  |
| ++ | Value | optional | 0..1 | normalizedString | Value for alternative key. |  |
|  | privateCodes | expected | 1..1 | PrivateCodesStructure |  |  |
| + | PrivateCode | expected | 0..* | PrivateCodeStructure |  | Mandatory if available for the following types: sjyid and rn. rn is the type used for the Postauto region. |
| ++ | @type | mandatory | 1..1 | xsd:string | Attribute type | |
|  | TransportMode | optional | 0..1 | AllPublicTransportModesEnumeration | PT MODE of JOURNEY. |  |
|  | TypeOfProductCategoryRef | mandatory | 0..1 | TypeOfProductCategoryRefStructure |  | Relevant elements are defined in the mapping excel. |
|  | TypeOfServiceRef | optional | 0..1 | TypeOfServiceRefStructure |  | Should always be ch:1:TypeOfService:1 |
|  | noticeAssignments | optional | 0..1 | noticeAssignments_RelStructure | NOTICEs relevant for the whole GROUP OF SERVICEs. | The complete set of all applicable Notices. Attention: Notices may be restricted to a a part of the journey (by defining the first and last stop). |
| + | [NoticeAssignment](NoticeAssignment.md) | optional | 0..* | NoticeAssignment_VersionStructure | The assignment of a NOTICE showing an exception in a JOURNEY PATTERN, a COMMON SECTION, or a VEHICLE JOURNEY, possibly specifying at which POINT IN JOURNEY PATTERN the validity of the NOTICE starts and ends respectively. |  |
|  | occupancies | optional | 0..1 | OccupancyView_RelStructure | OCCUPANCYs associated with this JOURNEY. +v2.0 |  |
| + | [OccupancyView](OccupancyView.md) | optional | 0..* | OccupancyView_VersionStructure | Type for an Occupancy. Details for OCCUPANCY. | Currently not available. |
|  | ServiceAlteration | mandatory | 0..1 | ServiceAlterationEnumeration | Whether journey is as planned, a cancellation or an extra journey. Default is as Planned. | Only the value planned is allowed. We might add the others, like cancelled, later. |
|  | DepartureTime | expected | 0..1 | time | Time of Departure. | Usually local time. Otherwise we have problems with summer time. See Usage Notes. |
|  | DepartureDayOffset | optional | 0..1 | DayOffsetType | Day offset if day of departure time of VEHICLE JOURNEY differs from the current OPERATING DAY. | 0 for current operating day. Could also be negative. |
|  | ServiceJourneyPatternRef | mandatory | 0..1 | ServiceJourneyPatternRefStructure |  | The reference to the ServiceJourneyPattern. |
|  | TimeDemandTypeRef | mandatory | 0..1 | TimeDemandTypeRefStructure |  | The timing behaviour is defined here. We allow only one TimeDemandType per ServiceJourney. |
|  | VehicleTypeRef | expected | 0..1 | VehicleTypeRefStructure |  | Simple VehicleType is used for general type like NF. Otherwise a CompoundTrainRef or TrainRef is expected for formations. |
| + | @ref | mandatory | 1..1 | xsd:string | Attribute ref | |
| + | @version | mandatory | 1..1 | xsd:string | Attribute version | |
| + | @nameOfRefClass | mandatory | 1..1 | xsd:string | Attribute nameOfRefClass | |
|  | trainNumbers | mandatory | 0..1 | trainNumberRefs_RelStructure | TRAIN NUMBERs -= derived through JOURNEY PARTs of a journey - for a multi-part journey only. |  |
| + | TrainNumberRef | mandatory | 0..* | TrainNumberRefStructure |  |  |
|  | [Destination](Destination.md) | expected | 0..1 | JourneyEndpointStructure | Destination for JOURNEY. |  |
|  | parts | optional | 0..1 | journeyParts_RelStructure | JOURNEY PARTs of a journey - for a multi-part journey only. | For some use cases e.g. change of Facilities during ServiceJourney |
| + | [JourneyPart](JourneyPart.md) | expected | 0..* | JourneyPart_VersionStructure | A part of a VEHICLE JOURNEY created according to a specific functional purpose, for instance in situations when vehicle coupling or separating occurs. |  |
|  | checkConstraints | optional | 0..1 | checkConstraints_RelStructure | CHECK CONSTRAINTs which apply to SERVICE JOURNEY, e.g. check in time, security time. These are advisory only and not for use in journey planning. |  |
| + | [CheckConstraint](CheckConstraint.md) | optional | 0..* | CheckConstraint_VersionStructure | Process associated with a Place, typically giving rise to a delay to the traveller. | CheckConstraints are used to encode foreseeable delays by check-in or other processes. |
