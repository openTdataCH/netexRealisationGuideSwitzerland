# DefaultConnection_Modes

General connection between two modes in the whole network, when not StopPlaceRef is mentioned. Most exist for each mode pair.

*Table: DefaultConnection*

| Sub | Element | Usage | Card | Type | Description | Note |
|-----|---------|-------|------|------|-------------|------|
|  | WalkTransferDuration | mandatory | 0..1 | TransferDurationStructure | Timings for walking over TRANSFER if different from the JOURNEY PATTERN transfer duration, |  |
| + | DefaultDuration | mandatory | 0..1 | xsd:duration | Default time needed for a traveller to make a TRANSFER. |  |
|  | From | mandatory | 0..1 | ConnectionEndStructure | Origin end of CONNECTION. |  |
| + | TransportMode | mandatory | 0..1 | AllModesEnumeration | MODE. |  |
|  | To | mandatory | 0..1 | ConnectionEndStructure | Destination end of CONNECTION. |  |
|  | StopPlaceRef | expected | 0..1 | StopPlaceRefStructure | System identifier of a STOP PLACE. May be omitted if given by context. | Usually a SLOID. Not set means whole network. |
