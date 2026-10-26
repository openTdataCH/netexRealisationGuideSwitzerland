# DefaultConnection_Operators

Connection between two operators on the whole network or on a defined STOP PLACE.

*Table: DefaultConnection*

| Sub | Element | Usage | Card | Type | Description | Note |
|-----|---------|-------|------|------|-------------|------|
|  | Extensions | optional | 1..1 | ExtensionsStructure |  | When also ProductCategory is relevant, then this extension must be used |
| + | FromProductCategoryRef | mandatory | 1..1 | unknown |  |  |
| + | ToProductCategoryRef | mandatory | 1..1 | unknown |  |  |
|  | WalkTransferDuration | mandatory | 0..1 | TransferDurationStructure |  |  |
| + | DefaultDuration | mandatory | 0..1 | duration | Default time needed for a traveller to make a TRANSFER. |  |
|  | From | mandatory | 0..1 | DefaultConnectionEndStructure | Origin end of DEFAULT TRANSFER. |  |
| + | OperatorView | mandatory | 1..1 | unknown |  |  |
| ++ | OperatorRef | mandatory | 0..1 | OperatorRefStructure |  | Should be a SBOID whenever possible. |
|  | To | mandatory | 0..1 | DefaultConnectionEndStructure | Destination end of DEFAULT TRANSFER. |  |
|  | StopPlaceRef | expected | 0..1 | StopPlaceRefStructure |  | Usually a SLOID. Not set means whole network. |
