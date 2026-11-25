# JourneyMeeting_deprecated

Used for joining and splitting of trains. Check latest policy - InterchangeRule may be the preferred alternative.

*Table: JourneyMeeting*

| Sub | Element | Usage | Card | Type | Description | Note |
|-----|---------|-------|------|------|-------------|------|
|  | @id | mandatory | 1..1 | xsd:string | Attribute id | |
|  | @version | mandatory | 1..1 | xsd:string | Attribute version | |
|  | validityConditions | expected | 1..1 | validityConditions_RelStructure |  | A specific type of VALIDITY CON-DITION used to specify a set of temporal conditions that can be associated with the JOURNEY MEETING, for example that the corresponding connections only apply on particular days of a period (indicated by ValidDayBits “Verkehrstagebitfeld”). |
| + | AvailabilityConditionRef | expected | 0..* | AvailabilityConditionRefStructure |  |  |
|  | AtStopPointRef | mandatory | 0..1 | ScheduledStopPointRefStructure | SCHEDULED STOP POINT at which JOURNEY MEETING takes place. |  |
|  | FromJourneyRef | mandatory | 1..1 | JourneyRefStructure | DEPRECATE: JOURNEY that feeds JOURNEY MEETING. -v2.0 |  |
|  | ToJourneyRef | mandatory | 1..1 | JourneyRefStructure | DEPRECATE: JOURNEY that distributes from JOURNEY MEETING. -v2.0 |  |
|  | Description | optional | 0..1 | MultilingualString |  |  |
|  | EarliestTime | optional | 0..1 | time | Earliest time for JOURNEY MEETING. |  |
|  | LatestTime | optional | 0..1 | time | Latest time for JOURNEY MEETING. |  |
|  | Reason | optional | 0..1 | ReasonForMeetingEnumeration | Reason for JOURNEY MEETING. |  |
