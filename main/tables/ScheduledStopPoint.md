# ScheduledStopPoint

Swiss ScheduledStopPoint are using the sloid in the id if possible. We keep the ScheduledStopPoint very minimalistic. The information is stored in the SiteFrame.

*Table: ScheduledStopPoint*

| Sub | Element | Usage | Card | Type | Description | Note |
|-----|---------|-------|------|------|-------------|------|
|  | @id | mandatory | 1..1 | xsd:string | Attribute id | |
|  | @version | mandatory | 1..1 | xsd:string | Attribute version | |
|  | keyList | optional | 1..1 | KeyListStructure |  |  |
| + | KeyValue | optional | 1..* | KeyValueStructure |  | Can contain a DIDOK key and a SLOID. We don't need it really. |
| ++ | Key | optional | 1..1 | xsd:normalizedString | Identifier of value e.g. System. |  |
| ++ | Value | optional | 0..1 | xsd:anyType | Value for alternative key. |  |
|  | privateCodes | optional | 1..1 | PrivateCodesStructure |  |  |
| + | PrivateCode | optional | 0..* | PrivateCodeStructure |  | If the id is not a SLOID then the SLOID must be added here. |
|  | Name | optional | 0..1 | MultilingualString | Name of Stop Point. | The names are the same in all languages. Can be omitted as this is taken from the StopPlace/Quay. |
| + | @lang | mandatory | 1..1 | xsd:string | Attribute lang | |
|  | PublicCode | optional | 0..1 | PublicCodeStructure |  | For Quay contains the plattform number/letter. |
