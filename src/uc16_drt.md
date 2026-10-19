---
mermaid: true
---

# Use Case: Demand Responsive Traffic (DRT)

In this chapter:
- [Overview](#overview)
- [Modelling Principles](#modelling-principles)
- [Line and LineType](#line-and-linetype)
- [Booking and Rules on the Line](#booking-and-rules-on-the-line)
- [BookingArrangement](#bookingarrangement)
- [ServiceBookingArrangement](#servicebookingarrangement)
- [ServiceCompetitiveCondition](#servicecompetitivecondition)
- [ServiceEligibilityCondition](#serviceeligibilitycondition)
- [FlexibleServiceProperties](#flexibleserviceproperties)
- [Request Stops](#request-stops)
- [Reservation as Service Facility](#reservation-as-service-facility)
- [Collection Points](#collection-points)
- [Templates and Examples](#templates-and-examples)
- [Open Points](#open-points)

## Overview

Demand responsive traffic (DRT, German: *On-Demand-Verkehr*, ODV) covers services that only run,
or only serve some stops, when passengers have booked or requested them.

The Swiss DRT types and their `LineType` are defined in the sheet *LineType* of the
[mapping table for NeTEx 2.0](media/Mappingtabellen_NeTEx_v2.0.xlsx):

*Table: Swiss DRT types*

| Swiss DRT type | LineType | TransportSubmode | Remarks from the mapping table |
|----------------|----------|------------------|--------------------------------|
| 1 – Bedarfslinie | `flexible` | `BusSubmode` `demandAndResponseBus` | Fixed stops, operated on request. |
| 2 – Anrufsammelverkehr | `mixedFlexibleAndFixed` | `BusSubmode` `demandAndResponseBus` | Combines fixed and flexible elements; passengers book individual trips, shared vehicle routing. |
| 3 – Richtungsband, örtlich disponierter Bus | `corridorService` | `BusSubmode` `demandAndResponseBus` | Flexible routing along a geographic corridor; stops constrained to the corridor. |
| 4 – Zeitbezogener Flächenverkehr | `freeAreaAreaWide` | `BusSubmode` `demandAndResponseBus` | time restriction via `AvailabilityCondition` / `Timeband`. |
| 5 – Freier Flächenverkehr | `freeAreaAreaWide` | `BusSubmode` `demandAndResponseBus` | Fully area-wide, no fixed stops. |

## Modelling Principles

A DRT offer is delivered with the same frames and elements as any other timetable. The
flexibility is expressed in these places:

- **Line:** every DRT service is a `Line` in the `ServiceFrame` with the `LineType` of its Swiss
  DRT type and `BusSubmode` `demandAndResponseBus`, see [Line and LineType](#line-and-linetype).
- **Line/bookingArrangements:** holds the booking conditions and the rules of the service, see
  [Booking and Rules on the Line](#booking-and-rules-on-the-line).
- **ServiceJourney:** a single on-demand journey has `FlexibleServiceProperties` referencing the
  `BookingArrangement` of the `Line` (example 04), see
  [FlexibleServiceProperties](#flexibleserviceproperties).
- **StopPointInJourneyPattern:** a request stop has `RequestStop` `true` and a request method; a
  flexible stop references the `BookingArrangement`, see [Request Stops](#request-stops).
- **ServiceFacilitySet and Notice:** reservation offers from HRDF are delivered as facility and
  `Notice`, see [Reservation as Service Facility](#reservation-as-service-facility).

`Line` replaces `FlexibleLine` (`forbidden` in the [ServiceFrame template](./templates/ServiceFrame.xml)),
and `LineType` replaces `TypeOfFlexibleService` (mapping table, sheet *LineType*).

```mermaid
classDiagram
    %% Styles
    classDef frame fill:#FFF8E1,stroke:#FFB300
    classDef contained fill:#E8F4FF,stroke:#1E90FF
    classDef external fill:#F6F6F6,stroke:#AAAAAA

    %% Frames
    class ServiceFrame:::frame {
        lines : Line[]
        journeyPatterns : ServiceJourneyPattern[]
    }
    class TimetableFrame:::frame {
        vehicleJourneys : ServiceJourney[]
    }

    %% Contained elements
    class Line:::contained {
        LineType
        TransportSubmode
        bookingArrangements
    }
    class BookingArrangement:::contained {
        BookingMethods
        BookWhen
        MinimumBookingPeriod
        bookingUrls
        BookingNote
    }
    class ServiceBookingArrangement:::contained {
        BookingChargeType
        DepositRequired
    }
    class ServiceCompetitiveCondition:::contained {
        DistanceFromClassical
        TemporalDistanceFromClassical
        InterchangeWithConventionalServicesAllowed
    }
    class ServiceEligibilityCondition:::contained {
        UserProfile
        ResidentialQualification
    }
    class ServiceJourneyPattern:::contained {
        pointsInSequence
    }
    class StopPointInJourneyPattern:::contained {
        ForBoarding
        ForAlighting
        RequestStop
        bookingArrangements
    }
    class ServiceJourney:::contained {
        ServiceJourneyPatternRef
        FlexibleServiceProperties
    }
    class FlexibleServiceProperties:::contained {
        FlexibleServiceType
        bookingArrangements
    }

    %% Containment relations
    ServiceFrame "1" o-- "0..*" Line : contains
    ServiceFrame "1" o-- "0..*" ServiceJourneyPattern : contains
    TimetableFrame "1" o-- "0..*" ServiceJourney : contains
    Line "1" o-- "0..*" BookingArrangement : contains
    Line "1" o-- "0..*" ServiceBookingArrangement : contains
    Line "1" o-- "0..*" ServiceCompetitiveCondition : contains
    Line "1" o-- "0..*" ServiceEligibilityCondition : contains
    ServiceJourneyPattern "1" o-- "1..*" StopPointInJourneyPattern : contains
    ServiceJourney "1" o-- "0..1" FlexibleServiceProperties : contains

    %% Foreign Key relations
    ServiceJourney "0..*" -- "1" ServiceJourneyPattern : references
    FlexibleServiceProperties "0..*" -- "0..*" BookingArrangement : references
    StopPointInJourneyPattern "0..*" -- "0..*" BookingArrangement : references
```
*Figure: Elements used for DRT*

## Line and LineType
*→ [Glossary definition](A4_annex_glossary.md#line)*

### Purpose
General rules for `Line` are in [Service Frame](06_service.md#line). `LineType` is `expected`
([Line template](./templates/Line.xml)); its values are defined in the mapping table.

### Usage Notes
- A DRT line gets the `LineType` of its Swiss DRT type (see [Overview](#overview)) and
  `BusSubmode` `demandAndResponseBus`.
- `fixed` is the default for all non-DRT lines. If `LineType` is omitted, `fixed` is assumed.
- The values `mainRouteWithFlexibleEnds`, `flexibleAreasOnly`, `hailAndRideSections`,
  `fixedStopAreaWide` and `mixedFlexible` are not used in the Swiss profile.

### Example

```xml
<Line id="ch:1:slnid:1026470" version="1" responsibilitySetRef="ch:1:ResponsibilitySet:BLT">
  <!-- ... -->
  <TransportMode>bus</TransportMode>
  <TransportSubmode>
    <BusSubmode>demandAndResponseBus</BusSubmode>
  </TransportSubmode>
  <!-- ... -->
  <LineType>flexible</LineType>
  <TypeOfProductCategoryRef ref="ch:1:TypeOfProductCategory:B" version="1"/>
  <bookingArrangements>
    <BookingArrangement id="ch:blt:generated:BOOK:29013" version="1">
      <BookingMethods>mobileApp</BookingMethods>
      <BookWhen>advanceOnly</BookWhen>
      <BookingNote>Einstieg nur auf Voranmeldung mind. 30 Min. vor der Fahrt.</BookingNote>
    </BookingArrangement>
  </bookingArrangements>
</Line>
```

## Booking and Rules on the Line

### Purpose
`Line/bookingArrangements` holds four kinds of elements:

*Table: Elements in Line/bookingArrangements*

| Element | Describes |
|---------|-----------|
| `BookingArrangement` | How to book. |
| `ServiceBookingArrangement` | How to book, with additional elements for booking duration and charges. |
| `ServiceCompetitiveCondition` | What the service may do and may not do in relation to classical public transport. |
| `ServiceEligibilityCondition` | Who can use the service. |

### Usage Notes
- Several `ServiceEligibilityCondition`s are combined with OR (e.g. "senior **or** child"). This
  may require splitting a service.
- `FlexibleServiceProperties` and `StopPointInJourneyPattern` can only reference a
  `BookingArrangement`. `ServiceBookingArrangement`, `ServiceCompetitiveCondition` and
  `ServiceEligibilityCondition` are only possible in `Line/bookingArrangements`.

## BookingArrangement

### Purpose
Describes how, when and where a DRT service is booked.

*Table: Elements of BookingArrangement*

| Element | Values / type |
|---------|---------------|
| `BookingContact` | Contact details of the booking office. |
| `BookingMethods` | `callDriver`, `callOffice`, `online`, `phoneAtStop`, `text`, `mobileApp`, `atOffice`, `none`, `other` (list) |
| `BookingAccess` | `public`, `authorisedPublic`, `staff`, `other` |
| `BookWhen` / `BuyWhen` | `advanceOnly`, `untilPreviousDay`, `dayOfTravelOnly`, `advanceAndDayOfTravel`, `timeOfTravelOnly`, `subscriptionChargeMoment`, `other` |
| `LatestBookingTime` | Time |
| `MinimumBookingPeriod` / `MaximumBookingPeriod` | Duration |
| `BookingUrl` | URI |
| `bookingUrls` | `BookingUrl` (URI), `BookingDeepUrl` (`Endpoint`, `parameterDescriptions`) or `BookingService` (`Endpoint`, `EndpointVersion`, `BookingServiceType`, `SupportedSteps`); at least one entry. |
| `BookingNote` | Text |

`BookingServiceType`: `tomp`, `osdm`, `bob`, `trias`, `ojp`, `other`. `SupportedSteps` (list):
`tripPlanning`, `pricing`, `availability`, `booking`, `reservation`, `fulfillment`, `full`, `other`.

### Usage Notes
- From the HRDF conversion only a `BookingNote` can be passed at the moment. With native NeTEx
  handling more information can be transferred
  ([ServiceJourneyPattern template](./templates/ServiceJourneyPattern.xml)).
- In a `ServiceJourneyPattern`, the `BookingArrangement` is referenced with
  `BookingArrangementRef`; an inline `BookingArrangement` is `ignored`.

## ServiceBookingArrangement

### Purpose
Contains the elements of `BookingArrangement` and additionally `MinimumBookingDuration`,
`MaximumBookingDuration`, `DepositRequired` and `BookingChargeType` (`fullAmount`,
`blockFullAmountOnCard`, `deposit`, `none`, `other`).

## ServiceCompetitiveCondition

### Purpose
Describes restrictions of the DRT service towards classical public transport. It contains
**either** the competition parameters **or** the two interchange flags.

*Table: Elements of ServiceCompetitiveCondition*

| Element | Meaning |
|---------|---------|
| `transferRestrictions` / `routingConstraintZones` / `serviceExclusions` | Restrictions towards other services. If not set, the rules apply in general. |
| `DistanceFromClassical` | Distance in metres to the line/service or classical public transport in general; builds geometric exclusion zones. |
| `TemporalDistanceFromClassical` | Temporal distance to the service/transfer in the routing constraint or classical public transport in general. |
| `PenaltyDrivingTimeFactor` / `PenaltyTransferTimeFactor` / `WalkTimeFactor` | Factors for the comparison with classical public transport (default `1.0`). |
| `InterchangeBetweenFlexibleServicesAllowed` | Default `false`. |
| `InterchangeWithConventionalServicesAllowed` | Default `false`. |

### Example

```xml
<ServiceCompetitiveCondition id="ch:1:ServiceCompetitiveCondition:1" version="1">
  <DistanceFromClassical>200</DistanceFromClassical>
  <TemporalDistanceFromClassical>PT15M</TemporalDistanceFromClassical>
</ServiceCompetitiveCondition>
```

## ServiceEligibilityCondition

### Purpose
Describes who can use the service. Each condition contains exactly one of `UserProfile`,
`CommercialProfile`, `ResidentialQualification` or `CompanionProfile`.

### Example

```xml
<ServiceEligibilityCondition id="ch:1:ServiceEligibilityCondition:1" version="1">
  <UserProfile id="ch:1:UserProfile:1" version="1">
    <MinimumAge>65</MinimumAge>
  </UserProfile>
</ServiceEligibilityCondition>
```

## FlexibleServiceProperties
*→ [Glossary definition](A4_annex_glossary.md#flexibleserviceproperties)*

### Purpose
Additional characteristics of a flexible service on a single `ServiceJourney`; a service may be
partly fixed, partly flexible. Elements: `FlexibleServiceType` (`dynamicPassingTimes`,
`fixedHeadwayFrequency`, `fixedPassingTimes`, `notFlexible`, `other`), `CancellationPossible`,
`ChangeOfTimePossible` and `bookingArrangements`.

### Example
From [example 04](./examples/04_NeTEx_CH_DRT_Line_50.110.xml):

```xml
<ServiceJourney id="ch:blt:generated:SJ:29013:ODV" version="1" responsibilitySetRef="ch:1:ResponsibilitySet:BLT">
  <!-- ... -->
  <FlexibleServiceProperties id="ch:blt:generated:FSP:SJ:29013:ODV" version="1">
    <bookingArrangements>
      <BookingArrangementRef ref="ch:blt:generated:BOOK:29013" version="1"/>
    </bookingArrangements>
  </FlexibleServiceProperties>
</ServiceJourney>
```

## Request Stops

### Purpose
Request stops are set in the `StopPointInJourneyPattern` (see
[Service Frame](06_service.md#servicejourneypattern)). The mapping from HRDF is defined in the
sheet *Haltecode* of the mapping table:

*Table: Request stops (Bedarfshalt, HRDF `*A X`)*

| HRDF | ForAlighting | ForBoarding | RequestStop | Request method |
|------|--------------|-------------|-------------|----------------|
| Bedarfshalt | `true` | `true` | `true` | `BoardingRequestMethod` and `AlightingRequestMethod` |
| Bedarfshalt nur zum Einsteigen | `false` | `true` | `true` | `BoardingRequestMethod` |
| Bedarfshalt nur zum Aussteigen | `true` | `false` | `true` | `AlightingRequestMethod` |

### Usage Notes
- `StopUse` is `access`, at stations with BHFArt 3 `interchangeOnly`.
- A flexible stop references the `BookingArrangement` with `BookingArrangementRef`
  ([ServiceJourneyPattern template](./templates/ServiceJourneyPattern.xml)).

## Reservation as Service Facility

Reservation offers from HRDF are delivered as `ServiceFacilitySet` and, where defined, as `Notice`
(sheet *Angebote* of the mapping table, see also [Service Facilities](uc04_service_facilities.md)).
Examples:

*Table: Reservation offers relevant for DRT*

| HRDF | Text | Facility | Notice |
|------|------|----------|--------|
| `BH` | Bedarfshalt nur auf telefonische Voranmeldung | `reservationsCompulsory`; `RequestStop` `true` in the call | yes |
| `RR` | Reservierung obligatorisch | `reservationsCompulsory` | – |
| `XR` | Einstieg nur nach telefonischer Voranmeldung | `reservationsCompulsory` | yes |
| `GR` | GRUPPEN: Reservierung obligatorisch | `groupsAllowedWithReservation` or `reservationsCompulsoryForGroups` | – |

## Collection Points

Collection points are described with `StopPlaceType` (Decision 2026-06-30, "namentlich für
drt:collectionPoint"). The `ResourceFrame` contains the `ValueSet` `ch:1:ValueSet:TypesOfPlace`
with the `TypeOfPlace`s `drtCollectionPoint` and `regularStop`
([ResourceFrame template](./templates/ResourceFrame.xml),
[Resource Frame](09_resources.md#typesofplace)).

## Templates and Examples

*Table: Templates relevant for DRT*

| Template | Relevant content |
|----------|------------------|
| [ServiceFrame](./templates/ServiceFrame.xml), [ServiceFrame_NETWORK_OFFER](./templates/ServiceFrame_NETWORK_OFFER.xml) | `Line` |
| [Line](./templates/Line.xml) | `LineType`, `TransportSubmode` |
| [ServiceJourneyPattern](./templates/ServiceJourneyPattern.xml) | `ForBoarding`, `ForAlighting`, `RequestStop`, `StopUse`, `BookingArrangementRef` |
| [ServiceFacilitySet](./templates/ServiceFacilitySet.xml) | Facilities, `GroupBookingFacility` |
| [Notice](./templates/Notice.xml) | Passenger information |
| [StopPlace](./templates/StopPlace.xml) | `StopPlaceType` |
| [TypesOfPlace](./templates/TypesOfPlace.xml), [ResourceFrame](./templates/ResourceFrame.xml) | `drtCollectionPoint`, `regularStop` |
| [AvailabilityCondition](./templates/AvailabilityCondition.xml) | `Timeband`s (time restriction of type 4) |

*Table: Examples relevant for DRT*

| Example | Content |
|---------|---------|
| [04_NeTEx_CH_DRT_Line_50.110](./examples/04_NeTEx_CH_DRT_Line_50.110.xml) | `BookingArrangement` on the `Line`, one on-demand journey with `FlexibleServiceProperties`. |
| [05_NeTEx_CH_DRT_Line_Dependent_On_Passengers_At_Start](./examples/05_NeTEx_CH_DRT_Line_Dependent_On_Passengers_At_Start.xml) | No reservation; passengers can only alight after the first stop (`ForBoarding` `false`), `Notice`. |

Further Swiss DRT examples are in the NeTEx repository under
[`examples/functions/drt/`](https://github.com/NeTEx-CEN/NeTEx/tree/v2.1-wip/examples/functions/drt).
