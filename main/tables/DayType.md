# DayType

In Switzerland only used for holidays and the like

*Table: DayType*

| Sub | Element | Usage | Card | Type | Description | Note |
|-----|---------|-------|------|------|-------------|------|
|  | @id | mandatory | 1..1 | xsd:string | Attribute id | |
|  | @version | mandatory | 1..1 | xsd:string | Attribute version | |
| + | AlternativeText | mandatory | 1..1 | unknown |  |  |
| ++ | Text | mandatory | 0..1 | MultilingualString | Name of the entity. |  |
| +++ | @lang | mandatory | 1..1 | xsd:string | Attribute lang | |
|  | Name | mandatory | 0..1 | MultilingualString |  | German or default text |
| + | @lang | mandatory | 1..1 | xsd:string | Attribute lang | |
| + | Text | expected | 0..* | MultilingualString |  | Italian |
| ++ | @lang | mandatory | 1..1 | xsd:string | Attribute lang | |
| + | Text | expected | 0..* | MultilingualString |  | French |
| ++ | @lang | mandatory | 1..1 | xsd:string | Attribute lang | |
| + | Text | expected | 0..* | MultilingualString |  | English |
| ++ | @lang | mandatory | 1..1 | xsd:string | Attribute lang | |
|  | properties | expected | 0..1 | propertiesOfDay_RelStructure |  |  |
| + | PropertyOfDay | mandatory | 0..* | unknown |  | Holidays only |
| ++ | HolidayTypes | expected | 0..1 | HolidayTypesListOfEnumerations |  |  |
| ++ | DayEvent | optional | 0..1 | DayEventEnumeration |  |  |
