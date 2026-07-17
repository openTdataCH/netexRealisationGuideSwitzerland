---
mermaid: true
---
# Basic concepts in NeTEx

NeTEx can support multiple use cases. Here we talk about the Swiss timetable delivery.

The following diagram shows the relevant core classes we will use. In the center is the ServiceJourney.

```mermaid
<<<<<<< HEAD
graph TD
  subgraph TimetableFrame["TimetableFrame"]
    SJ[ServiceJourney]
    DT[DirectionType]
  end

  subgraph ServiceCalendarFrame["ServiceCalendarFrame"]
    AC[AvailabilityCondition]
    UOP[ValidDayBits]
  end

  subgraph ServiceFrame["ServiceFrame"]
    L[Line]
    O[Operator]
    SSP[ScheduledStopPoint]
    PSA[PassengerStopAssignment]
    TL[TimingLink]
    SJP[ServiceJourneyPattern]
    TDT[TimeDemandType]
    SPtJP[StopPointInJourneyPattern]
  end

  subgraph SiteFrame["SiteFrame"]
    SP[StopPlace]
    Q[Quay]
  end

  subgraph OtherStuff["Other stuff"]
    CN[DefaultConnection]
    SI[ServiceJourneyInterchange]
    JP[JourneyPart]
    N[Notice]
    AN[AlternativeName]
    F[ServiceFacilities]
     SJI[ServiceJourneyInterchange]
   
  end

  %% ---------------------
  %% Visible semantic relationships
  SJ --> AC
  SJ --> DT
  SJ --> L
  SJ --> O
  SJ --> SJP
  SJ --> TDT

  TDT --> TL
  TDT --> SSP
  TDT --> SPtJP

  SJP --> L
  SJP --> SPtJP
  SPtJP --> SSP

  PSA ---> SP
  PSA ---> Q
  PSA ---> SSP

  SP ---> Q

  AC --> UOP


  %% ---------------------
  %% Layout hints to force rows and columns (dashed edges used only as hints)

  %% ---------------------
  %% Highlight central nodes in green
  style SJ fill:#e6f9e6,stroke:#2ea44f,stroke-width:2px
  style SJP fill:#e6f9e6,stroke:#2ea44f,stroke-width:2px
  style TDT fill:#e6f9e6,stroke:#2ea44f,stroke-width:2px
  style PSA fill:#e6f9e6,stroke:#2ea44f,stroke-width:2px

  %% Subgraph box styling (may be renderer-dependent)
  style TimetableFrame stroke:#999,stroke-width:1px,fill:none
  style ServiceCalendarFrame stroke:#999,stroke-width:1px,fill:none
  style ServiceFrame stroke:#999,stroke-width:1px,fill:none
  style SiteFrame stroke:#999,stroke-width:1px,fill:none
  style OtherStuff stroke:#999,stroke-width:1px,fill:none


```
Notes:
* Every `ServiceJourney` belongs to one Line and has one `Operator`. Some more information can be stored in associated `ResponsibilitySet`s (difference between operator and legal "owner"). 
* The pattern of the stops is defined in a `ServiceJourneyPattern` with additional details about each stop.
* The timing behaviour is stored in `TimeDemandType`. They contain run times and where needed wait times. The relevant `TimingLink`s are mostly based on `ScheduledStopPoint`s and not individual to each `ServiceJourneyPattern`.
* The physical stops are modeled as `StopPlace`e with `Quays`.
* `ScheduledStopPoint`s are the "logical" stops.
* The `PassengerStopAssignment` associates the physical and the logical stops.
* `DefaultConnection` and `SiteConnection` define transfers based on site elements.
* `ServiceJourneyMeeting`s are used for splitting and joining of trains and "Durchbindungen".
=======
flowchart TD
    %% Resources at the very top
    subgraph Resources["Resources"]
        direction LR
        AN[AlternativeName]
        O[Operator]
    end

    %% Main content area
    subgraph MainContent["Main Content"]
        %% Timetable & Calendar
        subgraph TimetableCalendar["Timetable & Calendar"]
            direction LR
            subgraph TimetableFrame["TimetableFrame"]
                SJ[ServiceJourney]
                DT[DirectionType]
                TN[TrainNumber]
                SI[ServiceJourneyInterchange]
                JP[JourneyPart]
            end
            subgraph ServiceCalendarFrame["ServiceCalendarFrame"]
                AC[AvailabilityCondition]
                UOP[ValidDayBits]
            end
        end

        %% Service & Network
        subgraph ServiceNetwork["Service & Network"]
            direction LR
            subgraph ServiceFrame["ServiceFrame"]
                SJP[ServiceJourneyPattern]
                TDT[TimeDemandType]
                L[Line]
                SPtJP[StopPointInJourneyPattern]
                TL[TimingLink]
                SSP[ScheduledStopPoint]
                N[Notice]
                F[ServiceFacilities]
                PSA[PassengerStopAssignment]
            end
            subgraph SiteFrame["SiteFrame"]
                SP[StopPlace]
                CN[DefaultConnection]
                Q[Quay]
            end
        end
    end

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

    %% Styling
    style SJ fill:#e6f9e6,stroke:#2ea44f,stroke-width:2px
    style SJP fill:#e6f9e6,stroke:#2ea44f,stroke-width:2px
    style TDT fill:#e6f9e6,stroke:#2ea44f,stroke-width:2px
    style PSA fill:#e6f9e6,stroke:#2ea44f,stroke-width:2px
    style TimetableFrame stroke:#999,stroke-width:1px,fill:none
    style ServiceCalendarFrame stroke:#999,stroke-width:1px,fill:none
    style ServiceFrame stroke:#999,stroke-width:1px,fill:none
    style SiteFrame stroke:#999,stroke-width:1px,fill:none
    style MainContent fill:none,stroke:none
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
>>>>>>> upstream/main
* `Notice`, `ServiceFacility` and `SiteFacility` model almost everything else (especially offers).
* The operating days are defined through `ValidDayBits` for the whole timetable year in `AvailabilityCondition`s.
