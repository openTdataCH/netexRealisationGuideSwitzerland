# StopPlaceEntrance

*Table: StopPlaceEntrance*

| Sub | Element | Usage | Card | Type | Description | Note |
|-----|---------|-------|------|------|-------------|------|
|  | Name | expected | 0..1 | MultilingualString | Name of VALIDITY CONDITION. |  |
|  | [AccessibilityAssessment](AccessibilityAssessment.md) | mandatory | 0..1 | AccessibilityAssessment_VersionedChildStructure | Assessment of the accessibility of a SITE. | Accessibility. See the element's table for all details. |
|  | LevelRef | expected | 0..1 | LevelRefStructure | Reference to LEVEL of a SITE. | Accessibility. Required if more than 1 level present. |
|  | placeEquipments | optional | 0..1 | placeEquipments_RelStructure | Items of fixed EQUIPMENT that may be located in places within the SITE ELEMENT. | Accessibility. **TODO** May be removed if we decide to drop below elements. |
| + | EntranceEquipment | optional | 0..* | EntranceEquipment_VersionStructure | Specialisation of PLACE ACCESS EQUIPMENT for ENTRANCEs (door, barrier, revolving door, etc.). | Accessibility. **TODO** May be removed if we decide to drop below elements. |
| ++ | Door | optional | 0..1 | xsd:boolean | Whether there is a door in the entrance. If false, opening does not have door. |  |
| ++ | DropKerbOutside | optional | 0..1 | xsd:boolean | Whether there is a drop Kerb outside door. | Accessibility. **TODO** Seems redundant, see below. |
| ++ | WheelchairPassable | optional | 0..1 | xsd:boolean | Whether lift is judged wheelchair passable. | Accessibility. **TODO** Seems unnecessary given AccessibilityAssessment |
| ++ | WheelchairUnaided | optional | 0..1 | xsd:boolean | Can be passed in a wheel chair unaided. | Accessibility. **TODO** seems unnecessary given AccessibilityAssessment |
|  | IsEntry | optional | 0..1 | xsd:boolean | Whether ENTRANCE can be used for entry. Default is true. | Use to indicate a one-way passage. Assume true if not present. |
|  | IsExit | optional | 0..1 | xsd:boolean | Whether ENTRANCE can be used for exit. Default is true. | Use to indicate a one-way passage. Assume true if not present. |
|  | DroppedKerbOutside | expected | 0..1 | xsd:boolean | Whether nearest crossing to ENTRANCE has dropped kerb. | Accessibility. |
|  | DropOffPointClose | expected | 0..1 | xsd:boolean | Whether there is a drop off point close by to ENTRANCE. | Accessibility. Starting point relevant for AccessibilityAssessments of Quays etc. |
