---
mermaid: true
---

# Use Case: Formations

>NOTE: We currently don't import or export formations. Currently, this is an experimental use case that defines how we might do it. It is still work in progress.

Most important elements:
- `Train`
- `TrainComponent`
- `TrainElement`

> **LATER** Add template for these elements.

```mermaid
classDiagram


    class Train {
        SelfPropelled: boolean
        components: TrainComponents[]
    }

    %% Contained elements
    class TrainComponent {
        Label: Text
        TrainElement
        TrainElementRef

        
    }

    class TrainElement {
        TrainElementType
        FareClasses

    }

class CompoundTrain {
    SelfPropelled : boolean
    components[]

    }

class TrainInCompoundTrain {
    TrainRef
    Label 
}
    class TrainBlock {
        TrainRef
        StartPointRef
        EndPointRef
        blockParts
    }

    class TrainBlockPart {
        Description
        CompoundTrainRef
        JourneyPartCoupleRef
    }

    class ServiceJourney {
        TrainRef
        BlockRef
        parts : JourneyPart[]
        passingTimes[]
        ServiceJourneyPatternRef
    }

    class ServiceJourneyPattern {
        stopPointInJourneyPattern []
    }

    class StopPointInJourneyPattern {
        ScheduledStopPointRef
    }


    class JourneyPart {
        ParentJourneyRef
        MainPartRef
        JourneyPartCoupleRef
        TrainNumberRef
        TrainBlockPartRef
        FromStopPointRef
        ToStopPointRef
    }

    class PassengerStopAssignment {
        ScheduledStopPointRef
        ArrivesForwards:boolean
        DepartsForwards: boolean
        StopPlaceRef
        QuayRef
        passengerBoardingPositionsAssignments
    }

    class PassengerBoardingPositionAssignment  {
     BoardingUse : boolean
     AlightingUse: boolean
     TrainComponentRef
     IsAllowed: boolean
    }

    %% Containment relations (only contained elements)
    Train "1" o-- "0..*" TrainComponent : contains
    TrainComponent "0" o-- "1" TrainElement : contains or references
    TrainBlock "1" o-- "0..*" TrainBlockPart : contains
    TrainBlock "1" --> "0..*" Train : references
    TrainBlockPart "1" --> "0..*" CompoundTrain : references
    CompoundTrain "1" --> "0..*" TrainInCompoundTrain : contains
    TrainInCompoundTrain "1" -- "1" Train : references
    ServiceJourney "1" o-- "0..1" Train : references
    ServiceJourney "1" o-- "0..1" TrainBlock : references
    ServiceJourney "1"  o-- "0..*" JourneyPart: contains
    JourneyPart  "1" o-- "0..1"  TrainBlock : references
    PassengerStopAssignment "0"  o-- "0..*" PassengerBoardingPositionAssignment : contains
    PassengerBoardingPositionAssignment "1" o-- "0..1"  TrainComponent : references
    ServiceJourney "1"  --> "1" ServiceJourneyPattern : references
    ServiceJourneyPattern "1" o-- "0..*" StopPointInJourneyPattern : contains
    StopPointInJourneyPattern "1"  --> "1" ScheduledStopPoint : references
    PassengerStopAssignment "1" --> "1" ScheduledStopPoint: references
    PassengerBoardingPositionAssignment "1" --> "0..1" ScheduledStopPoint: references
```

## Example
**LATER** Needs to be defined with TimeDemandType

## Usage Notes
- We intend to use a version without `Block` and `CompoundTrain`.
- We are unsure how to map to sectors as we don't want to have to invent new ScheduledStopPoints (especially as this would need new pseudo-sloid). **LATER**
- We have a special example for when the platform is too short on a given stop: **TODO**