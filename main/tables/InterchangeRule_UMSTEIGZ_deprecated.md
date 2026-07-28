# InterchangeRule_UMSTEIGZ_deprecated

transfer times between ServiceJourneys (UMSTEIGZ)

*Table: InterchangeRule*

| Sub | Element | Usage | Card | Type | Description | Note |
|-----|---------|-------|------|------|-------------|------|
|  | validityConditions | expected | 1..1 | validityConditions_RelStructure |  |  |
| + | AvailabilityConditionRef | expected | 1..1 | AvailabilityConditionRefStructure |  |  |
|  | StaySeated | mandatory | 0..1 | xsd:boolean |  |  |
|  | Planned | mandatory | 0..1 | xsd:boolean |  |  |
|  | Guaranteed | optional | 0..1 | xsd:boolean |  |  |
|  | MinimumTransferTime | expected | 0..1 | xsd:duration |  |  |
|  | MaximumTransferTime | expected | 0..1 | xsd:duration |  |  |
|  | timings | expected | 0..1 | interchangeRuleTimings_RelStructure |  |  |
| + | InterchangeRuleTiming | expected | 1..1 | unknown |  |  |
| ++ | TimebandRef | mandatory | 1..1 | TimebandRefStructure |  |  |
|  | FeederFilter | mandatory | 0..1 | InterchangeRuleParameterStructure |  |  |
| + | StopPlaceRef | mandatory | 0..1 | StopPlaceRefStructure |  |  |
| + | LineInDirectionRef | mandatory | 1..1 | LineInDirectionRef_Structure |  |  |
| ++ | LineRef | mandatory | 0..1 | LineRefStructure |  |  |
| ++ | DirectionRef | expected | 0..1 | DirectionRefStructure |  |  |
| + | AdjacentStopPlaceRef | expected | 0..1 | StopPlaceRefStructure |  |  |
| + | ServiceJourneyRef | mandatory | 1..1 | ServiceJourneyRefStructure |  |  |
| + | AdjacentStopPlaceRef | expected | 0..1 | StopPlaceRefStructure |  |  |
| + | ServiceJourneyRef | mandatory | 1..1 | ServiceJourneyRefStructure | Reference to a connecting VEHICLE JOURNEY to whom INTERCHANGE RULE applies. If absent applies to all journeys. |  |
