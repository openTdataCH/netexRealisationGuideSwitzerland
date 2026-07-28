# JourneyMeeting_deprecated

Used for joining and splitting of trains. Check latest policy - InterchangeRule may be the preferred alternative.

*Table: JourneyMeeting*

| Sub | Element | Usage | Card | Type | Description | Note |
|-----|---------|-------|------|------|-------------|------|
|  | @id | mandatory | 1..1 | xsd:string | Attribute id | |
|  | @version | mandatory | 1..1 | xsd:string | Attribute version | |
|  | validityConditions | expected | 1..1 | validityConditions_RelStructure |  | A specific type of VALIDITY CON-DITION used to specify a set of temporal conditions that can be associated with the JOURNEY MEETING, for example that the corresponding connections only apply on particular days of a period (indicated by ValidDayBits “Verkehrstagebitfeld”). |
| + | AvailabilityConditionRef | expected | 1..1 | AvailabilityConditionRefStructure |  |  |
|  | AtStopPointRef | mandatory | 0..1 | ScheduledStopPointRefStructure |  |  |
|  | FromJourneyRef | mandatory | 1..1 | JourneyRefStructure |  |  |
|  | ToJourneyRef | mandatory | 1..1 | JourneyRefStructure |  |  |
|  | Description | optional | 0..1 | MultilingualString |  |  |
|  | EarliestTime | optional | 0..1 | xsd:time |  |  |
|  | LatestTime | optional | 0..1 | xsd:time |  |  |
|  | Reason | optional | 0..1 | ReasonForMeetingEnumeration |  |  |
