# AlternativeName

In some cases we need an alias of the Name element. This is done with AlternativeName. And it basically happens only for StopPlace and rarely Operator.

*Table: AlternativeName*

| Sub | Element | Usage | Card | Type | Description | Note |
|-----|---------|-------|------|------|-------------|------|
|  | NameType | mandatory | 0..1 | NameTypeEnumeration | Type of Name - fixed value. Default is alias. | In some cases we need an alias of the Name element. This is done with AlternativeName. And it basically happens only for StopPlace and rarely Operator. alias allowed e.g. for StopPlace. |
|  | TypeOfName | optional | 0..1 | xsd:normalizedString | Type of Name - open value. | If it is the official name. If used, only "offical" should be used. |
|  | Name | mandatory | 0..1 | MultilingualString | Name of VALIDITY CONDITION. |  |
| + | @lang | mandatory | 1..1 | xsd:string | Attribute lang | |
