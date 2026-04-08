# FrameDefaults

| Sub | Element | Usage | Card | Type | Description | Note |
|-----|---------|-------|------|------|-------------|------|
|  | FrameDefaults | expected | 1..1 | unknown |  |  |
| + | DefaultLocale | mandatory | 1..1 | unknown | The default locale is German (de) for SBB and Swiss public transport. |  |
| ++ | DefaultLanguage | mandatory | 1..1 | unknown | Is always set to “de” for SKI and Swiss public transport. |  |
| ++ | SummerTimeZoneOffset | mandatory | 1..1 | unknown | We prefer times without the suf-fix "+hh:mm". Instead we specify a default TimeZoneOffset (+2) and SummerTimeZoneOffset (+1) |  |
| ++ | TimeZoneOffset | mandatory | 1..1 | unknown | We prefer times without the suf-fix "+hh:mm". Instead we specify a default TimeZoneOffset (+2) and SummerTimeZoneOffset (+1) |  |
