# ResourceFrame

*Table: ResourceFrame*

| Sub | Element | Usage | Card | Type | Description | Note |
|-----|---------|-------|------|------|-------------|------|
|  | @id | mandatory | 1..1 | xsd:string | Attribute id | |
|  | @version | mandatory | 1..1 | xsd:string | Attribute version | |
|  | responsibilitySets | mandatory | 0..1 | responsibilitySetsInFrame_RelStructure | RESPONSIBILITY SETs used in frame. | RESPONSIBILITY SETs contained in RESOURCE FRAME. ResponsibilitySets are used for the cases in which the LegalEntity, the Operator and the organisation selling the tickets are different. |
| + | [ResponsibilitySet](ResponsibilitySet.md) | mandatory | 1..1 | ResponsibilitySet | A set of responsibility roles assignments that can be associated with a DATA MANAGED OBJECT. A Child ENTITY has the same responsibilities as its parent. | Each combination of Authority and Operator needs a ResponsibilitySet. |
|  | typesOfValue | mandatory | 0..1 | typesOfValueInFrame_RelStructure | VALUE SETs and TYPE OF VALUEs in frame. | Sets of TYPE OF VALUE contained in the RESOURCE FRAME. |
| + | ValueSet | expected | 1..1 | ValueSet | An extensible set of code values which may be added to by user applications and is used to validate the properties of Entities. | We need a TypeOfNotice ValueSet. |
| ++ | values | expected | 0..1 | typesOfValue_RelStructure | Values in Set. |  |
| +++ | TypeOfNotice | expected | 1..1 | TypeOfNotice | A classification of a NOTICE according to its functional purpose. |  |
| + | ValueSet | expected | 1..1 | ValueSet | An extensible set of code values which may be added to by user applications and is used to validate the properties of Entities. | We need a TypeOfProductCategory ValueSet |
| + | ValueSet | expected | 1..1 | ValueSet | An extensible set of code values which may be added to by user applications and is used to validate the properties of Entities. | We expect a TypsOfPlace Valueset |
|  | organisations | mandatory | 0..1 | organisationsInFrame_RelStructure | ORGANISATIONs in frame. | ORGANISATIONs contained in RESOURCE FRAME. Contains the relevant Operators and other Organisations. We currently face a problem that the same sboid might be reused for Operator and Authority. We will have to check, if we only define Operators, but ue them in Authority as well. TBD |
| + | [Operator](Operator.md) | mandatory | 1..1 | Operator | A company providing public transport services. | We will use this organisation also in AuthorityRef. The problem is that the sboid can be used only once. |
|  | siteFacilitySets | optional | 0..1 | siteFacilitySetsInFrame_RelStructure | SITE FACILITY SETs in frame . +v1.2.2 | Depending on the export/import part, there will be SiteFacilitySets to be included or not. |
| + | [SiteFacilitySet](SiteFacilitySet.md) | optional | 1..1 | SiteFacilitySet | Set of enumerated FACILITY values that are relevant to a SITE (names based on TPEG classifications, augmented with UIC etc.). |  |
|  | serviceFacilitySets | optional | 0..1 | serviceFacilitySetsInFrame_RelStructure | SERVICE FACILITies in frame. | Depending on the export/import part, there will be ServiceFacilitySets to be included. If there are ServiceJourneys we expect there to be some. |
| + | [ServiceFacilitySet](ServiceFacilitySet.md) | optional | 1..1 | ServiceFacilitySet | Service FACILITY. Set of enumerated FACILITY values (Where available names are based on TPEG classifications, augmented with UIC etc.). |  |
|  | vehicleTypes | optional | 0..1 | transportTypeRefs_RelStructure | Opnen specifcation of VEHICLE TYPEs + v1.1 |  |
| + | [VehicleType](VehicleType.md) | optional | 1..1 | VehicleType | A classification of public transport vehicles according to the vehicle scheduling requirements in mode and capacity (e.g. standard bus, double-deck, ...). |  |
