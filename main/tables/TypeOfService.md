# TypeOfService

*Table: TypeOfService*

| Sub | Element | Usage | Card | Type | Description | Note |
|-----|---------|-------|------|------|-------------|------|
|  | Name | expected | 0..* | MultilingualString | Name of Traveller |  |
| + | @lang | mandatory | 1..1 | xsd:string | Attribute lang | |
|  | ShortName | expected | 0..* | MultilingualString | Short Name for service |  |
| + | @lang | mandatory | 1..1 | xsd:string | Attribute lang | |
|  | PrivateCode | expected | 1..1 | PrivateCodeStructure | A private code that uniquely identifies the element. May be used for inter-operating with other (legacy) systems. |  |
