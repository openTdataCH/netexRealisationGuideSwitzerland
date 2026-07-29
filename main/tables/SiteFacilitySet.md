# SiteFacilitySet

List of SiteFacility. Be careful: not all are supported. Consult profile. Make sure to not generate identical SiteFacilitySets. Reuse them. There might be an overlap to ServiceFacilitySet, but they are used for different purposes.

*Table: SiteFacilitySet*

| Sub | Element | Usage | Card | Type | Description | Note |
|-----|---------|-------|------|------|-------------|------|
|  | @id | mandatory | 1..1 | xsd:string | Attribute id | |
|  | @version | mandatory | 1..1 | xsd:string | Attribute version | |
|  | validityConditions | optional | 0..1 | validityConditions_RelStructure | SITE FACILITY SETs in frame . +v1.2.2 |  |
| + | [AvailabilityCondition](AvailabilityCondition.md) | optional | 0..* | siteFacilitySetsInFrame_RelStructure | SITE FACILITY SETs in frame . +v1.2.2 |  |
|  | Description | optional | 0..1 | MultilingualString | SITE FACILITY SETs in frame . +v1.2.2 | Description is optional |
| + | @lang | mandatory | 1..1 | xsd:string | Attribute lang | |
| + | Text | optional | 0..* | MultilingualString | SITE FACILITY SETs in frame . +v1.2.2 |  |
| ++ | @lang | mandatory | 1..1 | xsd:string | Attribute lang | |
|  | AssistanceFacilityList | optional | 0..1 | AssistanceFacilityListOfEnumerations | SITE FACILITY SETs in frame . +v1.2.2 |  |
|  | AccessibilityToolList | optional | 0..1 | AccessibilityToolListOfEnumerations | SITE FACILITY SETs in frame . +v1.2.2 |  |
|  | SanitaryFacilityList | optional | 0..1 | SanitaryFacilityListOfEnumerations | SITE FACILITY SETs in frame . +v1.2.2 |  |
|  | TicketingServiceFacilityList | optional | 0..1 | TicketingServiceFacilityListOfEnumerations | SITE FACILITY SETs in frame . +v1.2.2 |  |
|  | EmergencyServiceList | optional | 0..1 | EmergencyServiceListOfEnumerations | SITE FACILITY SETs in frame . +v1.2.2 |  |
|  | LuggageLockerFacilityList | optional | 0..1 | LuggageLockerFacilityListOfEnumerations | SITE FACILITY SETs in frame . +v1.2.2 |  |
|  | ParkingFacilityList | optional | 0..1 | ParkingFacilityListOfEnumerations | SITE FACILITY SETs in frame . +v1.2.2 |  |
