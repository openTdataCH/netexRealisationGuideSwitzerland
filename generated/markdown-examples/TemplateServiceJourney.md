# TemplateServiceJourney

| Sub | Element | Usage | Card | Type | Description | Note |
|-----|---------|-------|------|------|-------------|------|
| + | validityConditions | expected | 1..1 | validityConditions_RelStructure | VALIDITY CONDITIONs conditioning entity. | A specific type of VALIDITY CONDITION used to specify a set of temporal conditions that can be associated with the SERVICE JOURNEY, for example that the corresponding journey only applies on particular days of a period (indicated by ValidDayBits, “Verkehrstagebitfeld”). |
| ++ | [AvailabilityCondition](AvailabilityCondition.md) | expected | 1..1 | unknown | VALIDITY CONDITION stated in terms of DAY TYPES and PROPERTIES OF DAYs. | **TODO** Expand the element, see ServiceJourney: more spacific requirements than standard AvailabilityCondition. |
| + | keyList | mandatory | 1..1 | KeyListStructure | A list of alternative Key values for an element. | KEY LIST with the KEY VALUEs belonging to the repeating SERVICE JOURNEYs. Will contain the SJYID. |
| ++ | KeyValue | mandatory | 1..* | KeyValueStructure | Key value pair for Entity. | A KeyValue pair with the Key SJYID must exist. The Value contains a valid Swiss Journey ID. |
| +++ | Key | mandatory | 1..1 | xsd:normalizedString | Identifier of value e.g. System. |  |
| +++ | Value | mandatory | 0..1 | xsd:anyType | Value associated with QUALITY STRUCTURE FACTOR. |  |
| + | Extensions | optional | 1..1 | ExtensionsStructure | User defined Extensions to ENTITY in schema. (Wrapper tag used to avoid problems with handling of optional 'any' by some validators). | Used to indicate Facility changes. |
| ++ | facilities | optional | 0..1 | serviceFacilitySets_RelStructure | FACILITies available associated with JOURNEY. |  |
| +++ | Facility | optional | 1..1 | unknown |  |  |
| ++++ | ServiceFacilitySetRef | mandatory | 1..1 | ServiceFacilitySetRefStructure | Reference to a SERVICE FACILITY SET. |  |
| + | PrivateCode | optional | 1..1 | PrivateCodeStructure | A private code that uniquely identifies the element. May be used for inter-operating with other (legacy) systems. | Private code of the repeating SERVICE JOURNEY. |
| + | TransportMode | optional | 0..1 | AllModesEnumeration | MODE. |  |
| + | TypeOfProductCategoryRef | expected | 1..1 | TypeOfProductCategoryRefStructure | Reference to a TYPE OF PRODUCT CATEGORY. Product of a JOURNEY. e.g. ICS, Thales etc
See ERA B.4 7037 Characteristic description code. |  |
| + | TypeOfServiceRef | optional | 1..1 | TypeOfServiceRefStructure | Reference to a TYPE OF SERVICE. |  |
| + | noticeAssignments | optional | 0..1 | noticeAssignments_RelStructure | NOTICEs relevant for the whole GROUP OF SINGLE JOURNEYs. | The complete set of all applicable notices. Attention: Notices may be restricted to a given set of stops. |
| ++ | [NoticeAssignment](NoticeAssignment.md) | optional | 1..1 | unknown | The assignment of a NOTICE showing an exception in a JOURNEY PATTERN, a COMMON SECTION, or a VEHICLE JOURNEY, possibly specifying at which POINT IN JOURNEY PATTERN the validity of the NOTICE starts and ends respectively. |  |
| + | occupancies | optional | 0..1 | OccupancyView_RelStructure | OCCUPANCYs associated with this journey. +v2.0 |  |
| ++ | [OccupancyView](OccupancyView.md) | optional | 1..1 | OccupancyView_VersionStructure |  |  |
| + | ServiceAlteration | mandatory | 0..1 | ServiceAlterationEnumeration | Whether journey is as planned, a cancellation or an extra journey. Default is as Planned. | Only the value planned is allowed. |
| + | DepartureTime | optional | 0..1 | xsd:time | Departure time. | **TODO** - does this make sense given that repeated journeys are described ? |
| + | DepartureDayOffset | optional | 0..1 | DayOffsetType | Departure Time Day Offset. | **TODO** - same question as above |
| + | LineRef | mandatory | 1..1 | LineRefStructure | Reference to a LINE. |  |
| + | DirectionType | optional | 0..1 | RelativeDirectionEnumeration | For fares for DISTANCE MATRIXE LEMENTs, DIRECTION in which price applies. | Allowed are: inbound, outbound |
| + | trainNumbers | mandatory | 0..1 | trainNumbersInFrame_RelStructure | TRAIN NUMBERs in frame. |  |
| ++ | TrainNumberRef | mandatory | 1..1 | TrainNumberRefStructure | Reference to a TRAIN NUMBER. |  |
| + | [Destination](Destination.md) | expected | 0..1 | TravelSpecificationSummaryEndpointStructure | Destination of Travel. Note that for a point-to-point TARIFF the origin is assigned with a DISTANCE MATRIX ELEMENT. | **TODO** needs to be created as well |
| + | passingTimes | expected | 0..1 | timetabledPassingTimes_RelStructure | PASSING TIMEs for VEHICLE JOURNEY. |  |
| ++ | [TimetabledPassingTime](TimetabledPassingTime.md) | expected | 1..1 | unknown | TIMETABLED PASSING TIME at TIMING POINT. |  |
| + | TemplateVehicleJourneyType | expected | 0..1 | TemplateVehicleJourneyTypeEnumeration | Type of TEMPLATE VEHICLE JOURNEY. |  |
| + | frequencyGroups | mandatory | 0..1 | frequencyGroupsInFrame_RelStructure | FREQUENCY GROUPs In frame. Can be used to template VEHICLE JOURNEYs. | We strictly map one JOURNEY FREQUENCY per SERVICE JOURNEY. |
| ++ | RhythmicalJourneyGroup | expected | 1..1 | unknown | A group of VEHICLE JOURNEYS following the same JOURNEY PATTERN having the same "rhythm" every hour (for example runs all xxh10, xxh25 and xxh45... e) between a specified start and end time. |  |
| +++ | Name | optional | 0..1 | MultilingualString | Name of Traveller | **TODO** - wanted? more advice on how to handle language? |
| +++ | Description | optional | 0..1 | MultilingualString | Description of contents. |  |
| +++ | FirstDepartureTime | mandatory | 1..1 | xsd:time | Time of first departure in JOURNEY FREQUENCY GROUP at the first stop. |  |
| +++ | FirstDayOffset | optional | 0..1 | DayOffsetType | Offset days for the first arrival time. Number of days after the first arrival time of the journey if not same calendar day. Default is 0 for the same day. |  |
| +++ | LastDepartureTime | mandatory | 0..1 | xsd:time | Time of last departure in JOURNEY FREQUENCY GROUP. |  |
| +++ | LastDayOffset | optional | 0..1 | DayOffsetType | Offset days for the last arrival time. Number of days after the last arrival time of the journey if not same calendar day. Default is 0 for the same day. |  |
| +++ | timebands | optional | 0..1 | timebandRefs_RelStructure | TIMEBANDS associated with JOURNEY FREQUENCY GROUP. |  |
| ++ | HeadwayJourneyGroup | optional | 1..1 | unknown | A group of VEHICLE JOURNEYs following the same JOURNEY PATTERN and having the same headway interval between a specified start and end time (for example, ‘every 10 minutes’). This is especially useful for presenting passenger information. |  |
| +++ | ScheduledHeadwayInterval | mandatory | 0..1 | xsd:duration | Scheduled normal headway interval. |  |
| +++ | HeadwayDisplay | optional | 0..1 | HeadwayUseEnumeration | How headway value should be displayed to public. | Allowed values: displayPassingTimesOnly displayInsteadOfPassingTimes displayAsWellAsPassingTimes. We only export displayPassingTimesOnly. |
