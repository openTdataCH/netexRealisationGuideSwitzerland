# StopPlace

| Sub | Element | Usage | Card | Type | Description | Note |
|-----|---------|-------|------|------|-------------|------|
|  | StopPlace | mandatory | 1..1 | unknown | Version of a named place where public transport may be accessed. May be a building complex (e.g. a station) or an on-street location. Can be a STOP PLACE, VEHICLE MEETING POINT, TAXI RANK. Note: If a master id exists for a StopPlace (must be stable and globally unique), then it is best used in the id. Optimally it would be built according IFOPT. It can also be put into one of the privateCodes in addition. If it is stored in KeyValue, then it should be documented well, so that importing systems know, which id is the relevant one. | In some cases the id is not a sloid. |
| + | ValidBetween | optional | 1..1 | unknown | OPTIMISATION. Simple version of a VALIDITY CONDITION. Comprises a simple period. NO UNIQUENESS CONSTRAINT. | This can be used to show, when the StopPlace can be used. |
| ++ | FromDate | mandatory | 0..1 | xsd:dateTime | Start date of AVAILABILITY CONDITION. |  |
| ++ | ToDate | mandatory | 0..1 | xsd:dateTime | End of AVAILABILITY CONDITION. Date is INCLUSIVE. |  |
| + | keyList | mandatory | 1..1 | KeyListStructure | A list of alternative Key values for an element. | Key value pairs for DIDOK number and SLOID |
| ++ | KeyValue | mandatory | 1..* | KeyValueStructure | Key value pair for Entity. |  |
| +++ | Key | mandatory | 1..1 | xsd:normalizedString | Identifier of value e.g. System. |  |
| +++ | Value | mandatory | 0..1 | xsd:anyType | Value associated with QUALITY STRUCTURE FACTOR. |  |
| + | privateCodes | mandatory | 1..1 | PrivateCodesStructure | A list of private codes that uniquely identifiy the element. May be used for inter-operating with other (legacy) systems. +v2.0 |  |
| ++ | PrivateCode | mandatory | 1..1 | PrivateCodeStructure | A private code that uniquely identifies the element. May be used for inter-operating with other (legacy) systems. | In Switzerland to be filled with the didok number and the sloid |
| ++ | @type | mandatory | 1..1 | xsd:string | Attribute type | |
| + | Extensions | optional | 1..1 | ExtensionsStructure | User defined Extensions to ENTITY in schema. (Wrapper tag used to avoid problems with handling of optional 'any' by some validators). |  |
| ++ | HafasPriority | optional | 1..1 | unknown |  | Interchange priority if several alternative interchange possibilities exist. Integer allows for finer grained value than standard element Weighting. |
| ++ | HafasKMInfo | optional | 1..1 | unknown |  | Special value for Hafas environments. |
| + | Name | mandatory | 0..1 | MultilingualString | Name of Traveller |  |
| + | Centroid | mandatory | 0..1 | SimplePoint_VersionStructure | Centre Coordinates of GROUP of STOP PLACEs. | Global or national location |
| ++ | Location | mandatory | 0..1 | LocationStructure | Absolute location of EQUIPMENT. | Note concerning coordinates - The main coordinates are given as **WSG84**. |
| +++ | Longitude | mandatory | 1..1 | LongitudeType | Longitude from Greenwich Meridian. -180 (East) to +180 (West). |  |
| +++ | Latitude | mandatory | 1..1 | LatitudeType | Latitude from equator. -90 (South) to +90 (North). |  |
| +++ | Altitude | optional | 0..1 | AltitudeType | Altitude. |  |
| + | alternativeNames | optional | 0..1 | alternativeNames_RelStructure | ALTERNATIVE NAMES for MACHINE READABILITY. | Alternative names for the StopPlace. We will also use these for synonyms. From INFO+ the synonyms are used on the Stop-Place. |
| + | TopographicPlaceRef | optional | 1..* | TopographicPlaceRefStructure | Reference to the identifier of a TOPOGRAPHIC PLACE. | Id to the county, community, canton or country. |
| + | StopPlaceType | optional | 0..1 | StopTypeEnumeration | Type of STOP PLACE. |  |
| + | Weighting | optional | 0..1 | InterchangeWeightingEnumeration | Default rating of the STOP PLACE for making interchanges. | Default relative weighting to be used for stop place. Cf. HafasPriority in Extensions. |
| + | quays | expected | 1..1 | quays_RelStructure | QUAYs within the STOP PLACE. | The Quays contained in the StopPlace - platforms, jetties, bays, taxi ranks, and other points of physical access to vehicles. |
| ++ | [Quay](Quay.md) | expected | 1..1 | unknown | A place such as platform, stance, or quayside where passengers have access to PT vehicles, Taxi
cars or other means of transportation. A QUAY may contain other sub QUAYs. A child QUAY must be physically
contained within its parent QUAY. |  |
