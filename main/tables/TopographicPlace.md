# TopographicPlace

*Table: TopographicPlace*

| Sub | Element | Usage | Card | Type | Description | Note |
|-----|---------|-------|------|------|-------------|------|
|  | @id | mandatory | 1..1 | xsd:string | Attribute id | |
|  | @version | mandatory | 1..1 | xsd:string | Attribute version | |
|  | Descriptor | mandatory | 0..1 | TopographicPlaceDescriptor_VersionedChildStructure | PLACEs in frame. |  |
| + | Name | mandatory | 0..1 | MultilingualString | PLACEs in frame. |  |
| + | ShortName | expected | 0..1 | MultilingualString | PLACEs in frame. | Abbreviation of the canton (leave empty if TopographicPlaceType is country) |
|  | TopographicPlaceType | mandatory | 0..1 | TopographicPlaceTypeEnumeration | PLACEs in frame. | Allowed values: country, county |
|  | ParentTopographicPlaceRef | optional | 0..1 | TopographicPlaceRefStructure | PLACEs in frame. | Parent topographic place when it exists. |
