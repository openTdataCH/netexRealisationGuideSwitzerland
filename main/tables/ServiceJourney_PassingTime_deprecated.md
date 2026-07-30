# ServiceJourney_PassingTime_deprecated

*Table: ServiceJourney*

| Sub | Element | Usage | Card | Type | Description | Note |
|-----|---------|-------|------|------|-------------|------|
|  | @id | mandatory | 1..1 | xsd:string | Attribute id | |
|  | @version | mandatory | 1..1 | xsd:string | Attribute version | |
|  | @responsibilitySetRef | mandatory | 1..1 | xsd:string | Attribute responsibilitySetRef | |
|  | validityConditions | mandatory | 1..1 | validityConditions_RelStructure | VALIDITY CONDITIONs conditioning entity. | Used to specify a set of temporal conditions that can be associated with the ServiceJourney, for example that the corresponding journey only applies on particular days of a period (indicated by ValidDayBits, “Verkehrstagebitfeld”). |
| + | [AvailabilityCondition](AvailabilityCondition.md) | mandatory | 0..* | AvailabilityCondition_VersionStructure | VALIDITY CONDITION stated in terms of DAY TYPES and PROPERTIES OF DAYs. | Only a single occurence is allowed. The following elements are mandatory here, any other elements of AvailabilityCondition are not allowed or will be ignored. |
|  | privateCodes | mandatory | 0..1 | PrivateCodesStructure | A list of private codes that uniquely identifiy the element. May be used for inter-operating with other (legacy) systems. +v2.0 |  |
| + | PrivateCode | mandatory | 0..* | PrivateCodeStructure | A private code that uniquely identifies the element. May be used for inter-operating with other (legacy) systems. | The Value contains a valid Swiss Journey ID. |
| ++ | @type | mandatory | 1..1 | xsd:string | Attribute type | |
|  | TransportMode | optional | 0..1 | AllModesEnumeration | An area within a Site. May be connected to Quays by PATH LINKs. |  |
|  | TypeOfProductCategoryRef | mandatory | 1..1 | TypeOfProductCategoryRefStructure | Reference to a TYPE OF PRODUCT CATEGORY. Product of a JOURNEY. e.g. ICS, Thales etc See ERA B.4 7037 Characteristic description code. |  |
|  | TypeOfServiceRef | optional | 1..1 | TypeOfServiceRefStructure | Reference to a TYPE OF SERVICE. |  |
|  | noticeAssignments | optional | 0..1 | noticeAssignments_RelStructure | NOTICE ASSIGNMENTs in frame. | The complete set of all applicable notices. Attention: Notices may be restricted to a given set of stops. |
| + | [NoticeAssignment](NoticeAssignment.md) | optional | 0..* | NoticeAssignment_VersionStructure | The assignment of a NOTICE showing an exception in a JOURNEY PATTERN, a COMMON SECTION, or a VEHICLE JOURNEY, possibly specifying at which POINT IN JOURNEY PATTERN the validity of the NOTICE starts and ends respectively. |  |
|  | occupancies | optional | 0..1 | OccupancyView_RelStructure | OCCUPANCYs in frame. |  |
| + | [OccupancyView](OccupancyView.md) | optional | 0..* | OccupancyView_VersionStructure | A simple VIEW of OCCUPANCY as a first implementation without full support of DECK PLAN. |  |
|  | ServiceAlteration | mandatory | 0..1 | ServiceAlterationEnumeration | Whether journey is as planned, a cancellation or an extra journey. Default is as Planned. | Only the value planned is allowed. |
|  | DepartureTime | expected | 0..1 | xsd:time | Time of departure of JOURNEY from POINT. |  |
|  | DepartureDayOffset | optional | 0..1 | DayOffsetType | Daya offset if Time of departure of JOURNEY from origin POINT from current OPERATING DAY. |  |
|  | LineRef | mandatory | 1..* | LineRefStructure | Reference to a LINE. |  |
|  | DirectionType | mandatory | 0..1 | RelativeDirectionEnumeration | A Direction of a ROUTE. One of a restricted set of values. Default is "Outbound" | Allowed are: inbound, outbound |
|  | trainNumbers | mandatory | 0..1 | trainNumbersInFrame_RelStructure | TRAIN NUMBERs -= derived through JOURNEY PARTs of a journey - for a multi-part journey only. |  |
| + | TrainNumberRef | mandatory | 0..* | TrainNumberRefStructure | Reference to a TRAIN NUMBER. |  |
|  | [Destination](Destination.md) | expected | 0..1 | TravelSpecificationSummaryEndpointStructure | Destination for JOURNEY. |  |
|  | passingTimes | mandatory | 0..1 | timetabledPassingTimes_RelStructure | PASSING TIMEs for VEHICLE JOURNEY. |  |
| + | TimetabledPassingTime | expected | 1..* | TimetabledPassingTime_VersionedChildStructure | TIMETABLED PASSING TIME at TIMING POINT. |  |
| ++ | PointInJourneyPatternRef | expected | 0..1 | PointInJourneyPatternRefStructure | Reference to a POINT IN JOURNEY PATTERN. If Given by Context does not need to stated. |  |
