# CheckConstraint

CheckConstraints are used for different use cases

*Table: CheckConstraint*

| Sub | Element | Usage | Card | Type | Description | Note |
|-----|---------|-------|------|------|-------------|------|
|  | CheckDirection | optional | 0..1 | CheckDirectionEnumeration |  | We usually only use one direction. |
|  | CheckProcess | optional | 0..1 | CheckProcessTypeEnumeration |  | Only a given subset is allowed |
|  | Congestion | optional | 0..1 | CongestionEnumeration |  |  |
|  | delays | expected | 0..1 | unknown |  |  |
| + | CheckConstraintDelay | expected | 1..1 | unknown |  | We currently only model delays |
| ++ | AverageDelay | expected | 0..1 | xsd:duration |  |  |
| ++ | MaximumLikelyDelay | optional | 0..1 | xsd:duration |  |  |
