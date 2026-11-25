# StopPlaceEntrance

*Table: StopPlaceEntrance*

| Sub | Element | Usage | Card | Type | Description | Note |
|-----|---------|-------|------|------|-------------|------|
|  | Name | mandatory | 0..1 | MultilingualString | Name of STOP PLACE. | Will be exported from ATLAS for ERA TSI PRM (Referenzpunkt - "Bezeichnung"). |
|  | [AccessibilityAssessment](AccessibilityAssessment.md) | mandatory | 0..1 | AccessibilityAssessment_VersionedChildStructure | Accessibility values associated with LEVEL. | Accessibility. See the element's table for all details. |
|  | LevelRef | expected | 0..1 | LevelRefStructure |  | Required if more than 1 level present. |
|  | DroppedKerbOutside | optional | 0..1 | boolean | Whether nearest crossing to ENTRANCE has dropped kerb. | Will be exported from ATLAS for ERA TSI PRM (only set to `true` if Verbindung from Parkplatz with "Stufenfreier Zugang" = Ja). To indicate starting point relevant for AccessibilityAssessments of Quays etc. |
|  | DropOffPointClose | optional | 0..1 | boolean | Whether there is a drop off point close by to ENTRANCE. | Will be exported from ATLAS for ERA TSI PRM (only set to `true` if Verbindung from Parkplatz with "Stufenfreier Zugang" = Ja). To indicate starting point relevant for AccessibilityAssessments of Quays etc. |
