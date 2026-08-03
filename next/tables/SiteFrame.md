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
|  | siteFacilitySets | optional | 0..1 | siteFacilitySetsInFrame_RelStructure | SITE FACILITY SETs in frame . +v1.2.2 | We expect the SiteFacilitySet in the ResourceFrame |
| + | [SiteFacilitySet](SiteFacilitySet.md) | optional | 1..* | SiteFacilitySetStructure | Set of enumerated FACILITY values that are relevant to a SITE (names based on TPEG classifications, augmented with UIC etc.). |  |
