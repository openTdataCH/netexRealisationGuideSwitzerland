# DefaultConnection_Operators

Connection between two operators on the whole network or on a defined STOP PLACE.

*Table: DefaultConnection*

| Sub | Element | Usage | Card | Type | Description | Note |
|-----|---------|-------|------|------|-------------|------|
|  | Extensions | optional | 1..1 | ExtensionsStructure |  | When also ProductCategory is relevant, then this extension must be used |
| + | FromProductCategoryRef | mandatory | 1..1 | unknown |  |  |
| + | ToProductCategoryRef | mandatory | 1..1 | unknown |  |  |
|  | WalkTransferDuration | mandatory | 0..1 | TransferDurationStructure |  |  |
| + | DefaultDuration | mandatory | 0..1 | xsd:duration |  |  |
|  | From | mandatory | 0..1 | ConnectionEndStructure |  |  |
| + | OperatorView | mandatory | 1..1 | unknown |  | Should be a sboid whenever possible. |
| ++ | OperatorRef | mandatory | 1..1 | OperatorRefStructure |  |  |
|  | To | mandatory | 0..1 | ConnectionEndStructure |  |  |
|  | StopPlaceRef | expected | 0..1 | StopPlaceRefStructure |  | Usually a SLOID. Not set means whole network. |
