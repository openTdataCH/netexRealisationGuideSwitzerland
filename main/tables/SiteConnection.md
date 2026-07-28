# SiteConnection

SiteConnection are used only in the main file and not in timetable files.

*Table: SiteConnection*

| Sub | Element | Usage | Card | Type | Description | Note |
|-----|---------|-------|------|------|-------------|------|
|  | @id | mandatory | 1..1 | xsd:string | Attribute id | |
|  | @version | mandatory | 1..1 | xsd:string | Attribute version | |
|  | WalkTransferDuration | mandatory | 0..1 | TransferDurationStructure |  |  |
| + | DefaultDuration | mandatory | 0..1 | xsd:duration |  |  |
|  | BothWays | mandatory | 0..1 | xsd:boolean |  |  |
|  | From | mandatory | 0..1 | ConnectionEndStructure |  | Could also refer to a Quay or a different SiteElement. Currently, we only transfer StopPlaceRefs. |
| + | StopPlaceRef | mandatory | 0..1 | StopPlaceRefStructure |  |  |
|  | To | mandatory | 0..1 | ConnectionEndStructure |  | Could also refer to a Quay or a different SiteElement. Currently, we only transfer StopPlaceRefs. |
| + | StopPlaceRef | mandatory | 0..1 | StopPlaceRefStructure |  |  |
