# Quay

Can be a platform, track, sector group or sector. id is a SLOID whenever possible or generated.

*Table: Quay*

| Sub | Element | Usage | Card | Type | Description | Note |
|-----|---------|-------|------|------|-------------|------|
|  | @id | mandatory | 1..1 | xsd:string | Attribute id | |
|  | @version | mandatory | 1..1 | xsd:string | Attribute version | |
|  | keyList | expected | 0..1 | KeyListStructure | STOP PLACEs in frame. |  |
| + | KeyValue | expected | 1..* | KeyValueStructure | STOP PLACEs in frame. | When no SLOID is possible it may be omitted. |
| ++ | Key | mandatory | 0..1 | xsd:normalizedString | STOP PLACEs in frame. | SLOID is mandatory key |
| ++ | Value | mandatory | 0..1 | xsd:anyType | STOP PLACEs in frame. |  |
|  | privateCodes | expected | 0..1 | PrivateCodesStructure | STOP PLACEs in frame. |  |
| + | PrivateCode | expected | 0..* | PrivateCodeStructure | STOP PLACEs in frame. |  |
| ++ | @type | mandatory | 1..1 | xsd:string | Attribute type | |
|  | [Centroid](Centroid.md) | mandatory | 0..1 | SimplePoint_VersionStructure | STOP PLACEs in frame. | Location of Quay. |
|  | SiteRef | optional | 0..1 | SiteRefStructure | STOP PLACEs in frame. | Can reference the parent Quay or StopPlace |
|  | PublicCode | mandatory | 0..1 | PublicCodeStructure | STOP PLACEs in frame. | Code used to identify the Quay to the public |
