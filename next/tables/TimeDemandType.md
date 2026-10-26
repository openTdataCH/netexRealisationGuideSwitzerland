# TimeDemandType

TimeDemandType assigns a timing behaviour to a ServiceJourney

*Table: TimeDemandType*

| Sub | Element | Usage | Card | Type | Description | Note |
|-----|---------|-------|------|------|-------------|------|
|  | @id | mandatory | 1..1 | xsd:string | Attribute id | |
|  | @version | mandatory | 1..1 | xsd:string | Attribute version | |
|  | Description | optional | 0..1 | MultilingualString |  | Can be used if there exists a decription of the pattern. |
|  | runTimes | expected | 0..1 | journeyRunTimes_RelStructure | RUN TIMEs for TIME DEMAND TYPE. | The run time on the TimingLinks |
| + | JourneyRunTime | expected | 1..* | JourneyRunTime_VersionedChildStructure | The time taken to traverse a TIMING LINK in a particular JOURNEY PATTERN, for a specified TIME DEMAND TYPE. If it exists, it will override the DEFAULT SERVICE JOURNEY RUN TIME and DEFAULT DEAD RUN RUN TIME. |  |
| ++ | TimingLinkRef | mandatory | 0..1 | TimingLinkRefStructure |  | The timing link that is ued here and that that does have a given run time |
| ++ | RunTime | mandatory | 1..1 | duration | RUN TIME as an interval. |  |
|  | waitTimes | expected | 0..1 | journeyWaitTimes_RelStructure | WAIT TIMEs for TIME DEMAND TYPE. | We only need wait times if greater than 0. |
| + | JourneyWaitTime | expected | 1..* | JourneyWaitTime_VersionedChildStructure | The time a vehicle has to wait at a specific TIMING POINT IN JOURNEY PATTERN, for a specified TIME DEMAND TYPE. This wait time can be superseded by a VEHICLE JOURNEY WAIT TIME. | Relevant waiting times at the stop |
| ++ | ScheduledStopPointRef | expected | 0..1 | ScheduledStopPointRefStructure | Specific SCHEDULED STOP POINT at end of CONNECTION. | Which Quay is referenced. In the case of multiple visits, it should be a StopPointInJourneyPatternRef instead. It also can be a TimingPoint (choice). |
| ++ | WaitTime | mandatory | 0..1 | duration | Wait time as interval. |  |
