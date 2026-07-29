# DefaultConnection_UMSTEIGV

*Table: DefaultConnection*

| Sub | Element | Usage | Card | Type | Description | Note |
|-----|---------|-------|------|------|-------------|------|
|  | Extensions | optional | 1..1 | ExtensionsStructure | A coherent set of Service data to which the same frame VALIDITY CONDITIONs have been assigned. | When also ProductCategory is relevant, then this extension must be used |
| + | FromProductCategoryRef | mandatory | 1..1 | unknown | A coherent set of Service data to which the same frame VALIDITY CONDITIONs have been assigned. | Extension needed to map "Verkehrsmittel-Gattung", which is similar to but more detailed than Trans-portSubmode, for transfer times of interchanges. |
| + | ToProductCategoryRef | mandatory | 1..1 | unknown | A coherent set of Service data to which the same frame VALIDITY CONDITIONs have been assigned. | Extension needed to map "Verkehrsmittel-Gattung", which is similar to but more detailed than Trans-portSubmode, for transfer times of interchanges. |
|  | WalkTransferDuration | mandatory | 0..1 | TransferDurationStructure | A coherent set of Service data to which the same frame VALIDITY CONDITIONs have been assigned. |  |
| + | DefaultDuration | mandatory | 0..1 | xsd:duration | A coherent set of Service data to which the same frame VALIDITY CONDITIONs have been assigned. |  |
|  | BothWays | optional | 0..1 | xsd:boolean | A coherent set of Service data to which the same frame VALIDITY CONDITIONs have been assigned. | We don't use BothWays true, as it might differ. |
|  | From | mandatory | 0..1 | ConnectionEndStructure | A coherent set of Service data to which the same frame VALIDITY CONDITIONs have been assigned. |  |
| + | TransportMode | optional | 0..1 | AllModesEnumeration | A coherent set of Service data to which the same frame VALIDITY CONDITIONs have been assigned. |  |
| + | OperatorView | optional | 1..1 | unknown | A coherent set of Service data to which the same frame VALIDITY CONDITIONs have been assigned. | Should be a sboid whenever possible. |
| ++ | OperatorRef | mandatory | 1..1 | OperatorRefStructure | A coherent set of Service data to which the same frame VALIDITY CONDITIONs have been assigned. |  |
|  | To | mandatory | 0..1 | ConnectionEndStructure | A coherent set of Service data to which the same frame VALIDITY CONDITIONs have been assigned. |  |
|  | StopPlaceRef | optional | 0..1 | StopPlaceRefStructure | A coherent set of Service data to which the same frame VALIDITY CONDITIONs have been assigned. | Usually a SLOID. Not set means whole network. |
