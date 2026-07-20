# FrameDefaults

*Table: FrameDefaults*

| Sub | Element | Usage | Card | Type | Description | Note |
|-----|---------|-------|------|------|-------------|------|
|  | DefaultLocale | mandatory | 0..1 | LocaleStructure | Default LOCAL for frame elements. Assume this value for timezone and language of elements if not specified on individual elements. | The default locale is German (de) for Swiss public transport. |
| + | TimeZoneOffset | mandatory | 0..1 | TimeZoneOffsetType | Timezone offset from Greenwich at LOCALE. | We prefer times without the suf-fix "+hh:mm". Instead we specify a default TimeZoneOffset (+1) and SummerTimeZoneOffset (+2) |
| + | TimeZone | mandatory | 0..1 | xsd:normalizedString | Timezone name at LOCALE. |  |
| + | SummerTimeZoneOffset | mandatory | 0..1 | TimeZoneOffsetType | Summer timezone offset if different from Time zone offset. | We prefer times without the suf-fix "+hh:mm". Instead we specify a default TimeZoneOffset (+1) and SummerTimeZoneOffset (+2) |
| + | DefaultLanguage | mandatory | 0..1 | xsd:language | Default Language for LOCALE. Assume language use is "normally used" | Is always set to “de” for Swiss public transport. |
|  | DefaultLocationSystem | mandatory | 0..1 | xsd:normalizedString | Default spatial coordinate system (srsName). E.g. WGS84 Value to use for location elements using coordinates if not specified on individual elements. |  |
