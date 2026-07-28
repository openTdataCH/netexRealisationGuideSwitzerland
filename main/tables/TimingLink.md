# TimingLink

A timing link is basically defined between two ScheduledStopPoints. However, there may be different timing behaviours and then multiple TimingLinks between the same ScheduledStopPoint might be necessary

*Table: TimingLink*

| Sub | Element | Usage | Card | Type | Description | Note |
|-----|---------|-------|------|------|-------------|------|
|  | @id | mandatory | 1..1 | xsd:string | Attribute id | |
|  | @version | mandatory | 1..1 | xsd:string | Attribute version | |
|  | privateCodes | optional | 1..1 | PrivateCodesStructure |  | only for the "virtual" stops like Bahn2000 |
| + | PrivateCode | optional | 0..* | PrivateCodeStructure |  | DIDOK code of the virtual stop |
| ++ | @type | mandatory | 1..1 | xsd:string | Attribute type | |
|  | Name | optional | 0..1 | MultilingualString |  | Can be used to express "Neubaustrecke", "Lötschbergbasistunnel" and the like. |
|  | FromPointRef | mandatory | 1..1 | VehicleMeetingPointRefStructure |  | We use PointRef on purpose in preparation of BorderPoints. the nameOfClassRef helps to define this |
| + | @nameOfRefClass | mandatory | 1..1 | xsd:string | Attribute nameOfRefClass | |
|  | ToPointRef | mandatory | 0..* | VehicleMeetingPointRefStructure | Identifier of POINT at which LINK ends. | We use PointRef on purpose in preparation of BorderPoints. the nameOfClassRef helps to define this |
| + | @nameOfRefClass | mandatory | 1..1 | xsd:string | Attribute nameOfRefClass | |
|  | OperationalContextRef | optional | 1..1 | OperationalContextRefStructure |  | This is "Betriebszweig". Switzerland does not use it currently, but it might become interesting at some point |
