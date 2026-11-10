# SiteFrame

*Table: SiteFrame*

| Sub | Element | Usage | Card | Type | Description | Note |
|-----|---------|-------|------|------|-------------|------|
|  | @id | mandatory | 1..1 | xsd:string | Attribute id | |
|  | @version | mandatory | 1..1 | xsd:string | Attribute version | |
|  | topographicPlaces | expected | 0..1 | topographicPlacesInFrame_RelStructure | PLACEs in frame. |  |
| + | [TopographicPlace](TopographicPlace.md) | expected | 1..* | TopographicPlace_VersionStructure | A town, city, village, suburb, quarter or other name settlement within a country. Provides a Gazetteer of Transport related place names. | Used to represent countries if outside CH, cantons and communes if in CH. Cantons are referenced from StopPlaces. |
|  | stopPlaces | mandatory | 0..1 | stopPlacesInFrame_RelStructure | STOP PLACEs in frame. |  |
| + | [StopPlace](StopPlace.md) | mandatory | 1..* | StopPlace_VersionStructure | A STOP PLACE. |  |
|  | flexibleStopPlaces | optional | 0..1 | flexibleStopPlacesInFrame_RelStructure | STOP PLACEs in frame. | Service areas (Bediengebiete) of demand responsive services. Delivered in SITE_OFFER. |
| + | [FlexibleStopPlace](FlexibleStopPlace.md) | optional | 1..* | FlexibleStopPlace_VersionStructure | A named type of STOP PLACE for DRT comprising one or more flexible zones where vehicles may stop and where passengers may board or leave vehicles. |  |
|  | parkings | optional | 0..1 | parkingsInFrame_RelStructure | PARKINGs in frame. | Will be used at least in the export from ATLAS to ERSAD |
| + | Parking | optional | 0..* | Parking_VersionStructure | A named place where Parking may be accessed. May be a building complex (e.g. a station) or an on-street location. | Currently only very minimal as we don't have more information (e.g. no coordinates). |
| ++ | Name | optional | 0..1 | MultilingualString | Name of PARKING PROPERTIes.+V1.2.2 |  |
| ++ | ParentSiteRef | mandatory | 0..1 | SiteRefStructure |  |  |
| ++ | parkingAreas | optional | 0..1 | parkingAreas_RelStructure | PARKING AREAs within PARKING. |  |
| +++ | ParkingArea | optional | 0..* | ParkingArea_VersionStructure | Area within a PARKING. | Used to tell there is parking for handicapped people |
| ++++ | parkingProperties | optional | 1..1 | parkingProperties_RelStructure | Properties of PARKING AREA |  |
| +++++ | ParkingProperties | optional | 1..* | ParkingProperties_VersionedChildStructure | Properties of a PARKING. |  |
| ++++++ | ParkingUserTypes | optional | 0..1 | ParkingUserListOfEnumerations | Type of users: disabled, all etc. |  |
|  | siteFacilitySets | optional | 0..1 | siteFacilitySetsInFrame_RelStructure | SITE FACILITY SETs in frame . +v1.2.2 | We expect the SiteFacilitySet in the ResourceFrame |
| + | [SiteFacilitySet](SiteFacilitySet.md) | optional | 1..* | SiteFacilitySetStructure | Set of enumerated FACILITY values that are relevant to a SITE (names based on TPEG classifications, augmented with UIC etc.). |  |
