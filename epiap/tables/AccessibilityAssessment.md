# AccessibilityAssessment

*Table: AccessibilityAssessment*

| Sub | Element | Usage | Card | Type | Description | Note |
|-----|---------|-------|------|------|-------------|------|
|  | MobilityImpairedAccess | mandatory | 1..1 | LimitationStatusEnumeration | Summary indication as to whether the component is considered to be accessible or not. | Accessibility. Overall assessmentfor mobility impaired users. partial means that there must exist AccessibiltyAssessment at lower levels like Quays or other elements. Some Quays may not be accessible if partial is used on the StoPlace. |
|  | limitations | expected | 0..1 | usageParameters_RelStructure | The ACCESSIBILITY LIMITATION that apply to component. | Accessibility. Limitations can be omitted if MobilityImpairedaccess is set to true and no additional information needs to be conveyed. |
| + | AccessibilityLimitation | mandatory | 0..* | AccessibilityLimitation_VersionedChildStructure | Assessment of the accessibility of a SITE. | Accessibility. |
| ++ | WheelchairAccess | mandatory | 1..1 | LimitationStatusEnumeration | Whether a PLACE is wheelchair accessible. | Accessibility. |
| ++ | StepFreeAccess | expected | 0..1 | LimitationStatusEnumeration | Whether a PLACE has step free access. | Accessibility. If absent the value `unknown` is assumed. |
| ++ | StairFreeAccess | expected | 0..1 | LimitationStatusEnumeration | Whether a PLACE has stair free access, in comparison with step free access one single step in the route is allowed. +v2.0 | Accessibility. Not mandatory in EPIAP, but very useful for perambulators, assisted wheelchairs, bicycles, heavy luggage. |
| ++ | GuideDogAccess | expected | 0..1 | LimitationStatusEnumeration | Whether a PLACE allows guide dog access. | Accessibility. If absent the value `unknown` is assumed. |
| ++ | TactileGuidanceAvailable | expected | 0..1 | LimitationStatusEnumeration | Whether a PLACE has tactile guidance. | Accessibility. Whether the object has tactileGuidance (for the visually impaired). If absent the value `unknown` is assumed. |
| ++ | VisualSignsAvailable | expected | 0..1 | LimitationStatusEnumeration | Whether a PLACE has visual signals for the hearing impaired. | Accessibility. If absent the value `unknown` is assumed. |
| ++ | LevelAccessIntoVehicle | expected | 0..1 | LimitationStatusEnumeration | Whether the platform is high enough and gap is small enough for level access into vehicle. At least at a designated wheelchair door position the gap between platform and vehicle floor (of level access vehicle) does not exceed 75 mm measured horizontally and 50 mm measured vertically including sliding step (according to PRM TSI). | Accessibility. Whether the platform is high enough and gap is small enough for level access to vehicle. If absent the value `unknown` is assumed. |
