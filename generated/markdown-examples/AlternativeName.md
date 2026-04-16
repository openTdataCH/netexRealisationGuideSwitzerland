# AlternativeName

| Sub | Element | Usage | Card | Type | Description | Note |
|-----|---------|-------|------|------|-------------|------|
|  | AlternativeName | mandatory | 1..1 | None | Alternative Name. | In some cases we need translations or alias of the Name element. This is done with AlternativeName. |
| + | TypeOfName | optional | 0..1 | xsd:normalizedString | Type of Name - open value. |  |
| + | Name | mandatory | 0..1 | MultilingualString | Name of Traveller |  |
| + | @lang | mandatory | 1..1 | xsd:string | Attribute lang | |
