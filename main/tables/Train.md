# Train

*Table: Train*

| Sub | Element | Usage | Card | Type | Description | Note |
|-----|---------|-------|------|------|-------------|------|
|  | Name | optional | 0..1 | MultilingualString | Name of TRAIN ELEMENT TYPE. |  |
|  | Description | optional | 0..1 | MultilingualString |  |  |
|  | SelfPropelled | expected | 0..1 | xsd:boolean |  |  |
|  | components | mandatory | 0..1 | trainComponents_RelStructure | Ordered collection of TRAIN COMPONENTs making up TRAIN. | Can contain TrainComponent or TrainComponentRefs. order is not used, as the XML order defines, the order of the elements |
| + | [TrainComponent](TrainComponent.md) | expected. | 0..* | TrainComponent_VersionStructure | An area within a Site. May be connected to Quays by PATH LINKs. |  |
| + | TrainComponentRef | expected | 0..* | TrainComponentRefStructure |  |  |
