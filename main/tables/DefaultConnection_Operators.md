# DefaultConnection_Operators

Connection between two operators on the whole network or on a defined STOP PLACE.

*Table: DefaultConnection*

| Sub | Element | Usage | Card | Type | Description | Note |
|-----|---------|-------|------|------|-------------|------|
|  | Extensions | optional | 1..1 | ExtensionsStructure | A coherent set of Service data to which the same frame VALIDITY CONDITIONs have been assigned. | When also ProductCategory is relevant, then this extension must be used |
| + | FromProductCategoryRef | mandatory | 1..1 | unknown | A coherent set of Service data to which the same frame VALIDITY CONDITIONs have been assigned. |  |
| + | ToProductCategoryRef | mandatory | 1..1 | unknown | A coherent set of Service data to which the same frame VALIDITY CONDITIONs have been assigned. |  |
|  | WalkTransferDuration | mandatory | 0..1 | TransferDurationStructure | A coherent set of Service data to which the same frame VALIDITY CONDITIONs have been assigned. |  |
| + | DefaultDuration | mandatory | 0..1 | xsd:duration | A coherent set of Service data to which the same frame VALIDITY CONDITIONs have been assigned. |  |
|  | From | mandatory | 0..1 | ConnectionEndStructure | A coherent set of Service data to which the same frame VALIDITY CONDITIONs have been assigned. |  |
| + | OperatorView | mandatory | 1..1 | unknown | A coherent set of Service data to which the same frame VALIDITY CONDITIONs have been assigned. | Should be a sboid whenever possible. |
| ++ | OperatorRef | mandatory | 1..1 | OperatorRefStructure | A coherent set of Service data to which the same frame VALIDITY CONDITIONs have been assigned. |  |
|  | To | mandatory | 0..1 | ConnectionEndStructure | A coherent set of Service data to which the same frame VALIDITY CONDITIONs have been assigned. |  |
|  | StopPlaceRef | expected | 0..1 | StopPlaceRefStructure | A coherent set of Service data to which the same frame VALIDITY CONDITIONs have been assigned. | Usually a SLOID. Not set means whole network. |
