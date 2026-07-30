# Operator

We will use this organisation also in `AuthorityRef`. The problem is that the SBOID can be used only once. **TODO** Clarify

*Table: Operator*

| Sub | Element | Usage | Card | Type | Description | Note |
|-----|---------|-------|------|------|-------------|------|
|  | @id | mandatory | 1..1 | xsd:string | Attribute id | |
|  | @version | mandatory | 1..1 | xsd:string | Attribute version | |
|  | privateCodes | mandatory | 0..1 | PrivateCodesStructure | A list of private codes that uniquely identifiy the element. May be used for inter-operating with other (legacy) systems. +v2.0 |  |
| + | PrivateCode | expected | 0..* | PrivateCodeStructure | A private code that uniquely identifies the element. May be used for inter-operating with other (legacy) systems. | SBOID and GO (busines organisation) mandatory if they exist. |
|  | PrivateCode | expected | 1..1 | PrivateCodeStructure | A private code that uniquely identifies the element. May be used for inter-operating with other (legacy) systems. |  |
|  | Name | expected | 0..1 | MultilingualString | Name of VALIDITY CONDITION. |  |
|  | ShortName | expected | 0..1 | MultilingualString | Short Name for TYPE OF VALUE. | there may be cases, when it can't be set. However, when no sboid is there, then ShortName must be filled (especially for foreign operators. |
|  | parts | optional | 0..1 | blockParts_RelStructure | Parts of the ORGANISATION. |  |
| ++ | administrativeZones | optional | 0..* | administrativeZones_RelStructure | Zones managed by ORGANISATION PART. |  |
| +++ | TransportAdministrativeZone | optional | 0..* | TransportAdministrativeZone_VersionStructure | A ZONE relating to the management responsibilities of an ORGANISATION. For example to allocate bus stop identifiers for a region. |  |
| ++++ | PrivateCode | optional | 1..1 | PrivateCodeStructure | A private code that uniquely identifies the element. May be used for inter-operating with other (legacy) systems. |  |
