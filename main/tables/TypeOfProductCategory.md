# TypeOfProductCategory

*Table: TypeOfProductCategory*

| Sub | Element | Usage | Card | Type | Description | Note |
|-----|---------|-------|------|------|-------------|------|
|  | @id | mandatory | 1..1 | xsd:string | Attribute id | |
|  | @version | mandatory | 1..1 | xsd:string | Attribute version | |
|  | Name | mandatory | 0..1 | MultilingualString |  |  |
| + | @lang | mandatory | 1..1 | xsd:string | Attribute lang | |
| + | Text | optional | 0..* | MultilingualString |  |  |
| ++ | @lang | mandatory | 1..1 | xsd:string | Attribute lang | |
|  | ShortName | mandatory | 0..1 | MultilingualString |  |  |
