# ResourceFrame

*Table: ResourceFrame*

| Sub | Element | Usage | Card | Type | Description | Note |
|-----|---------|-------|------|------|-------------|------|
|  | @id | mandatory | 1..1 | xsd:string | Attribute id | |
|  | @version | mandatory | 1..1 | xsd:string | Attribute version | |
|  | responsibilitySets | mandatory | 0..1 | responsibilitySetsInFrame_RelStructure |  | RESPONSIBILITY SETs contained in RESOURCE FRAME. ResponsibilitySets are used for the cases in which the LegalEntity, the Operator and the organisation selling the tickets are different. |
| + | [ResponsibilitySet](ResponsibilitySet.md) | mandatory | 0..* | unknown |  | Each combination of Authority and Operator needs a ResponsibilitySet. |
|  | typesOfValue | mandatory | 0..1 | typesOfValueInFrame_RelStructure |  | Sets of TYPE OF VALUE contained in the RESOURCE FRAME. |
| + | ValueSet | expected | 0..* | unknown |  | We need a TypeOfNotice ValueSet. |
| ++ | values | expected | 0..1 | typesOfValue_RelStructure |  |  |
| +++ | TypeOfNotice | expected | 0..* | unknown |  |  |
| + | ValueSet | expected | 0..* | unknown |  | We need a TypeOfProductCategory ValueSet |
| + | ValueSet | expected | 0..* | unknown |  | We expect a TypsOfPlace Valueset |
|  | organisations | mandatory | 0..1 | organisationsInFrame_RelStructure |  | ORGANISATIONs contained in RESOURCE FRAME. Contains the relevant Operators and other Organisations. We currently face a problem that the same sboid might be reused for Operator and Authority. We will have to check, if we only define Operators, but ue them in Authority as well. TBD |
| + | [Operator](Operator.md) | mandatory | 0..* | unknown |  | We will use this organisation also in AuthorityRef. The problem is that the sboid can be used only once. |
|  | siteFacilitySets | optional | 0..1 | siteFacilitySetsInFrame_RelStructure |  | Depending on the export/import part, there will be SiteFacilitySets to be included or not. |
| + | [SiteFacilitySet](SiteFacilitySet.md) | optional | 0..* | unknown |  |  |
|  | serviceFacilitySets | optional | 0..1 | serviceFacilitySetsInFrame_RelStructure |  | Depending on the export/import part, there will be ServiceFacilitySets to be included. If there are ServiceJourneys we expect there to be some. |
| + | [ServiceFacilitySet](ServiceFacilitySet.md) | optional | 0..* | unknown |  |  |
|  | vehicleTypes | optional | 0..1 | transportTypeRefs_RelStructure |  | The VehicleType here are used for generic information like lowfloor and not for formation information |
| + | [VehicleType](VehicleType.md) | optional | 0..* | unknown |  |  |
