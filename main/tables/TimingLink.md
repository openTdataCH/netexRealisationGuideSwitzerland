# TimingLink

A timing link is basically defined between two ScheduledStopPoints. However, there may be different timing behaviours and then multiple TimingLinks between the same ScheduledStopPoint might be necessary

*Table: TimingLink*

| Sub | Element | Usage | Card | Type | Description | Note |
|-----|---------|-------|------|------|-------------|------|
|  | @id | mandatory | 1..1 | xsd:string | Attribute id | |
|  | @version | mandatory | 1..1 | xsd:string | Attribute version | |
|  | privateCodes | optional | 1..1 | PrivateCodesStructure | A list of private codes that uniquely identifiy the element. May be used for inter-operating with other (legacy) systems. +v2.0 | only for the "virtual" stops like Bahn2000 |
| + | PrivateCode | optional | 0..* | PrivateCodeStructure | A private code that uniquely identifies the element. May be used for inter-operating with other (legacy) systems. | DIDOK code of the virtual stop |
| ++ | @type | mandatory | 1..1 | xsd:string | Attribute type | |
|  | Name | optional | 0..* | MultilingualString | Name of Traveller | Can be used to express "Neubaustrecke", "Lötschbergbasistunnel" and the like. |
|  | FromPointRef | mandatory | 1..1 | VehicleMeetingPointRefStructure | Identifier of VEHICLE MEETING POINT from which Link starts. | We use PointRef on purpose in preparation of BorderPoints. the nameOfClassRef helps to define this |
| + | @nameOfRefClass | mandatory | 1..1 | xsd:string | Attribute nameOfRefClass | |
|  | ToPointRef | mandatory | 0..1 | VehicleMeetingPointRefStructure | Identifier of VEHICLE MEETING POINT at which Link ends. | We use PointRef on purpose in preparation of BorderPoints. the nameOfClassRef helps to define this |
| + | @nameOfRefClass | mandatory | 1..1 | xsd:string | Attribute nameOfRefClass | |
|  | OperationalContextRef | optional | 1..1 | OperationalContextRefStructure | Reference to an OPERATIONAL CONTEXT. | This is "Betriebszweig". Switzerland does not use it currently, but it might become interesting at some point |
