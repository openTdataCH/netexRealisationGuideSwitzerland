# TemplateServiceJourney

TemplateServiceJourney is used for journeys repeating at a certain frequency.

*Table: TemplateServiceJourney*

| Sub | Element | Usage | Card | Type | Description | Note |
|-----|---------|-------|------|------|-------------|------|
|  | @id | mandatory | 1..1 | xsd:string | Attribute id | |
|  | @version | mandatory | 1..1 | xsd:string | Attribute version | |
|  | @responsibilitySetRef | mandatory | 1..1 | xsd:string | Attribute responsibilitySetRef | |
|  | validityConditions | mandatory | 1..1 | validityConditions_RelStructure |  | Used to specify a set of temporal conditions that can be associated with the ServiceJourney, for example that the corresponding journey only applies on particular days of a period (indicated by ValidDayBits, “Verkehrstagebitfeld”). |
| + | AvailabilityConditionRef | mandatory | 0..* | AvailabilityConditionRefStructure |  | Only a single AvailabilityConditionRef is allowed. |
|  | keyList | optional | 1..1 | KeyListStructure |  | Key list for the repeating journeys. Contains the SJYID. |
| + | KeyValue | optional | 1..* | KeyValueStructure |  | A KeyValue pair with the key SJYID must exist. The Value contains a valid Swiss Journey ID. |
| ++ | Key | optional | 1..1 | xsd:normalizedString | Identifier of value e.g. System. |  |
| ++ | Value | optional | 0..1 | xsd:anyType | Value for alternative key. |  |
|  | privateCodes | expected | 1..1 | PrivateCodesStructure |  | Replaces the single PrivateCode. The following types are possible: sjyid and rn. rn is the type used for the Postauto region |
| + | PrivateCode | expected | 0..* | PrivateCodeStructure |  |  |
|  | TransportMode | optional | 0..1 | AllModesEnumeration |  |  |
|  | TypeOfProductCategoryRef | expected | 1..1 | TypeOfProductCategoryRefStructure |  |  |
|  | TypeOfServiceRef | optional | 1..1 | TypeOfServiceRefStructure |  |  |
|  | noticeAssignments | optional | 0..1 | noticeAssignments_RelStructure |  | The complete set of all applicable notices. Attention: Notices may be restricted to a given set of stops. |
| + | [NoticeAssignment](NoticeAssignment.md) | optional | 0..* | unknown |  |  |
|  | occupancies | optional | 0..1 | OccupancyView_RelStructure |  |  |
| + | [OccupancyView](OccupancyView.md) | optional | 0..* | OccupancyView_VersionStructure |  |  |
|  | ServiceAlteration | mandatory | 0..1 | ServiceAlterationEnumeration |  | Only the value planned is allowed. |
|  | DepartureTime | optional | 0..1 | xsd:time |  | Departure of the first journey. |
|  | DepartureDayOffset | optional | 0..1 | DayOffsetType |  | DayOffset if relevant. |
|  | JourneyPatternRef | mandatory | 1..1 | JourneyPatternRefStructure |  | The reference to the ServiceJourneyPattern |
| + | @nameOfRefClass | mandatory | 1..1 | xsd:string | Attribute nameOfRefClass | |
|  | TimeDemandTypeRef | mandatory | 0..1 | TimeDemandTypeRefStructure |  | The timing behaviour is defined here. We allow only one TimeDemandType per ServiceJourney. |
|  | VehicleTypeRef | expected | 1..1 | VehicleTypeRefStructure |  | Mostly used for accessibility information |
|  | LineRef | mandatory | 1..1 | LineRefStructure |  |  |
|  | DirectionType | optional | 0..1 | RelativeDirectionEnumeration |  | Allowed are: inbound, outbound |
|  | trainNumbers | mandatory | 0..1 | trainNumbersInFrame_RelStructure |  |  |
| + | TrainNumberRef | mandatory | 0..* | TrainNumberRefStructure |  |  |
|  | [Destination](Destination.md) | expected | 0..1 | TravelSpecificationSummaryEndpointStructure |  |  |
|  | parts | optional | 0..1 | blockParts_RelStructure |  | For some use cases e.g. change of Facilities during ServiceJourney |
| + | JourneyPartRef | expected | 0..* | JourneyPartRefStructure |  |  |
|  | TemplateVehicleJourneyType | expected | 0..1 | TemplateVehicleJourneyTypeEnumeration |  |  |
|  | frequencyGroups | mandatory | 0..1 | frequencyGroupsInFrame_RelStructure |  | We strictly map one frequency to the TemplateServiceJourney. |
| + | HeadwayJourneyGroup | mandatory | 0..* | unknown |  |  |
| ++ | ScheduledHeadwayInterval | mandatory | 0..1 | xsd:duration |  |  |
| ++ | HeadwayDisplay | optional | 0..1 | HeadwayUseEnumeration |  | Allowed values: displayPassingTimesOnly displayInsteadOfPassingTimes displayAsWellAsPassingTimes. We only export displayPassingTimesOnly. |
