# InterchangeRule_UMSTEIGZ

| Sub | Element | Usage | Card | Type | Description | Note |
|-----|---------|-------|------|------|-------------|------|
|  | InterchangeRule | mandatory | 1..1 | unknown | Conditions for considering journeys to meet or not to meet, specified indirectly: by a particular MODE, DIRECTION or LINE. Such conditions may alternatively be specified directly, indicating the corresponding services. In this case they are either a SERVICE JOURNEY PATTERN INTERCHANGE or a SERVICE JOURNEY INTERCHANGE. | transfer times between ServiceJourneys (UMSTEIGZ) |
| + | validityConditions | expected | 1..1 | validityConditions_RelStructure | VALIDITY CONDITIONs conditioning entity. |  |
| ++ | AvailabilityConditionRef | expected | 1..1 | AvailabilityConditionRefStructure | Reference to an AVAILABILITY CONDITION. A VALIDITY CONDITION defined in terms of temporal attributes. |  |
| + | StaySeated | mandatory | 0..1 | xsd:boolean | Whether the passenger can remain in vehicle (i.e. block linking). Default is false: the passenger must change vehicles for this INTERCHANGE.
Default is false. |  |
| + | Planned | mandatory | 0..1 | xsd:boolean | Whether INTERCHANGE is planned in a timetable. Default is true. |  |
| + | Guaranteed | optional | 0..1 | xsd:boolean | Whether INTERCHANGE is guaranteed. Default is false. |  |
| + | MinimumTransferTime | expected | 0..1 | xsd:duration | Maximum transfer duration for INTERCHANGE. |  |
| + | MaximumTransferTime | expected | 0..1 | xsd:duration | Maximum transfer duration for INTERCHANGE. |  |
| + | timings | expected | 0..1 | interchangeRuleTimings_RelStructure | Additional timings for the INTERCHANGE RULE for specific TIME DEMAND TYPEs. |  |
| ++ | [InterchangeRuleTiming](InterchangeRuleTiming.md) | expected | 1..1 | unknown | Conditions for considering journeys to meet or not to meet, specified indirectly: by a particular MODE, DIRECTION or LINE. Such conditions may alternatively be specified directly, indicating the corresponding services. In this case they are either a SERVICE JOURNEY PATTERN INTERCHANGE or a SERVICE JOURNEY INTERCHANGE. |  |
| + | FeederFilter | mandatory | 0..1 | InterchangeRuleParameterStructure | Feeder end of INTERCHANGE RULE. |  |
| ++ | StopPlaceRef | mandatory | 0..1 | StopPlaceRefStructure | System identifier of a STOP PLACE. May be omitted if given by context. |  |
| ++ | LineInDirectionRef | mandatory | 1..1 | LineInDirectionRef_Structure | Reference to LINEs in a specific DIRECTION |  |
| +++ | LineRef | mandatory | 1..1 | LineRefStructure | Reference to a LINE. |  |
| +++ | DirectionRef | expected | 1..1 | DirectionRefStructure | Reference to a DIRECTION. |  |
| ++ | AdjacentStopPlaceRef | expected | 0..1 | StopPlaceRefStructure | Prior (feeder) or onwards (distributor) SCHEDULED STOP PLACE before/after CONNECTION. |  |
| ++ | ServiceJourneyRef | mandatory | 1..1 | ServiceJourneyRefStructure | Reference to a connecting VEHICLE JOURNEY to whom INTERCHANGE RULE applies. If absent applies to all journeys. |  |
