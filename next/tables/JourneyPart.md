# JourneyPart

For some use cases e.g. change of Facilities during ServiceJourney

*Table: parts*

| Sub | Element | Usage | Card | Type | Description | Note |
|-----|---------|-------|------|------|-------------|------|
|  | JourneyPart | optional | 1..* | JourneyPart_VersionStructure | A part of a VEHICLE JOURNEY created according to a specific functional purpose, for instance in situations when vehicle coupling or separating occurs. |  |
| + | validityConditions | optional | 1..1 | validityConditions_RelStructure | VALIDITY CONDITIONs conditioning entity. | We prefer to not use those |
| ++ | AvailabilityConditionRef | optional | 0..* | AvailabilityConditionRefStructure | Reference to an AVAILABILITY CONDITION. A VALIDITY CONDITION defined in terms of temporal attributes. |  |
| + | MainPartRef | optional | 0..1 | JourneyPartRefStructure | Main JOURNEY PART for journey. | For the use cases we support, this is not necessary |
| + | TrainNumberRef | optional | 1..1 | TrainNumberRefStructure | Reference to a TRAIN NUMBER. | TrainNumber used for this part |
| + | FromStopPointRef | mandatory | 0..1 | ScheduledStopPointRefStructure | SCHEDULED STOP POINT feeding INTERCHANGE. If absent apply to all STOP POINTs. | `ScheduledStopPoint` where the part begins. On the level of Quay. |
| + | ToStopPointRef | expected | 0..1 | ScheduledStopPointRefStructure | SCHEDULED STOP POINT distributing from INTERCHANGE. If absent apply to all STOP POINTs. | `ScheduledStopPoint` where the part ends . If not present, it is to the end of the ServiceJourney. But we prefer to have it explicitly |
| + | StartTime | mandatory | 0..1 | xsd:time | The (inclusive) start date and time. | Time bounds of the part |
| + | StartTimeDayOffset | optional | 0..1 | DayOffsetType | Number of days after journey start time that start time is. |  |
| + | EndTime | mandatory | 0..1 | xsd:time | The (inclusive) end date and time. | Time bounds of the part. |
| + | EndTimeDayOffset | optional | 0..1 | DayOffsetType | Number of days after journey start time that end time is. |  |
| + | PurposeOfJourneyPartitionRef | mandatory | 1..1 | PurposeOfJourneyPartitionRefStructure | Reference to a PURPOSE OF JOURNEY PARTITION. | Reason for the partition (e.g. `FacilityChange`, `TrainNumberChange`, 'TypeOfProductCategorychage`). Only two values are allowed (see uc0_journey_parts). Other things are implemented with different elements. Especially Notices are done with NoticeAssignment and not ServiceJourneyPart. |
| + | facilities | expected | 0..1 | serviceFacilitySets_RelStructure | FACILITies available associated with LINE. It is always recommended to also model accessibility relevant things as equipment on the VEHICLE and physical elements, if real-time information is needed. | `ServiceFacilitySet` valid for this part only. Used when there is a change in facilities. |
| ++ | ServiceFacilitySetRef | expected | 0..* | ServiceFacilitySetRefStructure | Reference to a SERVICE FACILITY SET. |  |
| + | TypeOfProductCategoryRef | optional | 1..1 | TypeOfProductCategoryRefStructure | Reference to a TYPE OF PRODUCT CATEGORY. Product of a JOURNEY. e.g. ICS, Thales etc See ERA B.4 7037 Characteristic description code. | Used when the product category changes |
