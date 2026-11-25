# DefaultConnection

Be aware only some combinations are allowed: from mode A to mode B without operators taken into account; from operator A and product category A to operator B and product category B.

*Table: DefaultConnection*

| Sub | Element | Usage | Card | Type | Description | Note |
|-----|---------|-------|------|------|-------------|------|
|  | @id | mandatory | 1..1 | xsd:string | Attribute id | |
|  | @version | mandatory | 1..1 | xsd:string | Attribute version | |
|  | Extensions | optional | 1..1 | ExtensionsStructure |  | When also ProductCategory is relevant, then this extension must be used |
| + | FromProductCategoryRef | mandatory | 1..1 | unknown |  | Extension needed to map "Verkehrsmittel-Gattung", which is similar to but more detailed than Trans-portSubmode, for transfer times of interchanges. |
| + | ToProductCategoryRef | mandatory | 1..1 | unknown |  | Extension needed to map "Verkehrsmittel-Gattung", which is similar to but more detailed than Trans-portSubmode, for transfer times of interchanges. |
|  | WalkTransferDuration | mandatory | 0..1 | TransferDurationStructure |  | We use WalkTransferDuration. At some point we need a solution for bicyle duration too (TSI telemetics) |
| + | MobilityRestrictedTravellerDuration | expected | 0..1 | duration | Time for a Mobility Restricted traveller to make a TRANSFER. |  |
|  | BothWays | optional | 0..1 | xsd:boolean |  | Should be false - we always intend to use only one way because the behaviour may not be the same. |
|  | TransferMode | optional | 0..1 | AccessModeEnumeration |  | Is foot. Others might become possible in future |
|  | From | mandatory | 0..1 | DefaultConnectionEndStructure | Origin end of DEFAULT TRANSFER. |  |
| + | TransportMode | optional | 0..1 | AllModesEnumeration |  | All codes are shown in mapping excel. Use with care. |
| + | OperatorView | optional | 1..1 | unknown |  |  |
| ++ | OperatorRef | mandatory | 0..1 | OperatorRefStructure |  | Should be a SBOID whenever possible. |
|  | To | mandatory | 0..1 | DefaultConnectionEndStructure | Destination end of DEFAULT TRANSFER. |  |
|  | StopPlaceRef | optional | 0..1 | StopPlaceRefStructure |  | Usually a SLOID. Not set means whole network. |
