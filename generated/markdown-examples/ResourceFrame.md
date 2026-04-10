# ResourceFrame

| Sub | Element | Usage | Card | Type | Description | Note |
|-----|---------|-------|------|------|-------------|------|
| ++++ | ResourceFrame | mandatory | 1..1 | unknown |  |  |
| +++++ | organisations | mandatory | 1..1 | unknown | We currently face a problem that the same sboid might be reused for Operator and Authority. We will have to check, if we only define Operators, but ue them in Authority as well. TBD |  |
| +++++ | responsibilitySets | mandatory | 1..1 | unknown |  |  |
| +++++ | siteFacilitySets | optional | 1..1 | unknown | Depending on the export/import part, there will be SiteFacilitySets to be included or not. |  |
| +++++ | typesOfValue | mandatory | 1..1 | unknown |  |  |
| ln++++++ | [Operator](Operator.md) | mandatory | 1..1 | unknown | We will use this organisation also in AuthorityRef. The problem is that the sboid can be used only once. |  |
| ln++++++ | [ResponsibilitySet](ResponsibilitySet.md) | mandatory | 1..1 | unknown | Each combination of Authority and Operator needs a ResponsibilitySet. |  |
| ln++++++ | [SiteFacilitySet](SiteFacilitySet.md) | optional | 1..1 | unknown |  |  |
| ++++++ | ValueSet | mandatory | 1..1 | unknown |  |  |
| +++++++ | values | mandatory | 1..1 | unknown |  |  |
