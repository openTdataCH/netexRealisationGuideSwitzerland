# SiteConnection

SiteConnection are used only in the main file and not in timetable files.

*Table: SiteConnection*

| Sub | Element | Usage | Card | Type | Description | Note |
|-----|---------|-------|------|------|-------------|------|
|  | @id | mandatory | 1..1 | xsd:string | Attribute id | |
|  | @version | mandatory | 1..1 | xsd:string | Attribute version | |
|  | WalkTransferDuration | mandatory | 0..1 | TransferDurationStructure | A coherent set of Service data to which the same frame VALIDITY CONDITIONs have been assigned. |  |
| + | DefaultDuration | mandatory | 0..1 | xsd:duration | A coherent set of Service data to which the same frame VALIDITY CONDITIONs have been assigned. |  |
|  | BothWays | mandatory | 0..1 | xsd:boolean | A coherent set of Service data to which the same frame VALIDITY CONDITIONs have been assigned. |  |
|  | From | mandatory | 0..1 | ConnectionEndStructure | A coherent set of Service data to which the same frame VALIDITY CONDITIONs have been assigned. | Could also refer to a Quay or a different SiteElement. Currently, we only transfer StopPlaceRefs. |
| + | StopPlaceRef | mandatory | 0..1 | StopPlaceRefStructure | A coherent set of Service data to which the same frame VALIDITY CONDITIONs have been assigned. |  |
|  | To | mandatory | 0..1 | ConnectionEndStructure | A coherent set of Service data to which the same frame VALIDITY CONDITIONs have been assigned. | Could also refer to a Quay or a different SiteElement. Currently, we only transfer StopPlaceRefs. |
| + | StopPlaceRef | mandatory | 0..1 | StopPlaceRefStructure | A coherent set of Service data to which the same frame VALIDITY CONDITIONs have been assigned. |  |
