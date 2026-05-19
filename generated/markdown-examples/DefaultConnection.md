# DefaultConnection

| Sub | Element | Usage | Card | Type | Description | Note |
|-----|---------|-------|------|------|-------------|------|
|  | DefaultConnection | expected | 1..1 | unknown | Specifies the default transfer times to transfer between MODEs and / or OPERATORs within a region. | Be aware only some combinations areallowed  mode - mode, operator/type of product category - operator/type of  product category. |
| + | Extensions | optional | 1..1 | ExtensionsStructure | User defined Extensions to ENTITY in schema. (Wrapper tag used to avoid problems with handling of optional 'any' by some validators). | When also ProductCategory is relevant, then this extension must be used |
| ++ | FromProductCategoryRef | mandatory | 1..1 | unknown |  | Extension needed to map "Verkehrsmittel-Gattung", which is similar to but more detailed than Trans-portSubmode, for transfer times of interchanges. |
| ++ | ToProductCategoryRef | mandatory | 1..1 | unknown |  | Extension needed to map "Verkehrsmittel-Gattung", which is similar to but more detailed than Trans-portSubmode, for transfer times of interchanges. |
| + | WalkTransferDuration | mandatory | 0..1 | TransferDurationStructure | Timings for walking over TRANSFER if different from the JOURNEY PATTERN transfer duration, | We use WalkTransferDuration. At some point we need a solution for bicyle duration too (TSI telemetics) |
| ++ | MobilityRestrictedTravellerDuration | expected | 0..1 | xsd:duration | Time for a Mobility Restricted traveller to make a TRANSFER. |  |
| + | BothWays | optional | 0..1 | xsd:boolean | Whether timings and validity applies to both directions (true) or just to the from-to direction of the TRANSFER. | We always intend to use only one way, because the behaviour may not be the same. |
| + | From | mandatory | 0..1 | ConnectionEndStructure | Origin end of CONNECTION. |  |
| ++ | TransportMode | optional | 0..1 | AllModesEnumeration | MODE. |  |
| ++ | OperatorView | optional | 1..1 | unknown | Simplified view of OPERATOR. All data except the identifier will be derived through the relationship. |  |
| +++ | OperatorRef | mandatory | 1..1 | OperatorRefStructure | Reference to an OPERATOR. |  |
| + | To | mandatory | 0..1 | ConnectionEndStructure | Destination end of CONNECTION. |  |
| + | StopPlaceRef | optional | 0..1 | StopPlaceRefStructure | System identifier of a STOP PLACE. May be omitted if given by context. | Is a sloid usually. Not set, means whole network. |
