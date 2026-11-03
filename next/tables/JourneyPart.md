# JourneyPart

Used for a change of facilities and for direct carriages (see uc05_journey_parts). The first JourneyPart shows a change of facilities, the second one a direct carriage.

*Table: parts*

| Sub | Element | Usage | Card | Type | Description | Note |
|-----|---------|-------|------|------|-------------|------|
|  | JourneyPart | optional | 0..* | JourneyPart_VersionStructure | A part of a VEHICLE JOURNEY created according to a specific functional purpose, for instance in situations when vehicle coupling or separating occurs. |  |
| + | validityConditions | optional | 1..1 | validityConditions_RelStructure |  | We prefer to not use those |
| ++ | AvailabilityConditionRef | optional | 0..* | AvailabilityConditionRefStructure |  |  |
| + | MainPartRef | optional | 0..1 | JourneyPartRefStructure | Main JOURNEY PART for journey. | For the use cases we support, this is not necessary |
| + | TrainNumberRef | optional | 0..1 | TrainNumberRefStructure |  | TrainNumber used for this part. For a direct carriage the TrainNumber of the pulling train. |
| + | FromStopPointRef | optional | 1..1 | ScheduledStopPointRefStructure | Point at which this JOURNEY PART starts. | `ScheduledStopPoint` where the part begins. On the level of Quay. Used for a change of facilities. The XSD only allows either `FromStopPointRef`/`ToStopPointRef` or `FromPointInPatternRef`/`ToPointInPatternRef` (choice), so one of the two pairs must be present. |
| + | ToStopPointRef | expected | 0..1 | ScheduledStopPointRefStructure | Point at which this JOURNEY PART ends. If not set it is until the end of the JOURNEY. We will make this element mandatory in the future. | `ScheduledStopPoint` where the part ends. If not present, it is to the end of the ServiceJourney. But we prefer to have it explicitly. Not used together with `FromPointInPatternRef`/`ToPointInPatternRef`. |
| + | StartTime | mandatory | 0..1 | time | Start time of JOURNEY PART. | Time bounds of the part |
| + | StartTimeDayOffset | optional | 0..1 | DayOffsetType | Number of days after journey start time that start time is. |  |
| + | EndTime | mandatory | 0..1 | time | End time of JOURNEY PART. | Time bounds of the part. |
| + | EndTimeDayOffset | optional | 0..1 | DayOffsetType | Number of days after journey start time that end time is. |  |
| + | PurposeOfJourneyPartitionRef | mandatory | 0..1 | PurposeOfJourneyPartitionRefStructure |  | Reason for the partition. Allowed values: `ch:1:PurposeOfJourneyPartition:FacilityChange`, `ch:1:PurposeOfJourneyPartition:DirectCarriage`, `ch:1:PurposeOfJourneyPartition:TypeOfProductCategoryChange` (see uc05_journey_parts). A change of train number is not modelled with JourneyPart. Other things are implemented with different elements. Especially Notices are done with NoticeAssignment and not JourneyPart. |
| + | facilities | expected | 0..1 | serviceFacilitySets_RelStructure | Facilities available during JOURNEY PART. | `ServiceFacilitySet` valid for this part only. Used when there is a change in facilities. |
| ++ | ServiceFacilitySetRef | expected | 0..* | ServiceFacilitySetRefStructure |  |  |
| + | TypeOfProductCategoryRef | optional | 0..1 | TypeOfProductCategoryRefStructure |  | Used when the product category changes |
| + | Description | optional | 0..* | MultilingualString |  | Free text. In the example for direct carriages it names the direct carriage, the pulling train and the section. |
| ++ | @lang | mandatory | 1..1 | xsd:string | Attribute lang | |
| + | ParentJourneyRef | optional | 0..* | VehicleJourneyRefStructure | Reference to parent of which this is part. If given by context does not need to be stated. | Used for a direct carriage: the `ServiceJourney` of the pulling train. One `JourneyPart` per HRDF `*KWZ`. |
| + | FromPointInPatternRef | optional | 0..* | PointInSequenceRefStructure | POINT at which applicability of JOURNEY PART starts. When using PASSING TIME this element is to be used. +v2.1 | Used for a direct carriage: point in the `ServiceJourneyPattern` of the pulling train (`ParentJourneyRef`) where the part begins. Alternative to `FromStopPointRef` (choice in the XSD). |
| + | ToPointInPatternRef | optional | 0..* | PointInSequenceRefStructure | POINT at which applicability of JOURNEY PART ends. +v2.1 | Used for a direct carriage: point in the `ServiceJourneyPattern` of the pulling train where the part ends. Can be before the end of the pulling train. Mandatory in the XSD if `FromPointInPatternRef` is used. |
