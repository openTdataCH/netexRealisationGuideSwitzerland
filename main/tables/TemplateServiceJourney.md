# TemplateServiceJourney

TemplateServiceJourney is used for journeys repeating at a certain frequency.

*Table: TemplateServiceJourney*

| Sub | Element | Usage | Card | Type | Description | Note |
|-----|---------|-------|------|------|-------------|------|
|  | @id | mandatory | 1..1 | xsd:string | Attribute id | |
|  | @version | mandatory | 1..1 | xsd:string | Attribute version | |
|  | @responsibilitySetRef | mandatory | 1..1 | xsd:string | Attribute responsibilitySetRef | |
|  | validityConditions | mandatory | 1..1 | validityConditions_RelStructure |  | Used to specify the temporal conditions for the TemplateServiceJourney, for example that the corresponding journey only applies on particular days of a period (indicated by ValidDayBits, “Verkehrstagebitfeld”). |
| + | AvailabilityConditionRef | mandatory | 0..* | AvailabilityConditionRefStructure |  | Only a single AvailabilityConditionRef is allowed. |
|  | privateCodes | expected | 1..1 | PrivateCodesStructure |  | Replaces the single PrivateCode. |
| + | PrivateCode | expected | 0..* | PrivateCodeStructure |  | Mandatory if available for the following types: sjyid and rn. rn is the type used for the Postauto region. |
| ++ | @type | mandatory | 1..1 | xsd:string | Attribute type | |
|  | TransportMode | optional | 0..1 | AllPublicTransportModesEnumeration | PT MODE of JOURNEY. |  |
|  | TypeOfProductCategoryRef | expected | 0..1 | TypeOfProductCategoryRefStructure |  |  |
|  | TypeOfServiceRef | optional | 0..1 | TypeOfServiceRefStructure |  |  |
|  | noticeAssignments | optional | 0..1 | noticeAssignments_RelStructure | NOTICEs relevant for the whole GROUP OF SERVICEs. | The complete set of all applicable notices. Attention: Notices may be restricted to a given set of stops. |
| + | [NoticeAssignment](NoticeAssignment.md) | optional | 0..* | NoticeAssignment_VersionStructure | The assignment of a NOTICE showing an exception in a JOURNEY PATTERN, a COMMON SECTION, or a VEHICLE JOURNEY, possibly specifying at which POINT IN JOURNEY PATTERN the validity of the NOTICE starts and ends respectively. |  |
|  | occupancies | optional | 0..1 | OccupancyView_RelStructure | OCCUPANCYs associated with this JOURNEY. +v2.0 |  |
| + | [OccupancyView](OccupancyView.md) | optional | 0..* | OccupancyView_VersionStructure | Type for an Occupancy. Details for OCCUPANCY. | Currently not available. |
|  | ServiceAlteration | mandatory | 0..1 | ServiceAlterationEnumeration | Whether journey is as planned, a cancellation or an extra journey. Default is as Planned. | Only the value planned is allowed. |
|  | DepartureTime | optional | 0..1 | time | Time of Departure. | Departure of the first journey. For timezone see ServiceJourney |
|  | DepartureDayOffset | optional | 0..1 | DayOffsetType | Day offset if day of departure time of VEHICLE JOURNEY differs from the current OPERATING DAY. | DayOffset if relevant. |
|  | ServiceJourneyPatternRef | mandatory | 1..1 | ServiceJourneyPatternRefStructure |  | The reference to the ServiceJourneyPattern |
|  | TimeDemandTypeRef | mandatory | 0..1 | TimeDemandTypeRefStructure |  | The timing behaviour is defined here. We allow only one TimeDemandType per ServiceJourney. |
|  | VehicleTypeRef | expected | 0..1 | VehicleTypeRefStructure |  | Mostly used for accessibility information |
|  | trainNumbers | mandatory | 0..1 | trainNumberRefs_RelStructure | TRAIN NUMBERs -= derived through JOURNEY PARTs of a journey - for a multi-part journey only. |  |
| + | TrainNumberRef | mandatory | 0..* | TrainNumberRefStructure |  |  |
|  | [Destination](Destination.md) | expected | 0..1 | JourneyEndpointStructure | Destination for JOURNEY. |  |
|  | parts | optional | 0..1 | journeyParts_RelStructure | JOURNEY PARTs of a journey - for a multi-part journey only. | For some use cases e.g. change of Facilities during ServiceJourney |
| + | [JourneyPart](JourneyPart.md) | optional | 0..* | JourneyPart_VersionStructure | A part of a VEHICLE JOURNEY created according to a specific functional purpose, for instance in situations when vehicle coupling or separating occurs. | We don't expect JourneyPart for TemplateServiceJourney |
|  | TemplateVehicleJourneyType | expected | 0..1 | TemplateVehicleJourneyTypeEnumeration | Type of TEMPLATE VEHICLE JOURNEY. |  |
|  | frequencyGroups | mandatory | 0..1 | frequencyGroups_RelStructure | frequency groups defining Template journey. Can only be of one type. | We strictly map one frequency to the TemplateServiceJourney. |
| + | HeadwayJourneyGroup | mandatory | 0..* | HeadwayJourneyGroup_VersionStructure | A group of VEHICLE JOURNEYs following the same JOURNEY PATTERN and having the same headway interval between a specified start and end time (for example, ‘every 10 minutes’). This is especially useful for presenting passenger information. |  |
| ++ | ScheduledHeadwayInterval | mandatory | 0..1 | duration | Scheduled normal headway interval. |  |
| ++ | HeadwayDisplay | optional | 0..1 | HeadwayUseEnumeration | How headway value should be displayed to public. | Allowed values: displayPassingTimesOnly displayInsteadOfPassingTimes displayAsWellAsPassingTimes. We only export displayPassingTimesOnly. |
