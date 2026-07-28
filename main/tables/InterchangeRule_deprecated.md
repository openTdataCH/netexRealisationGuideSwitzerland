# InterchangeRule_deprecated

transfer times between Line/Directions at a given stop (UMSTEIGL)

*Table: InterchangeRule*

| Sub | Element | Usage | Card | Type | Description | Note |
|-----|---------|-------|------|------|-------------|------|
|  | validityConditions | mandatory | 1..1 | validityConditions_RelStructure |  |  |
| + | AvailabilityConditionRef | expected | 1..1 | AvailabilityConditionRefStructure |  |  |
|  | StaySeated | mandatory | 0..1 | xsd:boolean |  |  |
|  | Planned | mandatory | 0..1 | xsd:boolean |  |  |
|  | Guaranteed | mandatory | 0..1 | xsd:boolean |  |  |
|  | MinimumTransferTime | expected | 0..1 | xsd:duration |  |  |
|  | MaximumTransferTime | expected | 0..1 | xsd:duration |  |  |
|  | timings | optional | 0..1 | interchangeRuleTimings_RelStructure |  |  |
| + | InterchangeRuleTiming | optional | 1..1 | unknown |  |  |
| ++ | TimebandRef | mandatory | 1..1 | TimebandRefStructure |  | Timeband defined in ServiceCalendarFrame |
|  | FeederFilter | mandatory | 0..1 | InterchangeRuleParameterStructure |  |  |
| + | StopPlaceRef | mandatory | 0..1 | StopPlaceRefStructure |  |  |
| + | LineInDirectionRef | expected | 1..1 | LineInDirectionRef_Structure |  |  |
| ++ | LineRef | mandatory | 0..1 | LineRefStructure |  |  |
| ++ | DirectionRef | optional | 0..1 | DirectionRefStructure |  |  |
| + | AdjacentStopPlaceRef | optional | 0..1 | StopPlaceRefStructure |  |  |
| + | ServiceJourneyRef | optional | 1..1 | ServiceJourneyRefStructure |  |  |
|  | DistributorFilter | mandatory | 0..1 | InterchangeRuleParameterStructure |  |  |
| + | ServiceJourneyRef | optional | 1..1 | ServiceJourneyRefStructure |  |  |
