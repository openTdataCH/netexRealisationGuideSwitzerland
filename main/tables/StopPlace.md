# StopPlace

In some cases the id of a StopPlace is not a SLOID.

*Table: StopPlace*

| Sub | Element | Usage | Card | Type | Description | Note |
|-----|---------|-------|------|------|-------------|------|
|  | @id | mandatory | 1..1 | xsd:string | Attribute id | |
|  | @version | mandatory | 1..1 | xsd:string | Attribute version | |
|  | ValidBetween | optional | 1..1 | unknown |  | This can be used to show, when the StopPlace can be used. |
| + | FromDate | optional | 0..1 | xsd:dateTime | Start date of AVAILABILITY CONDITION. |  |
| + | ToDate | optional | 0..1 | xsd:dateTime | End of AVAILABILITY CONDITION. Date is INCLUSIVE. |  |
|  | keyList | expected | 1..1 | KeyListStructure |  | Key value pairs for DIDOK number and SLOID and special values. Prefered is privateCodes. |
| + | KeyValue | optional | 1..* | KeyValueStructure |  |  |
| ++ | Key | optional | 1..1 | xsd:normalizedString | Identifier of value e.g. System. |  |
| ++ | Value | optional | 0..1 | xsd:anyType | Value for alternative key. |  |
|  | privateCodes | mandatory | 1..1 | PrivateCodesStructure |  |  |
| + | PrivateCode | mandatory | 0..* | PrivateCodeStructure |  | In Switzerland to be filled with the DIDOK number and the SLOID. HafasPriority and HafasKMInfo are also types of PrivateCode used in Hafas environments. |
| ++ | @type | mandatory | 1..1 | xsd:string | Attribute type | |
|  | Name | mandatory | 0..1 | MultilingualString | Name of STOP PLACE. | The official stop name. If you have different versions one needs to use AlternativeName |
|  | Centroid | mandatory | 0..1 | SimplePoint_VersionStructure |  | Global or national location |
| + | Name | optional | 0..1 | MultilingualString |  |  |
| + | Location | mandatory | 0..1 | LocationStructure |  | Note concerning coordinates - The main coordinates are given as **WSG84**. |
| ++ | Longitude | mandatory | 1..1 | LongitudeType | Longitude from Greenwich Meridian. -180 (West) to +180 (East). Decimal degrees. eg 2.356 |  |
| ++ | Latitude | mandatory | 1..1 | LatitudeType | Latitude from equator. -90 (South) to +90 (North). Decimal degrees. eg 56.356 |  |
| ++ | Altitude | optional | 0..1 | AltitudeType | Altitude (metres) Above sea level. |  |
|  | alternativeNames | optional | 0..1 | alternativeNames_RelStructure |  | Alternative names for the StopPlace. We will also use these for synonyms. |
| + | [AlternativeName](AlternativeName.md) | optional | 1..* | unknown | ALTERNATIVE NAME for Element. |  |
|  | TopographicPlaceRef | optional | 1..* | TopographicPlaceRefStructure |  | Id to the county, community, canton or country. |
|  | StopPlaceType | optional | 0..1 | StopTypeEnumeration | Type of STOP PLACE. |  |
|  | LimitedUse | optional | 0..1 | LimitedUseTypeEnumeration |  | For stops like Sagliains |
|  | Weighting | optional | 0..1 | InterchangeWeightingEnumeration |  | Default relative weighting to be used for stop place. Cf. HafasPriority in Extensions. |
|  | quays | expected | 1..1 | quays_RelStructure |  | The Quays contained in the StopPlace - platforms, jetties, bays, taxi ranks, and other points of physical access to vehicles. |
| + | [Quay](Quay.md) | expected | 1..* | unknown |  |  |
