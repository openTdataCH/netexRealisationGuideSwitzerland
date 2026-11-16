# Quay_accessibility

*Table: Quay*

| Sub | Element | Usage | Card | Type | Description | Note |
|-----|---------|-------|------|------|-------------|------|
|  | [AccessibilityAssessment](AccessibilityAssessment.md) | expected | 0..1 | AccessibilityAssessment_VersionedChildStructure |  | Only required if the AccessibilityAssessment of the StopPlace contains value(s) `partial`. |
|  | [facilities](facilities.md) | optional | 0..1 | serviceFacilitySets_RelStructure |  | Only use to signal a facility not generally available for the StopPlace. Will be exported from ATLAS for ERA TSI PRM. |
|  | localServices | optional | 0..1 | localServices_RelStructure |  | NOT USED at the level of Quay. |
| + | AssistanceServiceRef | optional | 0..* | AssistanceServiceRefStructure | Identifier of an ASSISTANCE SERVICE. |  |
