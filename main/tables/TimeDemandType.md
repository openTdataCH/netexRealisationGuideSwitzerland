# TimeDemandType

TimeDemandType assigns a timing behaviour to a ServiceJourney

*Table: TimeDemandType*

| Sub | Element | Usage | Card | Type | Description | Note |
|-----|---------|-------|------|------|-------------|------|
|  | @id | mandatory | 1..1 | xsd:string | Attribute id | |
|  | @version | mandatory | 1..1 | xsd:string | Attribute version | |
|  | Description | optional | 0..1 | MultilingualString |  | Can be used if there exists a decription of the pattern. |
|  | runTimes | expected | 0..1 | vehicleJourneyRunTimes_RelStructure | A coherent set of Service data to which the same frame VALIDITY CONDITIONs have been assigned. | The run time on the TimingLinks |
| + | JourneyRunTime | expected | 0..* | unknown | A coherent set of Service data to which the same frame VALIDITY CONDITIONs have been assigned. |  |
| ++ | TimingLinkRef | mandatory | 1..1 | TimingLinkRefStructure | A coherent set of Service data to which the same frame VALIDITY CONDITIONs have been assigned. | The timing link that is ued here and that that does have a given run time |
| ++ | RunTime | mandatory | 1..1 | xsd:duration | A coherent set of Service data to which the same frame VALIDITY CONDITIONs have been assigned. |  |
|  | waitTimes | expected | 0..1 | vehicleJourneyWaitTimes_RelStructure | A coherent set of Service data to which the same frame VALIDITY CONDITIONs have been assigned. | We only need wait times if greater than 0. |
| + | JourneyWaitTime | expected | 0..* | unknown | A coherent set of Service data to which the same frame VALIDITY CONDITIONs have been assigned. | Relevant waiting times at the stop |
| ++ | ScheduledStopPointRef | expected | 0..1 | ScheduledStopPointRefStructure | A coherent set of Service data to which the same frame VALIDITY CONDITIONs have been assigned. | Which Quay is referenced. In the case of multiple visits, it should be a StopPointInJourneyPatternRef instead. It also can be a TimingPoint (choice). |
| ++ | WaitTime | mandatory | 0..1 | xsd:duration | A coherent set of Service data to which the same frame VALIDITY CONDITIONs have been assigned. |  |
