# NoticeAssignment

NoticeAssignment connects a Notice to an element. The attribute `id` must be unique.

*Table: NoticeAssignment*

| Sub | Element | Usage | Card | Type | Description | Note |
|-----|---------|-------|------|------|-------------|------|
|  | @id | mandatory | 1..1 | xsd:string | Attribute id | |
|  | @version | mandatory | 1..1 | xsd:string | Attribute version | |
|  | validityConditions | optional | 1..1 | validityConditions_RelStructure | VALIDITY CONDITIONs conditioning entity. |  |
| + | AvailabilityConditionRef | optional | 1..* | AvailabilityConditionRefStructure | Reference to an AVAILABILITY CONDITION. A VALIDITY CONDITION defined in terms of temporal attributes. |  |
|  | NoticeRef | expected | 1..1 | NoticeRefStructure | Reference to a NOTICE i.e. footnote, note, announcement or other informational text element. |  |
|  | NoticedObjectRef | optional | 0..1 | VersionOfObjectRefStructure | Object with which NOTICE is associated. If given by context can be omitted. | We currently have not plan of using it this way. We do it through embeddingt the NoticeAssignment within the relevant element. |
| + | @nameOfRefClass | mandatory | 1..1 | xsd:string | Attribute nameOfRefClass | |
|  | StartPointInPatternRef | optional | 0..1 | PointInSequenceRefStructure | POINT at which applicability of NOTICE starts. | If the notice is valid only on a part of a ServiceJourney then this can be marked with StartPointInPatternRef and EndPointInPatternRef. |
|  | EndPointInPatternRef | optional | 0..1 | PointInSequenceRefStructure | POINT at which applicabiity of NOTICE endsIf absent same as Start Point. |  |
