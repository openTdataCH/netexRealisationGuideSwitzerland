 ServiceJourneyInterchanges and JourneyMeetings

## ServiceJourneyInterchange
**Durchbindung, splitting and joining**

A "Durchbindung" (through-service) describes a planned operational connection between two `ServiceJourney`s where the same physical vehicle continues under a new service identity — typically with a new line, operator, or train number. 
From the passenger's perspective, no vehicle change is required (`StaySeated=true`).

This use case also covers splitting (Flügelzug) and joining (Vereinigung) of trains. 
All three cases are modelled using `ServiceJourneyInterchange` in NeTEx RG 2.0, 
replacing the deprecated `JourneyMeeting` from RG 1.0.
		
Situation with Realisation Guide 1.0
```
            <JourneyMeeting id="ch:1:JourneyMeeting:91014I-THU-17-1-5100_91030L-THU-80-1-7200_1642236775_1642209284_6660_7200" version="any">
              <validityConditions>
                <AvailabilityConditionRef ref="ch:1:AvailabilityCondition:2K" versionRef="any" />
              </validityConditions>
              <AtStopPointRef ref="ch:1:ScheduledStopPoint:8506105:3" versionRef="any" />
              <FromJourneyRef ref="ch:1:ServiceJourney:ch:1:sjyid:100046:30467-003_91014I.j26_17" version="any" />
              <ToJourneyRef ref="ch:1:ServiceJourney:ch:1:sjyid:100046:13602-002_91030L.j26_80" version="any" />
              <Description>LineChange</Description>
              <EarliestTime>01:51:00</EarliestTime>
              <LatestTime>02:00:00</LatestTime>
            </JourneyMeeting>
```

situation with Realisation Guide 2.0
```
			<ServiceJourneyInterchange version="2.0" id="ch:1:ServiceJourneyInterchange:91014I-THU-17-1-5100_91030L-THU-80-1-7200">
				<validityConditions>
					<AvailabilityConditionRef ref="ch:1:AvailabilityCondition:2K" versionRef="any"/>
				</validityConditions>
				<Description>LineChange</Description>
				<InterchangeLocationRef ref="ch:1:ScheduledStopPoint:8506105:3" versionRef="any"/>
				<FeederRef>
					<ServiceJourneyRef ref="ch:1:ServiceJourney:ch:1:sjyid:100046:30467-003_91014I.j26_17" version="any"/>
				</FeederRef>
				<DistributorRef>
					<ServiceJourneyRef ref="ch:1:ServiceJourney:ch:1:sjyid:100046:13602-002_91030L.j26_80" version="any"/>
				</DistributorRef>
				<MaximumWaitTime>PT9M</MaximumWaitTime>
				<StaySeated>true</StaySeated>
				<CrossBorder>false</CrossBorder>
			</ServiceJourneyInterchange>
```

