# InterchangeRule_UMSTEIGZ_deprecated

transfer times between ServiceJourneys (UMSTEIGZ)

*Table: InterchangeRule*

| Sub | Element | Usage | Card | Type | Description | Note |
|-----|---------|-------|------|------|-------------|------|
|  | validityConditions | expected | 1..1 | validityConditions_RelStructure |  |  |
| + | AvailabilityConditionRef | expected | 0..* | AvailabilityConditionRefStructure |  |  |
|  | StaySeated | mandatory | 0..1 | boolean | Whether the passenger can remain in vehicle (i.e. block linking). Default is false: the passenger must change vehicles for this INTERCHANGE. Default is false. |  |
|  | Planned | mandatory | 0..1 | boolean | Whether INTERCHANGE is planned in a timetable. Default is true. |  |
|  | Guaranteed | optional | 0..1 | boolean | Whether INTERCHANGE is guaranteed. Default is false. |  |
|  | MinimumTransferTime | expected | 0..1 | duration | Maximum transfer duration for INTERCHANGE. |  |
|  | MaximumTransferTime | expected | 0..1 | duration | Maximum transfer duration for INTERCHANGE. |  |
|  | timings | expected | 0..1 | interchangeRuleTimings_RelStructure | Additional timings for the INTERCHANGE RULE for specific TIME DEMAND TYPEs. |  |
| + | InterchangeRuleTiming | expected | 0..* | InterchangeRuleTiming_VersionStructure | Timings for an INTERCHANGE RULE for a given TIME DEMAND TYPE. |  |
| ++ | TimebandRef | mandatory | 1..1 | TimebandRefStructure |  |  |
|  | FeederFilter | mandatory | 0..1 | InterchangeRuleParameterStructure | Feeder end of INTERCHANGE RULE. |  |
| + | StopPlaceRef | mandatory | 0..1 | StopPlaceRefStructure |  |  |
| + | LineInDirectionRef | mandatory | 1..* | LineInDirectionRef_Structure |  |  |
| ++ | LineRef | mandatory | 0..1 | LineRefStructure |  |  |
| ++ | DirectionRef | expected | 0..1 | DirectionRefStructure |  |  |
| + | AdjacentStopPlaceRef | expected | 0..1 | StopPlaceRefStructure | Prior (feeder) or onwards (distributor) SCHEDULED STOP PLACE before/after CONNECTION. |  |
| + | ServiceJourneyRef | mandatory | 1..1 | ServiceJourneyRefStructure | Reference to a connecting VEHICLE JOURNEY to whom INTERCHANGE RULE applies. If absent applies to all journeys. |  |
| + | AdjacentStopPlaceRef | expected | 0..1 | StopPlaceRefStructure | Prior (feeder) or onwards (distributor) SCHEDULED STOP PLACE before/after CONNECTION. |  |
| + | ServiceJourneyRef | mandatory | 1..1 | ServiceJourneyRefStructure | Reference to a connecting VEHICLE JOURNEY to whom INTERCHANGE RULE applies. If absent applies to all journeys. |  |
