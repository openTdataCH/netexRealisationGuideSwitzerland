# InterchangeRule_UMSTEIGL_deprecated

transfer times between Line/Directions at a given stop (UMSTEIGL)

*Table: InterchangeRule*

| Sub | Element | Usage | Card | Type | Description | Note |
|-----|---------|-------|------|------|-------------|------|
|  | validityConditions | mandatory | 1..1 | validityConditions_RelStructure | VALIDITY CONDITIONs conditioning entity. |  |
| + | AvailabilityConditionRef | expected | 0..* | AvailabilityConditionRefStructure | Reference to an AVAILABILITY CONDITION. A VALIDITY CONDITION defined in terms of temporal attributes. |  |
|  | StaySeated | mandatory | 0..1 | xsd:boolean | Whether the passenger can remain in vehicle (i.e. block linking). Default is false: the passenger must change vehicles for this INTERCHANGE. Default is false. |  |
|  | Planned | mandatory | 0..1 | xsd:boolean | Whether INTERCHANGE is planned in a timetable. Default is true. |  |
|  | Guaranteed | mandatory | 0..1 | xsd:boolean | Whether INTERCHANGE is guaranteed. Default is false. |  |
|  | MinimumTransferTime | expected | 0..1 | xsd:duration | Maximum transfer duration for INTERCHANGE. |  |
|  | MaximumTransferTime | expected | 0..1 | xsd:duration | Maximum transfer duration for INTERCHANGE. |  |
|  | timings | optional | 0..1 | interchangeRuleTimings_RelStructure | Additional timings for the INTERCHANGE RULE for specific TIME DEMAND TYPEs. |  |
| + | InterchangeRuleTiming | optional | 0..* | InterchangeRuleTiming_VersionStructure | Timings for an INTERCHANGE RULE for a given TIME DEMAND TYPE. |  |
| ++ | TimebandRef | optional | 1..* | TimebandRefStructure | Reference to a TIME BAND. |  |
|  | FeederFilter | mandatory | 0..1 | InterchangeRuleParameterStructure | Feeder end of INTERCHANGE RULE. |  |
| + | StopPlaceRef | mandatory | 0..1 | StopPlaceRefStructure | Reference to a STOP PLACE. |  |
| + | LineInDirectionRef | mandatory | 1..1 | LineInDirectionRef_Structure | Reference to a LINE in a specific DIRECTION |  |
| ++ | LineRef | mandatory | 1..* | LineRefStructure | Reference to a LINE. |  |
| ++ | DirectionRef | optional | 1..1 | DirectionRefStructure | Reference to a DIRECTION. |  |
| + | AdjacentStopPlaceRef | optional | 0..1 | StopPlaceRefStructure | Prior (feeder) or onwards (distributor) SCHEDULED STOP PLACE before/after CONNECTION. |  |
|  | DistributorFilter | mandatory | 0..1 | InterchangeRuleParameterStructure | Distributor end of INTERCHANGE RULE. |  |
