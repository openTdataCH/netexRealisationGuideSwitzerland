# ServiceJourney_PassingTime_deprecated

*Table: ServiceJourney*

| Sub | Element | Usage | Card | Type | Description | Note |
|-----|---------|-------|------|------|-------------|------|
|  | @id | mandatory | 1..1 | xsd:string | Attribute id | |
|  | @version | mandatory | 1..1 | xsd:string | Attribute version | |
|  | @responsibilitySetRef | mandatory | 1..1 | xsd:string | Attribute responsibilitySetRef | |
|  | validityConditions | mandatory | 1..1 | validityConditions_RelStructure |  | Used to specify a set of temporal conditions that can be associated with the ServiceJourney, for example that the corresponding journey only applies on particular days of a period (indicated by ValidDayBits, “Verkehrstagebitfeld”). |
| + | [AvailabilityCondition](AvailabilityCondition.md) | mandatory | 0..* | unknown |  | Only a single occurence is allowed. The following elements are mandatory here, any other elements of AvailabilityCondition are not allowed or will be ignored. |
|  | keyList | expected | 1..1 | KeyListStructure |  | KEY LIST with the KEY VALUEs belonjing to the SERVICE JOURNEY. Will contain the SJYID. |
| + | KeyValue | mandatory | 1..* | KeyValueStructure |  | A KeyValue pair with the Key SJYID must exist. The Value contains a valid Swiss Journey ID. |
| ++ | Key | mandatory | 1..1 | xsd:normalizedString | Identifier of value e.g. System. |  |
| ++ | Value | mandatory | 0..1 | xsd:anyType | Value for alternative key. |  |
|  | privateCodes | expected | 1..1 | PrivateCodesStructure |  |  |
| + | PrivateCode | expected | 0..* | PrivateCodeStructure |  |  |
|  | TransportMode | optional | 0..1 | AllModesEnumeration |  |  |
|  | TypeOfProductCategoryRef | mandatory | 1..1 | TypeOfProductCategoryRefStructure |  |  |
|  | TypeOfServiceRef | optional | 1..1 | TypeOfServiceRefStructure |  |  |
|  | noticeAssignments | optional | 0..1 | noticeAssignments_RelStructure | NOTICEs of an interchange. | The complete set of all applicable notices. Attention: Notices may be restricted to a given set of stops. |
| + | [NoticeAssignment](NoticeAssignment.md) | optional | 0..* | unknown |  |  |
|  | occupancies | optional | 0..1 | OccupancyView_RelStructure |  |  |
| + | [OccupancyView](OccupancyView.md) | optional | 0..* | OccupancyView_VersionStructure |  |  |
|  | ServiceAlteration | mandatory | 0..1 | ServiceAlterationEnumeration |  | Only the value planned is allowed. |
|  | DepartureTime | expected | 0..1 | xsd:time | Time of Departure. |  |
|  | DepartureDayOffset | optional | 0..1 | DayOffsetType |  |  |
|  | LineRef | mandatory | 1..1 | LineRefStructure |  |  |
|  | DirectionType | mandatory | 0..1 | RelativeDirectionEnumeration |  | Allowed are: inbound, outbound |
|  | trainNumbers | mandatory | 0..1 | trainNumbersInFrame_RelStructure |  |  |
| + | TrainNumberRef | mandatory | 0..* | TrainNumberRefStructure |  |  |
|  | [Destination](Destination.md) | expected | 0..1 | TravelSpecificationSummaryEndpointStructure |  |  |
|  | passingTimes | mandatory | 0..1 | timetabledPassingTimes_RelStructure |  |  |
| + | TimetabledPassingTime | expected | 0..* | unknown |  |  |
| ++ | PointInJourneyPatternRef | expected | 0..1 | PointInJourneyPatternRefStructure |  |  |
