# PassengerStopAssignment_with_PassengerBoardingPositionAssignment

Stop assignments if formation is known.

*Table: PassengerStopAssignment*

| Sub | Element | Usage | Card | Type | Description | Note |
|-----|---------|-------|------|------|-------------|------|
|  | @id | mandatory | 1..1 | xsd:string | Attribute id | |
|  | @version | mandatory | 1..1 | xsd:string | Attribute version | |
|  | StopPlaceRef | mandatory | 0..1 | StopPlaceRefStructure |  | We assign the quay sector. The platform quay is known as the quay sector again references it (see definition of quay sector) |
|  | QuayRef | expected | 0..1 | QuayRefStructure | QUAY to which SCHEDULED STOP POINT is to be assigned. | Now we assign all train components to the sector with this sector/sector group. |
|  | passengerBoardingPositionAssignments | optional | 0..* | passengerBoardingPositionAssignments_RelStructure | Train stop assignments elements to use for which SCHEDULED STOP POINT is to be assigned. +v2.0 | Relevant for formations assigned to positions at quays. |
| + | PassengerBoardingPositionAssignment | optional | 1..1 | PassengerBoardingPositionAssignment_VersionStructure | The default allocation of a SCHEDULED STOP POINT to a specific STOP PLACE, and also possibly a QUAY and BOARDING POSITION. NB Rebmed from TRAIN STOP ASSIGNMENT in v2. |  |
| ++ | Description | optional | 0..1 | MultilingualString |  |  |
| ++ | ScheduledStopPointRef | mandatory | 0..1 | ScheduledStopPointRefStructure |  | This one needs to be on the sector level. |
| ++ | TrainComponentRef | expected | 0..1 | TrainComponentRefStructure |  | Map to the relevant TrainComponent |
