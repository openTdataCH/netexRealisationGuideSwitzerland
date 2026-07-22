# ServiceJourney_PassingTime_deprecated

*Table: ServiceJourney*

| Sub | Element | Usage | Card | Type | Description | Note |
|-----|---------|-------|------|------|-------------|------|
|  | @id | mandatory | 1..1 | xsd:string | Attribute id | |
|  | @version | mandatory | 1..1 | xsd:string | Attribute version | |
|  | @responsibilitySetRef | mandatory | 1..1 | xsd:string | Attribute responsibilitySetRef | |
|  | validityConditions | mandatory | 1..1 | validityConditions_RelStructure | VALIDITY CONDITIONs conditioning entity. | Used to specify a set of temporal conditions that can be associated with the ServiceJourney, for example that the corresponding journey only applies on particular days of a period (indicated by ValidDayBits, “Verkehrstagebitfeld”). |
| + | [AvailabilityCondition](AvailabilityCondition.md) | mandatory | 1..1 | AvailabilityCondition | VALIDITY CONDITION stated in terms of DAY TYPES and PROPERTIES OF DAYs. | Only a single occurence is allowed. The following elements are mandatory here, any other elements of AvailabilityCondition are not allowed or will be ignored. |
|  | keyList | expected | 1..1 | KeyListStructure | A list of alternative Key values for an element. | KEY LIST with the KEY VALUEs belonjing to the SERVICE JOURNEY. Will contain the SJYID. |
| + | KeyValue | mandatory | 1..* | KeyValueStructure | Key value pair for Entity. | A KeyValue pair with the Key SJYID must exist. The Value contains a valid Swiss Journey ID. |
| ++ | Key | mandatory | 1..1 | xsd:normalizedString | Identifier of value e.g. System. |  |
| ++ | Value | mandatory | 0..1 | xsd:anyType | Value associated with QUALITY STRUCTURE FACTOR. |  |
|  | privateCodes | expected | 1..1 | PrivateCodesStructure | A list of private codes that uniquely identifiy the element. May be used for inter-operating with other (legacy) systems. +v2.0 |  |
| + | PrivateCode | expected | 0..* | PrivateCodeStructure | A private code that uniquely identifies the element. May be used for inter-operating with other (legacy) systems. |  |
|  | TransportMode | optional | 0..1 | AllModesEnumeration | MODE. |  |
|  | TypeOfProductCategoryRef | mandatory | 1..1 | TypeOfProductCategoryRefStructure | Reference to a TYPE OF PRODUCT CATEGORY. Product of a JOURNEY. e.g. ICS, Thales etc See ERA B.4 7037 Characteristic description code. |  |
|  | TypeOfServiceRef | optional | 1..1 | TypeOfServiceRefStructure | Reference to a TYPE OF SERVICE. |  |
|  | noticeAssignments | optional | 0..1 | noticeAssignments_RelStructure | NOTICEs relevant for the whole GROUP OF SINGLE JOURNEYs. | The complete set of all applicable notices. Attention: Notices may be restricted to a given set of stops. |
| + | [NoticeAssignment](NoticeAssignment.md) | optional | 1..1 | NoticeAssignment | The assignment of a NOTICE showing an exception in a JOURNEY PATTERN, a COMMON SECTION, or a VEHICLE JOURNEY, possibly specifying at which POINT IN JOURNEY PATTERN the validity of the NOTICE starts and ends respectively. |  |
|  | occupancies | optional | 0..1 | OccupancyView_RelStructure | OCCUPANCYs associated with this journey. +v2.0 |  |
| + | [OccupancyView](OccupancyView.md) | optional | 1..1 | OccupancyView_VersionStructure | A simple VIEW of OCCUPANCY as a first implementation without full support of DECK PLAN. |  |
|  | ServiceAlteration | mandatory | 0..1 | ServiceAlterationEnumeration | Whether journey is as planned, a cancellation or an extra journey. Default is as Planned. | Only the value planned is allowed. |
|  | DepartureTime | expected | 0..1 | xsd:time | Departure time. |  |
|  | DepartureDayOffset | optional | 0..1 | DayOffsetType | Departure Time Day Offset. |  |
|  | LineRef | mandatory | 1..1 | LineRefStructure | Reference to a LINE. |  |
|  | DirectionType | mandatory | 0..1 | RelativeDirectionEnumeration | For fares for DISTANCE MATRIXE LEMENTs, DIRECTION in which price applies. | Allowed are: inbound, outbound |
|  | trainNumbers | mandatory | 0..1 | trainNumbersInFrame_RelStructure | TRAIN NUMBERs in frame. |  |
| + | TrainNumberRef | mandatory | 1..1 | TrainNumberRefStructure | Reference to a TRAIN NUMBER. |  |
|  | [Destination](Destination.md) | expected | 0..1 | TravelSpecificationSummaryEndpointStructure | Destination of Travel. Note that for a point-to-point TARIFF the origin is assigned with a DISTANCE MATRIX ELEMENT. |  |
|  | passingTimes | mandatory | 0..1 | timetabledPassingTimes_RelStructure | PASSING TIMEs for VEHICLE JOURNEY. |  |
| + | TimetabledPassingTime | expected | 1..1 | TimetabledPassingTime | TIMETABLED PASSING TIME at TIMING POINT. |  |
| ++ | PointInJourneyPatternRef | expected | 0..1 | PointInJourneyPatternRefStructure | Point in JOURNEY PATTERN upon which this DEAD RUN CALL is based. Can be used to obtain full association sets. |  |
