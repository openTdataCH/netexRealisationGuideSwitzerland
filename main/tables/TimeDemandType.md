# TimeDemandType

TimeDemandType assigns a timing behaviour to a ServiceJourney

*Table: TimeDemandType*

| Sub | Element | Usage | Card | Type | Description | Note |
|-----|---------|-------|------|------|-------------|------|
|  | @id | mandatory | 1..1 | xsd:string | Attribute id | |
|  | @version | mandatory | 1..1 | xsd:string | Attribute version | |
|  | Description | optional | 0..1 | MultilingualString |  | Can be used if there exists a decription of the pattern. |
|  | runTimes | expected | 0..1 | vehicleJourneyRunTimes_RelStructure |  | The run time on the TimingLinks |
| + | JourneyRunTime | expected | 1..1 | unknown |  |  |
| ++ | TimingLinkRef | mandatory | 1..1 | TimingLinkRefStructure |  | The timing link that is ued here and that that does have a given run time |
| ++ | RunTime | mandatory | 1..1 | xsd:duration |  |  |
|  | waitTimes | expected | 0..1 | vehicleJourneyWaitTimes_RelStructure |  | We only need wait times if greater than 0. |
| + | JourneyWaitTime | expected | 1..1 | unknown |  | Relevant waiting times at the stop |
| ++ | ScheduledStopPointRef | expected | 0..1 | ScheduledStopPointRefStructure |  | Which Quay is referenced. In the case of multiple visits, it should be a StopPointInJourneyPatternRef instead. It also can be a TimingPoint (choice). |
| ++ | WaitTime | mandatory | 0..1 | xsd:duration |  |  |
