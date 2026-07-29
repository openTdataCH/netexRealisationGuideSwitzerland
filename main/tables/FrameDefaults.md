# FrameDefaults

*Table: FrameDefaults*

| Sub | Element | Usage | Card | Type | Description | Note |
|-----|---------|-------|------|------|-------------|------|
|  | DefaultLocale | mandatory | 0..1 | LocaleStructure | Default values to use on elements in the frame that do not explicitly state a value. | The default locale is German (de) for Swiss public transport. |
| + | TimeZoneOffset | mandatory | 0..1 | TimeZoneOffsetType | Default values to use on elements in the frame that do not explicitly state a value. | We prefer times without the suf-fix "+hh:mm". Instead we specify a default TimeZoneOffset (+1) and SummerTimeZoneOffset (+2) |
| + | TimeZone | mandatory | 0..1 | xsd:normalizedString | Default values to use on elements in the frame that do not explicitly state a value. |  |
| + | SummerTimeZoneOffset | mandatory | 0..1 | TimeZoneOffsetType | Default values to use on elements in the frame that do not explicitly state a value. | We prefer times without the suf-fix "+hh:mm". Instead we specify a default TimeZoneOffset (+1) and SummerTimeZoneOffset (+2) |
| + | DefaultLanguage | mandatory | 0..1 | xsd:language | Default values to use on elements in the frame that do not explicitly state a value. | Is always set to “de” for Swiss public transport. |
|  | DefaultLocationSystem | mandatory | 0..1 | xsd:normalizedString | Default values to use on elements in the frame that do not explicitly state a value. |  |
