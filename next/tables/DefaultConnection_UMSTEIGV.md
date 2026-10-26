# DefaultConnection_UMSTEIGV

*Table: DefaultConnection*

| Sub | Element | Usage | Card | Type | Description | Note |
|-----|---------|-------|------|------|-------------|------|
|  | Extensions | optional | 1..1 | ExtensionsStructure |  | When also ProductCategory is relevant, then this extension must be used |
| + | FromProductCategoryRef | mandatory | 1..1 | unknown |  | Extension needed to map "Verkehrsmittel-Gattung", which is similar to but more detailed than Trans-portSubmode, for transfer times of interchanges. |
| + | ToProductCategoryRef | mandatory | 1..1 | unknown |  | Extension needed to map "Verkehrsmittel-Gattung", which is similar to but more detailed than Trans-portSubmode, for transfer times of interchanges. |
|  | WalkTransferDuration | mandatory | 0..1 | TransferDurationStructure |  |  |
| + | DefaultDuration | mandatory | 0..1 | duration | Default time needed for a traveller to make a TRANSFER. |  |
|  | BothWays | optional | 0..1 | xsd:boolean |  | We don't use BothWays true, as it might differ. |
|  | From | mandatory | 0..1 | DefaultConnectionEndStructure | Origin end of DEFAULT TRANSFER. |  |
| + | TransportMode | optional | 0..1 | AllModesEnumeration |  |  |
| + | OperatorView | optional | 1..1 | unknown |  |  |
| ++ | OperatorRef | mandatory | 0..1 | OperatorRefStructure |  | Should be a SBOID whenever possible. |
|  | To | mandatory | 0..1 | DefaultConnectionEndStructure | Destination end of DEFAULT TRANSFER. |  |
|  | StopPlaceRef | optional | 0..1 | StopPlaceRefStructure |  | Usually a SLOID. Not set means whole network. |
