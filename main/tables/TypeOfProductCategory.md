# TypeOfProductCategory

*Table: TypeOfProductCategory*

| Sub | Element | Usage | Card | Type | Description | Note |
|-----|---------|-------|------|------|-------------|------|
|  | @id | mandatory | 1..1 | xsd:string | Attribute id | |
|  | @version | mandatory | 1..1 | xsd:string | Attribute version | |
|  | Name | mandatory | 0..* | MultilingualString | Name of Traveller |  |
| + | @lang | mandatory | 1..1 | xsd:string | Attribute lang | |
| + | Text | optional | 0..* | MultilingualString | Text content of NOTICe. |  |
| ++ | @lang | mandatory | 1..1 | xsd:string | Attribute lang | |
|  | ShortName | mandatory | 0..* | MultilingualString | Short Name for service |  |
