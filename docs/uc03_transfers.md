# Transfers

## Overview
This use case describes how transfer times and interchange connections between journeys are modelled in the Swiss NeTEx profile. Depending on the granularity and type of connection, different elements are used.

## Mapping between HRDF and NeTEx 

The following table shows how we will map HRDF tables into NeTEX.

| HRDF     | NeTEx RG1           | NeTEx RG2                                                                                                      | Use Case                                   |
|----------|---------------------|----------------------------------------------------------------------------------------------------------------|--------------------------------------------|
| UMSTEIGZ | `InterchangeRule`   | `ServiceJourneyInterchange`                                                                                    | Fahrtbezogene Umsteigezeit                 |
| UMSTEIGL | `InterchangeRule`   | `ServiceJourneyInterchange`                                                                                    | Linien- und Richtungsbezogene Umsteigezeit |
| UMSTEIGB | `DefaultConnection` | `DefaultConnection`                                                                                            | Standardumsteigezeit pro Haltestelle       |
| METABHF  | `SiteConnection`    | `SiteConnection`                                                                                               | Umsteigezeit zwischen Haltestellen         |
| UMSTEIGV | `DefaultConnection` | `DefaultConnection`                                                                                            | Verwaltungsbezogene Umsteigezeit           |
| DURCHBI  | `JourneyMeeting`    | `ServiceJourneyInterchange`<br>Alternativ für Flügelzug, Vereinigung: <br>JourneyParts, JourneyPartsCouple<br> | Durchbindung, Flügelzug, Vereinigung       |


## Transfer times at a given StopPlace (UMSTEIGB)
Defines the default transfer time at a specific stop place, regardless of operator or line.

**When to use:** When a particular stop place has a transfer time that differs from the network-wide default.

- [Example](../generated/xml-snippets/DefaultConnection_UMSTEIGB.xml)

>Note: If no StopPlaceRef is set, the DefaultConnection applies network-wide for the given mode combination. A separate DefaultConnection must be defined for each relevant mode pair.


- [Example](../generated/xml-snippets/DefaultConnection_Modes.xml)


## Operator related transfer times (UMSTEIGV)
Defines transfer times between two specific operators at a stop place. The HRDF UMSTEIGV record specifies the default transfer time between two administrations (operators). 

**When to use:** When the transfer time depends on the operator combination at a given stop place.

- [Example](../generated/xml-snippets/DefaultConnection_UMSTEIGV.xml)


## Line and Direction-oriented transfer times (UMSTEIGL)
Defines transfer times between specific `lines` and `directions` at a stop place. Journeys are specified indirectly via Line and Direction, not as an explicit journey pair. The ! marker in HRDF indicates a guaranteed connection.
> **TODO** Adrian we don't have Direction anymore. This should be solved by the PR.
 

**When to use:** When the transfer time applies to all journeys of a specific line/direction combination at a given stop place.

- [Example](../generated/xml-snippets/ServiceJourneyInterchange_UMSTEIGL.xml)


## ServiceJourney related transfer times (UMSTEIGZ)
Defines transfer times between two specific `ServiceJourneys` at a given stop place. Unlike UMSTEIGL, journeys are referenced directly via `ServiceJourneyRef`. The ! marker in HRDF indicates a guaranteed connection; an optional `Verkehrstagebitfeldnummer` restricts validity to specific days.

**When to use**: When the transfer time applies to a specific feeder/distributor journey pair.

Connection between two services. 

The following situations exist: 
- I.	The connection should not take place. (Prohibition) 
- II.	The connection must take place, and the traveller must change vehicles
- III.	The connection has to take place, and the passenger can stay in the vehicle

The differences between the various situations are to be differentiated with the value in some attributes.

| Situation | `StaySeated` | `Guaranteed` | Description |
|-----------|-------------|--------------|-------------|
| Connection prohibited | — | — | `InterchangeRule` explicitly forbidding the connection |
| Transfer required | `false` | `false` / `true` | Passenger must change vehicles |
| Through-service (stay seated) | `true` | `true` | Passenger remains in vehicle → see [uc01_durchbindung](uc01_durchbindung.md) |

- [Example](../generated/xml-snippets/ServiceJourneyInterchange_UMSTEIGZ.xml)


## Transfer times between different StopPlaces (METABHF)
Describes the walking time between two adjacent `StopPlaces` (e.g. main station A → tram stop B). Used only in the master data file, not in timetable files.  
**When to use:** When passengers need to transfer between two physically separate stop places.

- [Example](../generated/xml-snippets/SiteConnection.xml)
