# StopPlaceEntrance

*Table: StopPlaceEntrance*

| Sub | Element | Usage | Card | Type | Description | Note |
|-----|---------|-------|------|------|-------------|------|
|  | Name | expected | 0..1 | MultilingualString | Name of VALIDITY CONDITION. |  |
|  | [AccessibilityAssessment](AccessibilityAssessment.md) | mandatory | 0..1 | AccessibilityAssessment_VersionedChildStructure | Assessment of the accessibility of a SITE. | Accessibility. See the element's table for all details. |
|  | LevelRef | expected | 0..1 | LevelRefStructure | Reference to LEVEL of a SITE. | Accessibility. Required if more than 1 level present. |
| ++ | DropKerbOutside | optional | 0..1 | xsd:boolean | Whether there is a drop Kerb outside door. | Accessibility. **TODO** Seems redundant, see below. |
| ++ | WheelchairPassable | optional | 0..1 | xsd:boolean | Whether lift is judged wheelchair passable. | Accessibility. **TODO** Seems unnecessary given AccessibilityAssessment |
| ++ | WheelchairUnaided | optional | 0..1 | xsd:boolean | Can be passed in a wheel chair unaided. | Accessibility. **TODO** seems unnecessary given AccessibilityAssessment |
|  | DroppedKerbOutside | expected | 0..1 | xsd:boolean | Whether nearest crossing to ENTRANCE has dropped kerb. | Accessibility. |
|  | DropOffPointClose | expected | 0..1 | xsd:boolean | Whether there is a drop off point close by to ENTRANCE. | Accessibility. Starting point relevant for AccessibilityAssessments of Quays etc. |
