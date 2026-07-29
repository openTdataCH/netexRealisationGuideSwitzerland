# ServiceFacilitySet

List of ServiceFacility. Be careful: not all are supported. Consult profile. Make sure to not generate identical ServiceFacilitySets. Reuse them. Details in the mapping excel.

*Table: ServiceFacilitySet*

| Sub | Element | Usage | Card | Type | Description | Note |
|-----|---------|-------|------|------|-------------|------|
|  | @id | mandatory | 1..1 | xsd:string | Attribute id | |
|  | @version | mandatory | 1..1 | xsd:string | Attribute version | |
|  | Extensions | expected | 0..1 | ExtensionsStructure | SERVICE FACILITY SETs in frame . +v1.2.2 | Two elements used in HRDF for ordering facilities |
| + | Priority | expected | 0..1 | InterchangePriorityType | SERVICE FACILITY SETs in frame . +v1.2.2 |  |
|  | Description | expected | 0..1 | MultilingualString |  |  |
| + | @lang | mandatory | 1..1 | xsd:string | Attribute lang | |
| + | Text | optional | 0..* | MultilingualString | SERVICE FACILITY SETs in frame . +v1.2.2 |  |
| ++ | @lang | mandatory | 1..1 | xsd:string | Attribute lang | |
|  | FareClasses | optional | 0..1 | FareClassListOfEnumerations | SERVICE FACILITY SETs in frame . +v1.2.2 |  |
|  | MobilityFacilityList | optional | 0..1 | MobilityFacilityListOfEnumerations | SERVICE FACILITY SETs in frame . +v1.2.2 |  |
|  | NuisanceFacilityList | optional | 0..1 | NuisanceFacilityListOfEnumerations | SERVICE FACILITY SETs in frame . +v1.2.2 |  |
|  | PassengerCommsFacilityList | optional | 0..1 | PassengerCommsFacilityListOfEnumerations | SERVICE FACILITY SETs in frame . +v1.2.2 |  |
|  | SanitaryFacilityList | optional | 0..1 | SanitaryFacilityListOfEnumerations | SERVICE FACILITY SETs in frame . +v1.2.2 |  |
|  | CouchetteFacilityList | optional | 0..1 | CouchetteFacilityListOfEnumerations | SERVICE FACILITY SETs in frame . +v1.2.2 |  |
|  | GroupBookingFacility | optional | 0..1 | GroupBookingEnumeration | SERVICE FACILITY SETs in frame . +v1.2.2 |  |
