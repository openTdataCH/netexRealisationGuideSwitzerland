# ResponsibilitySet

Each combination of Authority and Operator needs a ResponsibilitySet. EntitiyLegalOwnership ismandatory. All other roles are optional. However, we prefer to have the Operation part as well. If given Journeys are operated by a different Operator, then a different ResponsibilitySet should be referenced in the ServiceJourney from the Line.

*Table: ResponsibilitySet*

| Sub | Element | Usage | Card | Type | Description | Note |
|-----|---------|-------|------|------|-------------|------|
|  | @id | mandatory | 1..1 | xsd:string | Attribute id | |
|  | @version | mandatory | 1..1 | xsd:string | Attribute version | |
|  | Name | mandatory | 0..1 | MultilingualString | RESPONSIBILITY SETs used in frame. |  |
| + | @lang | mandatory | 1..1 | xsd:string | Attribute lang | |
|  | PrivateCode | expected | 0..1 | PrivateCodeStructure | RESPONSIBILITY SETs used in frame. |  |
|  | roles | mandatory | 0..1 | responsibilityRoleAssignments_RelStructure | RESPONSIBILITY SETs used in frame. |  |
| + | ResponsibilityRoleAssignment | mandatory | 0..* | unknown |  |  |
| ++ | StakeholderRoleType | mandatory | 0..1 | StakeholderRoleTypeListOfEnumerations | RESPONSIBILITY SETs used in frame. | "EntityLegalOwnership" must be defined once and "Operator" should be too. |
| ++ | ResponsibleOrganisationRef | mandatory | 0..1 | OrganisationRefStructure | RESPONSIBILITY SETs used in frame. |  |
