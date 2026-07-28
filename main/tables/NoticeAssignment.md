# NoticeAssignment

NoticeAssignment connects a Notice to an element. The attribute `id` must be unique.

*Table: NoticeAssignment*

| Sub | Element | Usage | Card | Type | Description | Note |
|-----|---------|-------|------|------|-------------|------|
|  | @id | mandatory | 1..1 | xsd:string | Attribute id | |
|  | @version | mandatory | 1..1 | xsd:string | Attribute version | |
|  | validityConditions | optional | 1..1 | validityConditions_RelStructure |  |  |
| + | AvailabilityConditionRef | optional | 0..* | AvailabilityConditionRefStructure |  |  |
|  | NoticeRef | expected | 0..1 | NoticeRefStructure |  |  |
|  | NoticedObjectRef | optional | 0..1 | VersionOfObjectRefStructure |  | We currently have not plan of using it this way. We do it through embeddingt the NoticeAssignment within the relevant element. |
| + | @nameOfRefClass | mandatory | 1..1 | xsd:string | Attribute nameOfRefClass | |
|  | StartPointInPatternRef | optional | 0..1 | PointInSequenceRefStructure |  | If the notice is valid only on a part of a ServiceJourney then this can be marked with StartPointInPatternRef and EndPointInPatternRef. |
|  | EndPointInPatternRef | optional | 0..1 | PointInSequenceRefStructure |  |  |
