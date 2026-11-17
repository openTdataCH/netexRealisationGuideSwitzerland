# Transfers

## Overview
This use case describes how transfer times and interchange connections between journeys are modelled in the Swiss NeTEx profile. Depending on the granularity and type of connection, different elements are used.

## Mapping between HRDF and NeTEx 

The following table shows how we will map HRDF tables into NeTEX. 
> NB: The UMSTEIG tables are curated by INFO+. So they are not delivered in NeTEx to INFO+, but are generated there. 

| HRDF     | NeTEx RG1           | NeTEx RG2                                                                                                      | Use Case                                   |
|----------|---------------------|----------------------------------------------------------------------------------------------------------------|--------------------------------------------|
| DURCHBI  | `JourneyMeeting`    | `ServiceJourneyInterchange`                                                                                    | Durchbindung, Flügelzug, Vereinigung       |
| UMSTEIGZ | `InterchangeRule`   | `ServiceJourneyInterchange`                                                                                    | Fahrtbezogene Umsteigezeit                 |
| UMSTEIGL | `InterchangeRule`   | `ServiceJourneyInterchange`                                                                                    | Linien- und Richtungsbezogene Umsteigezeit |
| UMSTEIGV | `DefaultConnection` | `DefaultConnection`                                                                                            | Verwaltungsbezogene Umsteigezeit           |
| UMSTEIGB | `DefaultConnection` | `DefaultConnection`                                                                                            | Standardumsteigezeit pro Haltestelle       |
| METABHF  | `SiteConnection`    | `SiteConnection`                                                                                               | Umsteigezeit zwischen Haltestellen         |

### Priority of transfer times

If several transfer times apply to the same transfer, the first matching rule in the following order applies. The order is the one in which HAFAS applies the HRDF transfer times (HAFAS raw data format 5.40.72, chapter 8).

| Priority | HRDF                                | NeTEx RG2.0                                                                  |
|----------|-------------------------------------|----------------------------------------------------------------------------|
| 1        | UMSTEIGZ (journey pair)             | `ServiceJourneyInterchange`                                                |
| 2        | UMSTEIGL at a stop                  | `ServiceJourneyInterchange` (resolved per journey pair)                    |
| 3        | UMSTEIGV at a stop                  | `DefaultConnection` with `StopPlaceRef` and `OperatorRef`                  |
| 4        | UMSTEIGB at a stop                  | `DefaultConnection` with `StopPlaceRef`, without `OperatorRef`             |
| 5        | UMSTEIGL global                     | `ServiceJourneyInterchange` (resolved per journey pair)                    |
| 6        | UMSTEIGV global                     | `DefaultConnection` with `OperatorRef`, without `StopPlaceRef`             |
| 7        | Standard transfer time (UMSTEIGB `9999999`) | `DefaultConnection` per mode pair, without `StopPlaceRef` and `OperatorRef` |

A `DefaultConnection` that references operators therefore only takes precedence over the transfer time of a stop if it is defined for that stop. A global operator rule ranks below the transfer time of the stop.

DURCHBI and METABHF are not part of this order: DURCHBI is a through-service (`StaySeated`), not a transfer time, and METABHF is a `SiteConnection` between two different stops.

### Export guarantees

The export guarantees that:
- for two service journeys and `FromPointRef` / `ToPointRef`, maximum one `ServiceJourneyInterchange` will be produced
- for a stop, maximum one `DefaultConnection` without `OperatorRef` will provide the transfer time at that stop
- for a combination of stop (or whole network), operator pair and product category pair, maximum one `DefaultConnection` will provide the transfer time

## Transfer times at a given StopPlace (UMSTEIGB)
Defines the default transfer time at a specific stop place, regardless of operator or line.

**When to use:** When a particular stop place has a transfer time that differs from the network-wide default.

- [Example](../site/xml-snippets/DefaultConnection_UMSTEIGB.xml)

>Note: If no StopPlaceRef is set, the DefaultConnection applies network-wide for the given mode combination. A separate DefaultConnection must be defined for each relevant mode pair.

- [Example](../site/xml-snippets/DefaultConnection_Modes.xml)


## Operator related transfer times (UMSTEIGV)
Defines transfer times between two specific operators at a stop place. The HRDF UMSTEIGV record specifies the default transfer time between two administrations (operators). 

**When to use:** When the transfer time depends on the operator combination at a given stop place.

- [Example](../site/xml-snippets/DefaultConnection_UMSTEIGV.xml)

## Line and Direction-oriented transfer times (UMSTEIGL)
Defines transfer times between specific `Lines` and `Directions` at a stop place in HRDF. `ServiceJourneyInterchange` has no element to reference a `Line`/`DirectionType` combination directly — it always requires two concrete journeys (`FromServiceJourneyRef`/`ToServiceJourneyRef`). UMSTEIGL is therefore fully resolved during import/export: one `ServiceJourneyInterchange` is generated per matching pair of actual journeys. The `!` marker in HRDF indicates a guaranteed connection (`Guaranteed=true`).
> In the Swiss profile, only `DirectionType` (type `DirectionTypeEnumeration`) is used, not `DirectionRef`.

**When to use:** When the transfer time applies to all journeys of a specific line/direction combination at a given stop place — resolved to one `ServiceJourneyInterchange` per journey pair.

- [Example](../site/xml-snippets/ServiceJourneyInterchange_UMSTEIGL.xml)

## ServiceJourney related transfer times (UMSTEIGZ)
Defines transfer times between two specific `ServiceJourneys` at a given stop place. Unlike UMSTEIGL, journeys are referenced directly via `ServiceJourneyRef`. The ! marker in HRDF indicates a guaranteed connection; an optional `Verkehrstagebitfeldnummer` restricts validity to specific days.

**When to use**: When the transfer time applies to a specific feeder/distributor journey pair.

Connection between two services. 

The following situations exist: 
- I.	The connection should not take place. (Prohibition) 
- II.	The connection must take place, and the traveler must change vehicles
- III.	The connection has to take place, and the passenger can stay in the vehicle

The differences between the various situations are to be differentiated with the value in some attributes.

| Situation | `StaySeated` | `Guaranteed` | Description |
|-----------|-------------|--------------|-------------|
| Connection prohibited | — | — | `InterchangeRule` explicitly forbidding the connection |
| Transfer required | `false` | `false` / `true` | Passenger must change vehicles |
| Through-service (stay seated) | `true` | `true` | Passenger remains in vehicle → see [uc01_durchbindung](uc01_durchbindung.md) |

- [Example](../site/xml-snippets/ServiceJourneyInterchange_UMSTEIGZ.xml)


## Transfer times between different StopPlaces (METABHF)
Describes the walking time between two adjacent `StopPlaces` (e.g. main station A → tram stop B). Used only in the master data file, not in timetable files.  
**When to use:** When passengers need to transfer between two physically separate stop places.

- [Example](../site/xml-snippets/SiteConnection.xml)
