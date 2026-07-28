# SiteFacilitySet

List of SiteFacility. Be careful: not all are supported. Consult profile. Make sure to not generate identical SiteFacilitySets. Reuse them. There might be an overlap to ServiceFacilitySet, but they are used for different purposes.

*Table: SiteFacilitySet*

| Sub | Element | Usage | Card | Type | Description | Note |
|-----|---------|-------|------|------|-------------|------|
|  | @id | mandatory | 1..1 | xsd:string | Attribute id | |
|  | @version | mandatory | 1..1 | xsd:string | Attribute version | |
|  | validityConditions | optional | 1..1 | validityConditions_RelStructure |  |  |
| + | [AvailabilityCondition](AvailabilityCondition.md) | optional | 1..1 | unknown |  |  |
|  | Description | optional | 0..1 | MultilingualString |  | Description is optional |
| + | @lang | mandatory | 1..1 | xsd:string | Attribute lang | |
| + | Text | optional | 0..* | MultilingualString |  |  |
| ++ | @lang | mandatory | 1..1 | xsd:string | Attribute lang | |
|  | AssistanceFacilityList | optional | 1..1 | AssistanceFacilityListOfEnumerations |  |  |
|  | AccessibilityToolList | optional | 0..1 | AccessibilityToolListOfEnumerations |  |  |
|  | SanitaryFacilityList | optional | 1..1 | SanitaryFacilityListOfEnumerations |  |  |
|  | TicketingServiceFacilityList | optional | 1..1 | TicketingServiceFacilityListOfEnumerations |  |  |
|  | EmergencyServiceList | optional | 0..1 | EmergencyServiceListOfEnumerations |  |  |
|  | LuggageLockerFacilityList | optional | 1..1 | LuggageLockerFacilityListOfEnumerations |  |  |
|  | ParkingFacilityList | optional | 1..1 | ParkingFacilityListOfEnumerations |  |  |
