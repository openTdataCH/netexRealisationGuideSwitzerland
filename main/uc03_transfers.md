# Transfers

## Overview
This use case describes how transfer times and interchange connections between journeys are modelled in the Swiss NeTEx profile. Depending on the granularity and type of connection, different elements are used.

## Mapping between HRDF and NeTEx 

The following table shows how we will map HRDF tables into NeTEX. 
> NB: The UMSTEIG tables are curated by INFO+. So they are not delivered in NeTEx to INFO+, but are generated there. 

| HRDF     | NeTEx RG1           | NeTEx RG2                                                                                                      | Use Case                                   |
|----------|---------------------|----------------------------------------------------------------------------------------------------------------|--------------------------------------------|
| UMSTEIGZ | `InterchangeRule`   | `ServiceJourneyInterchange`                                                                                    | Fahrtbezogene Umsteigezeit                 |
| UMSTEIGL | `InterchangeRule`   | `ServiceJourneyInterchange`                                                                                    | Linien- und Richtungsbezogene Umsteigezeit |
| UMSTEIGB | `DefaultConnection` | `DefaultConnection`                                                                                            | Standardumsteigezeit pro Haltestelle       |
| METABHF  | `SiteConnection`    | `SiteConnection`                                                                                               | Umsteigezeit zwischen Haltestellen         |
| UMSTEIGV | `DefaultConnection` | `DefaultConnection`                                                                                            | Verwaltungsbezogene Umsteigezeit           |
| DURCHBI  | `JourneyMeeting`    | `ServiceJourneyInterchange`                                                                                    | Durchbindung, Flügelzug, Vereinigung       |


## Transfer times at a given StopPlace (UMSTEIGB)
Defines the default transfer time at a specific stop place, regardless of operator or line.

**When to use:** When a particular stop place has a transfer time that differs from the network-wide default.



```xml
<?xml version="1.0" encoding="UTF-8"?>
<DefaultConnection id="ch:1:DefaultConnection:8506302" version="1">
  <!-- Be aware only some combinations are allowed: from mode A to mode B without operators taken into account; from operator A and product category A  to operator B and product category B. -->
  <WalkTransferDuration>
  <DefaultDuration>PT3M</DefaultDuration>
  </WalkTransferDuration>
  <StopPlaceRef ref="ch:2:StopPlace:8506302" version="1"/>
</DefaultConnection>
```



>Note: If no StopPlaceRef is set, the DefaultConnection applies network-wide for the given mode combination. A separate DefaultConnection must be defined for each relevant mode pair.



```xml
<?xml version="1.0" encoding="UTF-8"?>
<DefaultConnection id="ch:1:DefaultConnection:9999999-1" version="1">
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
  <!-- Usually a SLOID. Not set means whole network. -->
  </StopPlaceRef>
</DefaultConnection>
```




## Operator related transfer times (UMSTEIGV)
Defines transfer times between two specific operators at a stop place. The HRDF UMSTEIGV record specifies the default transfer time between two administrations (operators). 

**When to use:** When the transfer time depends on the operator combination at a given stop place.



```xml
<?xml version="1.0" encoding="UTF-8"?>
<DefaultConnection id="11-11" version="1">
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
  <BothWays>false
  <!-- We don't use BothWays true, as it might differ. -->
  </BothWays>
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
  <!-- Usually a SLOID. Not set means whole network. -->
  </StopPlaceRef>
</DefaultConnection>
```



## Line and Direction-oriented transfer times (UMSTEIGL)
Defines transfer times between specific `Lines` and `Directions` at a stop place. Journeys are specified indirectly via `Line` and `DirectionType`, not as an explicit journey pair. The ! marker in HRDF indicates a guaranteed connection.
> In the Swiss profile, only `DirectionType` (type `DirectionTypeEnumeration`) is used, not `DirectionRef`.

**When to use:** When the transfer time applies to all journeys of a specific line/direction combination at a given stop place.



```xml
<?xml version="1.0" encoding="UTF-8"?>
<ServiceJourneyInterchange id="ch:1:ServiceJourneyInterchange:1696906_TA" version="1">
  <!-- Transfer times between specific ServiceJourneys at a given stop (UMSTEIGL). StaySeated=false: passenger must change vehicles. One ServiceJourneyInterchange per journey pair. Replaces InterchangeRule in RG 2.0. -->
  <validityConditions>
  <AvailabilityConditionRef ref="ch:1:AvailabilityCondition:TA" version="1"/>
  </validityConditions>
  <Description>UMSTEIGL: transfer at Spiez, line 33.PE.GPX → line 11.IC.IC81</Description>
  <StaySeated>false</StaySeated>
  <CrossBorder>false</CrossBorder>
  <!-- ChangeWithinVehicle is not applicable when StaySeated=false -->
  <Planned>true</Planned>
  <Guaranteed>false</Guaranteed>
  <MaximumWaitTime>PT2M
  <!-- If not set or PT0M, connection is considered guaranteed. -->
  </MaximumWaitTime>
  <MinimumTransferTime>PT2M</MinimumTransferTime>
  <FromPointRef ref="ch:1:ScheduledStopPoint:8507483:3" nameOfRefClass="ScheduledStopPoint" version="1">
  <!-- ScheduledStopPoint at which the feeder journey arrives. Replaces StopPlaceRef+FeederFilter from InterchangeRule. -->
  </FromPointRef>
  <ToPointRef ref="ch:1:ScheduledStopPoint:8507483:3" nameOfRefClass="ScheduledStopPoint" version="1">
  <!-- ScheduledStopPoint at which the distributor journey departs. Same stop as FromPointRef for same-stop transfers. -->
  </ToPointRef>
  <FromServiceJourneyRef ref="ch:1:ServiceJourney:ch:1:sjyid:100033:XXXX-001_33PE.j26_YYY" version="1">
  <!-- Reference to the specific feeder ServiceJourney. Replaces FeederFilter/LineInDirectionRef from InterchangeRule. One element per journey pair required. -->
  </FromServiceJourneyRef>
  <ToServiceJourneyRef ref="ch:1:ServiceJourney:ch:1:sjyid:100011:XXXX-001_11IC.j26_ZZZ" version="1">
  <!-- Reference to the specific distributor ServiceJourney. Replaces DistributorFilter/LineInDirectionRef from InterchangeRule. -->
  </ToServiceJourneyRef>
</ServiceJourneyInterchange>
```



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



```xml
<?xml version="1.0" encoding="UTF-8"?>
<ServiceJourneyInterchange id="ch:1:ServiceJourneyInterchange:1692675_80600_18840_18960" version="1">
  <!-- Transfer time between two specific ServiceJourneys at a given stop (UMSTEIGZ). StaySeated=false: passenger must change vehicles. Replaces InterchangeRule in RG 2.0. One element per journey pair required. -->
  <validityConditions>
  <AvailabilityConditionRef ref="ch:1:AvailabilityCondition:80600" version="1"/>
  </validityConditions>
  <Description>UMSTEIGZ: transfer at stop 8506131, S1 → IR75</Description>
  <StaySeated>false</StaySeated>
  <CrossBorder>false</CrossBorder>
  <Planned>true</Planned>
  <Guaranteed>false</Guaranteed>
  <MaximumWaitTime>PT2M
  <!-- If not set or PT0M, connection is considered guaranteed. -->
  </MaximumWaitTime>
  <MinimumTransferTime>PT1M</MinimumTransferTime>
  <MaximumTransferTime>PT2M</MaximumTransferTime>
  <FromPointRef ref="ch:1:ScheduledStopPoint:8506131:1" nameOfRefClass="ScheduledStopPoint" version="1">
  <!-- ScheduledStopPoint at which the feeder journey arrives. Replaces StopPlaceRef+FeederFilter from InterchangeRule. -->
  </FromPointRef>
  <ToPointRef ref="ch:1:ScheduledStopPoint:8506131:1" nameOfRefClass="ScheduledStopPoint" version="1">
  <!-- ScheduledStopPoint at which the distributor journey departs. Same stop as FromPointRef for same-stop transfers. -->
  </ToPointRef>
  <FromServiceJourneyRef ref="ch:1:ServiceJourney:ch:1:sjyid:100046:11111-001_91001C.j26_1012" version="1">
  <!-- Reference to the specific feeder ServiceJourney. Replaces FeederFilter/ServiceJourneyRef from InterchangeRule. -->
  </FromServiceJourneyRef>
  <ToServiceJourneyRef ref="ch:1:ServiceJourney:ch:1:sjyid:100001:2106-001_91075_.j26_802" version="1">
  <!-- Reference to the specific distributor ServiceJourney. Replaces DistributorFilter/ServiceJourneyRef from InterchangeRule. -->
  </ToServiceJourneyRef>
</ServiceJourneyInterchange>
```




## Transfer times between different StopPlaces (METABHF)
Describes the walking time between two adjacent `StopPlaces` (e.g. main station A → tram stop B). Used only in the master data file, not in timetable files.  
**When to use:** When passengers need to transfer between two physically separate stop places.



```xml
<?xml version="1.0" encoding="UTF-8"?>
<SiteConnection id="ch:1:SiteConnection:8506302-8589913" version="1">
  <!-- SiteConnection are used only in the main file and not in timetable files. -->
  <WalkTransferDuration>
  <DefaultDuration>PT13M</DefaultDuration>
  </WalkTransferDuration>
  <BothWays>false</BothWays>
  <From>
  <!-- Could also refer to a Quay or a different SiteElement. Currently, we only transfer StopPlaceRefs. -->
  <StopPlaceRef ref="ch:2:StopPlace:8506302" version="1"/>
  </From>
  <To>
  <!-- Could also refer to a Quay or a different SiteElement. Currently, we only transfer StopPlaceRefs. -->
  <StopPlaceRef ref="ch:2:StopPlace:8589913" version="1"/>
  </To>
</SiteConnection>
```


