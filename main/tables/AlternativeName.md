# AlternativeName

In some cases we need translations or alias of the Name element. This is done with AlternativeName.

*Table: AlternativeName*

| Sub | Element | Usage | Card | Type | Description | Note |
|-----|---------|-------|------|------|-------------|------|
|  | TypeOfName | optional | 0..1 | xsd:normalizedString | Type of Name - open value. | For StopPlace official is used for the official name |
|  | Name | mandatory | 0..1 | MultilingualString | Name of Traveller |  |
|  | @lang | mandatory | 1..1 | xsd:string | Attribute lang | |
