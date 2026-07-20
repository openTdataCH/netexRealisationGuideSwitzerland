# GroupOfLines

We use GroupOfLine for the modeling of mixed lines. Only mixed lines have a GroupOfLines.

*Table: GroupOfLines*

| Sub | Element | Usage | Card | Type | Description | Note |
|-----|---------|-------|------|------|-------------|------|
|  | members | mandatory | 0..1 | singleJourneyRefs_RelStructure | Services in GROUP. |  |
| + | LineRef | mandatory | 1..* | LineRefStructure | Reference to a LINE. | one must be the main line |
|  | MainLineRef | mandatory | 0..1 | LineRefStructure | Primary LINE in GROUP OF LINEs, if relevant. | The main line must exist. It hasn't any ServiceJourneyPattern or ServiceJourneys. Those are all on the partial lines. |
|  | GroupOfLinesType | mandatory | 0..1 | GroupOfLinesTypeEnumeration | Classification of GROUP OF LINES. +v1.1 |  |
