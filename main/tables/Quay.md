# Quay

Can be a platform, track, sector group or sector. id is a SLOID whenever possible or generated.

*Table: Quay*

| Sub | Element | Usage | Card | Type | Description | Note |
|-----|---------|-------|------|------|-------------|------|
|  | @id | mandatory | 1..1 | xsd:string | Attribute id | |
|  | @version | mandatory | 1..1 | xsd:string | Attribute version | |
|  | keyList | expected | 1..1 | KeyListStructure | A list of alternative Key values for an element. |  |
| + | KeyValue | expected | 1..* | KeyValueStructure | Key value pair for Entity. | When no SLOID is possible it may be omitted. |
| ++ | Key | mandatory | 1..1 | xsd:normalizedString | Identifier of value e.g. System. | SLOID is mandatory key |
| ++ | Value | mandatory | 0..1 | xsd:anyType | Value associated with QUALITY STRUCTURE FACTOR. |  |
|  | privateCodes | expected | 1..1 | PrivateCodesStructure | A list of private codes that uniquely identifiy the element. May be used for inter-operating with other (legacy) systems. +v2.0 |  |
| + | PrivateCode | expected | 0..* | PrivateCodeStructure | A private code that uniquely identifies the element. May be used for inter-operating with other (legacy) systems. |  |
| ++ | @type | mandatory | 1..1 | xsd:string | Attribute type | |
|  | [Centroid](Centroid.md) | mandatory | 0..1 | SimplePoint_VersionStructure | Centre Coordinates of GROUP of STOP PLACEs. | Location of Quay. |
|  | SiteRef | optional | 0..1 | SiteRefStructure | Reference to parent of SITE, if any. | Can reference the parent Quay or StopPlace |
|  | PublicCode | mandatory | 0..1 | PublicCodeStructure | Public code for JOURNEY. | Code used to identify the Quay to the public |
