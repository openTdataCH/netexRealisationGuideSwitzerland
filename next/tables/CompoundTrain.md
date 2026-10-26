# CompoundTrain

*Table: CompoundTrain*

| Sub | Element | Usage | Card | Type | Description | Note |
|-----|---------|-------|------|------|-------------|------|
|  | Name | optional | 0..1 | MultilingualString | Name of TRAIN ELEMENT TYPE. |  |
|  | Description | optional | 0..1 | MultilingualString |  |  |
|  | SelfPropelled | expected | 0..1 | xsd:boolean |  |  |
|  | components | mandatory | 0..1 | trainsInCompoundTrain_RelStructure | Ordered collection of TRAIN in COMPOUND TRAINs making up COMPOUND TRAIN. Each references a TRAIN. |  |
| + | TrainInCompoundTrain | mandatory | 1..* | TrainInCompoundTrain_VersionedChildStructure | An instance of a TRAIN making up a COMPOUND TRAIN. |  |
| ++ | TrainRef | optional | 1..1 | TrainRefStructure | Reference to a TRAIN. |  |
| ++ | Label | optional | 0..1 | MultilingualString | Label for TRAIN IN COMPOUND TRAIN. |  |
