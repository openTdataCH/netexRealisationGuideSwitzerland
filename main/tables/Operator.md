# Operator

We will use this organisation also in AuthorityRef. The problem is that the sboid can be used only once.

*Table: Operator*

| Sub | Element | Usage | Card | Type | Description | Note |
|-----|---------|-------|------|------|-------------|------|
|  | @id | mandatory | 1..1 | xsd:string | Attribute id | |
|  | @version | mandatory | 1..1 | xsd:string | Attribute version | |
|  | keyList | expected | 0..1 | KeyListStructure | ORGANISATIONs in frame. |  |
| + | KeyValue | expected | 1..* | KeyValueStructure | ORGANISATIONs in frame. |  |
| ++ | Key | expected | 0..1 | xsd:normalizedString | ORGANISATIONs in frame. |  |
| ++ | Value | expected | 0..1 | xsd:anyType | ORGANISATIONs in frame. |  |
|  | privateCodes | expected | 0..1 | PrivateCodesStructure | ORGANISATIONs in frame. |  |
| + | PrivateCode | expected | 0..* | PrivateCodeStructure | ORGANISATIONs in frame. | Busines organisation |
|  | PrivateCode | expected | 0..1 | PrivateCodeStructure | ORGANISATIONs in frame. |  |
|  | Name | expected | 0..1 | MultilingualString | ORGANISATIONs in frame. |  |
|  | ShortName | expected | 0..1 | MultilingualString | ORGANISATIONs in frame. | there may be cases, when it can't be set. However, when no sboid is there, then ShortName must be filled (especially for foreign operators. |
|  | parts | optional | 0..1 | blockParts_RelStructure | ORGANISATIONs in frame. |  |
| ++ | administrativeZones | optional | 0..* | administrativeZones_RelStructure | ORGANISATIONs in frame. |  |
| +++ | TransportAdministrativeZone | optional | 0..* | organisationsInFrame_RelStructure | ORGANISATIONs in frame. |  |
| ++++ | PrivateCode | optional | 0..1 | PrivateCodeStructure | ORGANISATIONs in frame. |  |
