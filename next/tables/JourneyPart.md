# JourneyPart

For some use cases e.g. change of Facilities during ServiceJourney

*Table: parts*

| Sub | Element | Usage | Card | Type | Description | Note |
|-----|---------|-------|------|------|-------------|------|
|  | JourneyPart | optional | 0..* | JourneyPart_VersionStructure | A part of a VEHICLE JOURNEY created according to a specific functional purpose, for instance in situations when vehicle coupling or separating occurs. |  |
| + | validityConditions | optional | 1..1 | validityConditions_RelStructure |  | We prefer to not use those |
| ++ | AvailabilityConditionRef | optional | 0..* | AvailabilityConditionRefStructure |  |  |
| + | MainPartRef | optional | 0..1 | JourneyPartRefStructure | Main JOURNEY PART for journey. | For the use cases we support, this is not necessary |
| + | TrainNumberRef | optional | 0..1 | TrainNumberRefStructure |  | TrainNumber used for this part |
| + | FromStopPointRef | mandatory | 1..1 | ScheduledStopPointRefStructure | Point at which this JOURNEY PART starts. | `ScheduledStopPoint` where the part begins. On the level of Quay. |
| + | ToStopPointRef | expected | 0..1 | ScheduledStopPointRefStructure | Point at which this JOURNEY PART ends. If not set it is until the end of the JOURNEY. We will make this element mandatory in the future. | `ScheduledStopPoint` where the part ends . If not present, it is to the end of the ServiceJourney. But we prefer to have it explicitly |
| + | StartTime | mandatory | 0..1 | time | Start time of JOURNEY PART. | Time bounds of the part |
| + | StartTimeDayOffset | optional | 0..1 | DayOffsetType | Number of days after journey start time that start time is. |  |
| + | EndTime | mandatory | 0..1 | time | End time of JOURNEY PART. | Time bounds of the part. |
| + | EndTimeDayOffset | optional | 0..1 | DayOffsetType | Number of days after journey start time that end time is. |  |
| + | PurposeOfJourneyPartitionRef | mandatory | 0..1 | PurposeOfJourneyPartitionRefStructure |  | Reason for the partition (e.g. `FacilityChange`, `TrainNumberChange`, 'TypeOfProductCategorychage`). Only two values are allowed (see uc0_journey_parts). Other things are implemented with different elements. Especially Notices are done with NoticeAssignment and not ServiceJourneyPart. |
| + | facilities | expected | 0..1 | serviceFacilitySets_RelStructure | Facilities available during JOURNEY PART. | `ServiceFacilitySet` valid for this part only. Used when there is a change in facilities. |
| ++ | ServiceFacilitySetRef | expected | 0..* | ServiceFacilitySetRefStructure |  |  |
| + | TypeOfProductCategoryRef | optional | 0..1 | TypeOfProductCategoryRefStructure |  | Used when the product category changes |
