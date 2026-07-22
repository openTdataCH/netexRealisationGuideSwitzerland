# SiteFacilitySet

List of SiteFacility. Be careful: not all are supported. Consult profile. Make sure to not generate identical SiteFacilitySets. Reuse them. There might be an overlap to ServiceFacilitySet, but they are used for different purposes.

*Table: SiteFacilitySet*

| Sub | Element | Usage | Card | Type | Description | Note |
|-----|---------|-------|------|------|-------------|------|
|  | @id | mandatory | 1..1 | xsd:string | Attribute id | |
|  | @version | mandatory | 1..1 | xsd:string | Attribute version | |
|  | validityConditions | optional | 1..1 | validityConditions_RelStructure | VALIDITY CONDITIONs conditioning entity. |  |
| + | [AvailabilityCondition](AvailabilityCondition.md) | optional | 1..1 | AvailabilityCondition | VALIDITY CONDITION stated in terms of DAY TYPES and PROPERTIES OF DAYs. |  |
|  | Description | optional | 0..* | MultilingualString | Description of contents. | Description is optional |
| + | @lang | mandatory | 1..1 | xsd:string | Attribute lang | |
| + | Text | optional | 0..* | MultilingualString | Text content of NOTICe. |  |
| ++ | @lang | mandatory | 1..1 | xsd:string | Attribute lang | |
|  | AssistanceFacilityList | optional | 1..1 | AssistanceFacilityListOfEnumerations | List of ASSISTANCE FACILITies. |  |
|  | AccessibilityToolList | optional | 0..1 | AccessibilityToolListOfEnumerations |  |  |
|  | SanitaryFacilityList | optional | 1..1 | SanitaryFacilityListOfEnumerations | List of SANITARY FACILITies. |  |
|  | TicketingServiceFacilityList | optional | 1..1 | TicketingServiceFacilityListOfEnumerations | List of TICKETING SERVICE FACILITies, e.g. purchase, collection. top up. |  |
|  | EmergencyServiceList | optional | 0..1 | EmergencyServiceListOfEnumerations | Emergency service assistance available. |  |
|  | LuggageLockerFacilityList | optional | 1..1 | LuggageLockerFacilityListOfEnumerations | List of LUGGAGE LOCKER FACILITies. |  |
|  | ParkingFacilityList | optional | 1..1 | ParkingFacilityListOfEnumerations | List of PARKING FACILITies. |  |
