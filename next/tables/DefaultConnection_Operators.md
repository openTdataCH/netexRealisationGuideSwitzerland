# DefaultConnection_Operators

Connection between two operators on the whole network or on a defined STOP PLACE.

*Table: DefaultConnection*

| Sub | Element | Usage | Card | Type | Description | Note |
|-----|---------|-------|------|------|-------------|------|
|  | Extensions | optional | 1..1 | ExtensionsStructure | Extensions to schema. (Wrapper tag used to avoid problems with handling of optional 'any' by some validators). | When also ProductCategory is relevant, then this extension must be used |
| + | FromProductCategoryRef | mandatory | 1..1 | unknown |  |  |
| + | ToProductCategoryRef | mandatory | 1..1 | unknown |  |  |
|  | WalkTransferDuration | mandatory | 0..1 | TransferDurationStructure | Timings for walking over TRANSFER if different from the JOURNEY PATTERN transfer duration, |  |
| + | DefaultDuration | mandatory | 0..1 | xsd:duration | Default time needed for a traveller to make a TRANSFER. |  |
|  | From | mandatory | 0..1 | ConnectionEndStructure | Origin end of ACCESS link. |  |
| + | OperatorView | mandatory | 1..1 | Operator_DerivedViewStructure | Simplified view of OPERATOR. All data except the identifier will be derived through the relationship. |  |
| ++ | OperatorRef | mandatory | 1..1 | OperatorRefStructure | Reference to an OPERATOR. | Should be a SBOID whenever possible. |
|  | To | mandatory | 0..1 | ConnectionEndStructure | Destination end of ACCESS link. |  |
|  | StopPlaceRef | expected | 0..1 | StopPlaceRefStructure | Reference to a STOP PLACE. | Usually a SLOID. Not set means whole network. |
