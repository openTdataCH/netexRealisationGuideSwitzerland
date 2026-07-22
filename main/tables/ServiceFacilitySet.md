# ServiceFacilitySet

List of ServiceFacility. Be careful: not all are supported. Consult profile. Make sure to not generate identical ServiceFacilitySets. Reuse them. Details in the mapping excel.

*Table: ServiceFacilitySet*

| Sub | Element | Usage | Card | Type | Description | Note |
|-----|---------|-------|------|------|-------------|------|
|  | @id | mandatory | 1..1 | xsd:string | Attribute id | |
|  | @version | mandatory | 1..1 | xsd:string | Attribute version | |
|  | Extensions | expected | 1..1 | ExtensionsStructure | User defined Extensions to ENTITY in schema. (Wrapper tag used to avoid problems with handling of optional 'any' by some validators). | Two elements used in HRDF for ordering facilities |
| + | Priority | expected | 0..1 | InterchangePriorityType | Priority to assign to this INTERCHANGE. |  |
|  | Description | expected | 0..* | MultilingualString | Description of contents. |  |
| + | @lang | mandatory | 1..1 | xsd:string | Attribute lang | |
| + | Text | optional | 0..* | MultilingualString | Text content of NOTICe. |  |
| ++ | @lang | mandatory | 1..1 | xsd:string | Attribute lang | |
|  | FareClasses | optional | 1..1 | FareClassListOfEnumerations | List of FARE CLASSes. |  |
|  | MobilityFacilityList | optional | 1..1 | MobilityFacilityListOfEnumerations | List of MOBILITY FACILITies. |  |
|  | NuisanceFacilityList | optional | 1..1 | NuisanceFacilityListOfEnumerations | List of NUISANCE FACILITies. |  |
|  | PassengerCommsFacilityList | optional | 1..1 | PassengerCommsFacilityListOfEnumerations | List of PASSENGER COMMS FACILITies. |  |
|  | SanitaryFacilityList | optional | 1..1 | SanitaryFacilityListOfEnumerations | List of SANITARY FACILITies. |  |
|  | CouchetteFacilityList | optional | 1..1 | CouchetteFacilityListOfEnumerations | List of COUCHETTE FACILITies. |  |
|  | GroupBookingFacility | optional | 1..1 | GroupBookingEnumeration | Classification of GROUP FACILITY type - TPEG pti23. |  |
