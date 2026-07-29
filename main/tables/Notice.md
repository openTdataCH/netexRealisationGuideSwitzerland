# Notice

*Table: Notice*

| Sub | Element | Usage | Card | Type | Description | Note |
|-----|---------|-------|------|------|-------------|------|
|  | @id | mandatory | 1..1 | xsd:string | Attribute id | |
|  | @version | mandatory | 1..1 | xsd:string | Attribute version | |
|  | Text | expected | 0..1 | MultilingualString | A coherent set of Service data to which the same frame VALIDITY CONDITIONs have been assigned. |  |
| + | @lang | mandatory | 1..1 | xsd:string | Attribute lang | |
| + | Text | expected | 0..* | MultilingualString | Name of the entity. |  |
| ++ | @lang | mandatory | 1..1 | xsd:string | Attribute lang | |
|  | PublicCode | mandatory | 0..1 | PublicCodeStructure | A coherent set of Service data to which the same frame VALIDITY CONDITIONs have been assigned. | The public code is transmitted when it is to be published and when it is the type of notice 10. Only 1 and 10 aree allowed. |
|  | ShortCode | expected | 0..1 | CleardownCodeType | A coherent set of Service data to which the same frame VALIDITY CONDITIONs have been assigned. | A duplication, but we want it. "A__" indicates an offer based on BS KI |
|  | PrivateCode | expected | 1..1 | PrivateCodeStructure | A coherent set of Service data to which the same frame VALIDITY CONDITIONs have been assigned. | A duplication, but we want it. |
|  | TypeOfNoticeRef | expected | 1..1 | TypeOfNoticeRefStructure | A coherent set of Service data to which the same frame VALIDITY CONDITIONs have been assigned. | allowed are ch:1:TypeOfNotice:1 for general notice, ch:1:TypeOfNotice:10 for offer, ch:1:TypeOfNotice:11 for region code (only PAG) |
|  | CanBeAdvertised | expected | 0..1 | xsd:boolean | A coherent set of Service data to which the same frame VALIDITY CONDITIONs have been assigned. | Whether the NOTICE is advertised. |
