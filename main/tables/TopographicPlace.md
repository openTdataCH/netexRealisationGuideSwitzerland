# TopographicPlace

*Table: TopographicPlace*

| Sub | Element | Usage | Card | Type | Description | Note |
|-----|---------|-------|------|------|-------------|------|
|  | @id | mandatory | 1..1 | xsd:string | Attribute id | |
|  | @version | mandatory | 1..1 | xsd:string | Attribute version | |
|  | Descriptor | mandatory | 1..1 | TopographicPlaceDescriptor_VersionedChildStructure |  |  |
| + | Name | mandatory | 0..1 | MultilingualString | Name of the TOPOGRAPHIC PLACE. |  |
| + | ShortName | expected | 0..1 | MultilingualString | Short name for TOPOGRAPHIC PLACE to be used when qualifying children. | Abbreviation of the canton (leave empty if TopographicPlaceType is country) |
|  | TopographicPlaceType | mandatory | 0..1 | TopographicPlaceTypeEnumeration |  | Allowed values: country, county |
|  | ParentTopographicPlaceRef | optional | 0..1 | TopographicPlaceRefStructure |  | Parent topographic place when it exists. |
