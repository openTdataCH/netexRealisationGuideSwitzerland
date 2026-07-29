# ScheduledStopPoint

Swiss ScheduledStopPoint are using the sloid in the id if possible. We keep the ScheduledStopPoint very minimalistic. The information is stored in the SiteFrame.

*Table: ScheduledStopPoint*

| Sub | Element | Usage | Card | Type | Description | Note |
|-----|---------|-------|------|------|-------------|------|
|  | @id | mandatory | 1..1 | xsd:string | Attribute id | |
|  | @version | mandatory | 1..1 | xsd:string | Attribute version | |
|  | keyList | optional | 1..1 | KeyListStructure | A coherent set of Service data to which the same frame VALIDITY CONDITIONs have been assigned. |  |
| + | KeyValue | optional | 1..* | KeyValueStructure | A coherent set of Service data to which the same frame VALIDITY CONDITIONs have been assigned. | Can contain a DIDOK key and a SLOID. We don't need it really. |
| ++ | Key | optional | 1..1 | xsd:normalizedString | A coherent set of Service data to which the same frame VALIDITY CONDITIONs have been assigned. |  |
| ++ | Value | optional | 0..1 | xsd:anyType | A coherent set of Service data to which the same frame VALIDITY CONDITIONs have been assigned. |  |
|  | privateCodes | optional | 1..1 | PrivateCodesStructure | A coherent set of Service data to which the same frame VALIDITY CONDITIONs have been assigned. |  |
| + | PrivateCode | optional | 0..* | PrivateCodeStructure | A coherent set of Service data to which the same frame VALIDITY CONDITIONs have been assigned. | If the id is not a SLOID then the SLOID must be added here. |
|  | Name | optional | 0..1 | MultilingualString | A coherent set of Service data to which the same frame VALIDITY CONDITIONs have been assigned. | The names are the same in all languages. Can be omitted as this is taken from the StopPlace/Quay. |
| + | @lang | mandatory | 1..1 | xsd:string | Attribute lang | |
|  | PublicCode | optional | 0..1 | PublicCodeStructure | A coherent set of Service data to which the same frame VALIDITY CONDITIONs have been assigned. | For Quay contains the plattform number/letter. |
