# ServiceFacilitySet

List of ServiceFacility. Be careful: not all are supported. Consult profile. Make sure to not generate identical ServiceFacilitySets. Reuse them. Details in the mapping excel.

*Table: ServiceFacilitySet*

| Sub | Element | Usage | Card | Type | Description | Note |
|-----|---------|-------|------|------|-------------|------|
|  | @id | mandatory | 1..1 | xsd:string | Attribute id | |
|  | @version | mandatory | 1..1 | xsd:string | Attribute version | |
|  | Extensions | expected | 1..1 | ExtensionsStructure |  | Two elements used in HRDF for ordering facilities |
| + | Priority | expected | 0..1 | InterchangePriorityType |  |  |
|  | Description | expected | 0..1 | MultilingualString |  |  |
| + | @lang | mandatory | 1..1 | xsd:string | Attribute lang | |
| + | Text | optional | 0..* | MultilingualString |  |  |
| ++ | @lang | mandatory | 1..1 | xsd:string | Attribute lang | |
|  | FareClasses | optional | 1..1 | FareClassListOfEnumerations |  |  |
|  | MobilityFacilityList | optional | 1..1 | MobilityFacilityListOfEnumerations |  |  |
|  | NuisanceFacilityList | optional | 1..1 | NuisanceFacilityListOfEnumerations |  |  |
|  | PassengerCommsFacilityList | optional | 1..1 | PassengerCommsFacilityListOfEnumerations |  |  |
|  | SanitaryFacilityList | optional | 1..1 | SanitaryFacilityListOfEnumerations |  |  |
|  | CouchetteFacilityList | optional | 1..1 | CouchetteFacilityListOfEnumerations |  |  |
|  | GroupBookingFacility | optional | 1..1 | GroupBookingEnumeration |  |  |
