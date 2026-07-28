# TimetableFrame

*Table: TimetableFrame*

| Sub | Element | Usage | Card | Type | Description | Note |
|-----|---------|-------|------|------|-------------|------|
|  | @id | mandatory | 1..1 | xsd:string | Attribute id | |
|  | @version | mandatory | 1..1 | xsd:string | Attribute version | |
|  | vehicleJourneys | expected | 0..1 | journeysInFrame_RelStructure |  | Contains the ServiceJourneys and TemplateServiceJourneys. |
| + | [ServiceJourney](ServiceJourney.md) | expected | 1..1 | unknown |  | ServiceJourney is used for common Journeys. |
| + | [TemplateServiceJourney](TemplateServiceJourney.md) | expected | 1..1 | unknown |  | TemplateServiceJourney is only to be used if a line is serviced at a certain frequency. |
|  | trainNumbers | expected | 0..1 | trainNumbersInFrame_RelStructure |  |  |
| + | [TrainNumber](TrainNumber.md) | mandatory | 1..* | unknown |  |  |
|  | serviceFacilitySets | optional | 0..1 | serviceFacilitySetsInFrame_RelStructure |  |  |
| + | [ServiceFacilitySet](ServiceFacilitySet.md) | expected | 1..* | unknown |  |  |
|  | typesOfService | expected | 0..1 | typesOfServiceInFrame_RelStructure |  |  |
| + | TypeOfService | optional | 1..* | unknown |  | This is exactly how the TypeOfService should be defined for Switzerland. Attention: Only once per file. |
| ++ | Name | expected | 0..1 | MultilingualString |  |  |
| +++ | @lang | mandatory | 1..1 | xsd:string | Attribute lang | |
| ++ | ShortName | expected | 0..1 | MultilingualString |  |  |
| +++ | @lang | mandatory | 1..1 | xsd:string | Attribute lang | |
| ++ | PrivateCode | optional | 1..1 | PrivateCodeStructure |  |  |
| + | [ServiceJourneyInterchange](ServiceJourneyInterchange.md) | expected | 1..1 | unknown |  | For modeling many forms of interchanges |
|  | vehicleTypes | optional | 0..1 | transportTypeRefs_RelStructure |  | We will use this place to store Train and CompoundTrain information, when we will do formation. Not detailed at the moment |
| + | CompoundTrain | optional | 1..1 | unknown |  |  |
