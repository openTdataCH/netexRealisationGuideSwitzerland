# Joining and splitting of trains


**TODO** Input from slides

## Current data modeling of trains

**TODO** from slides

```mermaid
graph LR
  A ---|101| B
  B ---|102| C
  B ---|202| D
 ```

or

```mermaid
graph LR
  A ---|101| B
  B ---|101| C
  B ---|202| D
 ```

## Optimal modeling in Transmodel
```mermaid
graph LR
  A ---|101| B
  B ---|102| C
  B ---|202| D
  A --| ServiceJourney sj1 | C
  A --| ServiceJourney sj2 | D

  %% styled edges
  linkStyle 3 stroke:#ff0000,stroke-width:2px   %% A-C (4th link, index 3)
  linkStyle 4 stroke:#0000ff,stroke-width:2px   %% A-D (5th link, index 4)
 ```

## Modeling with JourneyMeeting

**TODO**
- [Example](../generated/xml-snippet/JourneyMeeting.xml)

## Modeling with JourneyPartCouples

**TODO**
- [Example](../generated/xml-snippet/JourneyPartCouple.xml)