# Notice

*Table: Notice*

| Sub | Element | Usage | Card | Type | Description | Note |
|-----|---------|-------|------|------|-------------|------|
|  | @id | mandatory | 1..1 | xsd:string | Attribute id | |
|  | @version | mandatory | 1..1 | xsd:string | Attribute version | |
|  | Text | expected | 0..* | MultilingualString | Text content of NOTICe. |  |
| + | @lang | mandatory | 1..1 | xsd:string | Attribute lang | |
| + | Text | expected | 0..* | MultilingualString | Text content of NOTICe. |  |
| ++ | @lang | mandatory | 1..1 | xsd:string | Attribute lang | |
|  | PublicCode | mandatory | 0..1 | PublicCodeStructure | Public code for JOURNEY. | The public code is transmitted when it is to be published and when it is the type of notice 10. Only 1 and 10 aree allowed. |
|  | ShortCode | expected | 0..1 | CleardownCodeType | A 20 bit number used for wireless cleardown of stop displays by some AVL systems. | A duplication, but we want it. "A__" indicates an offer based on BS KI |
|  | PrivateCode | expected | 1..1 | PrivateCodeStructure | A private code that uniquely identifies the element. May be used for inter-operating with other (legacy) systems. | A duplication, but we want it. |
|  | TypeOfNoticeRef | expected | 1..1 | TypeOfNoticeRefStructure | Reference to a TYPE OF NOTICE. | allowed are ch:1:TypeOfNotice:1 for general notice, ch:1:TypeOfNotice:10 for offer, ch:1:TypeOfNotice:11 for region code (only PAG) |
|  | CanBeAdvertised | expected | 0..1 | xsd:boolean | Whether NOTICE is advertised to public. This may be overridden on an assignment. | Whether the NOTICE is advertised. |
