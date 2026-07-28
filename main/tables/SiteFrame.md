# SiteFrame

*Table: SiteFrame*

| Sub | Element | Usage | Card | Type | Description | Note |
|-----|---------|-------|------|------|-------------|------|
|  | @id | mandatory | 1..1 | xsd:string | Attribute id | |
|  | @version | mandatory | 1..1 | xsd:string | Attribute version | |
|  | topographicPlaces | expected | 0..1 | topographicPlacesInFrame_RelStructure |  |  |
| + | [TopographicPlace](TopographicPlace.md) | expected | 0..* | unknown |  | Used to represent countries if outside CH, cantons and communes if in CH. Cantons are referenced from StopPlaces. |
|  | stopPlaces | mandatory | 0..1 | stopPlacesInFrame_RelStructure |  |  |
| + | [StopPlace](StopPlace.md) | mandatory | 0..* | unknown | A STOP PLACE. |  |
|  | siteFacilitySets | optional | 0..1 | siteFacilitySetsInFrame_RelStructure |  | We expect the SiteFacilitySet in the ResourceFrame |
| + | [SiteFacilitySet](SiteFacilitySet.md) | optional | 0..* | unknown |  |  |
