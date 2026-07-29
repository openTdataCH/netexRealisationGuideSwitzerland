# PassengerStopAssignment

*Table: PassengerStopAssignment*

| Sub | Element | Usage | Card | Type | Description | Note |
|-----|---------|-------|------|------|-------------|------|
|  | @id | mandatory | 1..1 | xsd:string | Attribute id | |
|  | @version | mandatory | 1..1 | xsd:string | Attribute version | |
|  | ScheduledStopPointRef | mandatory | 0..1 | ScheduledStopPointRefStructure | A coherent set of Service data to which the same frame VALIDITY CONDITIONs have been assigned. |  |
|  | StopPlaceRef | mandatory | 0..1 | StopPlaceRefStructure | A coherent set of Service data to which the same frame VALIDITY CONDITIONs have been assigned. |  |
|  | QuayRef | expected | 0..1 | QuayRefStructure | A coherent set of Service data to which the same frame VALIDITY CONDITIONs have been assigned. | Not having the track may be problematic, but it can happen |
