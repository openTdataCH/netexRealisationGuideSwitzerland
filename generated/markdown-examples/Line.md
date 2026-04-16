# Line

| Sub | Element | Usage | Card | Type | Description | Note |
|-----|---------|-------|------|------|-------------|------|
|  | Line | mandatory | 1..1 | None | A group of ROUTEs which is generally known to the public by a similar name or number. | We have a duplication with responsibilitySet and OperatorRef. With AuthorityRef we currently have a problem, because we can't use the same organisation **TODO** |
| + | ValidBetween | expected | 1..1 | None | OPTIMISATION. Simple version of a VALIDITY CONDITION. Comprises a simple period. NO UNIQUENESS CONSTRAINT. | Usually set to the whole timetable year |
| ++ | FromDate | expected | 0..1 | xsd:dateTime | Start date of AVAILABILITY CONDITION. |  |
| ++ | ToDate | expected | 0..1 | xsd:dateTime | End of AVAILABILITY CONDITION. Date is INCLUSIVE. |  |
| + | keyList | mandatory | 1..1 | KeyListStructure | A list of alternative Key values for an element. |  |
| ++ | KeyValue | expected | 1..* | KeyValueStructure | Key value pair for Entity. | The SLNID is mandatory, when it exists |
| +++ | Key | expected | 1..1 | xsd:normalizedString | Identifier of value e.g. System. |  |
| +++ | Value | expected | 0..1 | xsd:anyType | Value associated with QUALITY STRUCTURE FACTOR. |  |
| + | Name | mandatory | 0..1 | MultilingualString | Name of Traveller | contains attribute D T from HRDF. Is not translated on purpose. |
| + | ShortName | expected | 0..1 | MultilingualString | Short Name for service | contains the LinieKurzName (attribut N T in HRDF) |
| + | TransportMode | mandatory | 0..1 | AllModesEnumeration | MODE. |  |
| ++ | RailSubmode | expected | 1..1 | RailSubmodeEnumeration | TPEG pti02 Rail submodes loc13.
			See also See ERA B.4.7009 - Name: Item description code. |  |
| + | PublicCode | mandatory | 0..1 | PublicCodeStructure | Public code for JOURNEY. | Contains LinieLangName (attribute LT from HRDF) |
| + | AuthorityRef | mandatory | 1..1 | None | Reference to an AUTHORITY. | Contains the AUTHORITY OF the LINE. |
| + | OperatorRef | optional | 1..1 | OperatorRefStructure | Reference to an OPERATOR. | The operator is the transport organisation that really will do the operation. If different from AuthorityRef |
| + | TypeOfProductCategoryRef | mandatory | 1..1 | TypeOfProductCategoryRefStructure | Reference to a TYPE OF PRODUCT CATEGORY. Product of a JOURNEY. e.g. ICS, Thales etc
See ERA B.4 7037 Characteristic description code. | **TODO** needs tobe clarified from BS KI |
