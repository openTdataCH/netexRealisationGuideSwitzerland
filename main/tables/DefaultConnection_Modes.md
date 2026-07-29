# DefaultConnection_Modes

General connection between two modes in the whole network, when not StopPlaceRef is mentioned. Most exist for each mode pair.

*Table: DefaultConnection*

| Sub | Element | Usage | Card | Type | Description | Note |
|-----|---------|-------|------|------|-------------|------|
|  | WalkTransferDuration | mandatory | 0..1 | TransferDurationStructure | A coherent set of Service data to which the same frame VALIDITY CONDITIONs have been assigned. |  |
| + | DefaultDuration | mandatory | 0..1 | xsd:duration | A coherent set of Service data to which the same frame VALIDITY CONDITIONs have been assigned. |  |
|  | From | mandatory | 0..1 | ConnectionEndStructure | A coherent set of Service data to which the same frame VALIDITY CONDITIONs have been assigned. |  |
| + | TransportMode | mandatory | 0..1 | AllModesEnumeration | A coherent set of Service data to which the same frame VALIDITY CONDITIONs have been assigned. |  |
|  | To | mandatory | 0..1 | ConnectionEndStructure | A coherent set of Service data to which the same frame VALIDITY CONDITIONs have been assigned. |  |
|  | StopPlaceRef | expected | 0..1 | StopPlaceRefStructure | A coherent set of Service data to which the same frame VALIDITY CONDITIONs have been assigned. | Usually a SLOID. Not set means whole network. |
