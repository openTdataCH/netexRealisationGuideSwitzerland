# DefaultConnection_UMSTEIGB

| Sub | Element | Usage | Card | Type | Description | Note |
|-----|---------|-------|------|------|-------------|------|
|  | DefaultConnection | expected | 1..1 | unknown | Specifies the default transfer times to transfer between MODEs and / or OPERATORs within a region. | Be aware only some combinations areallowed  mode - mode, operator/type of product category - operator/type of  product category. |
| + | WalkTransferDuration | mandatory | 0..1 | TransferDurationStructure | Timings for walking over TRANSFER if different from the JOURNEY PATTERN transfer duration, |  |
| ++ | DefaultDuration | mandatory | 0..1 | xsd:duration | Default time needed for a traveller to make a TRANSFER. |  |
| + | StopPlaceRef | optional | 0..1 | StopPlaceRefStructure | System identifier of a STOP PLACE. May be omitted if given by context. |  |
