# ServiceFacilitySet

List of ServiceFacility. Be careful: not all are supported. Consult profile. Make sure to not generate identical ServiceFacilitySets. Reuse them. Details in the mapping excel.

*Table: ServiceFacilitySet*

| Sub | Element | Usage | Card | Type | Description | Note |
|-----|---------|-------|------|------|-------------|------|
|  | @id | mandatory | 1..1 | xsd:string | Attribute id | |
|  | @version | mandatory | 1..1 | xsd:string | Attribute version | |
|  | Extensions | expected | 0..1 | ExtensionsStructure |  | Two elements used in HRDF for ordering facilities |
| + | Priority | expected | 0..1 | InterchangePriorityType |  |  |
|  | Description | expected | 0..1 | MultilingualString |  |  |
| + | @lang | mandatory | 1..1 | xsd:string | Attribute lang | |
| + | Text | optional | 0..* | MultilingualString |  | For each language a Text element must be provided |
| ++ | @lang | mandatory | 1..1 | xsd:string | Attribute lang | |
|  | FareClasses | optional | 0..1 | FareClassListOfEnumerations | List of Fare Classes. |  |
|  | MobilityFacilityList | optional | 0..1 | MobilityFacilityListOfEnumerations | List of MOBILITY FACILITies. |  |
|  | NuisanceFacilityList | optional | 0..1 | NuisanceFacilityListOfEnumerations | List of NUISANCE FACILITies. |  |
|  | PassengerCommsFacilityList | optional | 0..1 | PassengerCommsFacilityListOfEnumerations | List of PASSENGER COMMS FACILITies. |  |
|  | SanitaryFacilityList | optional | 0..1 | SanitaryFacilityListOfEnumerations | List of SANITARY FACILITies. |  |
|  | CouchetteFacilityList | optional | 0..1 | CouchetteFacilityListOfEnumerations | List of COUCHETTE FACILITies. |  |
|  | GroupBookingFacility | optional | 0..1 | GroupBookingEnumeration | Classification of GROUP FACILITY type - TPEG pti23. |  |
