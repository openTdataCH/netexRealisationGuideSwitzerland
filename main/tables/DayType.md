# DayType

In Switzerland only used for holidays and the like

*Table: DayType*

| Sub | Element | Usage | Card | Type | Description | Note |
|-----|---------|-------|------|------|-------------|------|
|  | @id | mandatory | 1..1 | xsd:string | Attribute id | |
|  | @version | mandatory | 1..1 | xsd:string | Attribute version | |
| + | AlternativeText | mandatory | 1..1 | AlternativeText | Alternative Text. +v1.1 |  |
| ++ | Text | mandatory | 0..* | MultilingualString | Text content of NOTICe. |  |
| +++ | @lang | mandatory | 1..1 | xsd:string | Attribute lang | |
|  | Name | mandatory | 0..* | MultilingualString | Name of Traveller | German or default text |
| + | @lang | mandatory | 1..1 | xsd:string | Attribute lang | |
| + | Text | expected | 0..* | MultilingualString | Text content of NOTICe. | Italian |
| ++ | @lang | mandatory | 1..1 | xsd:string | Attribute lang | |
| + | Text | expected | 0..* | MultilingualString | Text content of NOTICe. | French |
| ++ | @lang | mandatory | 1..1 | xsd:string | Attribute lang | |
| + | Text | expected | 0..* | MultilingualString | Text content of NOTICe. | English |
| ++ | @lang | mandatory | 1..1 | xsd:string | Attribute lang | |
|  | properties | expected | 0..1 | propertiesOfDay_RelStructure | Properties of the DAY TYPE. |  |
| + | PropertyOfDay | mandatory | 1..1 | PropertyOfDay | A property which a day may possess, such as school holiday, weekday, summer, winter etc. | Holidays only |
| ++ | HolidayTypes | expected | 0..1 | HolidayTypesListOfEnumerations | Type of holiday. Default is Any day. |  |
| ++ | DayEvent | optional | 0..1 | DayEventEnumeration | Events happening on day. |  |
