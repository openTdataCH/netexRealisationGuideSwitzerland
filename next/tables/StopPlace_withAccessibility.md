# StopPlace_withAccessibility

*Table: StopPlace*

| Sub | Element | Usage | Card | Type | Description | Note |
|-----|---------|-------|------|------|-------------|------|
|  | [AccessibilityAssessment](AccessibilityAssessment.md) | mandatory | 0..1 | AccessibilityAssessment_VersionedChildStructure | Accessibility values associated with LEVEL. | Accessibility. |
|  | Covered | expected | 0..1 | CoveredEnumeration |  | Accessibility. |
|  | AllAreasWheelchairAccessible | mandatory | 0..1 | xsd:boolean |  | Accessibility. |
|  | facilities | expected | 0..1 | siteFacilitySets_RelStructure | Facilities available at SITe. | Accessibility. |
| + | SiteFacilitySet | optional | 0..* | SiteFacilitySetStructure | Set of enumerated FACILITY values that are relevant to a SITE (names based on TPEG classifications, augmented with UIC etc.). | Accessibility. |
| + | SiteFacilitySetRef | optional | 0..* | SiteFacilitySetRefStructure |  | Accessibility. TODO: EPIAP wants the SiteFacilitySets being defined here, referernces may be wrong. |
|  | levels | expected | 0..1 | levels_RelStructure | LEVELs found within SITe. | Accessibility. Mandatory if the StopPlace has more than one level. |
| + | [Level](Level.md) | expected | 0..* | Level_VersionStructure | Level of a Building or SITE. | Accessibility. Mandatory if the StopPlace has more than one level. |
| + | [Level](Level.md) | expected | 0..* | Level_VersionStructure | Level of a Building or SITE. | Accessibility. Mandatory if the StopPlace has more than one level. |
|  | entrances | expected | 0..1 | siteEntrances_RelStructure | ENTRANCEs to SPACE. | Accessibility. |
| + | [Entrance](Entrance.md) | expected | 0..* | SiteEntrance_VersionStructure | Entrance to a SITE. | Accessibility. |
|  | equipmentPlaces | optional | 0..1 | equipmentPlaces_RelStructure |  | Accessibility. TODO |
| + | EquipmentPlaceRef | optional | 0..* | EquipmentPlaceRefStructure |  |  |
|  | placeEquipments | optional | 0..1 | equipments_RelStructure | Items of EQUIPMENT that may be located in an EQUIPMENT PLACE. | Accessibility. TODO |
| + | EntranceSensor | optional | 0..* | EntranceSensor_VersionStructure | AN EQUIPMENT used to monitor or count passengers using a PASSENGER ENTRANCE. +v2.0 |  |
|  | localServices | expected | 0..1 | localServices_RelStructure |  | Accessibility. |
| + | AssistanceServiceRef | optional | 0..* | AssistanceServiceRefStructure | Identifier of an ASSISTANCE SERVICE. | Accessibility. |
|  | accessSpaces | expected | 0..1 | accessSpaces_RelStructure | ACCESS SPACEs within the STOP PLACE. | Accessibility. |
| + | [AccessSpace](AccessSpace.md) | expected | 0..* | AccessSpace_VersionStructure | An area within a STOP PLACE that does not give direct access to transport vehicles. May be connected to QUAYS by PATH LINKs. | Accessibility. |
