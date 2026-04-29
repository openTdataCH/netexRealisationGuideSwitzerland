# StopPlace

| Sub | Element | Usage | Card | Type | Description | Note |
|-----|---------|-------|------|------|-------------|------|
|  | StopPlace | optional | 1..1 | unknown | Version of a named place where public transport may be accessed. May be a building complex (e.g. a station) or an on-street location. Can be a STOP PLACE, VEHICLE MEETING POINT, TAXI RANK. Note: If a master id exists for a StopPlace (must be stable and globally unique), then it is best used in the id. Optimally it would be built according IFOPT. It can also be put into one of the privateCodes in addition. If it is stored in KeyValue, then it should be documented well, so that importing systems know, which id is the relevant one. | Used for the abbreviation of the name if an abbreviation exists / is necessary |
| + | TopographicPlaceRef | optional | 1..* | TopographicPlaceRefStructure | Reference to the identifier of a TOPOGRAPHIC PLACE. |  |
| + | keyList | mandatory | 1..1 | KeyListStructure | A list of alternative Key values for an element. | KEY LIST with the KEY VALUEs related to the STOP PLACE.\
                                SKI use KeyValues:\
                                - one for the Didok number
                                - one for the SLOID
                                For delivery to SKI only one Value is necessary. |
| ++ | KeyValue | mandatory | 1..* | KeyValueStructure | Key value pair for Entity. |  |
| +++ | Key | mandatory | 1..1 | xsd:normalizedString | Identifier of value e.g. System. | DIDOK number has to be provided |
| +++ | Value | mandatory | 0..1 | xsd:anyType | Value associated with QUALITY STRUCTURE FACTOR. |  |
| + | privateCodes | mandatory | 1..1 | PrivateCodesStructure | A list of private codes that uniquely identifiy the element. May be used for inter-operating with other (legacy) systems. +v2.0 |  |
| ++ | PrivateCode | mandatory | 1..1 | PrivateCodeStructure | A private code that uniquely identifies the element. May be used for inter-operating with other (legacy) systems. | In Switzerland to be filled with the DiDok number. Replaces single PublicCode from NeTEx 1.0 |
| + | Extensions | optional | 1..1 | ExtensionsStructure | User defined Extensions to ENTITY in schema. (Wrapper tag used to avoid problems with handling of optional 'any' by some validators). | Extensions of the STOP PLACE:
                                - HafasPriority
                                - HafasKMInfo |
| ++ | HafasPriority | optional | 1..1 | unknown |  | (**TODO** Replace by Weighting ?) Interchange Priority, when several alternative interchange possibilities exist. |
| ++ | HafasKMInfo | optional | 1..1 | unknown |  | **TODO** ...Value for Interchange points. |
| + | Name | mandatory | 0..1 | MultilingualString | Name of Traveller |  |
| + | Centroid | mandatory | 0..1 | SimplePoint_VersionStructure | Centre Coordinates of GROUP of STOP PLACEs. | Global or national location of STOP PLACE. |
| ++ | Location | mandatory | 0..1 | LocationStructure | Absolute location of EQUIPMENT. | Note concerning coordinates:
- The main coordinates are given as **WSG84**.
- The Swiss coordinates are added as well, when available
- INFO+ will not use the data from the import. Always the DIDOK master data will be used for all Swiss coordinates. INFO+ will use the data of foreign places. |
| +++ | Longitude | mandatory | 1..1 | LongitudeType | Longitude from Greenwich Meridian. -180 (East) to +180 (West). |  |
| +++ | Latitude | mandatory | 1..1 | LatitudeType | Latitude from equator. -90 (South) to +90 (North). |  |
| +++ | Altitude | optional | 0..1 | AltitudeType | Altitude. |  |
| + | alternativeNames | optional | 0..1 | alternativeNames_RelStructure | ALTERNATIVE NAMES for MACHINE READABILITY. | **TODO** Alternative names for SITE ELEMENT.\
                                We will also use these for synonyms. From INFO+ the synonyms are used on the Stop-Place. |
| + | StopPlaceType | optional | 0..1 | StopTypeEnumeration | Type of STOP PLACE. |  |
| + | quays | expected | 1..1 | quays_RelStructure | QUAYs within the STOP PLACE. | The QUAYs contained in the STOP PLACE, that is platforms, jetties, bays, taxi ranks, and other points of physical access to VEHICLEs. |
| ++ | [Quay](Quay.md) | expected | 1..1 | unknown | A place such as platform, stance, or quayside where passengers have access to PT vehicles, Taxi
cars or other means of transportation. A QUAY may contain other sub QUAYs. A child QUAY must be physically
contained within its parent QUAY. |  |
