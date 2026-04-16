# SiteFrame

| Sub | Element | Usage | Card | Type | Description | Note |
|-----|---------|-------|------|------|-------------|------|
|  | SiteFrame | expected | 1..1 | None | A coherent set of SITE data to which the same frame VALIDITY CONDITIONs have been assigned. | **TODO** most documenation from the RG is missing here. Pls note that with expection from ch-start and ch-stop. All other annotations are to be put within the element |
| + | topographicPlaces | optional | 0..1 | topographicPlacesInFrame_RelStructure | PLACEs in frame. |  |
| ++ | [TopographicPlace](TopographicPlace.md) | expected | 1..1 | None | A town, city, village, suburb, quarter or other name settlement within a country. Provides a Gazetteer of Transport related place names. |  |
| + | stopPlaces | mandatory | 0..1 | stopPlacesInFrame_RelStructure | STOP PLACEs in frame. |  |
| ++ | [StopPlace](StopPlace.md) | mandatory | 1..1 | None | Version of a named place where public transport may be accessed. May be a building complex (e.g. a station) or an on-street location. Can be a STOP PLACE, VEHICLE MEETING POINT, TAXI RANK. Note: If a master id exists for a StopPlace (must be stable and globally unique), then it is best used in the id. Optimally it would be built according IFOPT. It can also be put into one of the privateCodes in addition. If it is stored in KeyValue, then it should be documented well, so that importing systems know, which id is the relevant one. |  |
| + | siteFacilitySets | optional | 0..1 | siteFacilitySetsInFrame_RelStructure |  | We expect the SiteFacilitySet in the ResourceFrame |
| ++ | [SiteFacilitySet](SiteFacilitySet.md) | optional | 1..1 | None | Set of enumerated FACILITY values that are relevant to a SITE (names based on TPEG classifications, augmented with UIC etc.). |  |
