# ScheduledStopPoint

Swiss ScheduledStopPoint are using the sloid in the id if possible. We keep the ScheduledStopPoint very minimalistic. The information is stored in the SiteFrame.

*Table: ScheduledStopPoint*

| Sub | Element | Usage | Card | Type | Description | Note |
|-----|---------|-------|------|------|-------------|------|
|  | @id | mandatory | 1..1 | xsd:string | Attribute id | |
|  | @version | mandatory | 1..1 | xsd:string | Attribute version | |
|  | privateCodes | expected | 1..1 | PrivateCodesStructure |  |  |
| + | PrivateCode | expected | 0..* | PrivateCodeStructure |  | SLOID mandatory if it exists. |
|  | Name | optional | 0..1 | MultilingualString | Name of POINT. | The names are the same in all languages. Can be omitted as this is taken from the StopPlace/Quay. |
| + | @lang | mandatory | 1..1 | xsd:string | Attribute lang | |
|  | PublicCode | optional | 0..1 | PublicCodeStructure | A PUBLIC code that uniquely identifies the STOP POINT. | For Quay contains the plattform number/letter. |
