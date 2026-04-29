# Timeband

| Sub | Element | Usage | Card | Type | Description | Note |
|-----|---------|-------|------|------|-------------|------|
|  | Timeband | mandatory | 1..1 | unknown | A period in a day, significant for some aspect of public transport, e.g. similar traffic conditions or fare category. |  |
| + | StartTime | mandatory | 0..1 | xsd:time | Start time of USAGE VALIDITY PERIOD. | Local time (not Zulu), i.e., without “Z” or “hh:mm:ss” suffix. Seconds are not used. |
| + | EndTime | mandatory | 0..1 | xsd:time | End time of USAGE VALIDITY PERIOD. | Local time (not Zulu), i.e., without “Z” or “hh:mm:ss” suffix. Seconds are not used. |
