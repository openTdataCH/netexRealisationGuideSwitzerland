# TimeDemandType

TimeDemandType assigns a timing behaviour to a ServiceJourney

*Table: TimeDemandType*

| Sub | Element | Usage | Card | Type | Description | Note |
|-----|---------|-------|------|------|-------------|------|
|  | @id | mandatory | 1..1 | xsd:string | Attribute id | |
|  | @version | mandatory | 1..1 | xsd:string | Attribute version | |
|  | Description | optional | 0..1 | MultilingualString | Description of contents. | Can be used if there exists a decription of the pattern. |
|  | runTimes | expected | 0..1 | vehicleJourneyRunTimes_RelStructure | Run times for VEHICLE JOURNEY over different TIMING LINKs. | The run time on the TimingLinks |
| + | JourneyRunTime | expected | 1..* | JourneyRunTime | The time taken to traverse a TIMING LINK in a particular JOURNEY PATTERN, for a specified TIME DEMAND TYPE. If it exists, it will override the DEFAULT SERVICE JOURNEY RUN TIME and DEFAULT DEAD RUN RUN TIME. |  |
| ++ | TimingLinkRef | mandatory | 1..1 | TimingLinkRefStructure | Reference to a TIMING LINK. | The timing link that is ued here and that that does have a given run time |
| ++ | RunTime | mandatory | 1..1 | xsd:duration | Run time as interval. |  |
|  | waitTimes | expected | 0..1 | vehicleJourneyWaitTimes_RelStructure | WAIT TIMEs for VEHICLE JOURNEY at different TIMING POINTs. | We only need wait times if greater than 0. |
| + | JourneyWaitTime | expected | 1..* | JourneyWaitTime | The time a vehicle has to wait at a specific TIMING POINT IN JOURNEY PATTERN, for a specified TIME DEMAND TYPE. This wait time can be superseded by a VEHICLE JOURNEY WAIT TIME. | Relevant waiting times at the stop |
| ++ | ScheduledStopPointRef | expected | 0..1 | ScheduledStopPointRefStructure | Specific SCHEDULED STOP POINT at end of CONNECTION. | Which Quay is referenced. In the case of multiple visits, it should be a StopPointInJourneyPatternRef instead. It also can be a TimingPoint (choice). |
| ++ | WaitTime | mandatory | 0..1 | xsd:duration | Timetabled waiting interval. |  |
