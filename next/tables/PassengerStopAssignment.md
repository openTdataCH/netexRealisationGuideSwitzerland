# PassengerStopAssignment

*Table: PassengerStopAssignment*

| Sub | Element | Usage | Card | Type | Description | Note |
|-----|---------|-------|------|------|-------------|------|
|  | @id | mandatory | 1..1 | xsd:string | Attribute id | |
|  | @version | mandatory | 1..1 | xsd:string | Attribute version | |
|  | ScheduledStopPointRef | expected | 0..1 | ScheduledStopPointRefStructure |  | Be aware that a ScheduledStopPointRef is only not present, when we are doing `passengerBoardingPositionAssignments` |
|  | StopPlaceRef | mandatory | 0..1 | StopPlaceRefStructure |  |  |
|  | QuayRef | expected | 0..1 | QuayRefStructure | QUAY to which SCHEDULED STOP POINT is to be assigned. | Not having the track may be problematic, but it can happen sometimes for stops abroad. However, the goal is to always have a QuyRef. |
|  | passengerBoardingPositionAssignments | optional | 0..* | passengerBoardingPositionAssignments_RelStructure | Train stop assignments elements to use for which SCHEDULED STOP POINT is to be assigned. +v2.0 | Relevant for formations assigned to positions at quays. |
| + | PassengerBoardingPositionAssignment | optional | 1..1 | PassengerBoardingPositionAssignment_VersionStructure | The default allocation of a SCHEDULED STOP POINT to a specific STOP PLACE, and also possibly a QUAY and BOARDING POSITION. NB Rebmed from TRAIN STOP ASSIGNMENT in v2. |  |
| ++ | Description | optional | 0..1 | MultilingualString |  |  |
| ++ | ScheduledStopPointRef | mandatory | 0..1 | ScheduledStopPointRefStructure |  | This one needs to be on the sector level. |
| ++ | TrainComponentRef | expected | 0..1 | TrainComponentRefStructure |  | Map to the relevant TrainComponent |
