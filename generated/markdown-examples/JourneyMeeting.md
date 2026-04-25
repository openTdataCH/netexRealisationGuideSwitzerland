# JourneyMeeting

| Sub | Element | Usage | Card | Type | Description | Note |
|-----|---------|-------|------|------|-------------|------|
| + | validityConditions | expected | 1..1 | validityConditions_RelStructure | VALIDITY CONDITIONs conditioning entity. | A specific type of VALIDITY CON-DITION used to specify a set of temporal conditions that can be associated with the JOURNEY MEETING, for example that the corresponding connections only apply on particular days of a period (indicated by ValidDayBits “Verkehrstagebitfeld”). |
| ++ | AvailabilityConditionRef | expected | 1..1 | AvailabilityConditionRefStructure | Reference to an AVAILABILITY CONDITION. A VALIDITY CONDITION defined in terms of temporal attributes. |  |
| + | AtStopPointRef | mandatory | 0..1 | ScheduledStopPointRefStructure | SCHEDULED STOP POINT at which JOURNEY MEETING takes place. |  |
| + | FromJourneyRef | mandatory | 1..1 | JourneyRefStructure | DEPRECATE: JOURNEY that feeds the INTERCHANGE. -v2.0 |  |
| + | ToJourneyRef | mandatory | 1..1 | JourneyRefStructure | DEPRECATE: JOURNEY that distributes from the INTERCHANGE. -v2.0 |  |
| + | Description | optional | 0..1 | MultilingualString | Description of contents. |  |
| + | EarliestTime | optional | 0..1 | xsd:time | Earliest time for JOURNEY MEETING. |  |
| + | LatestTime | optional | 0..1 | xsd:time | Latest time on specified last day when ticket can be purchased. |  |
| + | Reason | optional | 0..1 | ReasonForMeetingEnumeration | Reason for JOURNEY MEETING. |  |
