# ServiceJourney_PassingTime_deprecated

*Table: ServiceJourney*

| Sub | Element | Usage | Card | Type | Description | Note |
|-----|---------|-------|------|------|-------------|------|
|  | @id | mandatory | 1..1 | xsd:string | Attribute id | |
|  | @version | mandatory | 1..1 | xsd:string | Attribute version | |
|  | @responsibilitySetRef | mandatory | 1..1 | xsd:string | Attribute responsibilitySetRef | |
|  | validityConditions | mandatory | 1..1 | validityConditions_RelStructure |  | Used to specify a set of temporal conditions that can be associated with the ServiceJourney, for example that the corresponding journey only applies on particular days of a period (indicated by ValidDayBits, “Verkehrstagebitfeld”). |
| + | [AvailabilityCondition](AvailabilityCondition.md) | mandatory | 0..* | AvailabilityCondition_VersionStructure | VALIDITY CONDITION stated in terms of DAY TYPES and PROPERTIES OF DAYs. | Only a single occurence is allowed. The following elements are mandatory here, any other elements of AvailabilityCondition are not allowed or will be ignored. |
|  | privateCodes | mandatory | 1..1 | PrivateCodesStructure |  |  |
| + | PrivateCode | mandatory | 0..* | PrivateCodeStructure |  | The Value contains a valid Swiss Journey ID. |
| ++ | @type | mandatory | 1..1 | xsd:string | Attribute type | |
|  | TransportMode | optional | 0..1 | AllPublicTransportModesEnumeration | PT MODE of JOURNEY. |  |
|  | TypeOfProductCategoryRef | mandatory | 0..1 | TypeOfProductCategoryRefStructure |  |  |
|  | TypeOfServiceRef | optional | 0..1 | TypeOfServiceRefStructure |  |  |
|  | noticeAssignments | optional | 0..1 | noticeAssignments_RelStructure | NOTICEs relevant for the whole GROUP OF SERVICEs. | The complete set of all applicable notices. Attention: Notices may be restricted to a given set of stops. |
| + | [NoticeAssignment](NoticeAssignment.md) | optional | 0..* | NoticeAssignment_VersionStructure | The assignment of a NOTICE showing an exception in a JOURNEY PATTERN, a COMMON SECTION, or a VEHICLE JOURNEY, possibly specifying at which POINT IN JOURNEY PATTERN the validity of the NOTICE starts and ends respectively. |  |
|  | occupancies | optional | 0..1 | OccupancyView_RelStructure | OCCUPANCYs associated with this JOURNEY. +v2.0 |  |
| + | [OccupancyView](OccupancyView.md) | optional | 0..* | OccupancyView_VersionStructure | Type for an Occupancy. Details for OCCUPANCY. |  |
|  | ServiceAlteration | mandatory | 0..1 | ServiceAlterationEnumeration | Whether journey is as planned, a cancellation or an extra journey. Default is as Planned. | Only the value planned is allowed. |
|  | DepartureTime | expected | 0..1 | time | Time of Departure. |  |
|  | DepartureDayOffset | optional | 0..1 | DayOffsetType | Day offset if day of departure time of VEHICLE JOURNEY differs from the current OPERATING DAY. |  |
|  | LineRef | mandatory | 1..1 | LineRefStructure |  |  |
|  | DirectionType | mandatory | 0..1 | RelativeDirectionEnumeration |  | Allowed are: inbound, outbound |
|  | trainNumbers | mandatory | 0..1 | trainNumberRefs_RelStructure | TRAIN NUMBERs -= derived through JOURNEY PARTs of a journey - for a multi-part journey only. |  |
| + | TrainNumberRef | mandatory | 0..* | TrainNumberRefStructure |  |  |
|  | [Destination](Destination.md) | expected | 0..1 | JourneyEndpointStructure | Destination for JOURNEY. |  |
|  | passingTimes | mandatory | 0..1 | timetabledPassingTimes_RelStructure | PASSING TIMEs for VEHICLE JOURNEY. |  |
| + | TimetabledPassingTime | expected | 1..* | TimetabledPassingTime_VersionedChildStructure | TIMETABLED PASSING TIME at TIMING POINT. |  |
| ++ | PointInJourneyPatternRef | expected | 0..1 | PointInJourneyPatternRefStructure |  |  |
