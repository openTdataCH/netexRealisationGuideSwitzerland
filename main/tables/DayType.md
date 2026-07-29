# DayType

In Switzerland only used for holidays and the like

*Table: DayType*

| Sub | Element | Usage | Card | Type | Description | Note |
|-----|---------|-------|------|------|-------------|------|
|  | @id | mandatory | 1..1 | xsd:string | Attribute id | |
|  | @version | mandatory | 1..1 | xsd:string | Attribute version | |
| + | AlternativeText | mandatory | 1..* | unknown | ALTERNATIVE TEXT for a text attribute of Element. |  |
| ++ | Text | mandatory | 0..1 | MultilingualString | Name of the entity. |  |
| +++ | @lang | mandatory | 1..1 | xsd:string | Attribute lang | |
|  | Name | mandatory | 0..1 | MultilingualString | Name of VALIDITY CONDITION. | German or default text |
| + | @lang | mandatory | 1..1 | xsd:string | Attribute lang | |
| + | Text | expected | 0..* | MultilingualString |  | Italian |
| ++ | @lang | mandatory | 1..1 | xsd:string | Attribute lang | |
| + | Text | expected | 0..* | MultilingualString |  | French |
| ++ | @lang | mandatory | 1..1 | xsd:string | Attribute lang | |
| + | Text | expected | 0..* | MultilingualString |  | English |
| ++ | @lang | mandatory | 1..1 | xsd:string | Attribute lang | |
|  | properties | expected | 0..1 | propertiesOfDay_RelStructure | Properties of the DAY TYPE. |  |
| + | PropertyOfDay | mandatory | 1..* | unknown | A property which a day may possess, such as school holiday, weekday, summer, winter etc. | Holidays only |
| ++ | HolidayTypes | expected | 0..1 | HolidayTypesListOfEnumerations | Type of holiday. Default is Any day. |  |
| ++ | DayEvent | optional | 0..1 | DayEventEnumeration | Events happening on day. |  |
