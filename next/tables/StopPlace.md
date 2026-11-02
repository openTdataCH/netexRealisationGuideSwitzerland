# StopPlace

In some cases the id of a StopPlace is not a SLOID.

*Table: StopPlace*

| Sub | Element | Usage | Card | Type | Description | Note |
|-----|---------|-------|------|------|-------------|------|
|  | @id | mandatory | 1..1 | xsd:string | Attribute id | |
|  | @version | mandatory | 1..1 | xsd:string | Attribute version | |
|  | ValidBetween | optional | 1..1 | unknown |  | This can be used to show when the StopPlace can be used. Note that the usage (optional) overrides the cardinality. |
| + | FromDate | optional | 0..1 | dateTime | Start date of AVAILABILITY CONDITION. |  |
| + | ToDate | optional | 0..1 | dateTime | End of AVAILABILITY CONDITION. Date is INCLUSIVE. |  |
|  | keyList | optional | 1..1 | KeyListStructure |  | Key value pairs. |
| + | KeyValue | optional | 1..* | KeyValueStructure | Key value pair for Entity. | HafasPriority and HafasKMInfo for Hafas environments, only used in exports by INFO+. |
| ++ | Key | mandatory | 1..1 | normalizedString | Identifier of value e.g. System. |  |
| ++ | Value | mandatory | 0..1 | normalizedString | Value for alternative key. |  |
|  | privateCodes | expected | 1..1 | PrivateCodesStructure |  |  |
| + | PrivateCode | expected | 0..* | PrivateCodeStructure |  | Mandatory for DIDOK and SLOID if they exist. |
| ++ | @type | mandatory | 1..1 | xsd:string | Attribute type | |
|  | Name | mandatory | 0..1 | MultilingualString | Name of STOP PLACE. | The official stop name. If you have different versions one needs to use AlternativeName |
|  | Centroid | mandatory | 0..1 | SimplePoint_VersionStructure | Centre Coordinates of GROUP of STOP PLACEs. | Global or national location |
| + | Name | optional | 0..1 | MultilingualString |  |  |
| + | Location | mandatory | 0..1 | LocationStructure |  | Note concerning coordinates - The main coordinates are given as **WGS84**. |
| ++ | Longitude | mandatory | 1..1 | LongitudeType | Longitude from Greenwich Meridian. -180 (West) to +180 (East). Decimal degrees. eg 2.356 |  |
| ++ | Latitude | mandatory | 1..1 | LatitudeType | Latitude from equator. -90 (South) to +90 (North). Decimal degrees. eg 56.356 |  |
| ++ | Altitude | optional | 0..1 | AltitudeType | Altitude (metres) Above sea level. |  |
|  | [AccessibilityAssessment](AccessibilityAssessment.md) | expected | 0..1 | AccessibilityAssessment_VersionedChildStructure | Accessibility values associated with LEVEL. | Accessibility. Whether the StopPlace and the Quays are accessible for passengers with different mobility or sensory impairments. |
|  | alternativeNames | optional | 0..1 | alternativeNames_RelStructure | Alternative names for the GROUP of STOP PLACEs. | Alternative names for the StopPlace. We will only use these for synonyms. |
| + | [AlternativeName](AlternativeName.md) | expected | 1..* | AlternativeName_VersionedChildStructure | ALTERNATIVE NAME for Element. |  |
|  | TopographicPlaceRef | optional | 1..* | TopographicPlaceRefStructure |  | Id to the county, community, canton or country. |
|  | Locale | optional | 0..1 | LocaleStructure |  |  |
| + | TimeZone | optional | 0..1 | normalizedString | Timezone name at LOCALE. | Must be present, when not in DefaultTimeZone. |
|  | entrances | optional | 0..1 | siteEntrances_RelStructure | ENTRANCEs to SPACE. | We currently use this for the reference point that each Swiss stop uses. Unfortunately it currently has no Centroid and coordinates |
| + | StopPlaceEntrance | mandatory | 0..* | StopPlaceEntrance_VersionStructure | Passenger Entrance to a STOP PLACE. | Currently only the sloid is known. From this point all references to accessibility are made in Switzerland |
| ++ | Name | optional | 0..1 | MultilingualString | Name of STOP PLACE. |  |
|  | placeEquipments | optional | 0..1 | equipments_RelStructure | Items of EQUIPMENT that may be located in an EQUIPMENT PLACE. | Used in exports for all TSI PRM relevant equipments. Especially in the data transmissions for rail to ERA. We only have Equipments and no EquipmentPlaces. |
| + | TicketingEquipment | optional | 0..* | unknown |  | Ticketing equipment |
| ++ | TicketMachines | mandatory | 0..1 | boolean | Whether there are ticket machines. |  |
| + | AccessVehicleEquipment | optional | 0..* | AccessVehicleEquipment_VersionStructure | Specialisation of VEHICLE EQUIPMENT for ACCESS providing information such as low floor, ramp, access area dimensions, etc. | Method to get on the vehicle |
| ++ | Hoist | expected | 0..1 | boolean | VEHICLE has a hoist or lift for wheelchairs. |  |
| ++ | Ramp | expected | 0..1 | boolean | Whether a ramp may be used to access VEHICLE. |  |
| + | SanitaryEquipment | optional | 0..* | unknown |  |  |
| ++ | [AccessibilityAssessment](AccessibilityAssessment.md) | optional | 0..1 | AccessibilityAssessment_VersionedChildStructure |  |  |
| ++ | SanitaryFacilityList | mandatory | 0..1 | SanitaryFacilityListOfEnumerations |  |  |
| ++ | ToiletsType | optional | 0..1 | ToiletsTypeEnumeration | Indicates the position of using the toilet. |  |
|  | localServices | optional | 0..1 | localServices_RelStructure |  | Will be exported from ATLAS for ERA TSI PRM. |
| + | AssistanceService | optional | 0..* | AssistanceService_VersionStructure | Specialisation of LOCAL SERVICE for ASSISTANCE providing information like language, accessibility trained staff, etc. |  |
| + | AssistanceService | mandatory | 0..* | AssistanceService_VersionStructure | Specialisation of LOCAL SERVICE for ASSISTANCE providing information like language, accessibility trained staff, etc. |  |
| ++ | AssistanceFacilityList | expected | 0..1 | AssistanceFacilityListOfEnumerations |  |  |
| ++ | AssistanceAvailability | optional | 0..1 | AssistanceAvailabilityEnumeration | Availability of assistance service. |  |
|  | StopPlaceType | expected | 0..1 | StopTypeEnumeration | Type of STOP PLACE. |  |
|  | LimitedUse | optional | 0..1 | LimitedUseTypeEnumeration | Further categorisation of stop as having topographic limitations. | For stops like Sagliains. We currently use only interchangeOnly. |
|  | Weighting | optional | 0..1 | InterchangeWeightingEnumeration | Default rating of the STOP PLACE for making interchanges. | Default relative weighting to be used for stop place. See also mapping excel. Cf. HafasPriority in Extensions. |
|  | quays | expected | 1..1 | quays_RelStructure | QUAYs within the STOP PLACE. | The Quays contained in the StopPlace - platforms, jetties, bays, taxi ranks, and other points of physical access to vehicles. Note that the usage (expected) overrides the cardinality. |
| + | [Quay](Quay.md) | expected | 0..* | Quay_VersionStructure | A place such as platform, stance, or quayside where passengers have access to PT vehicles, Taxi cars or other means of transportation. A QUAY may contain other sub QUAYs. A child QUAY must be physically contained within its parent QUAY. |  |
|  | navigationPaths | optional | 0..1 | navigationPaths_RelStructure | NAVIGATION PATHs within the SITE and or between the SITE elsewhere. | Will be provided at least for rail in a first export for ERA TSI PRM |
| + | NavigationPath | expected | 0..* | SiteNavigationPath_VersionStructure | NAVIGATION PATH for a SITE. |  |
| ++ | From | mandatory | 0..1 | DeckPathLinkEndStructure | Origin end of DECK NAVIGATION path. Only needed if detailed PATH LINKs are not given. | One of the points is the reference point. |
| +++ | PlaceRef | mandatory | 1..1 | PlaceRefStructure |  |  |
| ++ | To | mandatory | 0..1 | DeckPathLinkEndStructure | Destination end of DECK NAVIGATION PATH. Only needed if detailed PATH LINKs not given. |  |
| +++ | PlaceRef | mandatory | 1..1 | PlaceRefStructure |  |  |
| ++ | [AccessibilityAssessment](AccessibilityAssessment.md) | mandatory | 0..1 | AccessibilityAssessment_VersionedChildStructure |  | If the NavigationPath is provided, then an AccessibilityAssessment must be provided too |
