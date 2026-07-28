# Quay

Can be a platform, track, sector group or sector. id is a SLOID whenever possible or generated.

*Table: Quay*

| Sub | Element | Usage | Card | Type | Description | Note |
|-----|---------|-------|------|------|-------------|------|
|  | @id | mandatory | 1..1 | xsd:string | Attribute id | |
|  | @version | mandatory | 1..1 | xsd:string | Attribute version | |
|  | keyList | expected | 1..1 | KeyListStructure |  |  |
| + | KeyValue | expected | 1..* | KeyValueStructure |  | When no SLOID is possible it may be omitted. |
| ++ | Key | mandatory | 1..1 | xsd:normalizedString | Identifier of value e.g. System. | SLOID is mandatory key |
| ++ | Value | mandatory | 0..1 | xsd:anyType | Value for alternative key. |  |
|  | privateCodes | expected | 1..1 | PrivateCodesStructure |  |  |
| + | PrivateCode | expected | 0..* | PrivateCodeStructure |  |  |
| ++ | @type | mandatory | 1..1 | xsd:string | Attribute type | |
|  | [Centroid](Centroid.md) | mandatory | 0..1 | SimplePoint_VersionStructure |  | Location of Quay. |
|  | SiteRef | optional | 0..1 | SiteRefStructure |  | Can reference the parent Quay or StopPlace |
|  | PublicCode | mandatory | 0..1 | PublicCodeStructure |  | Code used to identify the Quay to the public |
