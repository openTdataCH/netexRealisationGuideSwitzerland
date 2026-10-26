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
|  | [AccessibilityAssessment](AccessibilityAssessment.md) | mandatory | 0..1 | AccessibilityAssessment_VersionedChildStructure | Accessibility values associated with LEVEL. | Accessibility. Whether the StopPlace and the Quays are accessible for passengers with different mobility or sensory impairments. |
|  | alternativeNames | optional | 0..1 | alternativeNames_RelStructure | Alternative names for the GROUP of STOP PLACEs. | Alternative names for the StopPlace. We will only use these for synonyms. |
| + | [AlternativeName](AlternativeName.md) | optional | 1..* | AlternativeName_VersionedChildStructure | ALTERNATIVE NAME for Element. |  |
|  | TopographicPlaceRef | optional | 1..* | TopographicPlaceRefStructure |  | Id to the county, community, canton or country. |
|  | Locale | optional | 0..1 | LocaleStructure |  |  |
| + | TimeZone | optional | 0..1 | normalizedString | Timezone name at LOCALE. | Must be present, when not in DefaultTimeZone. |
|  | StopPlaceType | optional | 0..1 | StopTypeEnumeration | Type of STOP PLACE. |  |
|  | LimitedUse | optional | 0..1 | LimitedUseTypeEnumeration | Further categorisation of stop as having topographic limitations. | For stops like Sagliains. We currently use only interchangeOnly. |
|  | Weighting | optional | 0..1 | InterchangeWeightingEnumeration | Default rating of the STOP PLACE for making interchanges. | Default relative weighting to be used for stop place. See also mapping excel. Cf. HafasPriority in Extensions. |
|  | quays | expected | 1..1 | quays_RelStructure | QUAYs within the STOP PLACE. | The Quays contained in the StopPlace - platforms, jetties, bays, taxi ranks, and other points of physical access to vehicles. Note that the usage (expected) overrides the cardinality. |
| + | [Quay](Quay.md) | expected | 0..* | Quay_VersionStructure | A place such as platform, stance, or quayside where passengers have access to PT vehicles, Taxi cars or other means of transportation. A QUAY may contain other sub QUAYs. A child QUAY must be physically contained within its parent QUAY. |  |
