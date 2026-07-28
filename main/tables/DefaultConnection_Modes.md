# DefaultConnection_Modes

General connection between two modes in the whole network, when not StopPlaceRef is mentioned. Most exist for each mode pair.

*Table: DefaultConnection*

| Sub | Element | Usage | Card | Type | Description | Note |
|-----|---------|-------|------|------|-------------|------|
|  | WalkTransferDuration | mandatory | 0..1 | TransferDurationStructure |  |  |
| + | DefaultDuration | mandatory | 0..1 | xsd:duration |  |  |
|  | From | mandatory | 0..1 | ConnectionEndStructure |  |  |
| + | TransportMode | mandatory | 0..1 | AllModesEnumeration |  |  |
|  | To | mandatory | 0..1 | ConnectionEndStructure |  |  |
|  | StopPlaceRef | expected | 0..1 | StopPlaceRefStructure |  | Usually a SLOID. Not set means whole network. |
