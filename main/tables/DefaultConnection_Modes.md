# DefaultConnection_Modes

General connection between two modes in the whole network, when not StopPlaceRef is mentioned. Most exist for each mode pair.

*Table: DefaultConnection*

| Sub | Element | Usage | Card | Type | Description | Note |
|-----|---------|-------|------|------|-------------|------|
|  | WalkTransferDuration | mandatory | 0..1 | TransferDurationStructure |  |  |
| + | DefaultDuration | mandatory | 0..1 | duration | Default time needed for a traveller to make a TRANSFER. |  |
|  | From | mandatory | 0..1 | DefaultConnectionEndStructure | Origin end of DEFAULT TRANSFER. |  |
| + | TransportMode | mandatory | 0..1 | AllModesEnumeration |  |  |
|  | To | mandatory | 0..1 | DefaultConnectionEndStructure | Destination end of DEFAULT TRANSFER. |  |
|  | StopPlaceRef | expected | 0..1 | StopPlaceRefStructure |  | Usually a SLOID. Not set means whole network. |
