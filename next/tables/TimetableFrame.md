# TimetableFrame

*Table: TimetableFrame*

| Sub | Element | Usage | Card | Type | Description | Note |
|-----|---------|-------|------|------|-------------|------|
|  | @id | mandatory | 1..1 | xsd:string | Attribute id | |
|  | @version | mandatory | 1..1 | xsd:string | Attribute version | |
|  | vehicleJourneys | expected | 0..1 | journeysInFrame_RelStructure | VEHICLE JOURNEYs in frame. | Contains the ServiceJourneys and TemplateServiceJourneys. |
| + | [ServiceJourney](ServiceJourney.md) | expected | 0..* | unknown |  | ServiceJourney is used for common Journeys. |
| + | [TemplateServiceJourney](TemplateServiceJourney.md) | expected | 0..* | unknown | A VEHICLE JOURNEY with a set of frequencies that may be used to represent a set of similar journeys differing only by their time of departure. | TemplateServiceJourney is only to be used if a line is serviced at a certain frequency. |
|  | trainNumbers | expected | 0..1 | trainNumbersInFrame_RelStructure | TRAIN NUMBERs in frame. |  |
| + | [TrainNumber](TrainNumber.md) | mandatory | 0..* | TrainNumber_VersionStructure | Specification of codes assigned to particular VEHICLE JOURNEYs when operated by TRAINs of COMPOUND TRAINs according to a functional purpose (passenger information, operation follow-up, etc). |  |
|  | serviceFacilitySets | optional | 0..1 | serviceFacilitySetsInFrame_RelStructure | SERVICE FACILITies in frame. |  |
| + | [ServiceFacilitySet](ServiceFacilitySet.md) | expected | 1..* | ServiceFacilitySet_VersionStructure | Service FACILITY. Set of enumerated FACILITY values (Where available names are based on TPEG classifications, augmented with UIC etc.). |  |
|  | typesOfService | expected | 0..1 | typesOfServiceInFrame_RelStructure | TYPEs of SERVICE in frame. |  |
| + | TypeOfService | optional | 1..* | TypeOfServiceStructure | Classification of a Service. | This is exactly how the TypeOfService should be defined for Switzerland. Attention: Only once per file. |
| ++ | Name | expected | 0..1 | MultilingualString | Name of TYPE OF VALUE. |  |
| +++ | @lang | mandatory | 1..1 | xsd:string | Attribute lang | |
| ++ | ShortName | expected | 0..1 | MultilingualString | Short Name for TYPE OF VALUE. |  |
| +++ | @lang | mandatory | 1..1 | xsd:string | Attribute lang | |
| ++ | PrivateCode | optional | 0..1 | PrivateCodeStructure | DEPRECATED - use privateCodes. -v2.0 |  |
| + | [ServiceJourneyInterchange](ServiceJourneyInterchange.md) | expected | 1..1 | ServiceJourneyInterchange_VersionStructure | The scheduled possibility for transfer of passengers between two SERVICE JOURNEYs at the same or different STOP POINTs. | For modeling many forms of interchanges |
|  | vehicleTypes | optional | 0..1 | vehicleTypesInFrame_RelStructure | VEHICLE TYPEs in frame. | We will use this place to store Train and CompoundTrain information, when we will do formation. Not detailed at the moment |
| + | [CompoundTrain](CompoundTrain.md) | expected | 0..* | CompoundTrain_VersionStructure | A vehicle composed of COMPOUND TRAIN ELEMENTs in a certain order, i.e. of wagons assembled together and propelled by a locomotive or one of the wagons. |  |
| + | [Train](Train.md) | expected | 0..* | Train_VersionStructure | A vehicle composed of TRAIN ELEMENTs in a certain order, i.e. of wagons assembled together and propelled by a locomotive or one of the wagons. |  |
