# TemplateServiceJourney

TemplateServiceJourney is used for journeys repeating at a certain frequency.

*Table: TemplateServiceJourney*

| Sub | Element | Usage | Card | Type | Description | Note |
|-----|---------|-------|------|------|-------------|------|
|  | @id | mandatory | 1..1 | xsd:string | Attribute id | |
|  | @version | mandatory | 1..1 | xsd:string | Attribute version | |
|  | @responsibilitySetRef | mandatory | 1..1 | xsd:string | Attribute responsibilitySetRef | |
|  | validityConditions | mandatory | 1..1 | validityConditions_RelStructure | VALIDITY CONDITIONs conditioning entity. | Used to specify a set of temporal conditions that can be associated with the ServiceJourney, for example that the corresponding journey only applies on particular days of a period (indicated by ValidDayBits, “Verkehrstagebitfeld”). |
| + | AvailabilityConditionRef | mandatory | 0..* | AvailabilityConditionRefStructure | Reference to an AVAILABILITY CONDITION. A VALIDITY CONDITION defined in terms of temporal attributes. | Only a single AvailabilityConditionRef is allowed. |
|  | privateCodes | expected | 0..1 | PrivateCodesStructure | A list of private codes that uniquely identifiy the element. May be used for inter-operating with other (legacy) systems. +v2.0 | Replaces the single PrivateCode. |
| + | PrivateCode | expected | 0..* | PrivateCodeStructure | A private code that uniquely identifies the element. May be used for inter-operating with other (legacy) systems. | Mandatory if available for the following types: sjyid and rn. rn is the type used for the Postauto region. |
| ++ | @type | mandatory | 1..1 | xsd:string | Attribute type | |
|  | TransportMode | optional | 0..1 | AllModesEnumeration | An area within a Site. May be connected to Quays by PATH LINKs. |  |
|  | TypeOfProductCategoryRef | expected | 1..1 | TypeOfProductCategoryRefStructure | Reference to a TYPE OF PRODUCT CATEGORY. Product of a JOURNEY. e.g. ICS, Thales etc See ERA B.4 7037 Characteristic description code. |  |
|  | TypeOfServiceRef | optional | 1..1 | TypeOfServiceRefStructure | Reference to a TYPE OF SERVICE. |  |
|  | noticeAssignments | optional | 0..1 | noticeAssignments_RelStructure | NOTICE ASSIGNMENTs in frame. | The complete set of all applicable notices. Attention: Notices may be restricted to a given set of stops. |
| + | [NoticeAssignment](NoticeAssignment.md) | optional | 0..* | NoticeAssignment_VersionStructure | The assignment of a NOTICE showing an exception in a JOURNEY PATTERN, a COMMON SECTION, or a VEHICLE JOURNEY, possibly specifying at which POINT IN JOURNEY PATTERN the validity of the NOTICE starts and ends respectively. |  |
|  | occupancies | optional | 0..1 | OccupancyView_RelStructure | OCCUPANCYs in frame. |  |
| + | [OccupancyView](OccupancyView.md) | optional | 0..* | OccupancyView_VersionStructure | A simple VIEW of OCCUPANCY as a first implementation without full support of DECK PLAN. | Currently not available. |
|  | ServiceAlteration | mandatory | 0..1 | ServiceAlterationEnumeration | Whether journey is as planned, a cancellation or an extra journey. Default is as Planned. | Only the value planned is allowed. |
|  | DepartureTime | optional | 0..1 | xsd:time | Time of departure of JOURNEY from POINT. | Departure of the first journey. |
|  | DepartureDayOffset | optional | 0..1 | DayOffsetType | Daya offset if Time of departure of JOURNEY from origin POINT from current OPERATING DAY. | DayOffset if relevant. |
|  | JourneyPatternRef | mandatory | 1..* | JourneyPatternRefStructure | Reference to a JOURNEY PATTERN. | The reference to the ServiceJourneyPattern |
| + | @nameOfRefClass | mandatory | 1..1 | xsd:string | Attribute nameOfRefClass | |
|  | TimeDemandTypeRef | mandatory | 0..1 | TimeDemandTypeRefStructure | Reference to a TIME DEMAND TYPE. If given by context need not be stated. | The timing behaviour is defined here. We allow only one TimeDemandType per ServiceJourney. |
|  | VehicleTypeRef | expected | 1..* | VehicleTypeRefStructure | Reference to a VEHICLE TYPE. | Mostly used for accessibility information |
|  | LineRef | mandatory | 1..* | LineRefStructure | Reference to a LINE. |  |
|  | DirectionType | optional | 0..1 | RelativeDirectionEnumeration | A Direction of a ROUTE. One of a restricted set of values. Default is "Outbound" | Allowed are: inbound, outbound |
|  | trainNumbers | mandatory | 0..1 | trainNumbersInFrame_RelStructure | TRAIN NUMBERs -= derived through JOURNEY PARTs of a journey - for a multi-part journey only. |  |
| + | TrainNumberRef | mandatory | 0..* | TrainNumberRefStructure | Reference to a TRAIN NUMBER. |  |
|  | [Destination](Destination.md) | expected | 0..1 | TravelSpecificationSummaryEndpointStructure | Destination for JOURNEY. |  |
|  | parts | optional | 0..1 | blockParts_RelStructure | Parts of the ORGANISATION. | For some use cases e.g. change of Facilities during ServiceJourney |
| + | JourneyPartRef | expected | 0..* | JourneyPartRefStructure | Reference to a JOURNEY PART. |  |
|  | TemplateVehicleJourneyType | expected | 0..1 | TemplateVehicleJourneyTypeEnumeration | Type of TEMPLATE VEHICLE JOURNEY. |  |
|  | frequencyGroups | mandatory | 0..1 | frequencyGroupsInFrame_RelStructure | frequency groups defining Template journey. Can only be of one type. | We strictly map one frequency to the TemplateServiceJourney. |
| + | HeadwayJourneyGroup | mandatory | 0..* | HeadwayJourneyGroup_VersionStructure | A group of VEHICLE JOURNEYs following the same JOURNEY PATTERN and having the same headway interval between a specified start and end time (for example, ‘every 10 minutes’). This is especially useful for presenting passenger information. |  |
| ++ | ScheduledHeadwayInterval | mandatory | 0..1 | xsd:duration | Scheduled normal headway interval. |  |
| ++ | HeadwayDisplay | optional | 0..1 | HeadwayUseEnumeration | Use to be made of Headway information when displaying to public. Default is Display Instead of Passing Times. | Allowed values: displayPassingTimesOnly displayInsteadOfPassingTimes displayAsWellAsPassingTimes. We only export displayPassingTimesOnly. |
