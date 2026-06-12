# Basic concepts in NeTEx

NeTEx can support multiple use cases. Here we talk about the Swiss timetable delivery.

The following diagram shows the relevant core classes we will use. In the center is the ServiceJourney.

```mermaid
graph TD
  %% Top: TimetableFrame
  subgraph TimetableFrame["TimetableFrame"]
    SJ[ServiceJourney]
    TPT[TimetabledPassingTime]
  end

  %% Middle row: ServiceCalendarFrame (left)
  subgraph ServiceCalendarFrame["ServiceCalendarFrame"]
    AC[AvailabilityCondition]
    UOP[ValidDayBits]
  end

  %% Middle row: ServiceFrame (center)
  subgraph ServiceFrame["ServiceFrame"]
    L[Line]
    D[Direction]
    O[Operator]
    SSP[ScheduledStopPoint]
    PSA[PassengerStopAssignment]
    SJP[ServiceJourneyPattern]
    SPtJP[StopPointInJourneyPattern]
  end

  %% Middle row: SiteFrame (right)
  subgraph SiteFrame["SiteFrame"]
    SP[StopPlace]
    Q[Quay]
  end

  %% Bottom: Other stuff
  subgraph OtherStuff["Other stuff"]
    CN[DefaultConnection]
    SI[ServiceJourneyInterchange]
    JP[JourneyPart]
    N[Notice]
    AT[AlternativeText]
    AN[AlternativeName]
    F[ServiceFacilities]
  end

  %% ---------------------
  %% Visible semantic relationships
  SJ --> AC
  SJ --> L
  SJ --> D
  SJ --> O
  SJ --> SJP
  SJ --> TPT

  TPT --> SJ
  TPT --> SPtJP

  SJP --> L
  SJP --> D
  SJP --> SPtJP
  SPtJP --> SSP

  PSA --- SP
  PSA --- Q
  PSA --- SSP

  SP --- Q

  AC --> UOP

  JP --> N

  %% ---------------------
  %% Layout hints to force rows and columns (dashed edges used only as hints)
  SJ -.-> L
  AC -.-> L
  L -.-> SP
  SSP -.-> JP

  %% ---------------------
  %% Highlight central nodes in green
  style SJ fill:#e6f9e6,stroke:#2ea44f,stroke-width:2px
  style SJP fill:#e6f9e6,stroke:#2ea44f,stroke-width:2px
  style TPT fill:#e6f9e6,stroke:#2ea44f,stroke-width:2px

  %% Subgraph box styling (may be renderer-dependent)
  style TimetableFrame stroke:#999,stroke-width:1px,fill:none
  style ServiceCalendarFrame stroke:#999,stroke-width:1px,fill:none
  style ServiceFrame stroke:#999,stroke-width:1px,fill:none
  style SiteFrame stroke:#999,stroke-width:1px,fill:none
  style OtherStuff stroke:#999,stroke-width:1px,fill:none


```
Notes:
* Every `ServiceJourney` belongs to one Line and has one `Operator`. Some more information can be stored in associated `ResponsibilitySet`s. 
* The pattern of the stops is defined in a `ServiceJourneyPattern`. The timing behaviour is part of the `TimetablePassingtime`.
* The physical stops are modeled as `StopPlac`e with `Quays`.
* `ScheduledStopPoint`s are are the "logical" stops.
* The `PassengerStopAssignment` associates the physical and the logical stops.
* `DefaultConnection`, `SiteConnection` and `ServiceJourneyInterchange` defined transfers
* `JourneyMeetin`gs are used for splitting and joining of trains.
* `Notice`, `ServiceFacility` and `SiteFacility` model almost everythingelse
* The operating days are defined through `ValidDayBits` for the whole timetable year in `AvailabilityCondition`s.
