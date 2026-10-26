# Quay

Can be a platform, track, sector group or sector. id is a SLOID whenever possible or generated.

*Table: Quay*

| Sub | Element | Usage | Card | Type | Description | Note |
|-----|---------|-------|------|------|-------------|------|
|  | @id | mandatory | 1..1 | xsd:string | Attribute id | |
|  | @version | mandatory | 1..1 | xsd:string | Attribute version | |
|  | privateCodes | expected | 1..1 | PrivateCodesStructure |  |  |
| + | PrivateCode | expected | 0..* | PrivateCodeStructure |  | SLOID mandatory if it exists. |
| ++ | @type | mandatory | 1..1 | xsd:string | Attribute type | |
|  | [Centroid](Centroid.md) | mandatory | 0..1 | SimplePoint_VersionStructure |  | Location of Quay. Note that the usage (mandatory) overrides the cardinality. |
|  | [AccessibilityAssessment](AccessibilityAssessment.md) | expected | 0..1 | AccessibilityAssessment_VersionedChildStructure |  | Only required if the AccessibilityAssessment of the StopPlace contains value(s) `partial`. |
|  | AccessModes | optional | 0..1 | AccessModeListOfEnumerations |  |  |
|  | SiteRef | optional | 0..1 | SiteRefStructure |  | Can reference the parent Quay or StopPlace |
|  | PublicCode | mandatory | 0..1 | PublicCodeStructure | Pubic identifier code of QUAY. | Code used to identify the Quay to the public |
|  | QuayType | optional | 0..1 | QuayTypeEnumeration | Type of QUAY. | will be used for formations. Allowed values are defined in mapping excel. |
|  | ParentQuayRef | optional | 0..1 | QuayRefStructure | if QUAY is a subzone of another QUAY, identifies parent. | Will be used when we do sectors and sector groups. |
