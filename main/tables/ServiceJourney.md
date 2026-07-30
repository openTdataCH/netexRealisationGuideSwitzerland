# ServiceJourney

*Table: ServiceJourney*

| Sub | Element | Usage | Card | Type | Description | Note |
|-----|---------|-------|------|------|-------------|------|
|  | @id | mandatory | 1..1 | xsd:string | Attribute id | |
|  | @version | mandatory | 1..1 | xsd:string | Attribute version | |
|  | @responsibilitySetRef | mandatory | 1..1 | xsd:string | Attribute responsibilitySetRef | |
|  | validityConditions | mandatory | 1..1 | validityConditions_RelStructure | VALIDITY CONDITIONs conditioning entity. | Used to specify a set of temporal conditions that can be associated with the ServiceJourney, for example that the corresponding journey only applies on particular days of a period (indicated by ValidDayBits, “Verkehrstagebitfeld”). |
| + | AvailabilityConditionRef | mandatory | 0..* | AvailabilityConditionRefStructure | Reference to an AVAILABILITY CONDITION. A VALIDITY CONDITION defined in terms of temporal attributes. | Only a single AvailabilityConditionRef is allowed. |
|  | keyList | optional | 0..1 | KeyListStructure | A list of alternative Key values for an element. | KEY LIST with the KEY VALUEs belonging to the SERVICE JOURNEY. We don't use it for sjyid! |
| + | KeyValue | optional | 1..* | KeyValueStructure | Key value pair for Entity. | We use it for tariff codes and region codes PAG mostly. |
| ++ | Key | optional | 0..1 | xsd:normalizedString | User key. |  |
| ++ | Value | optional | 0..1 | xsd:anyType | Value for alternative key. |  |
|  | privateCodes | expected | 0..1 | PrivateCodesStructure | A list of private codes that uniquely identifiy the element. May be used for inter-operating with other (legacy) systems. +v2.0 |  |
| + | PrivateCode | expected | 0..* | PrivateCodeStructure | A private code that uniquely identifies the element. May be used for inter-operating with other (legacy) systems. | The following types are possible: sjyid and rn. rn is the type used for the Postauto region. |
| ++ | @type | mandatory | 1..1 | xsd:string | Attribute type | |
|  | TransportMode | optional | 0..1 | AllModesEnumeration | An area within a Site. May be connected to Quays by PATH LINKs. |  |
|  | TypeOfProductCategoryRef | mandatory | 1..1 | TypeOfProductCategoryRefStructure | Reference to a TYPE OF PRODUCT CATEGORY. Product of a JOURNEY. e.g. ICS, Thales etc See ERA B.4 7037 Characteristic description code. | Relevant elements are defined in the mapping excel. |
|  | TypeOfServiceRef | optional | 1..1 | TypeOfServiceRefStructure | Reference to a TYPE OF SERVICE. | Should always be ch:1:TypeOfService:1 |
|  | noticeAssignments | optional | 0..1 | noticeAssignments_RelStructure | NOTICE ASSIGNMENTs in frame. | The complete set of all applicable Notices. Attention: Notices may be restricted to a a part of the journey (by defining the first and last stop). |
| + | [NoticeAssignment](NoticeAssignment.md) | optional | 0..* | NoticeAssignment_VersionStructure | The assignment of a NOTICE showing an exception in a JOURNEY PATTERN, a COMMON SECTION, or a VEHICLE JOURNEY, possibly specifying at which POINT IN JOURNEY PATTERN the validity of the NOTICE starts and ends respectively. |  |
|  | occupancies | optional | 0..1 | OccupancyView_RelStructure | OCCUPANCYs in frame. |  |
| + | [OccupancyView](OccupancyView.md) | optional | 0..* | OccupancyView_VersionStructure | A simple VIEW of OCCUPANCY as a first implementation without full support of DECK PLAN. | Currently not available |
|  | ServiceAlteration | mandatory | 0..1 | ServiceAlterationEnumeration | Whether journey is as planned, a cancellation or an extra journey. Default is as Planned. | Only the value planned is allowed. We might add the others, like cancelled, later. |
|  | DepartureTime | expected | 0..1 | xsd:time | Time of departure of JOURNEY from POINT. |  |
|  | DepartureDayOffset | optional | 0..1 | DayOffsetType | Daya offset if Time of departure of JOURNEY from origin POINT from current OPERATING DAY. | 0 for current operating day. Could also be negative. |
|  | JourneyPatternRef | mandatory | 1..* | JourneyPatternRefStructure | Reference to a JOURNEY PATTERN. | The reference to the ServiceJourneyPattern. |
| + | @nameOfRefClass | mandatory | 1..1 | xsd:string | Attribute nameOfRefClass | |
|  | TimeDemandTypeRef | mandatory | 0..1 | TimeDemandTypeRefStructure | Reference to a TIME DEMAND TYPE. If given by context need not be stated. | The timing behaviour is defined here. We allow only one TimeDemandType per ServiceJourney. |
|  | VehicleTypeRef | expected | 1..* | VehicleTypeRefStructure | Reference to a VEHICLE TYPE. | Mostly used for accessibility information like NF. Relevant definitions in the mapping excel. |
|  | LineRef | mandatory | 1..* | LineRefStructure | Reference to a LINE. |  |
|  | DirectionType | mandatory | 0..1 | RelativeDirectionEnumeration | A Direction of a ROUTE. One of a restricted set of values. Default is "Outbound" | Allowed are: inbound, outbound |
|  | trainNumbers | mandatory | 0..1 | trainNumbersInFrame_RelStructure | TRAIN NUMBERs -= derived through JOURNEY PARTs of a journey - for a multi-part journey only. |  |
| + | TrainNumberRef | mandatory | 0..* | TrainNumberRefStructure | Reference to a TRAIN NUMBER. |  |
|  | [Destination](Destination.md) | expected | 0..1 | TravelSpecificationSummaryEndpointStructure | Destination for JOURNEY. |  |
|  | parts | optional | 0..1 | blockParts_RelStructure | Parts of the ORGANISATION. | For some use cases e.g. change of Facilities during ServiceJourney |
| + | JourneyPartRef | expected | 0..* | JourneyPartRefStructure | Reference to a JOURNEY PART. |  |
|  | checkConstraints | optional | 0..1 | checkConstraints_RelStructure | CHECK CONSTRAINTs in frame. |  |
| + | CheckConstraint | optional | 1..* | CheckConstraint_VersionStructure | Characteristics of a SITE COMPONENT representing a process, such as check-in, security screening, ticket control or immigration, that may potentially incur a time penalty that should be allowed for when journey planning. Used to mark PATH LINKs to determine transit routes through interchanges. | CheckConstraints are used for different use cases |
