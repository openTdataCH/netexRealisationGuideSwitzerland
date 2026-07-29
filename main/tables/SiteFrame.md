# SiteFrame

*Table: SiteFrame*

| Sub | Element | Usage | Card | Type | Description | Note |
|-----|---------|-------|------|------|-------------|------|
|  | @id | mandatory | 1..1 | xsd:string | Attribute id | |
|  | @version | mandatory | 1..1 | xsd:string | Attribute version | |
|  | topographicPlaces | expected | 0..1 | topographicPlacesInFrame_RelStructure | PLACEs in frame. |  |
| + | [TopographicPlace](TopographicPlace.md) | expected | 0..* | topographicPlacesInFrame_RelStructure | PLACEs in frame. | Used to represent countries if outside CH, cantons and communes if in CH. Cantons are referenced from StopPlaces. |
|  | stopPlaces | mandatory | 0..1 | stopPlacesInFrame_RelStructure | STOP PLACEs in frame. |  |
| + | [StopPlace](StopPlace.md) | mandatory | 0..* | stopPlacesInFrame_RelStructure | STOP PLACEs in frame. |  |
|  | siteFacilitySets | optional | 0..1 | siteFacilitySetsInFrame_RelStructure | SITE FACILITY SETs in frame . +v1.2.2 | We expect the SiteFacilitySet in the ResourceFrame |
| + | [SiteFacilitySet](SiteFacilitySet.md) | optional | 0..* | siteFacilitySetsInFrame_RelStructure | SITE FACILITY SETs in frame . +v1.2.2 |  |
