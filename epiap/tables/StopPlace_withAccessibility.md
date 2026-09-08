# StopPlace_withAccessibility

*Table: StopPlace*

| Sub | Element | Usage | Card | Type | Description | Note |
|-----|---------|-------|------|------|-------------|------|
|  | ValidBetween | mandatory | 1..* | unknown |  |  |
| + | Location | mandatory | 0..1 | LocationStructure | The position of a POINT with a reference to a given LOCATING SYSTEM (e. g. coordinates). | Element before ... |
| ++ | Longitude | mandatory | 1..1 | LongitudeType | Longitude from Greenwich Meridian. -180 (East) to +180 (West). |  |
|  | [AccessibilityAssessment](AccessibilityAssessment.md) | mandatory | 0..1 | AccessibilityAssessment_VersionedChildStructure | Assessment of the accessibility of a SITE. | Accessibility. |
|  | Covered | expected | 0..1 | CoveredEnumeration | Whether the component is Indoors or outdoors. Default is Indoors. | Accessibility. |
|  | AllAreasWheelchairAccessible | mandatory | 0..1 | xsd:boolean | Whether all areas of the component are wheelchair accessible. | Accessibility. |
|  | facilities | expected | 0..1 | serviceFacilitySets_RelStructure | FACILITies available associated with LINE. It is always recommended to also model accessibility relevant things as equipment on the VEHICLE and physical elements, if real-time information is needed. | Accessibility. |
| + | SiteFacilitySet | optional | 1..* | SiteFacilitySetStructure | Set of enumerated FACILITY values that are relevant to a SITE (names based on TPEG classifications, augmented with UIC etc.). | Accessibility. |
| + | SiteFacilitySetRef | optional | 0..* | SiteFacilitySetRefStructure | Reference to a SITE FACILITY SET. | Accessibility. TODO: EPIAP wants the SiteFacilitySets being defined here, referernces may be wrong. |
|  | Locale | optional | 1..1 | LocaleStructure | Common LOCALE dependent properties. | Element before ... |
| + | TimeZone | optional | 0..1 | xsd:normalizedString | Timezone name at LOCALE. |  |
|  | levels | expected | 0..1 | levels_RelStructure | LEVELs found within SITe. | Accessibility. Mandatory if the StopPlace has more than one level. |
| + | [Level](Level.md) | expected | 0..* | Level_VersionStructure | Level of a Building or SITE. | Accessibility. Mandatory if the StopPlace has more than one level. |
| + | [Level](Level.md) | expected | 0..* | Level_VersionStructure | Level of a Building or SITE. | Accessibility. Mandatory if the StopPlace has more than one level. |
|  | entrances | expected | 0..1 | pointOfInterestEntrances_RelStructure | ENTRANCEs to and within SITE. | Accessibility. |
| + | [Entrance](Entrance.md) | expected | 0..* | SiteEntrance_VersionStructure | Entrance to a SITE. | Accessibility. |
|  | equipmentPlaces | optional | 0..1 | equipmentPlaces_RelStructure | EQUIPMENT PLACEs within SITE COMPONENT. | Accessibility. TODO |
|  | placeEquipments | optional | 0..1 | placeEquipments_RelStructure | Items of fixed EQUIPMENT that may be located in places within the SITE ELEMENT. | Accessibility. TODO |
|  | localServices | expected | 0..1 | localServices_RelStructure | LOCAL SERVICEs that may be located in PLACEs within the SITE ELEMENT. | Accessibility. |
| + | AssistanceServiceRef | optional | 0..* | AssistanceServiceRefStructure | Identifier of an ASSISTANCE SERVICE. | Accessibility. |
|  | quays | expected | 1..1 | quays_RelStructure | QUAYs within the STOP PLACE. | Element before ... |
| + | Quay | expected | 0..* | Quay_VersionStructure | A place such as platform, stance, or quayside where passengers have access to PT vehicles, Taxi cars or other means of transportation. A QUAY may contain other sub QUAYs. A child QUAY must be physically contained within its parent QUAY. |  |
|  | accessSpaces | expected | 0..1 | accessSpaces_RelStructure | ACCESS SPACEs within the STOP PLACE. | Accessibility. |
| + | [AccessSpace](AccessSpace.md) | expected | 0..* | AccessSpace_VersionStructure | An area within a STOP PLACE that does not give direct access to transport vehicles. May be connected to QUAYS by PATH LINKs. | Accessibility. |
