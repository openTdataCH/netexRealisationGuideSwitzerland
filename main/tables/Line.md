# Line

For referencing the `Operator`s we redundantly use `ResponsibilitySet` and `OperatorRef`. This is to maintain compatibility with different data consumers.

*Table: Line*

| Sub | Element | Usage | Card | Type | Description | Note |
|-----|---------|-------|------|------|-------------|------|
|  | @id | mandatory | 1..1 | xsd:string | Attribute id | |
|  | @version | mandatory | 1..1 | xsd:string | Attribute version | |
|  | @responsibilitySetRef | mandatory | 1..1 | xsd:string | Attribute responsibilitySetRef | |
|  | ValidBetween | expected | 1..1 | ValidBetween | OPTIMISATION. Simple version of a VALIDITY CONDITION. Comprises a simple period. NO UNIQUENESS CONSTRAINT. | Usually set to the whole timetable year |
| + | FromDate | expected | 0..1 | xsd:dateTime | Start date of AVAILABILITY CONDITION. |  |
| + | ToDate | expected | 0..1 | xsd:dateTime | End of AVAILABILITY CONDITION. Date is INCLUSIVE. |  |
|  | keyList | mandatory | 1..1 | KeyListStructure | A list of alternative Key values for an element. |  |
| + | KeyValue | expected | 1..* | KeyValueStructure | Key value pair for Entity. | The SLNID is mandatory, when it exists |
| ++ | Key | expected | 1..1 | xsd:normalizedString | Identifier of value e.g. System. |  |
| ++ | Value | expected | 0..1 | xsd:anyType | Value associated with QUALITY STRUCTURE FACTOR. |  |
|  | privateCodes | expected | 1..1 | PrivateCodesStructure | A list of private codes that uniquely identifiy the element. May be used for inter-operating with other (legacy) systems. +v2.0 | The SLNID is mandatory, when it exists |
|  | Name | mandatory | 0..1 | MultilingualString | Name of Traveller | contains attribute D T from HRDF. Is not translated on purpose. |
|  | ShortName | expected | 0..1 | MultilingualString | Short Name for service | contains the LinieKurzName (attribut N T in HRDF) |
|  | TransportMode | mandatory | 0..1 | AllModesEnumeration | MODE. |  |
|  | TransportSubmode | optional | 1..1 | TransportSubmodeStructure | A submode of a public or private TRANSPORT MODE. | the mapping excel describe how to use the TransportSubmode |
| + | RailSubmode | optional | 1..1 | RailSubmodeEnumeration | TPEG pti02 Rail submodes loc13. See also See ERA B.4.7009 - Name: Item description code. | Here an example for rail. Be aware that other XXXSubmode are used for other mode. |
|  | PublicCode | mandatory | 0..1 | PublicCodeStructure | Public code for JOURNEY. | Contains LinieLangName (attribute LT from HRDF) |
|  | OperatorRef | expected | 1..1 | OperatorRefStructure | Reference to an OPERATOR. | The operator is the transport organisation that really "owns" the line. Additional operators can be added in additionalOperators. The actual operating organisation can be set in the ServiceJourney. Is redundant to the responsibilitySetRef on purpose. |
|  | additionalOperators | optional | 0..1 | transportOrganisationRefs_RelStructure | Additional OPERATORs for LINE. | Used for other operating companies. Is redundant to the responsibilitySetRef on purpose. this is especially important, when a co-ownership of the Line was defined. |
|  | LineType | expected | 0..1 | LineTypeEnumeration | Classification of LINE, including flexible options. +v2.0. | Will be used especially, when not "fixed". Details in mapping excel. |
|  | TypeOfProductCategoryRef | mandatory | 1..1 | TypeOfProductCategoryRefStructure | Reference to a TYPE OF PRODUCT CATEGORY. Product of a JOURNEY. e.g. ICS, Thales etc See ERA B.4 7037 Characteristic description code. | Always aligned with BS KI oev-info.ch |
