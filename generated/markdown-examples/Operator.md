# Operator

| Sub | Element | Usage | Card | Type | Description | Note |
|-----|---------|-------|------|------|-------------|------|
|  | Operator | mandatory | 1..1 | unknown | A company providing public transport services. | We will use this organisation also in AuthorityRef. The problem is that the sboid can be used only once. |
| + | keyList | expected | 1..1 | KeyListStructure | A list of alternative Key values for an element. |  |
| ++ | KeyValue | expected | 1..* | KeyValueStructure | Key value pair for Entity. |  |
| + | privateCodes | expected | 1..1 | PrivateCodesStructure | A list of private codes that uniquely identifiy the element. May be used for inter-operating with other (legacy) systems. +v2.0 |  |
| ++ | PrivateCode | expected | 1..1 | PrivateCodeStructure | A private code that uniquely identifies the element. May be used for inter-operating with other (legacy) systems. | Busines organisation |
| + | Name | expected | 0..1 | MultilingualString | Name of Traveller |  |
| + | ShortName | expected | 0..1 | MultilingualString | Short Name for service | there may be cases, when it can't be set. However, when no sboid is there, then ShortName must be filled (especially for foreign operators. |
| + | parts | optional | 0..1 | blockParts_RelStructure | BLOCK PARTs which make up COMPOUND BLOCK. |  |
| ++ | OrganisationPart | optional | 1..1 | unknown | A named subdivision of an ORGANISATION. | We want to get rid of the OrganisationPart. **todo** |
| +++ | administrativeZones | optional | 0..1 | administrativeZones_RelStructure | Zones managed by ORGANISATION PART. |  |
| ++++ | TransportAdministrativeZone | optional | 1..1 | unknown | A ZONE relating to the management responsibilities of an ORGANISATION. For example to allocate bus stop identifiers for a region. |  |
