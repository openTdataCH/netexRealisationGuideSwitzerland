# DefaultConnection_Modes

General connection between two modes in the whole network, when not StopPlaceRef is mentioned. Most exist for each mode pair.

*Table: DefaultConnection*

| Sub | Element | Usage | Card | Type | Description | Note |
|-----|---------|-------|------|------|-------------|------|
|  | WalkTransferDuration | mandatory | 0..1 | TransferDurationStructure | Timings for walking over TRANSFER if different from the JOURNEY PATTERN transfer duration, |  |
| + | DefaultDuration | mandatory | 0..1 | xsd:duration | Default time needed for a traveller to make a TRANSFER. |  |
|  | From | mandatory | 0..1 | ConnectionEndStructure | Origin end of ACCESS link. |  |
| + | TransportMode | mandatory | 0..1 | AllModesEnumeration | An area within a Site. May be connected to Quays by PATH LINKs. |  |
|  | To | mandatory | 0..1 | ConnectionEndStructure | Destination end of ACCESS link. |  |
|  | StopPlaceRef | expected | 0..1 | StopPlaceRefStructure | Reference to a STOP PLACE. | Usually a SLOID. Not set means whole network. |
