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



```xml
<?xml version="1.0" encoding="UTF-8"?>
<DefaultConnection  id="ch:1:DefaultConnection:8506302" version="1">
  <!-- Be aware only some combinations areallowed  mode - mode, operator/type of product category - operator/type of  product category. -->
  <WalkTransferDuration>
    <DefaultDuration>PT3M</DefaultDuration>
  </WalkTransferDuration>
  <StopPlaceRef ref="ch:2:StopPlace:8506302" version="1"/>
</DefaultConnection>

```



>Note: If no StopPlaceRef is set, the DefaultConnection applies network-wide for the given mode combination. A separate DefaultConnection must be defined for each relevant mode pair.




```xml
<?xml version="1.0" encoding="UTF-8"?>
<DefaultConnection  id="ch:1:DefaultConnection:9999999-1" version="1">
  <!-- General connection between two modes in the whole network, when not StopPlaceRef is mentioned. Most exist for each mode pair. -->
  <WalkTransferDuration>
    <DefaultDuration>PT2M</DefaultDuration>
  </WalkTransferDuration>
  <From>
    <TransportMode>tram</TransportMode>
  </From>
  <To>
    <TransportMode>tram</TransportMode>
  </To>
  <StopPlaceRef ref="ch:1:sloid:19231" version="1">
    <!-- Is a sloid usually. Not set, means whole network. -->
  </StopPlaceRef>
</DefaultConnection>

```




## Operator related transfer times (UMSTEIGV)
Defines transfer times between two specific operators at a stop place. The HRDF UMSTEIGV record specifies the default transfer time between two administrations (operators). 

**When to use:** When the transfer time depends on the operator combination at a given stop place.



```xml
<?xml version="1.0" encoding="UTF-8"?>
<DefaultConnection  id="11-11" version="1">
  <Extensions>
    <!-- When also ProductCategory is relevant, then this extension must be used -->
    <FromProductCategoryRef ref="ch:1:TypeOfProductCategory:ICE" version="1">
      <!-- Extension needed to map "Verkehrsmittel-Gattung", which is similar to but more detailed than Trans-portSubmode, for transfer times of interchanges. -->
    </FromProductCategoryRef>
    <ToProductCategoryRef ref="ch:1:TypeOfProductCategory:TE2" version="1">
      <!-- Extension needed to map "Verkehrsmittel-Gattung", which is similar to but more detailed than Trans-portSubmode, for transfer times of interchanges. -->
    </ToProductCategoryRef>
  </Extensions>
  <WalkTransferDuration>
    <DefaultDuration>PT2M</DefaultDuration>
  </WalkTransferDuration>
  <BothWays>false</BothWays>
  <!-- We don't use BothWays true, as it might differ. -->
  <From>
    <TransportMode>all</TransportMode>
    <OperatorView>
      <OperatorRef ref="ch:1:Operator:11" version="1"/>
    </OperatorView>
  </From>
  <To>
    <TransportMode>all</TransportMode>
    <OperatorView>
      <OperatorRef ref="ch:1:Operator:11" version="1"/>
    </OperatorView>
  </To>
  <StopPlaceRef ref="ch:1:sloid:19231" version="1">
    <!-- Is a sloid usually. Not set, means whole network. -->
  </StopPlaceRef>
</DefaultConnection>

```




## Line and Direction-oriented transfer times (UMSTEIGL)
Defines transfer times between specific `lines` and `directions` at a stop place. Journeys are specified indirectly via Line and Direction, not as an explicit journey pair. The ! marker in HRDF indicates a guaranteed connection.
> **TODO** Adrian we don't have Direction anymore. This should be solved by the PR.
 

**When to use:** When the transfer time applies to all journeys of a specific line/direction combination at a given stop place.



```xml
<?xml version="1.0" encoding="UTF-8"?>
<InterchangeRule  id="ch:1:InterchangeRule:1696906_TA_0_86400" version="1">
  <!-- transfer times between Line/Directions at a given stop (UMSTEIGL) -->
  <validityConditions>
    <AvailabilityConditionRef ref="ch:1:AvailabilityCondition:TA" version="1"/>
  </validityConditions>
  <StaySeated>false</StaySeated>
  <Planned>true</Planned>
  <Guaranteed>false</Guaranteed>
  <MinimumTransferTime>PT2M</MinimumTransferTime>
  <MaximumTransferTime>PT2M</MaximumTransferTime>
  <timings>
    <InterchangeRuleTiming id="ch:1:InterchangeRuleTiming:1696906:0:86400" version="1">
      <TimebandRef ref="ch:1:Timeband:0:0" version="1"/>
    </InterchangeRuleTiming>
  </timings>
  <FeederFilter>
    <StopPlaceRef ref="ch:generated:StopPlace:8507483" version="1"/>
    <LineInDirectionRef>
      <LineRef ref="ch:generated:Line:33.PE.GPX" version="1"/>
      <DirectionRef ref="ch:1:Direction:R" version="1"/>
    </LineInDirectionRef>
    <AdjacentStopPlaceRef ref="ch:generated:StopPlace:8507493" version="1"/>
  </FeederFilter>
  <DistributorFilter>
    <StopPlaceRef ref="ch:generated:StopPlace:8507483" version="1"/>
    <LineInDirectionRef>
      <LineRef ref="ch:generated:Line:11.IC.IC81" version="1"/>
      <DirectionRef ref="ch:1:Direction:R" version="1"/>
    </LineInDirectionRef>
    <AdjacentStopPlaceRef ref="ch:generated:StopPlace:8507493" version="1"/>
  </DistributorFilter>
</InterchangeRule>

```




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



```xml
<?xml version="1.0" encoding="UTF-8"?>
<InterchangeRule  id="ch:1:InterchangeRule:1692675_80600_18840_18960" version="1">
  <!-- transfer times between ServiceJourneys (UMSTEIGZ) -->
  <validityConditions>
    <AvailabilityConditionRef ref="ch:1:AvailabilityCondition:80600" version="1"/>
  </validityConditions>
  <StaySeated>false</StaySeated>
  <Planned>true</Planned>
  <Guaranteed>false</Guaranteed>
  <MinimumTransferTime>PT1M</MinimumTransferTime>
  <MaximumTransferTime>PT2M</MaximumTransferTime>
  <timings>
    <InterchangeRuleTiming id="ch:1:InterchangeRuleTiming:1692675:18840:18960" version="1">
      <TimebandRef ref="ch:1:Timeband:18840:18960" version="1"/>
    </InterchangeRuleTiming>
  </timings>
  <FeederFilter>
    <StopPlaceRef ref="ch:2:StopPlace:8506131" version="any"/>
    <LineInDirectionRef>
      <LineRef ref="ch:2:Line:65.S.S1" version="any"/>
      <DirectionRef ref="ch:1:Direction:R" version="any"/>
    </LineInDirectionRef>
    <AdjacentStopPlaceRef ref="ch:2:StopPlace:8506128" version="1"/>
    <ServiceJourneyRef ref="ch:1:ServiceJourney:ch:1:sjyid:100046:11111-001_91001C.j26_1012" version="1"/>
  </FeederFilter>
  <DistributorFilter>
    <StopPlaceRef ref="ch:2:StopPlace:8506131" version="any"/>
    <LineInDirectionRef>
      <LineRef ref="ch:2:Line:11.IR.IR75" version="any"/>
      <DirectionRef ref="ch:1:Direction:R" version="any"/>
    </LineInDirectionRef>
    <AdjacentStopPlaceRef ref="ch:2:StopPlace:8506105" version="1"/>
    <ServiceJourneyRef ref="ch:1:ServiceJourney:ch:1:sjyid:100001:2106-001_91075_.j26_802" version="1"/>
  </DistributorFilter>
</InterchangeRule>

```




## Transfer times between different StopPlaces (METABHF)
Describes the walking time between two adjacent `StopPlaces` (e.g. main station A → tram stop B). Used only in the master data file, not in timetable files.  
**When to use:** When passengers need to transfer between two physically separate stop places.



```xml
<?xml version="1.0" encoding="UTF-8"?>
<SiteConnection  id="ch:1:SiteConnection:8506302-8589913" version="1">
  <!-- SiteConnection are used only in the main file and not in timetable files. -->
  <WalkTransferDuration>
    <DefaultDuration>PT13M</DefaultDuration>
  </WalkTransferDuration>
  <BothWays>false</BothWays>
  <From>
    <!-- Could also refer to a Quay or a different SiteElement. Currently we only transfer StopPlaceRefs. -->
    <StopPlaceRef ref="ch:2:StopPlace:8506302" version="1"/>
  </From>
  <To>
    <!-- Could also refer to a Quay or a different SiteElement. Currently we only transfer StopPlaceRefs. -->
    <StopPlaceRef ref="ch:2:StopPlace:8589913" version="1"/>
  </To>
</SiteConnection>

```


