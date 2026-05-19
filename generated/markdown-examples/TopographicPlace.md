# TopographicPlace

| Sub | Element | Usage | Card | Type | Description | Note |
|-----|---------|-------|------|------|-------------|------|
|  | TopographicPlace | mandatory | 1..1 | unknown | A town, city, village, suburb, quarter or other name settlement within a country. Provides a Gazetteer of Transport related place names. |  |
| + | Descriptor | mandatory | 1..1 | TopographicPlaceDescriptor_VersionedChildStructure | Structured text descriptor of TOPOGRAPHIC PLACE. |  |
| ++ | Name | mandatory | 0..1 | MultilingualString | Name of Traveller |  |
| ++ | ShortName | expected | 0..1 | MultilingualString | Short Name for service | Abbreviation of the canton (leave empty if TopographicPlaceType is country) |
| + | TopographicPlaceType | mandatory | 0..1 | TopographicPlaceTypeEnumeration | Classification of the TOPOGRAPHIC PLACE as a settlement. Enumerated value. | Allowed values: country, county |
| + | ParentTopographicPlaceRef | optional | 0..1 | TopographicPlaceRefStructure | Parent TOPOGRAPHIC PLACE. Reference to another TOPOGRAPHIC PLACE that contains the child TOPOGRAPHIC PLACE completely. Must not be cyclic. | Parent topographic place when it exists. |
