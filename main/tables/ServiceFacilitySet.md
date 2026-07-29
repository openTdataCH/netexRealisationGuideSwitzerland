# ServiceFacilitySet

List of ServiceFacility. Be careful: not all are supported. Consult profile. Make sure to not generate identical ServiceFacilitySets. Reuse them. Details in the mapping excel.

*Table: ServiceFacilitySet*

| Sub | Element | Usage | Card | Type | Description | Note |
|-----|---------|-------|------|------|-------------|------|
|  | @id | mandatory | 1..1 | xsd:string | Attribute id | |
|  | @version | mandatory | 1..1 | xsd:string | Attribute version | |
|  | Extensions | expected | 0..1 | ExtensionsStructure | SERVICE FACILITies in frame. | Two elements used in HRDF for ordering facilities |
| + | Priority | expected | 0..1 | InterchangePriorityType | SERVICE FACILITies in frame. |  |
|  | Description | expected | 0..1 | MultilingualString | SERVICE FACILITies in frame. |  |
| + | @lang | mandatory | 1..1 | xsd:string | Attribute lang | |
| + | Text | optional | 0..* | MultilingualString | SERVICE FACILITies in frame. |  |
| ++ | @lang | mandatory | 1..1 | xsd:string | Attribute lang | |
|  | FareClasses | optional | 0..1 | FareClassListOfEnumerations | SERVICE FACILITies in frame. |  |
|  | MobilityFacilityList | optional | 0..1 | MobilityFacilityListOfEnumerations | SERVICE FACILITies in frame. |  |
|  | NuisanceFacilityList | optional | 0..1 | NuisanceFacilityListOfEnumerations | SERVICE FACILITies in frame. |  |
|  | PassengerCommsFacilityList | optional | 0..1 | PassengerCommsFacilityListOfEnumerations | SERVICE FACILITies in frame. |  |
|  | SanitaryFacilityList | optional | 0..1 | SanitaryFacilityListOfEnumerations | SERVICE FACILITies in frame. |  |
|  | CouchetteFacilityList | optional | 0..1 | CouchetteFacilityListOfEnumerations | SERVICE FACILITies in frame. |  |
|  | GroupBookingFacility | optional | 0..1 | GroupBookingEnumeration | SERVICE FACILITies in frame. |  |
