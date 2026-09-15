# TypesOfPlace

We expect a TypsOfPlace Valueset. It must have two entries: drtCollectionPoint and regularStop.

*Table: ValueSet*

| Sub | Element | Usage | Card | Type | Description | Note |
|-----|---------|-------|------|------|-------------|------|
|  | values | expected | 0..1 | typesOfValue_RelStructure | Values in Set. |  |
| + | TypeOfPlace | expected | 0..* | TypeOfPlace_ValueStructure | Classification of a PLACE. |  |
| ++ | Name | expected | 0..1 | MultilingualString | Name of VALIDITY CONDITION. |  |
| +++ | @lang | mandatory | 1..1 | xsd:string | Attribute lang | |
| +++ | Text | expected | 0..* | MultilingualString |  |  |
| ++++ | @lang | mandatory | 1..1 | xsd:string | Attribute lang | |
