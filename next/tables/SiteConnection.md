# SiteConnection

SiteConnection are used only in the main file and not in timetable files.

*Table: SiteConnection*

| Sub | Element | Usage | Card | Type | Description | Note |
|-----|---------|-------|------|------|-------------|------|
|  | @id | mandatory | 1..1 | xsd:string | Attribute id | |
|  | @version | mandatory | 1..1 | xsd:string | Attribute version | |
|  | WalkTransferDuration | mandatory | 0..1 | TransferDurationStructure | Timings for walking over TRANSFER if different from the JOURNEY PATTERN transfer duration, |  |
| + | DefaultDuration | mandatory | 0..1 | xsd:duration | Default time needed for a traveller to make a TRANSFER. |  |
|  | BothWays | mandatory | 0..1 | xsd:boolean | Whether timings and validity applies to both directions (true) or just to the from-to direction of the TRANSFER. |  |
|  | From | mandatory | 0..1 | ConnectionEndStructure | Origin end of ACCESS link. | Could also refer to a Quay or a different SiteElement. Currently, we only transfer StopPlaceRefs. |
| + | StopPlaceRef | mandatory | 0..1 | StopPlaceRefStructure | Reference to a STOP PLACE. |  |
|  | To | mandatory | 0..1 | ConnectionEndStructure | Destination end of ACCESS link. | Could also refer to a Quay or a different SiteElement. Currently, we only transfer StopPlaceRefs. |
| + | StopPlaceRef | mandatory | 0..1 | StopPlaceRefStructure | Reference to a STOP PLACE. |  |
