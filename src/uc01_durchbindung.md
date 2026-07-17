## ServiceJourneyInterchange
**Durchbindung, splitting and joining**

A "Durchbindung" (through-service) describes a planned operational connection between two `ServiceJourney`s where the same physical vehicle continues under a new service identity — typically with a new line, operator, or train number. 
From the passenger's perspective, no vehicle change is required (`StaySeated=true`).

This use case also covers splitting (Flügelzug) and joining (Vereinigung) of trains.  Be aware that in this case `ChangeWithinVehicle` might be necessary and we discuss it in [use case 2](uc02_joining_splitting.md).

All three cases are modeled using `ServiceJourneyInterchange` in NeTEx RG 2.0, 
replacing the deprecated `JourneyMeeting` and `InterchangeRule` from RG 1.0.  

  
**Situation**
>The feeder train IR 17 (Thurbo/SBB, line 91014I) arrives at Weinfelden platform 3, where it continues as regional train R 80 (line 91030L) towards Wil SG or Winterthur. The passenger remains seated (StaySeated=true) — this is a through-service where the train changes its line identity at Weinfelden without the passenger needing to change vehicles. Maximum wait time is 9 minutes (PT9M).
		
**Situation according to Realisation Guide 1.0**
```xml
<JourneyMeeting id="ch:1:JourneyMeeting:91014I-THU-17-1-5100_91030L-THU-80-1-7200_1642236775_1642209284_6660_7200" version="1">
  <validityConditions>
    <AvailabilityConditionRef ref="ch:1:AvailabilityCondition:2K" versionRef="any" />
  </validityConditions>
  <AtStopPointRef ref="ch:1:ScheduledStopPoint:8506105:3" versionRef="any" />
  <FromJourneyRef ref="ch:1:ServiceJourney:ch:1:sjyid:100046:30467-003_91014I.j26_17" version="1" />
  <ToJourneyRef ref="ch:1:ServiceJourney:ch:1:sjyid:100046:13602-002_91030L.j26_80" version="1" />
  <Description>LineChange</Description>
  <EarliestTime>01:51:00</EarliestTime>
  <LatestTime>02:00:00</LatestTime>
</JourneyMeeting>
```

**Situation with Realisation Guide 2.0**
```xml
<ServiceJourneyInterchange version="1" id="ch:1:ServiceJourneyInterchange:91014I-THU-17-1-5100_91030L-THU-80-1-7200">
	<validityConditions>
    	<AvailabilityConditionRef ref="ch:1:AvailabilityCondition:2K" version="1"/>
  	</validityConditions>
  	<Description lang="de">LineChange</Description>
	<StaySeated>true</StaySeated>
  	<CrossBorder>false</CrossBorder>
	<MaximumWaitTime>PT9M</MaximumWaitTime>
	<FromPointRef ref="ch:1:ScheduledStopPoint:8506105:3" version="1" nameOfClass="ScheduledStopPoint"/>
  	<ToPointRef ref="ch:1:ScheduledStopPoint:8506105:3" version="1" nameOfClass="ScheduledStopPoint"/>
	<FromServiceJourneyRef ref="ch:1:ServiceJourney:ch:1:sjyid:100046:30467-003_91014I.j26_17" version="1"/>
	<ToServiceJourneyRef ref="ch:1:ServiceJourney:ch:1:sjyid:100046:13602-002_91030L.j26_80" version="1"/>
</ServiceJourneyInterchange>
```
The detailed handling is described for the element [ServiceJourneyInterchange](09_timetable.md#servicejourneyinterchange).
