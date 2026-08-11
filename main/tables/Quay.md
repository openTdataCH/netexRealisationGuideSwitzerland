# Quay

Can be a platform, track, sector group or sector. id is a SLOID whenever possible or generated.

*Table: Quay*

| Sub | Element | Usage | Card | Type | Description | Note |
|-----|---------|-------|------|------|-------------|------|
|  | @id | mandatory | 1..1 | xsd:string | Attribute id | |
|  | @version | mandatory | 1..1 | xsd:string | Attribute version | |
|  | privateCodes | expected | 0..1 | PrivateCodesStructure | A list of private codes that uniquely identifiy the element. May be used for inter-operating with other (legacy) systems. +v2.0 |  |
| + | PrivateCode | expected | 0..* | PrivateCodeStructure | A private code that uniquely identifies the element. May be used for inter-operating with other (legacy) systems. | SLOID mandatory if it exists. |
| ++ | @type | mandatory | 1..1 | xsd:string | Attribute type | |
|  | [Centroid](Centroid.md) | mandatory | 0..1 | SimplePoint_VersionStructure | Centre Coordinates of ZONE. | Location of Quay. Note that the usage (mandatory) overrides the cardinality. |
|  | AccessibilityAssessment | optional | 0..1 | AccessibilityAssessment_VersionedChildStructure | Assessment of the accessibility of a SITE. | Will be used at some point for the basic accessibility information. Currently not used. |
| + | MobilityImpairedAccess | optional | 1..1 | LimitationStatusEnumeration | Summary indication as to whether the component is considered to be accessible or not. | Basic information about accessibility. |
|  | AccessModes | optional | 0..1 | AccessModeListOfEnumerations | List of ACCESS MODEs that are allowed for this line. If not specified means all the usual ones for classic public transport. Can be used for example to indicate in vehicle only access. +v2.0 |  |
|  | SiteRef | optional | 0..1 | SiteRefStructure | Reference to a SITE. | Can reference the parent Quay or StopPlace |
|  | PublicCode | mandatory | 0..1 | PublicCodeStructure | Public identifier code of TARIFF ZONE. +v2.0 | Code used to identify the Quay to the public |
|  | QuayType | optional | 0..1 | QuayTypeEnumeration | Type of QUAY. | will be used for formations. Allowed values are defined in mapping excel. |
|  | ParentQuayRef | optional | 0..1 | QuayRefStructure | if QUAY is a subzone of another QUAY, identifies parent. | Will be used when we do sectors and sector groups. |
