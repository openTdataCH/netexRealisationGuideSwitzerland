# TrainComponent

The "logical" structure of the train.

*Table: TrainComponent*

| Sub | Element | Usage | Card | Type | Description | Note |
|-----|---------|-------|------|------|-------------|------|
|  | Label | expected | 0..1 | MultilingualString | Label for TRAIN COMPONENT. |  |
|  | [TrainElement](TrainElement.md) | expected | 1..1 | TrainElementType_VersionStructure | According to Transmodel 6.2 This shoud really be called TRAIN ELEMENT TYPE and be abstract . Use as concrete element DEPRECATED - use more specific TRAILING ELEMENT TYPE or TRACTIVE ELEMENT TYPE subtypes, Shoul dbe renmaed and removed in V3.0 |  |
|  | ForwardCoupling | optional | 0..1 | TrainComponentCouplingStructure | The nature of the coupling between the TRAIN COMPONENT and the TRAIN COMPONENT ahead of it within the TRAIN. +v2.0 |  |
| + | Splittable | optional | 0..1 | boolean | Whether the component can be split in normal usage. |  |
| + | ThroughAccess | optional | 1..1 | ThroughAccessEnumeration | Whether passenger can walk through coupling to next carriage. | If you can pass to the next carriage in front. |
