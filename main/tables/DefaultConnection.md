# DefaultConnection

Be aware only some combinations are allowed: from mode A to mode B without operators taken into account; from operator A and product category A to operator B and product category B.

*Table: DefaultConnection*

| Sub | Element | Usage | Card | Type | Description | Note |
|-----|---------|-------|------|------|-------------|------|
|  | @id | mandatory | 1..1 | xsd:string | Attribute id | |
|  | @version | mandatory | 1..1 | xsd:string | Attribute version | |
|  | Extensions | optional | 1..1 | ExtensionsStructure | A coherent set of Service data to which the same frame VALIDITY CONDITIONs have been assigned. | When also ProductCategory is relevant, then this extension must be used |
| + | FromProductCategoryRef | mandatory | 1..1 | unknown | A coherent set of Service data to which the same frame VALIDITY CONDITIONs have been assigned. | Extension needed to map "Verkehrsmittel-Gattung", which is similar to but more detailed than Trans-portSubmode, for transfer times of interchanges. |
| + | ToProductCategoryRef | mandatory | 1..1 | unknown | A coherent set of Service data to which the same frame VALIDITY CONDITIONs have been assigned. | Extension needed to map "Verkehrsmittel-Gattung", which is similar to but more detailed than Trans-portSubmode, for transfer times of interchanges. |
|  | WalkTransferDuration | mandatory | 0..1 | TransferDurationStructure | A coherent set of Service data to which the same frame VALIDITY CONDITIONs have been assigned. | We use WalkTransferDuration. At some point we need a solution for bicyle duration too (TSI telemetics) |
| + | MobilityRestrictedTravellerDuration | expected | 0..1 | xsd:duration | A coherent set of Service data to which the same frame VALIDITY CONDITIONs have been assigned. |  |
|  | BothWays | optional | 0..1 | xsd:boolean | A coherent set of Service data to which the same frame VALIDITY CONDITIONs have been assigned. | Should be false - we always intend to use only one way because the behaviour may not be the same. |
|  | From | mandatory | 0..1 | ConnectionEndStructure | A coherent set of Service data to which the same frame VALIDITY CONDITIONs have been assigned. |  |
| + | TransportMode | optional | 0..1 | AllModesEnumeration | A coherent set of Service data to which the same frame VALIDITY CONDITIONs have been assigned. |  |
| + | OperatorView | optional | 1..1 | unknown | A coherent set of Service data to which the same frame VALIDITY CONDITIONs have been assigned. | Should be a sboid whenever possible. |
| ++ | OperatorRef | mandatory | 1..1 | OperatorRefStructure | A coherent set of Service data to which the same frame VALIDITY CONDITIONs have been assigned. |  |
|  | To | mandatory | 0..1 | ConnectionEndStructure | A coherent set of Service data to which the same frame VALIDITY CONDITIONs have been assigned. |  |
|  | StopPlaceRef | optional | 0..1 | StopPlaceRefStructure | A coherent set of Service data to which the same frame VALIDITY CONDITIONs have been assigned. | Usually a SLOID. Not set means whole network. |
