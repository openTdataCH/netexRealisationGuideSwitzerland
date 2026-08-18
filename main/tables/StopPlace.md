# StopPlace

In some cases the id of a StopPlace is not a SLOID.

*Table: StopPlace*

| Sub | Element | Usage | Card | Type | Description | Note |
|-----|---------|-------|------|------|-------------|------|
|  | @id | mandatory | 1..1 | xsd:string | Attribute id | |
|  | @version | mandatory | 1..1 | xsd:string | Attribute version | |
|  | ValidBetween | optional | 1..* | unknown |  | This can be used to show when the StopPlace can be used. Note that the usage (optional) overrides the cardinality. |
| + | FromDate | optional | 0..1 | xsd:dateTime | Start date of AVAILABILITY CONDITION. |  |
| + | ToDate | optional | 0..1 | xsd:dateTime | End of AVAILABILITY CONDITION. Date is INCLUSIVE. |  |
|  | keyList | optional | 0..1 | KeyListStructure | A list of alternative Key values for an element. | Key value pairs. |
| + | KeyValue | optional | 1..* | KeyValueStructure | Key value pair for Entity. | HafasPriority and HafasKMInfo for Hafas environments, only used in exports by INFO+. |
| ++ | Key | mandatory | 0..1 | xsd:normalizedString | User key. |  |
| ++ | Value | mandatory | 0..1 | xsd:anyType | Value for alternative key. |  |
|  | privateCodes | expected | 0..1 | PrivateCodesStructure | A list of private codes that uniquely identifiy the element. May be used for inter-operating with other (legacy) systems. +v2.0 |  |
| + | PrivateCode | expected | 0..* | PrivateCodeStructure | A private code that uniquely identifies the element. May be used for inter-operating with other (legacy) systems. | Mandatory for DIDOK and SLOID if they exist. |
| ++ | @type | mandatory | 1..1 | xsd:string | Attribute type | |
|  | Name | mandatory | 0..1 | MultilingualString | Name of VALIDITY CONDITION. | The official stop name. If you have different versions one needs to use AlternativeName |
|  | Centroid | mandatory | 0..1 | SimplePoint_VersionStructure | Centre Coordinates of ZONE. | Global or national location |
| + | Name | optional | 0..1 | MultilingualString | Name of VALIDITY CONDITION. |  |
| + | Location | mandatory | 0..1 | LocationStructure | The position of a POINT with a reference to a given LOCATING SYSTEM (e. g. coordinates). | Note concerning coordinates - The main coordinates are given as **WSG84**. |
| ++ | Longitude | mandatory | 1..1 | LongitudeType | Longitude from Greenwich Meridian. -180 (East) to +180 (West). |  |
| ++ | Latitude | mandatory | 1..1 | LatitudeType | Latitude from equator. -90 (South) to +90 (North). |  |
| ++ | Altitude | optional | 0..1 | AltitudeType | Altitude. |  |
|  | alternativeNames | optional | 0..1 | alternativeNames_RelStructure | Alternativie names for ORGANISATION. | Alternative names for the StopPlace. We will only use these for synonyms. |
| + | [AlternativeName](AlternativeName.md) | optional | 1..* | AlternativeName_VersionedChildStructure | ALTERNATIVE NAME for Element. |  |
|  | TopographicPlaceRef | optional | 1..* | TopographicPlaceRefStructure | Reference to a TOPOGRAPHIC PLACE. | Id to the county, community, canton or country. |
|  | Locale | optional | 1..1 | LocaleStructure | Common LOCALE dependent properties. |  |
| + | TimeZone | optional | 0..1 | xsd:normalizedString | Timezone name at LOCALE. | Must be present, when not in DefaultTimeZone. |
|  | StopPlaceType | optional | 0..1 | StopTypeEnumeration | Type of STOP PLACE. |  |
|  | LimitedUse | optional | 0..1 | LimitedUseTypeEnumeration | Further categorisation of stop as having topographic limitations. | For stops like Sagliains. We currently use only interchangeOnly. |
|  | Weighting | optional | 0..1 | InterchangeWeightingEnumeration | Default rating of the STOP PLACE for making interchanges. | Default relative weighting to be used for stop place. See also mapping excel. Cf. HafasPriority in Extensions. |
|  | quays | expected | 1..1 | quays_RelStructure | QUAYs within the STOP PLACE. | The Quays contained in the StopPlace - platforms, jetties, bays, taxi ranks, and other points of physical access to vehicles. Note that the usage (expected) overrides the cardinality. |
| + | [Quay](Quay.md) | expected | 0..* | Quay_VersionStructure | A place such as platform, stance, or quayside where passengers have access to PT vehicles, Taxi cars or other means of transportation. A QUAY may contain other sub QUAYs. A child QUAY must be physically contained within its parent QUAY. |  |
