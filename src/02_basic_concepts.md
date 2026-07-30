---
mermaid: true
---
# Basic concepts in NeTEx

NeTEx can support multiple use cases. Here we talk about the Swiss timetable delivery.

The following diagram shows the relevant core classes we will use. In the center is the ServiceJourney.

```mermaid
flowchart TD
    AN[AlternativeName]
    O[Operator]
    SJ[ServiceJourney]
    DT[DirectionType]
    TN[TrainNumber]
    SI[ServiceJourneyInterchange]
    JP[JourneyPart]
    AC[AvailabilityCondition]
    UOP[ValidDayBits]
    SJP[ServiceJourneyPattern]
    TDT[TimeDemandType]
    L[Line]
    SPtJP[StopPointInJourneyPattern]
    TL[TimingLink]
    SSP[ScheduledStopPoint]
    N[Notice]
    F[ServiceFacilities]
    PSA[PassengerStopAssignment]
    SP[StopPlace]
    CN[DefaultConnection]
    Q[Quay]
    
    %% Relationships
    SJ --> DT
    SJ --> L
    SJ --> O
    SJ --> SJP
    SJ --> TDT
    SJ --> SI
    SJ --> JP
    SJ --> TN
    SJ --> AC
    AC --> UOP
    SJP --> L
    SJP --> DT
    SJP --> SPtJP
    SPtJP --> SSP
    TDT --> TL
    TDT --> SSP
    TDT --> SPtJP
    PSA --> SP
    PSA --> Q
    PSA --> SSP
    SP --> Q
    O --> AN

    %% Styling ResourceFrame
    style O fill:#ffffff,stroke:#eea44f,stroke-width:2px
    style F fill:#ffffff,stroke:#eea44f,stroke-width:2px
  
    %% Styling ServiceCalendarFrame
    style AC fill:#ff8888,stroke:#eea44f,stroke-width:2px
    style UOP fill:#ff8888,stroke:#eea44f,stroke-width:2px


    %% everyhwere
      style AN fill:#88ff88,stroke:#eea44f,stroke-width:2px
      style DT fill:#88ff88,stroke:#eea44f,stroke-width:2px
   
    %% Styling SiteFrame
    style SP fill:#a6c9a6,stroke:#eea44f,stroke-width:2px
    style Q fill:#a6c9a6,stroke:#2ea44f,stroke-width:2px

    %% Styling TimetableFrame
    style SJ fill:#d6b9e6,stroke:#2ea44f,stroke-width:2px
    style TN fill:#d6b9e6,stroke:#2ea44f,stroke-width:2px

    
    %% Styling ServiceFrame
    style TDT fill:#e6f9e6,stroke:#2ea44f,stroke-width:2px
    style SJP fill:#e6f9e6,stroke:#2ea44f,stroke-width:2px
    style PSA fill:#e6f9e6,stroke:#2ea44f,stroke-width:2px
    style L fill:#e6f9e6,stroke:#2ea44f,stroke-width:2px
    style TL fill:#e6f9e6,stroke:#2ea44f,stroke-width:2px
    style SPtJP fill:#e6f9e6,stroke:#2ea44f,stroke-width:2px
    style JP fill:#e6f9e6,stroke:#2ea44f,stroke-width:2px
    style SI fill:#e6f9e6,stroke:#2ea44f,stroke-width:2px
    style SI fill:#e6f9e6,stroke:#2ea44f,stroke-width:2px
    style N fill:#e6f9e6,stroke:#2ea44f,stroke-width:2px
    style CN fill:#e6f9e6,stroke:#2ea44f,stroke-width:2px
    style SSP fill:#e6f9e6,stroke:#2ea44f,stroke-width:2px

```
*Core elements for timetables in NeTEx*

Notes:
* Every `ServiceJourney` belongs to one `Line` and has one `Operator`. Some more information can be stored in associated `ResponsibilitySet`s (difference between operator and legal "owner"). 
* The pattern of the stops is defined in a `ServiceJourneyPattern` with additional details about each stop.
* The timing behaviour is stored in `TimeDemandType`. They contain run times and where needed wait times. The `TimingLink`s are mostly based on `ScheduledStopPoint`s and may be used by multiple `ServiceJourneyPattern`.
* The physical stops are modeled as `StopPlace`s with `Quays`.
* `ScheduledStopPoint`s are the "logical" stops.
* The `PassengerStopAssignment` associates the physical and the logical stops.
* `DefaultConnection` and `SiteConnection` define transfers based on site elements.
* `ServiceJourneyInterchange`s are used for splitting, joining and connecting trains and for "Durchbindungen".
* `Notice`, `ServiceFacility` and `SiteFacility` model almost everything else (especially offers).
* The operating days are defined through `ValidDayBits` for the whole timetable year in `AvailabilityCondition`s.

## 

```
StopPlace SP
  * Quay Q1
  * Quay Q2
  
ScheduledStopPoint SPS

PassengerStopAssignment PSA
  -> ScheduledStopPoint SPS
  -> Quay Q1
  -> StopPlace SP 

TimingLink TL
  -> ScheduledStopPoint X
  -> ScheduledStopPoint y
  * some properties
  
 ServiceJourneyPattern SJP
   * StopPointInJourneyPattern
        -> ScheduledStopPoint X
        * multiple properties
   * lots of properties
        
  TimeDemandType TDT
    runTimes
      ServiceJourneyRunTime
        -> TimingLink TL
        * Duration
    waitTimes
       ServiceJourneyWaitTime
         -> ScheduledStopPoint A
         * Duration
         
  ServiceJourney
    -> ServiceJourneyPattern SJP
    -> TimeDemandType TDT
    * lots of properties
        
   
  
```
