# Operator

We will use this organisation also in AuthorityRef. The problem is that the sboid can be used only once.

*Table: Operator*

| Sub | Element | Usage | Card | Type | Description | Note |
|-----|---------|-------|------|------|-------------|------|
|  | @id | mandatory | 1..1 | xsd:string | Attribute id | |
|  | @version | mandatory | 1..1 | xsd:string | Attribute version | |
|  | keyList | expected | 1..1 | KeyListStructure |  |  |
| + | KeyValue | expected | 1..* | KeyValueStructure |  |  |
| ++ | Key | expected | 1..1 | xsd:normalizedString | Identifier of value e.g. System. |  |
| ++ | Value | expected | 0..1 | xsd:anyType | Value for alternative key. |  |
|  | privateCodes | expected | 1..1 | PrivateCodesStructure |  |  |
| + | PrivateCode | expected | 0..* | PrivateCodeStructure |  | Busines organisation |
|  | PrivateCode | expected | 1..1 | PrivateCodeStructure |  |  |
|  | Name | expected | 0..1 | MultilingualString |  |  |
|  | ShortName | expected | 0..1 | MultilingualString |  | there may be cases, when it can't be set. However, when no sboid is there, then ShortName must be filled (especially for foreign operators. |
|  | parts | optional | 0..1 | blockParts_RelStructure |  |  |
| ++ | administrativeZones | optional | 0..1 | administrativeZones_RelStructure |  |  |
| +++ | TransportAdministrativeZone | optional | 1..1 | unknown |  |  |
| ++++ | PrivateCode | optional | 1..1 | PrivateCodeStructure |  |  |
