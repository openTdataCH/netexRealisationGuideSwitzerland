# Line

For referencing the `Operator`s we redundantly use `ResponsibilitySet` and `OperatorRef`. This is to maintain compatibility with different data consumers. See chapter on ResourceFrame and Use Case 17.

*Table: Line*

| Sub | Element | Usage | Card | Type | Description | Note |
|-----|---------|-------|------|------|-------------|------|
|  | @id | mandatory | 1..1 | xsd:string | Attribute id | |
|  | @version | mandatory | 1..1 | xsd:string | Attribute version | |
|  | @responsibilitySetRef | mandatory | 1..1 | xsd:string | Attribute responsibilitySetRef | |
|  | ValidBetween | expected | 1..1 | unknown | A coherent set of Service data to which the same frame VALIDITY CONDITIONs have been assigned. | Usually set to the whole timetable year |
| + | FromDate | expected | 0..1 | xsd:dateTime | A coherent set of Service data to which the same frame VALIDITY CONDITIONs have been assigned. |  |
| + | ToDate | expected | 0..1 | xsd:dateTime | A coherent set of Service data to which the same frame VALIDITY CONDITIONs have been assigned. |  |
|  | keyList | mandatory | 1..1 | KeyListStructure | A coherent set of Service data to which the same frame VALIDITY CONDITIONs have been assigned. |  |
| + | KeyValue | expected | 1..* | KeyValueStructure | A coherent set of Service data to which the same frame VALIDITY CONDITIONs have been assigned. | The SLNID is mandatory, when it exists |
| ++ | Key | expected | 1..1 | xsd:normalizedString | A coherent set of Service data to which the same frame VALIDITY CONDITIONs have been assigned. |  |
| ++ | Value | expected | 0..1 | xsd:anyType | A coherent set of Service data to which the same frame VALIDITY CONDITIONs have been assigned. |  |
|  | privateCodes | expected | 1..1 | PrivateCodesStructure | A coherent set of Service data to which the same frame VALIDITY CONDITIONs have been assigned. | The SLNID is mandatory, when it exists |
| + | PrivateCode | expected | 0..* | PrivateCodeStructure | A coherent set of Service data to which the same frame VALIDITY CONDITIONs have been assigned. |  |
| ++ | @type | mandatory | 1..1 | xsd:string | Attribute type | |
|  | Name | mandatory | 0..1 | MultilingualString | A coherent set of Service data to which the same frame VALIDITY CONDITIONs have been assigned. | contains attribute D T from HRDF. Is not translated on purpose. |
|  | ShortName | expected | 0..1 | MultilingualString | A coherent set of Service data to which the same frame VALIDITY CONDITIONs have been assigned. | contains the LinieKurzName (attribut N T in HRDF) |
|  | TransportMode | mandatory | 0..1 | AllModesEnumeration | A coherent set of Service data to which the same frame VALIDITY CONDITIONs have been assigned. |  |
|  | TransportSubmode | optional | 1..1 | TransportSubmodeStructure | A coherent set of Service data to which the same frame VALIDITY CONDITIONs have been assigned. | the mapping excel describe how to use the TransportSubmode |
| + | RailSubmode | optional | 1..1 | RailSubmodeEnumeration | A coherent set of Service data to which the same frame VALIDITY CONDITIONs have been assigned. | Here an example for rail. Be aware that other XXXSubmode are used for other mode. |
|  | PublicCode | mandatory | 0..1 | PublicCodeStructure | A coherent set of Service data to which the same frame VALIDITY CONDITIONs have been assigned. | Contains LinieLangName (attribute LT from HRDF) |
|  | OperatorRef | expected | 1..1 | OperatorRefStructure | A coherent set of Service data to which the same frame VALIDITY CONDITIONs have been assigned. | The operator is the transport organisation that really "owns" the line. Additional operators can be added in additionalOperators. The actual operating organisation can be set in the ServiceJourney. Is redundant to the responsibilitySetRef on purpose. |
|  | additionalOperators | optional | 0..1 | transportOrganisationRefs_RelStructure | A coherent set of Service data to which the same frame VALIDITY CONDITIONs have been assigned. | Used for other operating companies. Is redundant to the responsibilitySetRef on purpose. this is especially important, when a co-ownership of the Line was defined. |
| + | OperatorRef | optional | 0..* | OperatorRefStructure | A coherent set of Service data to which the same frame VALIDITY CONDITIONs have been assigned. |  |
|  | LineType | expected | 0..1 | LineTypeEnumeration | A coherent set of Service data to which the same frame VALIDITY CONDITIONs have been assigned. | Will be used especially, when not "fixed". Details in mapping excel. |
|  | TypeOfProductCategoryRef | mandatory | 1..1 | TypeOfProductCategoryRefStructure | A coherent set of Service data to which the same frame VALIDITY CONDITIONs have been assigned. | Always aligned with BS KI oev-info.ch |
