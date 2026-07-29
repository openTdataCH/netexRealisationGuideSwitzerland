# AlternativeName

In some cases we need translations or alias of the Name element. This is done with AlternativeName.

*Table: AlternativeName*

| Sub | Element | Usage | Card | Type | Description | Note |
|-----|---------|-------|------|------|-------------|------|
|  | NameType | mandatory | 0..1 | NameTypeEnumeration | ORGANISATIONs in frame. | In some cases we need translations or alias of the Name element. This is done with AlternativeName. alias allowed for StopPlace. |
|  | TypeOfName | optional | 0..1 | xsd:normalizedString | ORGANISATIONs in frame. | For StopPlace official is used for the official name |
|  | Name | mandatory | 0..1 | MultilingualString | ORGANISATIONs in frame. |  |
| + | @lang | mandatory | 1..1 | xsd:string | Attribute lang | |
