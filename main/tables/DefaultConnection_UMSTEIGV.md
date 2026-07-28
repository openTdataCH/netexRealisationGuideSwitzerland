# DefaultConnection_UMSTEIGV

*Table: DefaultConnection*

| Sub | Element | Usage | Card | Type | Description | Note |
|-----|---------|-------|------|------|-------------|------|
|  | Extensions | optional | 1..1 | ExtensionsStructure |  | When also ProductCategory is relevant, then this extension must be used |
| + | FromProductCategoryRef | mandatory | 1..1 | unknown |  | Extension needed to map "Verkehrsmittel-Gattung", which is similar to but more detailed than Trans-portSubmode, for transfer times of interchanges. |
| + | ToProductCategoryRef | mandatory | 1..1 | unknown |  | Extension needed to map "Verkehrsmittel-Gattung", which is similar to but more detailed than Trans-portSubmode, for transfer times of interchanges. |
|  | WalkTransferDuration | mandatory | 0..1 | TransferDurationStructure |  |  |
| + | DefaultDuration | mandatory | 0..1 | xsd:duration |  |  |
|  | BothWays | optional | 0..1 | xsd:boolean |  | We don't use BothWays true, as it might differ. |
|  | From | mandatory | 0..1 | ConnectionEndStructure |  |  |
| + | TransportMode | optional | 0..1 | AllModesEnumeration |  |  |
| + | OperatorView | optional | 1..1 | unknown |  | Should be a sboid whenever possible. |
| ++ | OperatorRef | mandatory | 1..1 | OperatorRefStructure |  |  |
|  | To | mandatory | 0..1 | ConnectionEndStructure |  |  |
|  | StopPlaceRef | optional | 0..1 | StopPlaceRefStructure |  | Usually a SLOID. Not set means whole network. |
