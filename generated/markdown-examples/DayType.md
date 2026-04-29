# DayType

| Sub | Element | Usage | Card | Type | Description | Note |
|-----|---------|-------|------|------|-------------|------|
|  | DayType | optional | 1..1 | unknown | A type of day characterized by one or more properties which affect public transport operation. For example: weekday in school holidays. | In Switzerland only used for holidays and the like |
| + | alternativeTexts | expected | 0..1 | alternativeTexts_RelStructure | Additional Translations of text elements. |  |
| ++ | AlternativeText | mandatory | 1..1 | unknown | Alternative Text. +v1.1 |  |
| +++ | Text | mandatory | 0..1 | MultilingualString | Text content of NOTICe. |  |
| + | Name | mandatory | 0..1 | MultilingualString | Name of Traveller |  |
| + | properties | expected | 0..1 | propertiesOfDay_RelStructure | Properties of the DAY TYPE. |  |
| ++ | PropertyOfDay | mandatory | 1..1 | unknown | A property which a day may possess, such as school holiday, weekday, summer, winter etc. | Holidays only |
| +++ | HolidayTypes | expected | 0..1 | HolidayTypesListOfEnumerations | Type of holiday. Default is Any day. |  |
| +++ | DayEvent | optional | 0..1 | DayEventEnumeration | Events happening on day. |  |
