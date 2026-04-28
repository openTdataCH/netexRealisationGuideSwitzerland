# InterchangeRule_UMSTEIGL

| Sub | Element | Usage | Card | Type | Description | Note |
|-----|---------|-------|------|------|-------------|------|
|  | InterchangeRule | mandatory | 1..1 | unknown | Conditions for considering journeys to meet or not to meet, specified indirectly: by a particular MODE, DIRECTION or LINE. Such conditions may alternatively be specified directly, indicating the corresponding services. In this case they are either a SERVICE JOURNEY PATTERN INTERCHANGE or a SERVICE JOURNEY INTERCHANGE. | transfer times between Line/Directions at a given stop (UMSTEIGL) |
| ++ | AvailabilityConditionRef | expected | 1..1 | AvailabilityConditionRefStructure | Reference to an AVAILABILITY CONDITION. A VALIDITY CONDITION defined in terms of temporal attributes. |  |
| + | StaySeated | mandatory | 0..1 | xsd:boolean | Whether the passenger can remain in vehicle (i.e. block linking). Default is false: the passenger must change vehicles for this INTERCHANGE.
Default is false. |  |
| + | Planned | mandatory | 0..1 | xsd:boolean | Whether INTERCHANGE is planned in a timetable. Default is true. |  |
| + | Guaranteed | mandatory | 0..1 | xsd:boolean | Whether INTERCHANGE is guaranteed. Default is false. |  |
| + | MinimumTransferTime | expected | 0..1 | xsd:duration | Maximum transfer duration for INTERCHANGE. |  |
| + | MaximumTransferTime | expected | 0..1 | xsd:duration | Maximum transfer duration for INTERCHANGE. |  |
| + | timings | optional | 0..1 | interchangeRuleTimings_RelStructure | Additional timings for the INTERCHANGE RULE for specific TIME DEMAND TYPEs. |  |
| ++ | InterchangeRuleTiming | optional | 1..1 | unknown | Conditions for considering journeys to meet or not to meet, specified indirectly: by a particular MODE, DIRECTION or LINE. Such conditions may alternatively be specified directly, indicating the corresponding services. In this case they are either a SERVICE JOURNEY PATTERN INTERCHANGE or a SERVICE JOURNEY INTERCHANGE. |  |
| +++ | TimebandRef | optional | 1..1 | TimebandRefStructure | Reference to a TIME BAND. |  |
| + | FeederFilter | mandatory | 0..1 | InterchangeRuleParameterStructure | Feeder end of INTERCHANGE RULE. |  |
| ++ | StopPlaceRef | mandatory | 0..1 | StopPlaceRefStructure | System identifier of a STOP PLACE. May be omitted if given by context. |  |
| ++ | LineInDirectionRef | mandatory | 1..1 | LineInDirectionRef_Structure | Reference to LINEs in a specific DIRECTION |  |
| +++ | LineRef | mandatory | 1..1 | LineRefStructure | Reference to a LINE. |  |
| ++ | AdjacentStopPlaceRef | optional | 0..1 | StopPlaceRefStructure | Prior (feeder) or onwards (distributor) SCHEDULED STOP PLACE before/after CONNECTION. |  |
| + | DistributorFilter | mandatory | 0..1 | InterchangeRuleParameterStructure | Distributor end of INTERCHANGE RULE. |  |
