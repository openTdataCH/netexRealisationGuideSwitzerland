# StopPlaceEntrance

*Table: StopPlaceEntrance*

| Sub | Element | Usage | Card | Type | Description | Note |
|-----|---------|-------|------|------|-------------|------|
|  | Name | expected | 0..1 | MultilingualString | Name of STOP PLACE. |  |
|  | [AccessibilityAssessment](AccessibilityAssessment.md) | mandatory | 0..1 | AccessibilityAssessment_VersionedChildStructure | Accessibility values associated with LEVEL. | Accessibility. See the element's table for all details. |
|  | LevelRef | expected | 0..1 | LevelRefStructure |  | Required if more than 1 level present. |
|  | DroppedKerbOutside | expected | 0..1 | boolean | Whether nearest crossing to ENTRANCE has dropped kerb. | To indicate starting point relevant for AccessibilityAssessments of Quays etc. **TODO** To be discussed. |
|  | DropOffPointClose | expected | 0..1 | boolean | Whether there is a drop off point close by to ENTRANCE. | To indicate starting point relevant for AccessibilityAssessments of Quays etc. |
