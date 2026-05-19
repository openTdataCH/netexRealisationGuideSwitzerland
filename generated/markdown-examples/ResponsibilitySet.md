# ResponsibilitySet

| Sub | Element | Usage | Card | Type | Description | Note |
|-----|---------|-------|------|------|-------------|------|
|  | ResponsibilitySet | mandatory | 1..1 | unknown | A set of responsibility roles assignments that can be associated with a DATA MANAGED OBJECT. A Child ENTITY has the same responsibilities as its parent. | Each combination of Authority and Operator needs a ResponsibilitySet. EntitiyLegalOwnership ismandatory. All other roles are optional. However, we prefer to have the Operation part as well. If given Journeys are operated by a different Operator, then a different ResponsibilitySet should be referenced in the ServiceJourney from the Line. |
| + | Name | mandatory | 0..1 | MultilingualString | Name of Traveller |  |
| + | PrivateCode | expected | 1..1 | PrivateCodeStructure | A private code that uniquely identifies the element. May be used for inter-operating with other (legacy) systems. |  |
| + | roles | mandatory | 0..1 | responsibilityRoleAssignments_RelStructure | Roles defined by this RESPONSIBILITY SET. |  |
| ++ | ResponsibilityRoleAssignment | mandatory | 1..1 | unknown | Assignment of a specific RESPONSIBILITY ROLE to a specific organisation and/or subdivision. |  |
| +++ | StakeholderRoleType | mandatory | 0..1 | StakeholderRoleTypeListOfEnumerations | Stakeholder roles which this assignment assigns. | "EntityLegalOwnership" must be defined once and "Operator" should be too. |
| +++ | ResponsibleOrganisationRef | mandatory | 0..1 | OrganisationRefStructure | Responsible ORGANISATION. |  |
