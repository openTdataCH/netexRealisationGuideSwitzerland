# TemplateServiceJourney

TemplateServiceJourney is used for journeys repeating at a certain frequency.

*Table: TemplateServiceJourney*

| Sub | Element | Usage | Card | Type | Description | Note |
|-----|---------|-------|------|------|-------------|------|
|  | @id | mandatory | 1..1 | xsd:string | Attribute id | |
|  | @version | mandatory | 1..1 | xsd:string | Attribute version | |
|  | @responsibilitySetRef | mandatory | 1..1 | xsd:string | Attribute responsibilitySetRef | |
|  | validityConditions | mandatory | 1..1 | validityConditions_RelStructure | VALIDITY CONDITIONs conditioning entity. | Used to specify a set of temporal conditions that can be associated with the ServiceJourney, for example that the corresponding journey only applies on particular days of a period (indicated by ValidDayBits, “Verkehrstagebitfeld”). |
| + | AvailabilityConditionRef | mandatory | 1..1 | AvailabilityConditionRefStructure | Reference to an AVAILABILITY CONDITION. A VALIDITY CONDITION defined in terms of temporal attributes. | Only a single AvailabilityConditionRef is allowed. |
|  | keyList | mandatory | 1..1 | KeyListStructure | A list of alternative Key values for an element. | Key list for the repeating journeys. Contains the SJYID. |
| + | KeyValue | mandatory | 1..* | KeyValueStructure | Key value pair for Entity. | A KeyValue pair with the key SJYID must exist. The Value contains a valid Swiss Journey ID. |
| ++ | Key | mandatory | 1..1 | xsd:normalizedString | Identifier of value e.g. System. |  |
| ++ | Value | mandatory | 0..1 | xsd:anyType | Value associated with QUALITY STRUCTURE FACTOR. |  |
|  | privateCodes | expected | 1..1 | PrivateCodesStructure | A list of private codes that uniquely identifiy the element. May be used for inter-operating with other (legacy) systems. +v2.0 | Replaces the single PrivateCode. The following types are possible: sjyid and rn. rn is the type used for the Postauto region |
| + | PrivateCode | expected | 0..* | PrivateCodeStructure | A private code that uniquely identifies the element. May be used for inter-operating with other (legacy) systems. |  |
|  | TransportMode | optional | 0..1 | AllModesEnumeration | MODE. |  |
|  | TypeOfProductCategoryRef | expected | 1..1 | TypeOfProductCategoryRefStructure | Reference to a TYPE OF PRODUCT CATEGORY. Product of a JOURNEY. e.g. ICS, Thales etc See ERA B.4 7037 Characteristic description code. |  |
|  | TypeOfServiceRef | optional | 1..1 | TypeOfServiceRefStructure | Reference to a TYPE OF SERVICE. |  |
|  | noticeAssignments | optional | 0..1 | noticeAssignments_RelStructure | NOTICEs relevant for the whole GROUP OF SINGLE JOURNEYs. | The complete set of all applicable notices. Attention: Notices may be restricted to a given set of stops. |
| + | [NoticeAssignment](NoticeAssignment.md) | optional | 1..1 | NoticeAssignment | The assignment of a NOTICE showing an exception in a JOURNEY PATTERN, a COMMON SECTION, or a VEHICLE JOURNEY, possibly specifying at which POINT IN JOURNEY PATTERN the validity of the NOTICE starts and ends respectively. |  |
|  | occupancies | optional | 0..1 | OccupancyView_RelStructure | OCCUPANCYs associated with this journey. +v2.0 |  |
| + | [OccupancyView](OccupancyView.md) | optional | 1..1 | OccupancyView_VersionStructure | A simple VIEW of OCCUPANCY as a first implementation without full support of DECK PLAN. |  |
|  | ServiceAlteration | mandatory | 0..1 | ServiceAlterationEnumeration | Whether journey is as planned, a cancellation or an extra journey. Default is as Planned. | Only the value planned is allowed. |
|  | DepartureTime | optional | 0..1 | xsd:time | Departure time. | Departure of the first journey. |
|  | DepartureDayOffset | optional | 0..1 | DayOffsetType | Departure Time Day Offset. | DayOffset if relevant. |
|  | JourneyPatternRef | mandatory | 1..1 | JourneyPatternRefStructure | Reference to a JOURNEY PATTERN. | The reference to the ServiceJourneyPattern |
| + | @nameOfRefClass | mandatory | 1..1 | xsd:string | Attribute nameOfRefClass | |
|  | TimeDemandTypeRef | mandatory | 0..1 | TimeDemandTypeRefStructure | Reference to a TIME DEMAND TYPE used at start of JOURNEY. | The timing behaviour is defined here. We allow only one TimeDemandType per ServiceJourney. |
|  | VehicleTypeRef | expected | 1..1 | VehicleTypeRefStructure | Reference to a VEHICLE TYPE. | Mostly used for accessibility information |
|  | LineRef | mandatory | 1..1 | LineRefStructure | Reference to a LINE. |  |
|  | DirectionType | optional | 0..1 | RelativeDirectionEnumeration | For fares for DISTANCE MATRIXE LEMENTs, DIRECTION in which price applies. | Allowed are: inbound, outbound |
|  | trainNumbers | mandatory | 0..1 | trainNumbersInFrame_RelStructure | TRAIN NUMBERs in frame. |  |
| + | TrainNumberRef | mandatory | 1..1 | TrainNumberRefStructure | Reference to a TRAIN NUMBER. |  |
|  | [Destination](Destination.md) | expected | 0..1 | TravelSpecificationSummaryEndpointStructure | Destination of Travel. Note that for a point-to-point TARIFF the origin is assigned with a DISTANCE MATRIX ELEMENT. |  |
|  | parts | optional | 0..1 | blockParts_RelStructure | BLOCK PARTs which make up COMPOUND BLOCK. | For some use cases e.g. change of Facilities during ServiceJourney |
| + | JourneyPartRef | expected | 1..1 | JourneyPartRefStructure | Reference to a JOURNEY PART. |  |
|  | TemplateVehicleJourneyType | expected | 0..1 | TemplateVehicleJourneyTypeEnumeration | Type of TEMPLATE VEHICLE JOURNEY. |  |
|  | frequencyGroups | mandatory | 0..1 | frequencyGroupsInFrame_RelStructure | FREQUENCY GROUPs In frame. Can be used to template VEHICLE JOURNEYs. | We strictly map one frequency to the TemplateServiceJourney. |
| + | HeadwayJourneyGroup | mandatory | 1..1 | HeadwayJourneyGroup | A group of VEHICLE JOURNEYs following the same JOURNEY PATTERN and having the same headway interval between a specified start and end time (for example, ‘every 10 minutes’). This is especially useful for presenting passenger information. |  |
| ++ | ScheduledHeadwayInterval | mandatory | 0..1 | xsd:duration | Scheduled normal headway interval. |  |
| ++ | HeadwayDisplay | optional | 0..1 | HeadwayUseEnumeration | How headway value should be displayed to public. | Allowed values: displayPassingTimesOnly displayInsteadOfPassingTimes displayAsWellAsPassingTimes. We only export displayPassingTimesOnly. |
