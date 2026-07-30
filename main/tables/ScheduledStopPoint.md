# ScheduledStopPoint

Swiss ScheduledStopPoint are using the sloid in the id if possible. We keep the ScheduledStopPoint very minimalistic. The information is stored in the SiteFrame.

*Table: ScheduledStopPoint*

| Sub | Element | Usage | Card | Type | Description | Note |
|-----|---------|-------|------|------|-------------|------|
|  | @id | mandatory | 1..1 | xsd:string | Attribute id | |
|  | @version | mandatory | 1..1 | xsd:string | Attribute version | |
|  | keyList | mandatory | 0..1 | KeyListStructure | A list of alternative Key values for an element. | Swiss ScheduledStopPoint are using the sloid in the id if possible. We keep the ScheduledStopPoint very minimalistic. The information is stored in the SiteFrame. |
|  | privateCodes | mandatory | 0..1 | PrivateCodesStructure | A list of private codes that uniquely identifiy the element. May be used for inter-operating with other (legacy) systems. +v2.0 |  |
| + | PrivateCode | expected | 0..* | PrivateCodeStructure | A private code that uniquely identifies the element. May be used for inter-operating with other (legacy) systems. | SLOID mandatory if it exists. |
|  | Name | optional | 0..1 | MultilingualString | Name of VALIDITY CONDITION. | The names are the same in all languages. Can be omitted as this is taken from the StopPlace/Quay. |
| + | @lang | mandatory | 1..1 | xsd:string | Attribute lang | |
|  | PublicCode | optional | 0..1 | PublicCodeStructure | Public identifier code of TARIFF ZONE. +v2.0 | For Quay contains the plattform number/letter. |
