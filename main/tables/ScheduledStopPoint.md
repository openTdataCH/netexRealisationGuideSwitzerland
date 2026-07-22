# ScheduledStopPoint

Swiss ScheduledStopPoint are using the sloid in the id if possible. We keep the ScheduledStopPoint very minimalistic. The information is stored in the SiteFrame.

*Table: ScheduledStopPoint*

| Sub | Element | Usage | Card | Type | Description | Note |
|-----|---------|-------|------|------|-------------|------|
|  | @id | mandatory | 1..1 | xsd:string | Attribute id | |
|  | @version | mandatory | 1..1 | xsd:string | Attribute version | |
|  | keyList | optional | 1..1 | KeyListStructure | A list of alternative Key values for an element. |  |
| + | KeyValue | optional | 1..* | KeyValueStructure | Key value pair for Entity. | Can contain a DIDOK key and a SLOID. We don't need it really. |
| ++ | Key | optional | 1..1 | xsd:normalizedString | Identifier of value e.g. System. |  |
| ++ | Value | optional | 0..1 | xsd:anyType | Value associated with QUALITY STRUCTURE FACTOR. |  |
|  | privateCodes | optional | 1..1 | PrivateCodesStructure | A list of private codes that uniquely identifiy the element. May be used for inter-operating with other (legacy) systems. +v2.0 |  |
| + | PrivateCode | optional | 0..* | PrivateCodeStructure | A private code that uniquely identifies the element. May be used for inter-operating with other (legacy) systems. | If the id is not a SLOID then the SLOID must be added here. |
|  | Name | optional | 0..* | MultilingualString | Name of Traveller | The names are the same in all languages. Can be omitted as this is taken from the StopPlace/Quay. |
| + | @lang | mandatory | 1..1 | xsd:string | Attribute lang | |
|  | PublicCode | optional | 0..1 | PublicCodeStructure | Public code for JOURNEY. | For Quay contains the plattform number/letter. |
