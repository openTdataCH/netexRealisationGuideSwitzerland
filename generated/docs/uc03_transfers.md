# Transfers

## Mapping between HRDF and NeTEx 

The following table shows how we will map HRDF tables into NeTEX.

| HRDF     | NeTEx RG1         | NeTEx RG2                                                                                                    | Use Case                                   |
|----------|-------------------|--------------------------------------------------------------------------------------------------------------|--------------------------------------------|
| UMSTEIGZ | `InterchangeRule`   | `InterchangeRule`, alternativ `ServiceJourneyInterchange`                                                        | Fahrtbezogene Umsteigezeit                 |
| UMSTEIGL | `InterchangeRule`   | `InterchangeRule`, alternativ `ServiceJourneyInterchange`                                                        | Linien- und Richtungsbezogene Umsteigezeit |
| UMSTEIGB | `DefaultConnection` | `DefaultConnection`                                                                                        | Standardumsteigezeit pro Haltestelle       |
| METABHF  | `SiteConnection`    | `SiteConnection`                                                                                           | Umsteigezeit zwischen Haltestellen         |
| UMSTEIGV | `DefaultConnection` | `DefaultConnection`                                                                                        | Verwaltungsbezoge Umsteigezeit             |
| DURCHBI  | `JourneyMeeting`    | `ServiceJourneyInterchange`<br>Alternativ für Flügelzug, Vereinigung: <br>JourneyParts, JourneyPartsCouple<br> | Durchbindung, Flügelzug, Vereinigung       |



**TODO** details from  Powerpoint to be included
## General transfer time between modes


```xml
<?xml version="1.0" encoding="UTF-8"?>
<DefaultConnection  id="ch:1:DefaultConnection:9999999-1" version="1">
  <!-- General connection between two modes in the whole network, when not StopPlaceRef is mentioned. Most exist for each mode pair. -->
  <TransferDuration>
    <DefaultDuration>PT2M</DefaultDuration>
  </TransferDuration>
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




## Transfer times at a given StopPlace
**TODO** details from  Powerpoint to be included



```xml
<?xml version="1.0" encoding="UTF-8"?>
<DefaultConnection  id="ch:1:DefaultConnection:8506302" version="1">
  <!-- Be aware only some combinations areallowed  mode - mode, operator/type of product category - operator/type of  product category. -->
  <TransferDuration>
    <!-- We use WalkTransferDuration sometimes. need to clarify **TODO** -->
    <DefaultDuration>PT3M</DefaultDuration>
  </TransferDuration>
  <StopPlaceRef ref="ch:2:StopPlace:8506302" version="1"/>
</DefaultConnection>

```




## Operator related transfer times
**TODO** details from  Powerpoint to be included



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
  <TransferDuration>
    <!-- We use WalkTransferDuration sometimes. need to clarify **TODO** -->
    <DefaultDuration>PT2M</DefaultDuration>
  </TransferDuration>
  <BothWays>false</BothWays>
  <!-- **TODO** to use or not -->
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




## Line and Direction-oriented transfer times
**TODO** details from  Powerpoint to be included



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




## ServiceJourney related transfer times
**TODO** details from  Powerpoint to be included

Connection between two services. 

The following situations exist: 
- I.	The connection should not take place. (Prohibition) 
- II.	The connection must take place, and the traveller must change ve-hicles
- III.	The connection has to take place, and the passenger can stay in the vehicle

The differences between the various situations are to be differentiated with the value in some attributes.
**TODO** copy stuff from 10.2



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




## Transfer times between StopPlaces
**TODO** details from  Powerpoint to be included

The differences between the various situations are to be differentiated with the value in some attributes.



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


