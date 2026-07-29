# PassengerStopAssignment

*Table: PassengerStopAssignment*

| Sub | Element | Usage | Card | Type | Description | Note |
|-----|---------|-------|------|------|-------------|------|
|  | @id | mandatory | 1..1 | xsd:string | Attribute id | |
|  | @version | mandatory | 1..1 | xsd:string | Attribute version | |
|  | ScheduledStopPointRef | mandatory | 0..1 | ScheduledStopPointRefStructure | Reference to a SCHEDULED STOP POINT. |  |
|  | StopPlaceRef | mandatory | 0..1 | StopPlaceRefStructure | Reference to a STOP PLACE. |  |
|  | QuayRef | expected | 0..1 | QuayRefStructure | Reference to a QUAY. | Not having the track may be problematic, but it can happen |
