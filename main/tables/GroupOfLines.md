# GroupOfLines

We use GroupOfLine for the modeling of mixed lines. Only mixed lines have a GroupOfLines.

*Table: GroupOfLines*

| Sub | Element | Usage | Card | Type | Description | Note |
|-----|---------|-------|------|------|-------------|------|
|  | members | mandatory | 0..1 | singleJourneyRefs_RelStructure | A coherent set of Service data to which the same frame VALIDITY CONDITIONs have been assigned. |  |
| + | LineRef | mandatory | 0..* | LineRefStructure | A coherent set of Service data to which the same frame VALIDITY CONDITIONs have been assigned. | one must be the main line |
|  | MainLineRef | mandatory | 0..1 | LineRefStructure | A coherent set of Service data to which the same frame VALIDITY CONDITIONs have been assigned. | The main line must exist. It hasn't any ServiceJourneyPattern or ServiceJourneys. Those are all on the partial lines. |
|  | GroupOfLinesType | mandatory | 0..1 | GroupOfLinesTypeEnumeration | A coherent set of Service data to which the same frame VALIDITY CONDITIONs have been assigned. |  |
