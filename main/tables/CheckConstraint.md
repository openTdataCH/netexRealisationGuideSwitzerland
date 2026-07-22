# CheckConstraint

CheckConstraints are used for different use cases

*Table: CheckConstraint*

| Sub | Element | Usage | Card | Type | Description | Note |
|-----|---------|-------|------|------|-------------|------|
|  | CheckDirection | optional | 0..1 | CheckDirectionEnumeration | For CHECK CONSTRAINTs associated with PATH LINKs, the direction in which the check applies. Forwards = from/to, backwards = to/from. For Check constraints associated with an external ENTRANCE, forwards is into the SITE, backwards is out of the SITE. | We usually only use one direction. |
|  | CheckProcess | optional | 0..1 | CheckProcessTypeEnumeration | Type of process that may occur at CHECK CONSTRAINT. | Only a given subset is allowed |
|  | Congestion | optional | 0..1 | CongestionEnumeration | Type of crowding that may slow use of CHECK CONSTRAINT. |  |
|  | delays | expected | 0..1 | delays | Delays for CHECK CONSTRAINT .process. |  |
| + | CheckConstraintDelay | expected | 1..1 | CheckConstraintDelay | Time penalty associated with a CHECK CONSTRAINT. | We currently only model delays |
| ++ | AverageDelay | expected | 0..1 | xsd:duration | Average duration expected to pass through Check. |  |
| ++ | MaximumLikelyDelay | optional | 0..1 | xsd:duration | Maximum duration expected to pass through CHECK CONSTRAINT. |  |
