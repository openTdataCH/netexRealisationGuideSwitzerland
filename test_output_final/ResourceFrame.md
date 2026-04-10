# ResourceFrame

| Sub | Element | Usage | Card | Type | Description | Note |
|-----|---------|-------|------|------|-------------|------|
|  | PublicationDelivery | ignored | 1..1 | PublicationDeliveryStructure | A set of NeTEx objects as assembled by a publication request or other service. Provides a general purpose wrapper for NeTEx data content. |  |
| + | ParticipantRef | ignored | 1..1 | siri:ParticipantCodeType | Identifier of system requesting Data. |  |
| + | PublicationTimestamp | ignored | 1..1 | xsd:dateTime | Time of output of data. |  |
| + | dataObjects | ignored | 1..1 | unknown |  |  |
| ++ | CompositeFrame | ignored | 1..1 | unknown |  |  |
| +++ | frames | ignored | 1..1 | unknown |  |  |
| ++++ | ResourceFrame | ignored | 1..1 | unknown |  |  |
| +++++ | organisations | ignored | 1..1 | unknown |  |  |
| +++++ | responsibilitySets | mandatory | 1..1 | unknown |  |  |
| +++++ | serviceFacilitySets | ignored | 1..1 | unknown |  |  |
| +++++ | siteFacilitySets | ignored | 1..1 | unknown |  |  |
| +++++ | typesOfValue | mandatory | 1..1 | unknown |  |  |
| ln++++++ | [Operator](Operator.md) | mandatory | 1..1 | unknown | We will use this organisation also in AuthorityRef. The problem is that the sboid can be used only once. |  |
| ln++++++ | [ResponsibilitySet](ResponsibilitySet.md) | mandatory | 1..1 | unknown | Each combination of Authority and Operator needs a ResponsibilitySet. |  |
| ln++++++ | [ServiceFacilitySet](ServiceFacilitySet.md) | ignored | 1..1 | unknown |  |  |
| ln++++++ | [SiteFacilitySet](SiteFacilitySet.md) | ignored | 1..1 | unknown |  |  |
| ++++++ | ValueSet | mandatory | 1..1 | unknown |  |  |
| ++++++ | ValueSet | ignored | 1..1 | unknown |  |  |
| +++++++ | values | mandatory | 1..1 | unknown |  |  |
| ++++++++ | TypeOfNotice | ignored | 1..1 | unknown |  |  |
| ++++++++ | TypeOfNotice | ignored | 1..1 | unknown |  |  |
| ++++++++ | TypeOfNotice | ignored | 1..1 | unknown |  |  |
| ++++++++ | TypeOfNotice | ignored | 1..1 | unknown |  |  |
| ++++++++ | TypeOfNotice | ignored | 1..1 | unknown |  |  |
| +++++++++ | Name | ignored | 1..1 | unknown |  |  |
| +++++++++ | PrivateCode | ignored | 1..1 | unknown |  |  |
