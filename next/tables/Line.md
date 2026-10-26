# Line

For referencing the `Operator`s we redundantly use `ResponsibilitySet` and `OperatorRef`. This is to maintain compatibility with different data consumers. See chapter on ResourceFrame and Use Case 17.

*Table: Line*

| Sub | Element | Usage | Card | Type | Description | Note |
|-----|---------|-------|------|------|-------------|------|
|  | @id | mandatory | 1..1 | xsd:string | Attribute id | |
|  | @version | mandatory | 1..1 | xsd:string | Attribute version | |
|  | @responsibilitySetRef | mandatory | 1..1 | xsd:string | Attribute responsibilitySetRef | |
|  | ValidBetween | expected | 1..1 | unknown |  | Usually set to the whole timetable year |
| + | FromDate | expected | 0..1 | dateTime | Start date of AVAILABILITY CONDITION. |  |
| + | ToDate | expected | 0..1 | dateTime | End of AVAILABILITY CONDITION. Date is INCLUSIVE. |  |
|  | keyList | optional | 1..1 | KeyListStructure |  |  |
| + | KeyValue | optional | 1..* | KeyValueStructure | Key value pair for Entity. | We might use KeyValue for some additional information |
| ++ | Key | optional | 1..1 | normalizedString | Identifier of value e.g. System. |  |
| ++ | Value | optional | 0..1 | normalizedString | Value for alternative key. |  |
|  | privateCodes | mandatory | 1..1 | PrivateCodesStructure |  | The SLNID is mandatory if it exists |
| + | PrivateCode | expected | 0..* | PrivateCodeStructure |  | The SLNID is mandatory if it exists |
| ++ | @type | mandatory | 1..1 | xsd:string | Attribute type | |
|  | Name | mandatory | 0..1 | MultilingualString | Name of LINE SHAPE. | contains attribute D T from HRDF. Is not translated on purpose. |
|  | ShortName | expected | 0..1 | MultilingualString | Short name of LINE. | contains the LinieKurzName (attribut N T in HRDF) |
|  | TransportMode | mandatory | 0..1 | AllPublicTransportModesEnumeration | Primary PUBLIC TRANSPORT MODE of NETWORK. |  |
|  | TransportSubmode | optional | 0..1 | TransportSubmodeStructure |  | the mapping excel describe how to use the TransportSubmode |
| + | RailSubmode | optional | 1..1 | RailSubmodeEnumeration | TPEG pti02 Rail submodes loc13. See also See ERA B.4.7009 - Name: Item description code. | Here an example for rail. Be aware that other XXXSubmode are used for other mode. |
|  | PublicCode | mandatory | 0..1 | PublicCodeStructure | Public identifier of a LINe. | Contains LinieLangName (attribute LT from HRDF) |
|  | OperatorRef | expected | 0..1 | OperatorRefStructure | An OPERATOR should be set, even when the same as the AUTHORITY. In some cases OPERATOR or AUTHORITY are managed through a ResponsibilitySet. However, for compatibility OperatorRef and AuthorityRef still should be filled in. +v2.0 | The operator is the transport organisation that really "owns" the line. Additional operators can be added in additionalOperators. The actual operating organisation can be set in the ServiceJourney. Is redundant to the responsibilitySetRef on purpose. |
|  | additionalOperators | optional | 0..1 | transportOrganisationRefs_RelStructure | Additional OPERATORs for LINE. | Used for other operating companies. Is redundant to the responsibilitySetRef on purpose. this is especially important, when a co-ownership of the Line was defined. |
| + | OperatorRef | optional | 0..* | OperatorRefStructure |  |  |
|  | LineType | expected | 0..1 | LineTypeEnumeration | Classification of LINE, including flexible options. +v2.0. | Will be used especially, when not "fixed". Details in mapping excel. |
|  | TypeOfProductCategoryRef | mandatory | 0..1 | TypeOfProductCategoryRefStructure |  | Always aligned with BS KI oev-info.ch |
