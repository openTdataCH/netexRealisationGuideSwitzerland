# Timetables
In this chapter:
- [TimetableFrame](09_timetable.md#timetableframe)
- [ServiceJourney](09_timetable.md#servicejourney)
- [TemplateServiceJourney](09_timetable.md#templateservicejourney)
- [OccupancyView](09_timetable.md#occupancyview)
- [TrainNumber](09_timetable.md#trainnumber)
- [TypeOfService](#typeofservice)
- [TimetabledPassingTime](09_timetable.md#timetabledpassingtime)
- [ServiceJourneyInterchange](#servicejourneyinterchange)
- [InterchangeRule](09_timetable.md#interchangerule)

In Service: 
- [NoticeAssignment](07_service.md#noticeassignment)
- [ServiceFacilitySet](10_common.md#servicefacilityset)

In ServiceCalendar:
- [AvailabilityCondition](08_service_calendars.md#availabilitycondition)
- [Timeband](08_service_calendars.md#timeband)



## TimetableFrame
*→ [Glossary definition](A4_annex_glossary.md#timetableframe)*

### Purpose

A `TimetableFrame` contains the operational journey definitions — the actual trips that run on the network. It groups `ServiceJourney`s, `TemplateServiceJourney`s, and `ServiceJourneyInterchange` that together describe the timetabled service offering.

### Contained Elements
- `vehicleJourneys`– collection of journey types:
  -  `ServiceJourney`- describes an individual timetabled journey
  -  `TemplateServiceJourney`- describes a set of journeys repeating at a certain frequency
  -  The Swiss profile only models journeys that are available to the passengers
- `TrainNumber`- each `ServiceJourney` and `TemplateServiceJourney` is mapped one-to-one to exactly one train number
- Each `ServiceJourney`/`TemplateServiceJourney` in the `TimetableFrame` carries a `TimeDemandTypeRef` element pointing to exactly one `TimeDemandType`. The referenced `TimeDemandType` object itself — together with the `TimingLink`s it builds on — is defined in the `ServiceFrame`, not in the `TimetableFrame`. 
  It holds the `RunTime`s (`JourneyRunTime`, per `TimingLink`) and `WaitTime`s (`JourneyWaitTime`, per stop) that together replace the deprecated `passingTimes`/`TimetabledPassingTime` mechanism (see below).
- `journeyInterchanges` – collection of ServiceJourneyInterchanges describing planned connections and through-services between journeys
- `NoticeAssignment`s- link `Notice`s to specific journeys or stop points within journeys
- `ServiceFacilitySet`s- describe the various services and facilities offered by the vehicles of a journey


### Table



*Table: TimetableFrame*

| Sub | Element | Usage | Card | Type | Description | Note |
|-----|---------|-------|------|------|-------------|------|
|  | @id | mandatory | 1..1 | xsd:string | Attribute id | |
|  | @version | mandatory | 1..1 | xsd:string | Attribute version | |
|  | vehicleJourneys | expected | 0..1 | journeysInFrame_RelStructure | A coherent set of timetable data (VEHICLE JOURNEYs and BLOCKs) to which the same VALIDITY CONDITIONs have been assigned. | Contains the ServiceJourneys and TemplateServiceJourneys. |
| + | [ServiceJourney](./tables/ServiceJourney.md) | expected | 0..* | unknown | A coherent set of timetable data (VEHICLE JOURNEYs and BLOCKs) to which the same VALIDITY CONDITIONs have been assigned. | ServiceJourney is used for common Journeys. |
| + | [TemplateServiceJourney](./tables/TemplateServiceJourney.md) | expected | 0..* | unknown | A coherent set of timetable data (VEHICLE JOURNEYs and BLOCKs) to which the same VALIDITY CONDITIONs have been assigned. | TemplateServiceJourney is only to be used if a line is serviced at a certain frequency. |
|  | trainNumbers | expected | 0..1 | trainNumbersInFrame_RelStructure | A coherent set of timetable data (VEHICLE JOURNEYs and BLOCKs) to which the same VALIDITY CONDITIONs have been assigned. |  |
| + | [TrainNumber](./tables/TrainNumber.md) | mandatory | 0..* | unknown | A coherent set of timetable data (VEHICLE JOURNEYs and BLOCKs) to which the same VALIDITY CONDITIONs have been assigned. |  |
|  | serviceFacilitySets | optional | 0..1 | serviceFacilitySetsInFrame_RelStructure | A coherent set of timetable data (VEHICLE JOURNEYs and BLOCKs) to which the same VALIDITY CONDITIONs have been assigned. |  |
| + | [ServiceFacilitySet](./tables/ServiceFacilitySet.md) | expected | 0..* | unknown | A coherent set of timetable data (VEHICLE JOURNEYs and BLOCKs) to which the same VALIDITY CONDITIONs have been assigned. |  |
|  | typesOfService | expected | 0..1 | typesOfServiceInFrame_RelStructure | A coherent set of timetable data (VEHICLE JOURNEYs and BLOCKs) to which the same VALIDITY CONDITIONs have been assigned. |  |
| + | TypeOfService | optional | 0..* | unknown | A coherent set of timetable data (VEHICLE JOURNEYs and BLOCKs) to which the same VALIDITY CONDITIONs have been assigned. | This is exactly how the TypeOfService should be defined for Switzerland. Attention: Only once per file. |
| ++ | Name | expected | 0..1 | MultilingualString | A coherent set of timetable data (VEHICLE JOURNEYs and BLOCKs) to which the same VALIDITY CONDITIONs have been assigned. |  |
| +++ | @lang | mandatory | 1..1 | xsd:string | Attribute lang | |
| ++ | ShortName | expected | 0..1 | MultilingualString | A coherent set of timetable data (VEHICLE JOURNEYs and BLOCKs) to which the same VALIDITY CONDITIONs have been assigned. |  |
| +++ | @lang | mandatory | 1..1 | xsd:string | Attribute lang | |
| ++ | PrivateCode | optional | 1..1 | PrivateCodeStructure | A coherent set of timetable data (VEHICLE JOURNEYs and BLOCKs) to which the same VALIDITY CONDITIONs have been assigned. |  |
| + | [ServiceJourneyInterchange](./tables/ServiceJourneyInterchange.md) | expected | 1..1 | unknown | A coherent set of timetable data (VEHICLE JOURNEYs and BLOCKs) to which the same VALIDITY CONDITIONs have been assigned. | For modeling many forms of interchanges |
|  | vehicleTypes | optional | 0..1 | transportTypeRefs_RelStructure | A coherent set of timetable data (VEHICLE JOURNEYs and BLOCKs) to which the same VALIDITY CONDITIONs have been assigned. | We will use this place to store Train and CompoundTrain information, when we will do formation. Not detailed at the moment |
| + | CompoundTrain | optional | 0..* | unknown | A coherent set of timetable data (VEHICLE JOURNEYs and BLOCKs) to which the same VALIDITY CONDITIONs have been assigned. |  |




*→ [General NeTEx definition ](../xcore/netex/elements/TimetableFrame.html)*

### Example


```xml
<?xml version="1.0" encoding="UTF-8"?>
<TimetableFrame id="ch:1:TimetableFrame:j23" version="1">
  <vehicleJourneys>
  <!-- Contains the ServiceJourneys and TemplateServiceJourneys. -->
  <ServiceJourney id="generatedOrsjyid" version="1">
  <!-- ServiceJourney is used for common Journeys. -->
  </ServiceJourney>
  <TemplateServiceJourney id="generatedOrsjyid1" version="1">
  <!-- TemplateServiceJourney is only to be used if a line is serviced at a certain frequency. -->
  </TemplateServiceJourney>
  <TemplateServiceJourney id="generated2" version="1"/>
  </vehicleJourneys>
  <trainNumbers>
  <TrainNumber id="2123" version="1"/>
  </trainNumbers>
  <serviceFacilitySets>
  <ServiceFacilitySet id="86558" version="1"/>
  </serviceFacilitySets>
  <typesOfService>
  <TypeOfService id="ch:1:TypeOfService:1" version="1">
  <!-- This is exactly how the TypeOfService should be defined for Switzerland. Attention: Only once per file. -->
  <Name lang="en">PublicJourney</Name>
  <ShortName lang="en">PJ</ShortName>
  <PrivateCode>1</PrivateCode>
  </TypeOfService>
  </typesOfService>
  <journeyInterchanges>
  <!-- In NETWORK_OFFER for splitting and joining. Otherwise mostly in INTERCHANGE -->
  <ServiceJourneyInterchange id="ch:1:sji:generated-1" version="1">
  <!-- For modeling many forms of interchanges -->
  <FromJourneyRef ref="sjyid-1" version="1"/>
  <ToJourneyRef ref="sjyid-2" version="1"/>
  </ServiceJourneyInterchange>
  </journeyInterchanges>
  <vehicleTypes>
  <!-- We will use this place to store Train and CompoundTrain information, when we will do formation. Not detailed at the moment -->
  <CompoundTrain id="generated" version="1"/>
  <Train id="generated" version="1"/>
  </vehicleTypes>
</TimetableFrame>
```



*→ [Template](./templates/TimetableFrame.xml)*

### Frame Relationships
`TimetableFrame` depends on `ServiceFrame` for `JourneyPattern`s, `Line`s, `TimeDemandType`s and `TimingLink`s referenced by `ServiceJourney`s. It depends on `ResourceFrame` for `Operator` definitions. `TimetableFrame` is typically wrapped in a `CompositeFrame` within a `PublicationDelivery`.

## ServiceJourney
*→ [Glossary definition](A4_annex_glossary.md#servicejourney)*

### Purpose
A `ServiceJourney` represents a planned trip in the timetable operating on a recurring schedule. It defines the stop sequence via reference to a `JourneyPattern`, includes scheduled timing via `TimeDemandTypeRef`, and specifies operational details such as operator. Its operating days are controlled via
`AvailabilityConditionRef` (`ValidDayBits`), not via `DayType` — see [AvailabilityCondition](08_service_calendars.md#availabilitycondition). `DatedServiceJourney` is **not used** in the Swiss profile.

### Table



*Table: ServiceJourney*

| Sub | Element | Usage | Card | Type | Description | Note |
|-----|---------|-------|------|------|-------------|------|
|  | @id | mandatory | 1..1 | xsd:string | Attribute id | |
|  | @version | mandatory | 1..1 | xsd:string | Attribute version | |
|  | @responsibilitySetRef | mandatory | 1..1 | xsd:string | Attribute responsibilitySetRef | |
|  | validityConditions | mandatory | 1..1 | validityConditions_RelStructure | A coherent set of timetable data (VEHICLE JOURNEYs and BLOCKs) to which the same VALIDITY CONDITIONs have been assigned. | Used to specify a set of temporal conditions that can be associated with the ServiceJourney, for example that the corresponding journey only applies on particular days of a period (indicated by ValidDayBits, “Verkehrstagebitfeld”). |
| + | AvailabilityConditionRef | mandatory | 0..* | AvailabilityConditionRefStructure | A coherent set of timetable data (VEHICLE JOURNEYs and BLOCKs) to which the same VALIDITY CONDITIONs have been assigned. | Only a single AvailabilityConditionRef is allowed. |
|  | keyList | optional | 1..1 | KeyListStructure | A coherent set of timetable data (VEHICLE JOURNEYs and BLOCKs) to which the same VALIDITY CONDITIONs have been assigned. | KEY LIST with the KEY VALUEs belonging to the SERVICE JOURNEY. We don't use it for sjyid! |
| + | KeyValue | optional | 1..* | KeyValueStructure | A coherent set of timetable data (VEHICLE JOURNEYs and BLOCKs) to which the same VALIDITY CONDITIONs have been assigned. | We use it for tariff codes and region codes PAG mostly. |
| ++ | Key | optional | 1..1 | xsd:normalizedString | A coherent set of timetable data (VEHICLE JOURNEYs and BLOCKs) to which the same VALIDITY CONDITIONs have been assigned. |  |
| ++ | Value | optional | 0..1 | xsd:anyType | A coherent set of timetable data (VEHICLE JOURNEYs and BLOCKs) to which the same VALIDITY CONDITIONs have been assigned. |  |
|  | privateCodes | expected | 1..1 | PrivateCodesStructure | A coherent set of timetable data (VEHICLE JOURNEYs and BLOCKs) to which the same VALIDITY CONDITIONs have been assigned. |  |
| + | PrivateCode | expected | 0..* | PrivateCodeStructure | A coherent set of timetable data (VEHICLE JOURNEYs and BLOCKs) to which the same VALIDITY CONDITIONs have been assigned. | The following types are possible: sjyid and rn. rn is the type used for the Postauto region. |
| ++ | @type | mandatory | 1..1 | xsd:string | Attribute type | |
|  | TransportMode | optional | 0..1 | AllModesEnumeration | A coherent set of timetable data (VEHICLE JOURNEYs and BLOCKs) to which the same VALIDITY CONDITIONs have been assigned. |  |
|  | TypeOfProductCategoryRef | mandatory | 1..1 | TypeOfProductCategoryRefStructure | A coherent set of timetable data (VEHICLE JOURNEYs and BLOCKs) to which the same VALIDITY CONDITIONs have been assigned. | Relevant elements are defined in the mapping excel. |
|  | TypeOfServiceRef | optional | 1..1 | TypeOfServiceRefStructure | A coherent set of timetable data (VEHICLE JOURNEYs and BLOCKs) to which the same VALIDITY CONDITIONs have been assigned. | Should always be ch:1:TypeOfService:1 |
|  | noticeAssignments | optional | 0..1 | noticeAssignments_RelStructure | A coherent set of timetable data (VEHICLE JOURNEYs and BLOCKs) to which the same VALIDITY CONDITIONs have been assigned. | The complete set of all applicable Notices. Attention: Notices may be restricted to a a part of the journey (by defining the first and last stop). |
| + | [NoticeAssignment](./tables/NoticeAssignment.md) | optional | 0..* | unknown | A coherent set of timetable data (VEHICLE JOURNEYs and BLOCKs) to which the same VALIDITY CONDITIONs have been assigned. |  |
|  | occupancies | optional | 0..1 | OccupancyView_RelStructure | A coherent set of timetable data (VEHICLE JOURNEYs and BLOCKs) to which the same VALIDITY CONDITIONs have been assigned. |  |
| + | [OccupancyView](./tables/OccupancyView.md) | optional | 0..* | OccupancyView_VersionStructure | A coherent set of timetable data (VEHICLE JOURNEYs and BLOCKs) to which the same VALIDITY CONDITIONs have been assigned. | Currently not available |
|  | ServiceAlteration | mandatory | 0..1 | ServiceAlterationEnumeration | A coherent set of timetable data (VEHICLE JOURNEYs and BLOCKs) to which the same VALIDITY CONDITIONs have been assigned. | Only the value planned is allowed. We might add the others, like cancelled, later. |
|  | DepartureTime | expected | 0..1 | xsd:time | A coherent set of timetable data (VEHICLE JOURNEYs and BLOCKs) to which the same VALIDITY CONDITIONs have been assigned. |  |
|  | DepartureDayOffset | optional | 0..1 | DayOffsetType | A coherent set of timetable data (VEHICLE JOURNEYs and BLOCKs) to which the same VALIDITY CONDITIONs have been assigned. | 0 for current operating day. Could also be negative. |
|  | JourneyPatternRef | mandatory | 1..1 | JourneyPatternRefStructure | A coherent set of timetable data (VEHICLE JOURNEYs and BLOCKs) to which the same VALIDITY CONDITIONs have been assigned. | The reference to the ServiceJourneyPattern. |
| + | @nameOfRefClass | mandatory | 1..1 | xsd:string | Attribute nameOfRefClass | |
|  | TimeDemandTypeRef | mandatory | 0..1 | TimeDemandTypeRefStructure | A coherent set of timetable data (VEHICLE JOURNEYs and BLOCKs) to which the same VALIDITY CONDITIONs have been assigned. | The timing behaviour is defined here. We allow only one TimeDemandType per ServiceJourney. |
|  | VehicleTypeRef | expected | 1..1 | VehicleTypeRefStructure | A coherent set of timetable data (VEHICLE JOURNEYs and BLOCKs) to which the same VALIDITY CONDITIONs have been assigned. | Mostly used for accessibility information like NF. Relevant definitions in the mapping excel. |
|  | LineRef | mandatory | 1..1 | LineRefStructure | A coherent set of timetable data (VEHICLE JOURNEYs and BLOCKs) to which the same VALIDITY CONDITIONs have been assigned. |  |
|  | DirectionType | mandatory | 0..1 | RelativeDirectionEnumeration | A coherent set of timetable data (VEHICLE JOURNEYs and BLOCKs) to which the same VALIDITY CONDITIONs have been assigned. | Allowed are: inbound, outbound |
|  | trainNumbers | mandatory | 0..1 | trainNumbersInFrame_RelStructure | A coherent set of timetable data (VEHICLE JOURNEYs and BLOCKs) to which the same VALIDITY CONDITIONs have been assigned. |  |
| + | TrainNumberRef | mandatory | 0..* | TrainNumberRefStructure | A coherent set of timetable data (VEHICLE JOURNEYs and BLOCKs) to which the same VALIDITY CONDITIONs have been assigned. |  |
|  | [Destination](./tables/Destination.md) | expected | 0..1 | TravelSpecificationSummaryEndpointStructure | A coherent set of timetable data (VEHICLE JOURNEYs and BLOCKs) to which the same VALIDITY CONDITIONs have been assigned. |  |
|  | parts | optional | 0..1 | blockParts_RelStructure | A coherent set of timetable data (VEHICLE JOURNEYs and BLOCKs) to which the same VALIDITY CONDITIONs have been assigned. | For some use cases e.g. change of Facilities during ServiceJourney |
| + | JourneyPartRef | expected | 0..* | JourneyPartRefStructure | A coherent set of timetable data (VEHICLE JOURNEYs and BLOCKs) to which the same VALIDITY CONDITIONs have been assigned. |  |
|  | checkConstraints | optional | 0..1 | checkConstraints_RelStructure | A coherent set of timetable data (VEHICLE JOURNEYs and BLOCKs) to which the same VALIDITY CONDITIONs have been assigned. |  |
| + | CheckConstraint | optional | 0..* | unknown | A coherent set of timetable data (VEHICLE JOURNEYs and BLOCKs) to which the same VALIDITY CONDITIONs have been assigned. | CheckConstraints are used for different use cases |




*→ [General NeTEx definition ](../xcore/netex/elements/ServiceJourney.html)*

### Example


```xml
<?xml version="1.0" encoding="UTF-8"?>
<ServiceJourney id="generated" version="1">
  <validityConditions>
  <!-- Used to specify a set of temporal conditions that can be associated with the ServiceJourney, for example that the corresponding journey only applies on particular days of a period (indicated by ValidDayBits, “Verkehrstagebitfeld”). -->
  <AvailabilityConditionRef ref="generated" version="1">
  <!-- Only a single AvailabilityConditionRef is allowed. -->
  </AvailabilityConditionRef>
  </validityConditions>
  <keyList>
  <!-- KEY LIST with the KEY VALUEs belonging to the SERVICE JOURNEY. We don't use it for sjyid! -->
  <KeyValue>
  <!-- We use it for tariff codes and region codes PAG mostly. -->
  <Key>RN</Key>
  <Value>1203</Value>
  </KeyValue>
  <KeyValue>
  <Key>TC</Key>
  <Value>293912</Value>
  </KeyValue>
  </keyList>
  <privateCodes>
  <PrivateCode type="sjyid">ch:1:sjyid:100001:71707-003
  <!-- The following types are possible: sjyid and rn. rn is the type used for the Postauto region. -->
  </PrivateCode>
  <PrivateCode type="rn">12</PrivateCode>
  </privateCodes>
  <TransportMode>rail</TransportMode>
  <TypeOfProductCategoryRef ref="ch:1:TypeOfProductCategory:IR" version="1">
  <!-- Relevant elements are defined in the mapping excel. -->
  </TypeOfProductCategoryRef>
  <TypeOfServiceRef ref="ch:1:TypeOfService:1" version="1">
  <!-- Should always be ch:1:TypeOfService:1 -->
  </TypeOfServiceRef>
  <noticeAssignments>
  <!-- The complete set of all applicable Notices. Attention: Notices may be restricted to a a part of the journey (by defining the first and last stop). -->
  <NoticeAssignment id="ch:1:NoticeAssignment:ch_1_ServiceJourney_ch_1_sjyid_100001_71707-003_1_0" version="1">
  <validityConditions>
  <AvailabilityConditionRef ref="ch:1:AvailabilityCondition:c3" version="1"/>
  </validityConditions>
  <NoticeRef ref="ch:1:Notice:A___1" version="1"/>
  </NoticeAssignment>
  </noticeAssignments>
  <occupancies>
  <OccupancyView id="generated" version="1">
  <!-- Currently not available -->
  </OccupancyView>
  </occupancies>
  <ServiceAlteration>planned
  <!-- Only the value planned is allowed. We might add the others, like cancelled, later. -->
  </ServiceAlteration>
  <DepartureTime>06:21:00</DepartureTime>
  <DepartureDayOffset>0
  <!-- 0 for current operating day. Could also be negative. -->
  </DepartureDayOffset>
  <JourneyPatternRef ref="ch:1:ServiceJourneyPattern:1" nameOfRefClass="ServiceJourneyPattern" version="1">
  <!-- The reference to the ServiceJourneyPattern. -->
  </JourneyPatternRef>
  <TimeDemandTypeRef ref="generated" version="1">
  <!-- The timing behaviour is defined here. We allow only one TimeDemandType per ServiceJourney. -->
  </TimeDemandTypeRef>
  <VehicleTypeRef ref="ch:1:VehicleType:NF" version="1">
  <!-- Mostly used for accessibility information like NF. Relevant definitions in the mapping excel. -->
  </VehicleTypeRef>
  <LineRef ref="ch:2:Line:11.IR.90" version="1"/>
  <DirectionType>outbound
  <!-- Allowed are: inbound, outbound -->
  </DirectionType>
  <trainNumbers>
  <TrainNumberRef ref="ch:1:TrainNumber:71707" version="1"/>
  </trainNumbers>
  <Destination>
  <ScheduledStopPointRef ref="generated" version="1"/>
  <DestinationDisplayRef ref="generated" version="1"/>
  </Destination>
  <parts>
  <!-- For some use cases e.g. change of Facilities during ServiceJourney -->
  <JourneyPartRef ref="generated" version="1"/>
  </parts>
  <checkConstraints>
  <CheckConstraint id="" version="1">
  <!-- CheckConstraints are used for different use cases -->
  </CheckConstraint>
  </checkConstraints>
</ServiceJourney>
```



*→ [Template](./templates/ServiceJourney.xml)*


### Usage Notes

- **Template vs. Instance:** `ServiceJourney` directly carries its validity via `AvailabilityConditionRef`. `DatedServiceJourney` is not used in the Swiss profile.
- **Consistency:** A `ServiceJourney` must reference exactly one `JourneyPattern`. The pattern's stop sequence is authoritative.
- **Day Governance:** Operating days are controlled via `AvailabilityConditionRef` (`ValidDayBits`), not via `DayType`. `DayType`/`DayTypeAssignment` are reserved for flagging national holidays only (see [ServiceCalendarFrame](08_service_calendars.md#daytype)). `DatedServiceJourney` is not used in the Swiss profile.
- **Validation:** Ensure `JourneyPatternRef`, `LineRef`, and `OperatorRef` are consistent and reference existing objects.
- We assume that a Swiss Journey ID exists for almost every `ServiceJourney`. However, the  `@id` can't be set to `sjyid`, because for different days the `ServiceJourney` are different. Also problematic cases: some cableways, when the frequency group is not done right (we try to remove those cases), foreign journeys. In those cases the `@id` will contain a `_gen` substring, but it still starts with the sjyid, when it exists (e.g. `ch:1:sjyid:100011:12391293:_gen_:1231` or `DE:12319123123:_gen_14`).
- A `ServiceJourney`can be associated with exactly one `ServiceJourneyPattern` and `TimeDemandType`.
- `@id` needs to be kept stable between exports if possible. However, when new variants are used for different operating days, it changes.
- Tarif codes (`TC`) and region codes (`RN`) are put into a key/value pair (see example).


### Calculation of passing times at stops
The departure and arrival times of a `ServiceJourney` are determined by the `ServiceJourneyPattern` and the `TimeDemandType` referenced by the `ServiceJourney`.
Element `ServiceJourney/DepartureTime` contains the departure time at the first `ScheduledStopPoint` indicated by  `ServiceJourneyPattern/pointsInSequence/StopPointInJourneyPattern[1]`. The arrival time at all subsequent `ScheduledStopPoint`s is calculated by adding the run time between the previous `ScheduledStopPoint` and the current `ScheduledStopPoint` of the `ServiceJourneyPattern`. The correct run time is obtained by searching `TimeDemandType/runTimes/JourneyRunTime/Runtime` with the `TimingLink` corresponding to the previous and current `ScheduledStopPoint`. The `TimingLink` to be used is indicated by `ServiceJourneyPattern/pointsInSequence/StopPointInJourneyPattern/OnwardTimingLinkRef`.
The departure time at each `ScheduledStopPoint` is obtained by adding `TimeDemandType/waitTimes/JourneyWaitTime/Waitime` for the `ScheduledStopPoint`. Please observe that a `ScheduledStopPoint` may be visited more than once within a `ServiceJourneyPattern` and may have different waiting times at each visit. In this case, `TimeDemandType/waitTimes/StopPointInJourneyPatternRef` will be used to override `TimeDemandType/waitTimes/ScheduledStopPointRef`. 

## TemplateServiceJourney
*→ [Glossary definition](A4_annex_glossary.md#templateservicejourney)*
### Purpose
A `TemplateServiceJourney` represents a sequence of planned trips. It is similar to the `ServiceJourney`, but it is used if there is a frequency defined at which the trips are scheduled on an operating day. 

A frequency is specified in a `HeadwayJourneyGroup` (e.g. every 20 minutes). The `TemplateServiceJourney` may thus represent multiple journeys or it could be used simply as a template for adding extra date journeys after the planning phase. 

### Table



TemplateServiceJourney is used for journeys repeating at a certain frequency.

*Table: TemplateServiceJourney*

| Sub | Element | Usage | Card | Type | Description | Note |
|-----|---------|-------|------|------|-------------|------|
|  | @id | mandatory | 1..1 | xsd:string | Attribute id | |
|  | @version | mandatory | 1..1 | xsd:string | Attribute version | |
|  | @responsibilitySetRef | mandatory | 1..1 | xsd:string | Attribute responsibilitySetRef | |
|  | validityConditions | mandatory | 1..1 | validityConditions_RelStructure | A coherent set of timetable data (VEHICLE JOURNEYs and BLOCKs) to which the same VALIDITY CONDITIONs have been assigned. | Used to specify a set of temporal conditions that can be associated with the ServiceJourney, for example that the corresponding journey only applies on particular days of a period (indicated by ValidDayBits, “Verkehrstagebitfeld”). |
| + | AvailabilityConditionRef | mandatory | 0..* | AvailabilityConditionRefStructure | A coherent set of timetable data (VEHICLE JOURNEYs and BLOCKs) to which the same VALIDITY CONDITIONs have been assigned. | Only a single AvailabilityConditionRef is allowed. |
|  | keyList | optional | 1..1 | KeyListStructure | A coherent set of timetable data (VEHICLE JOURNEYs and BLOCKs) to which the same VALIDITY CONDITIONs have been assigned. | Key List values |
| + | KeyValue | optional | 1..* | KeyValueStructure | A coherent set of timetable data (VEHICLE JOURNEYs and BLOCKs) to which the same VALIDITY CONDITIONs have been assigned. | For special Key value pairs. We don't use it for SJYID any longer |
| ++ | Key | optional | 1..1 | xsd:normalizedString | A coherent set of timetable data (VEHICLE JOURNEYs and BLOCKs) to which the same VALIDITY CONDITIONs have been assigned. |  |
| ++ | Value | optional | 0..1 | xsd:anyType | A coherent set of timetable data (VEHICLE JOURNEYs and BLOCKs) to which the same VALIDITY CONDITIONs have been assigned. |  |
|  | privateCodes | expected | 1..1 | PrivateCodesStructure | A coherent set of timetable data (VEHICLE JOURNEYs and BLOCKs) to which the same VALIDITY CONDITIONs have been assigned. | Replaces the single PrivateCode. The following types are possible: sjyid and rn. rn is the type used for the Postauto region |
| + | PrivateCode | expected | 0..* | PrivateCodeStructure | A coherent set of timetable data (VEHICLE JOURNEYs and BLOCKs) to which the same VALIDITY CONDITIONs have been assigned. |  |
|  | TransportMode | optional | 0..1 | AllModesEnumeration | A coherent set of timetable data (VEHICLE JOURNEYs and BLOCKs) to which the same VALIDITY CONDITIONs have been assigned. |  |
|  | TypeOfProductCategoryRef | expected | 1..1 | TypeOfProductCategoryRefStructure | A coherent set of timetable data (VEHICLE JOURNEYs and BLOCKs) to which the same VALIDITY CONDITIONs have been assigned. |  |
|  | TypeOfServiceRef | optional | 1..1 | TypeOfServiceRefStructure | A coherent set of timetable data (VEHICLE JOURNEYs and BLOCKs) to which the same VALIDITY CONDITIONs have been assigned. |  |
|  | noticeAssignments | optional | 0..1 | noticeAssignments_RelStructure | A coherent set of timetable data (VEHICLE JOURNEYs and BLOCKs) to which the same VALIDITY CONDITIONs have been assigned. | The complete set of all applicable notices. Attention: Notices may be restricted to a given set of stops. |
| + | [NoticeAssignment](./tables/NoticeAssignment.md) | optional | 0..* | unknown | A coherent set of timetable data (VEHICLE JOURNEYs and BLOCKs) to which the same VALIDITY CONDITIONs have been assigned. |  |
|  | occupancies | optional | 0..1 | OccupancyView_RelStructure | A coherent set of timetable data (VEHICLE JOURNEYs and BLOCKs) to which the same VALIDITY CONDITIONs have been assigned. |  |
| + | [OccupancyView](./tables/OccupancyView.md) | optional | 0..* | OccupancyView_VersionStructure | A coherent set of timetable data (VEHICLE JOURNEYs and BLOCKs) to which the same VALIDITY CONDITIONs have been assigned. |  |
|  | ServiceAlteration | mandatory | 0..1 | ServiceAlterationEnumeration | A coherent set of timetable data (VEHICLE JOURNEYs and BLOCKs) to which the same VALIDITY CONDITIONs have been assigned. | Only the value planned is allowed. |
|  | DepartureTime | optional | 0..1 | xsd:time | A coherent set of timetable data (VEHICLE JOURNEYs and BLOCKs) to which the same VALIDITY CONDITIONs have been assigned. | Departure of the first journey. |
|  | DepartureDayOffset | optional | 0..1 | DayOffsetType | A coherent set of timetable data (VEHICLE JOURNEYs and BLOCKs) to which the same VALIDITY CONDITIONs have been assigned. | DayOffset if relevant. |
|  | JourneyPatternRef | mandatory | 1..1 | JourneyPatternRefStructure | A coherent set of timetable data (VEHICLE JOURNEYs and BLOCKs) to which the same VALIDITY CONDITIONs have been assigned. | The reference to the ServiceJourneyPattern |
| + | @nameOfRefClass | mandatory | 1..1 | xsd:string | Attribute nameOfRefClass | |
|  | TimeDemandTypeRef | mandatory | 0..1 | TimeDemandTypeRefStructure | A coherent set of timetable data (VEHICLE JOURNEYs and BLOCKs) to which the same VALIDITY CONDITIONs have been assigned. | The timing behaviour is defined here. We allow only one TimeDemandType per ServiceJourney. |
|  | VehicleTypeRef | expected | 1..1 | VehicleTypeRefStructure | A coherent set of timetable data (VEHICLE JOURNEYs and BLOCKs) to which the same VALIDITY CONDITIONs have been assigned. | Mostly used for accessibility information |
|  | LineRef | mandatory | 1..1 | LineRefStructure | A coherent set of timetable data (VEHICLE JOURNEYs and BLOCKs) to which the same VALIDITY CONDITIONs have been assigned. |  |
|  | DirectionType | optional | 0..1 | RelativeDirectionEnumeration | A coherent set of timetable data (VEHICLE JOURNEYs and BLOCKs) to which the same VALIDITY CONDITIONs have been assigned. | Allowed are: inbound, outbound |
|  | trainNumbers | mandatory | 0..1 | trainNumbersInFrame_RelStructure | A coherent set of timetable data (VEHICLE JOURNEYs and BLOCKs) to which the same VALIDITY CONDITIONs have been assigned. |  |
| + | TrainNumberRef | mandatory | 0..* | TrainNumberRefStructure | A coherent set of timetable data (VEHICLE JOURNEYs and BLOCKs) to which the same VALIDITY CONDITIONs have been assigned. |  |
|  | [Destination](./tables/Destination.md) | expected | 0..1 | TravelSpecificationSummaryEndpointStructure | A coherent set of timetable data (VEHICLE JOURNEYs and BLOCKs) to which the same VALIDITY CONDITIONs have been assigned. |  |
|  | parts | optional | 0..1 | blockParts_RelStructure | A coherent set of timetable data (VEHICLE JOURNEYs and BLOCKs) to which the same VALIDITY CONDITIONs have been assigned. | For some use cases e.g. change of Facilities during ServiceJourney |
| + | JourneyPartRef | expected | 0..* | JourneyPartRefStructure | A coherent set of timetable data (VEHICLE JOURNEYs and BLOCKs) to which the same VALIDITY CONDITIONs have been assigned. |  |
|  | TemplateVehicleJourneyType | expected | 0..1 | TemplateVehicleJourneyTypeEnumeration | A coherent set of timetable data (VEHICLE JOURNEYs and BLOCKs) to which the same VALIDITY CONDITIONs have been assigned. |  |
|  | frequencyGroups | mandatory | 0..1 | frequencyGroupsInFrame_RelStructure | A coherent set of timetable data (VEHICLE JOURNEYs and BLOCKs) to which the same VALIDITY CONDITIONs have been assigned. | We strictly map one frequency to the TemplateServiceJourney. |
| + | HeadwayJourneyGroup | mandatory | 0..* | unknown | A coherent set of timetable data (VEHICLE JOURNEYs and BLOCKs) to which the same VALIDITY CONDITIONs have been assigned. |  |
| ++ | ScheduledHeadwayInterval | mandatory | 0..1 | xsd:duration | A coherent set of timetable data (VEHICLE JOURNEYs and BLOCKs) to which the same VALIDITY CONDITIONs have been assigned. |  |
| ++ | HeadwayDisplay | optional | 0..1 | HeadwayUseEnumeration | A coherent set of timetable data (VEHICLE JOURNEYs and BLOCKs) to which the same VALIDITY CONDITIONs have been assigned. | Allowed values: displayPassingTimesOnly displayInsteadOfPassingTimes displayAsWellAsPassingTimes. We only export displayPassingTimesOnly. |




*→ [General NeTEx definition ](../xcore/netex/elements/TemplateServiceJourney.html)*

### Example


```xml
<?xml version="1.0" encoding="UTF-8"?>
<TemplateServiceJourney id="generated" version="1">
  <!-- TemplateServiceJourney is used for journeys repeating at a certain frequency. -->
  <validityConditions>
  <!-- Used to specify a set of temporal conditions that can be associated with the ServiceJourney, for example that the corresponding journey only applies on particular days of a period (indicated by ValidDayBits, “Verkehrstagebitfeld”). -->
  <AvailabilityConditionRef ref="generated" version="1">
  <!-- Only a single AvailabilityConditionRef is allowed. -->
  </AvailabilityConditionRef>
  </validityConditions>
  <keyList>
  <!-- Key List values -->
  <KeyValue>
  <!-- For special Key value pairs. We don't use it for SJYID any longer -->
  <Key>RN</Key>
  <Value>1001</Value>
  </KeyValue>
  </keyList>
  <privateCodes>
  <!-- Replaces the single PrivateCode. The following types are possible: sjyid and rn. rn is the type used for the Postauto region -->
  <PrivateCode type="sjyid">ch:1:sjyid:100001:71707-003</PrivateCode>
  <PrivateCode type="rn">12</PrivateCode>
  </privateCodes>
  <TransportMode>rail</TransportMode>
  <TypeOfProductCategoryRef ref="ch:1:TypeOfProductCategory:IR" version="1"/>
  <TypeOfServiceRef ref="ch:1:TypeOfService:1" version="1"/>
  <noticeAssignments>
  <!-- The complete set of all applicable notices. Attention: Notices may be restricted to a given set of stops. -->
  <NoticeAssignment id="ch:1:NoticeAssignment:ch_1_ServiceJourney_ch_1_sjyid_100001_71707-003_1_0" version="1">
  <validityConditions>
  <AvailabilityConditionRef ref="ch:1:AvailabilityCondition:c3" version="1"/>
  </validityConditions>
  <NoticeRef ref="ch:1:Notice:A___1" version="1"/>
  </NoticeAssignment>
  </noticeAssignments>
  <occupancies>
  <OccupancyView id="generated" version="1"/>
  </occupancies>
  <ServiceAlteration>planned
  <!-- Only the value planned is allowed. -->
  </ServiceAlteration>
  <DepartureTime>06:21:00
  <!-- Departure of the first journey. -->
  </DepartureTime>
  <DepartureDayOffset>0
  <!-- DayOffset if relevant. -->
  </DepartureDayOffset>
  <JourneyPatternRef ref="ch:1:ServiceJourneyPattern:1" nameOfRefClass="ServiceJourneyPattern" version="1">
  <!-- The reference to the ServiceJourneyPattern -->
  </JourneyPatternRef>
  <TimeDemandTypeRef ref="generated" version="1">
  <!-- The timing behaviour is defined here. We allow only one TimeDemandType per ServiceJourney. -->
  </TimeDemandTypeRef>
  <VehicleTypeRef ref="ch:1:VehicleType:NF" version="1">
  <!-- Mostly used for accessibility information -->
  </VehicleTypeRef>
  <LineRef ref="ch:2:Line:11.IR.90" version="1"/>
  <DirectionType>inbound
  <!-- Allowed are: inbound, outbound -->
  </DirectionType>
  <trainNumbers>
  <TrainNumberRef ref="ch:1:TrainNumber:71707" version="1"/>
  </trainNumbers>
  <Destination>
  <ScheduledStopPointRef ref="generated" version="1"/>
  <DestinationDisplayRef ref="generated" version="1"/>
  </Destination>
  <parts>
  <!-- For some use cases e.g. change of Facilities during ServiceJourney -->
  <JourneyPartRef ref="generated" version="1"/>
  </parts>
  <TemplateVehicleJourneyType>headway</TemplateVehicleJourneyType>
  <frequencyGroups>
  <!-- We strictly map one frequency to the TemplateServiceJourney. -->
  <HeadwayJourneyGroup version="1" id="ch:1:HeadwayJourneyGroup:432">
  <Name>Regular Interval service between 12am and 18:00 pm</Name>
  <Description>About every 20 minutes</Description>
  <FirstDepartureTime>12:00:00</FirstDepartureTime>
  <FirstDayOffset>0</FirstDayOffset>
  <LastDepartureTime>18:00:00</LastDepartureTime>
  <LastDayOffset>0</LastDayOffset>
  <ScheduledHeadwayInterval>PT20M</ScheduledHeadwayInterval>
  <HeadwayDisplay>DisplayInsteadOfPassingTimes
  <!-- Allowed values: displayPassingTimesOnly displayInsteadOfPassingTimes displayAsWellAsPassingTimes. We only export displayPassingTimesOnly. -->
  </HeadwayDisplay>
  </HeadwayJourneyGroup>
  </frequencyGroups>
</TemplateServiceJourney>
```



*→ [Template](./templates/TemplateServiceJourney.xml)*

### Usage Notes
- `HeadwayJourneyGroup` holds all the frequency-based information of the journey, as for example when the stops of the journey are serviced the first/last time and in what interval (or at which frequency, respectively). 
- Note that in addition to `HeadwayJourneyGroup`, standard NeTEx also features `RhythmicalJourneyGroup` to specifiy, e.g., departures at 15, 27 and 40 minutes past the hour - this is not used in the Swiss profile.
- For sjyid see information about [frequencies](uc14_frequencies.md) and also the remarks for the [`ServiceJourney`](#servicejourney).
- `@id` needs to be kept stable between exports.

## TimeDemandType
*→ [Glossary definition](A4_annex_glossary.md#timedemandtype)*

## TimingLink
*→ [Glossary definition](A4_annex_glossary.md#timinglink)*

## OccupancyView

### Purpose
`OccupancyView`can be used on the `Journey` and `JourneyPart` elements. Used for predicted and planned occupancies of vehicles.

### Table



*Table: OccupancyView*

| Sub | Element | Usage | Card | Type | Description | Note |
|-----|---------|-------|------|------|-------------|------|
|  | @id | mandatory | 1..1 | xsd:string | Attribute id | |
|  | @version | mandatory | 1..1 | xsd:string | Attribute version | |
|  | dayTypeRefs | optional | 0..1 | unknown | A coherent set of timetable data (VEHICLE JOURNEYs and BLOCKs) to which the same VALIDITY CONDITIONs have been assigned. |  |
| + | DayTypeRef | optional | 1..* | DayTypeRefStructure | A coherent set of timetable data (VEHICLE JOURNEYs and BLOCKs) to which the same VALIDITY CONDITIONs have been assigned. |  |
|  | dayTypes | expected | 0..1 | unknown | A coherent set of timetable data (VEHICLE JOURNEYs and BLOCKs) to which the same VALIDITY CONDITIONs have been assigned. |  |
| + | [DayType](./tables/DayType.md) | expected | 1..1 | unknown | A coherent set of timetable data (VEHICLE JOURNEYs and BLOCKs) to which the same VALIDITY CONDITIONs have been assigned. |  |
|  | FareClass | expected | 0..1 | FareClassEnumeration | A coherent set of timetable data (VEHICLE JOURNEYs and BLOCKs) to which the same VALIDITY CONDITIONs have been assigned. |  |
|  | OccupancyLevel | expected | 0..1 | OccupancyEnumeration | A coherent set of timetable data (VEHICLE JOURNEYs and BLOCKs) to which the same VALIDITY CONDITIONs have been assigned. | Niedrige Belegung: empty; mittlere Belegung: manySeatsAvailable; hohe Belegung: fewSeatsAvailable |
|  | GroupReservation | optional | 0..* | GroupReservationStructure | A coherent set of timetable data (VEHICLE JOURNEYs and BLOCKs) to which the same VALIDITY CONDITIONs have been assigned. |  |
| + | NameOfGroup | expected | 1..1 | MultilingualString | A coherent set of timetable data (VEHICLE JOURNEYs and BLOCKs) to which the same VALIDITY CONDITIONs have been assigned. |  |
| + | NumberOfReservedSeats | expected | 1..1 | NumberOfPassengers | A coherent set of timetable data (VEHICLE JOURNEYs and BLOCKs) to which the same VALIDITY CONDITIONs have been assigned. |  |




*→ [General NeTEx definition ](../xcore/netex/elements/OccupancyView.html)*

### Example


```xml
<?xml version="1.0" encoding="UTF-8"?>
<OccupancyView id="generated" version="1">
  <dayTypeRefs>
  <DayTypeRef ref="generated" version="1"/>
  </dayTypeRefs>
  <dayTypes>
  <DayType id="generated" version="1"/>
  </dayTypes>
  <FareClass>firstClass</FareClass>
  <OccupancyLevel>seatsAvailable
  <!-- Niedrige Belegung: empty; mittlere Belegung: manySeatsAvailable; hohe Belegung: fewSeatsAvailable -->
  </OccupancyLevel>
  <GroupReservation>
  <NameOfGroup lang="fr">Gymnase français de Bienne></NameOfGroup>
  <NumberOfReservedSeats>21</NumberOfReservedSeats>
  </GroupReservation>
</OccupancyView>
```



*→ [Template](./templates/OccupancyView.xml)*

### Usage Notes
- We currently don't use OccupancyView.

## TrainNumber
*→ [Glossary definition](A4_annex_glossary.md#trainnumber)*

### Purpose

Codes assigned to particular journeys (`ServiceJourney`, `TemplateServiceJourney`) when operated by trains. `ServiceJourney`s can in principle have multiple different `TrainNumber`s whereas a `JourneyPart` can only reference a single one — however, `JourneyPart` is **not used** for modelling train number changes in the Swiss profile; use two `ServiceJourney`s linked via `ServiceJourneyInterchange` instead (see [uc05 Journey Parts](uc05_journey_parts.md)).

### Table



The TrainNumber are currently a maximum of 6 digits long. TrainNumber for advertisment und production are identical. It is the number from *Z in HRDF. Must be unique per operating day in Switzerland.

*Table: TrainNumber*

| Sub | Element | Usage | Card | Type | Description | Note |
|-----|---------|-------|------|------|-------------|------|
|  | @id | mandatory | 1..1 | xsd:string | Attribute id | |
|  | @version | mandatory | 1..1 | xsd:string | Attribute version | |
|  | ForAdvertisement | expected | 0..1 | xsd:normalizedString | A coherent set of timetable data (VEHICLE JOURNEYs and BLOCKs) to which the same VALIDITY CONDITIONs have been assigned. | TrainNumber to use for advertisement to public. Use if different from ID. |
|  | ForProduction | optional | 0..1 | xsd:normalizedString | A coherent set of timetable data (VEHICLE JOURNEYs and BLOCKs) to which the same VALIDITY CONDITIONs have been assigned. | TrainNumber to use for production purposes, for instance towards technical systems that require an odd or even value according to safety regulations. Use iff different from ID. |




*→ [General NeTEx definition ](../xcore/netex/elements/TrainNumber.html)*

### Example


```xml
<?xml version="1.0" encoding="UTF-8"?>
<TrainNumber id="71707" version="1">
  <!-- The TrainNumber are currently a maximum of 6 digits long. TrainNumber for advertisment und production are identical. It is the number from *Z in HRDF. Must be unique per operating day in Switzerland. -->
  <ForAdvertisement>12311A
  <!-- TrainNumber to use for advertisement to public. Use if different from ID. -->
  </ForAdvertisement>
  <ForProduction>12311A
  <!-- TrainNumber to use for production purposes, for instance towards technical systems that require an odd or even value according to safety regulations. Use iff different from ID. -->
  </ForProduction>
</TrainNumber>
```



*→ [Template](./templates/TrainNumber.xml)*

### Usage Note
- `@id` needs to be kept stable between exports.

## TypeOfService

### Purpose

`TypeOfService` indicates the purpose of a `ServiceJourney`, for example, whether if it is a passenger transport or a garage run-in. We only use `ch:1:TypeOfService:1`

### Table



*Table: TypeOfService*

| Sub | Element | Usage | Card | Type | Description | Note |
|-----|---------|-------|------|------|-------------|------|
|  | Name | expected | 0..1 | MultilingualString | VALUE SETs and TYPE OF VALUEs in frame. |  |
| + | @lang | mandatory | 1..1 | xsd:string | Attribute lang | |
|  | ShortName | expected | 0..1 | MultilingualString | VALUE SETs and TYPE OF VALUEs in frame. |  |
| + | @lang | mandatory | 1..1 | xsd:string | Attribute lang | |
|  | PrivateCode | expected | 0..1 | PrivateCodeStructure | VALUE SETs and TYPE OF VALUEs in frame. |  |




*→ [General NeTEx definition](../xcore/netex/elements/TypeOfService.html)*

### Example


```xml
<?xml version="1.0" encoding="UTF-8"?>
<TypeOfService id="ch:1:TypeOfService:1" version="1">
  <Name lang="en">PublicJourney</Name>
  <ShortName lang="en">N</ShortName>
  <PrivateCode>1</PrivateCode>
</TypeOfService>
```



*→ - [Template](./templates/TypeOfService.xml)*

### Usage Notes
- `@id` needs to be kept stable between exports.

The following types are currently used:

| Name	             | Description                                                                                                                                               |
|-------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------|
| PublicJourney	    | A public passenger transport                                                                                                                              |
| ~~GarageRunOut~~	 | A garage run-out                                                                                                                                          |
| ~~GarageRunIn~~	  | A garage run-in                                                                                                                                           |
| ~~ThroughCoach~~  | 	A special type of public passenger transport that is used if a ServiceJourney is comprised of JourneyParts of other ServiceJourneys because of coupling. |

Actually there is only one allowed value that we use in the Swiss profile: Only the `PublicJourney` is to be exchanged.


## TimetabledPassingTime
> **Deprecated** - We don't use TimetabledPassingTime in RG2.0. We use TimeDemandType now.

## ServiceJourneyInterchange
*→ [Glossary definition](A4_annex_glossary.md#servicejourneyinterchange)*

### Purpose
The standard states: "In some cases, a SERVICE JOURNEY INTERCHANGE expresses an interchange between two SERVICE JOURNEYs specifically planned to be operated by the same physical vehicle. This concept is for instance used for circular lines and coupled journeys. This means that passenger information should be adapted
to the fact that the passenger should not change vehicle as the transfer is implicit. In this case it is also important that operation control staff is aware of the consequences to passengers if the operation is altered in such a way that two different vehicles are used for the two involved SERVICE JOURNEYs."

`StaySeated=true` should be used for through-services (Durchbindung) and joining (Vereinigung). While splitting (Flügelzug) technically involves different vehicle parts, the passenger does not leave the train — however, they may need to move to the correct coach. For splitting, `StaySeated=false` combined with
`ChangeWithinVehicle=true` is therefore the correct modelling. See [uc02 Joining and splitting](uc02_joining_splitting.md).

### Table




*Table: ServiceJourneyInterchange*

| Sub | Element | Usage | Card | Type | Description | Note |
|-----|---------|-------|------|------|-------------|------|
|  | @id | mandatory | 1..1 | xsd:string | Attribute id | |
|  | @version | mandatory | 1..1 | xsd:string | Attribute version | |
|  | validityConditions | expected | 1..1 | validityConditions_RelStructure | A coherent set of timetable data (VEHICLE JOURNEYs and BLOCKs) to which the same VALIDITY CONDITIONs have been assigned. |  |
| + | AvailabilityConditionRef | expected | 0..* | AvailabilityConditionRefStructure | A coherent set of timetable data (VEHICLE JOURNEYs and BLOCKs) to which the same VALIDITY CONDITIONs have been assigned. |  |
|  | Description | optional | 0..1 | MultilingualString |  |  |
|  | StaySeated | mandatory | 0..1 | xsd:boolean | A coherent set of timetable data (VEHICLE JOURNEYs and BLOCKs) to which the same VALIDITY CONDITIONs have been assigned. |  |
|  | CrossBorder | optional | 0..1 | xsd:boolean | A coherent set of timetable data (VEHICLE JOURNEYs and BLOCKs) to which the same VALIDITY CONDITIONs have been assigned. |  |
|  | ChangeWithinVehicle | optional | 0..1 | xsd:boolean | A coherent set of timetable data (VEHICLE JOURNEYs and BLOCKs) to which the same VALIDITY CONDITIONs have been assigned. | Set to true for train splitting (Flügelzug) when the passenger may have to move to a different coach. Default is false. |
|  | Planned | optional | 0..1 | xsd:boolean | A coherent set of timetable data (VEHICLE JOURNEYs and BLOCKs) to which the same VALIDITY CONDITIONs have been assigned. |  |
|  | Guaranteed | optional | 0..1 | xsd:boolean | A coherent set of timetable data (VEHICLE JOURNEYs and BLOCKs) to which the same VALIDITY CONDITIONs have been assigned. |  |
|  | MaximumWaitTime | optional | 0..1 | xsd:duration | A coherent set of timetable data (VEHICLE JOURNEYs and BLOCKs) to which the same VALIDITY CONDITIONs have been assigned. | If not set or PT0M, it is guaranteed. |
|  | FromPointRef | mandatory | 1..1 | VehicleMeetingPointRefStructure | A coherent set of timetable data (VEHICLE JOURNEYs and BLOCKs) to which the same VALIDITY CONDITIONs have been assigned. |  |
| + | @nameOfRefClass | mandatory | 1..1 | xsd:string | Attribute nameOfRefClass | |
|  | FromVisitNumber | optional | 0..1 | xsd:nonNegativeInteger | A coherent set of timetable data (VEHICLE JOURNEYs and BLOCKs) to which the same VALIDITY CONDITIONs have been assigned. |  |
|  | ToPointRef | mandatory | 1..1 | VehicleMeetingPointRefStructure | A coherent set of timetable data (VEHICLE JOURNEYs and BLOCKs) to which the same VALIDITY CONDITIONs have been assigned. |  |
| + | @nameOfRefClass | mandatory | 1..1 | xsd:string | Attribute nameOfRefClass | |
|  | FromServiceJourneyRef | mandatory | 1..1 | ServiceJourneyRefStructure | A coherent set of timetable data (VEHICLE JOURNEYs and BLOCKs) to which the same VALIDITY CONDITIONs have been assigned. |  |
|  | ToServiceJourneyRef | mandatory | 1..1 | ServiceJourneyRefStructure | A coherent set of timetable data (VEHICLE JOURNEYs and BLOCKs) to which the same VALIDITY CONDITIONs have been assigned. |  |




*→ [General NeTEx definition ](../xcore/netex/elements/ServiceJourneyInterchange.html)*

### Example


```xml
<?xml version="1.0" encoding="UTF-8"?>
<ServiceJourneyInterchange version="1" id="ch:1:ServiceJourneyInterchange:91014I-THU-17-1-5100_91030L-THU-80-1-7200">
  <validityConditions>
  <AvailabilityConditionRef ref="ch:1:AvailabilityCondition:2K" version="1"/>
  </validityConditions>
  <Description>LineChange</Description>
  <StaySeated>true</StaySeated>
  <CrossBorder>false</CrossBorder>
  <ChangeWithinVehicle>false
  <!-- Set to true for train splitting (Flügelzug) when the passenger may have to move to a different coach. Default is false. -->
  </ChangeWithinVehicle>
  <Planned>true</Planned>
  <Guaranteed>false</Guaranteed>
  <MaximumWaitTime>PT9M
  <!-- If not set or PT0M, it is guaranteed. -->
  </MaximumWaitTime>
  <FromPointRef ref="ch:1:ScheduledStopPoint:8506105:3" nameOfRefClass="ScheduledStopPoint" version="1"/>
  <FromVisitNumber>1</FromVisitNumber>
  <ToPointRef ref="ch:1:ScheduledStopPoint:8506105:3" nameOfRefClass="ScheduledStopPoint" version="1"/>
  <FromServiceJourneyRef ref="ch:1:ServiceJourney:ch:1:sjyid:100046:30467-003_91014I.j26_17" version="1"/>
  <ToServiceJourneyRef ref="ch:1:ServiceJourney:ch:1:sjyid:100046:13602-002_91030L.j26_80" version="1"/>
</ServiceJourneyInterchange>
```



*→ [Template](./templates/ServiceJourneyInterchange.xml)*

### Usage Notes
- `ServiceJourneyInterchange` is placed in the `TimetableFrame` within the `journeyInterchanges` collection.
- `StaySeated=true` indicates that the passenger remains in the vehicle — typically used for through-services (Durchbindung) and joining (Vereinigung). See [uc01 Durchbindung](uc01_durchbindung.md).
- `StaySeated=false` indicates that the passenger must change vehicles. This covers guaranteed and non-guaranteed connections. See [uc03 Transfers](uc03_transfers.md).
- `Guaranteed=true` explicitly marks the connection as guaranteed. 
- `MaximumWaitTime` defines how long the distributor waits — if absent, no explicit wait time is defined.
- `CrossBorder=true` must be set if the interchange crosses a national border.
- `ChangeWithinVehicle=true` indicates that in case of train splitting, the passenger may have to move to a different part of the train. Default is `false`. See [uc02 Joining and splitting](uc02_joining_splitting.md)
- `FromPointRef` and `ToPointRef` reference the `ScheduledStopPoint` at which the interchange takes place. For a line change at the same stop, both refs point to the same `ScheduledStopPoint`.
- `FromServiceJourneyRef` references the feeder journey; `ToServiceJourneyRef` references the distributor journey. Note: the deprecated elements `FromJourneyRef` / `ToJourneyRef` from RG 1.0 (`JourneyMeeting`) must not be used.
- Element order must follow the XSD sequence: `StaySeated` → `CrossBorder` → `ChangeWithinVehicle` → `MaximumWaitTime` → `FromPointRef` / `ToPointRef` → `FromServiceJourneyRef` / `ToServiceJourneyRef`.
- Make sure not to generate identical `ServiceJourneyInterchange`s. Reuse them where possible.
- `@id` should be kept stable between exports.

## InterchangeRule
> **Deprecated** — `InterchangeRule` is replaced by `ServiceJourneyInterchange` in RG 2.0.  
> See [uc03 Transfers](uc03_transfers.md) for the current modelling approach.

*→ [Glossary definition](A4_annex_glossary.md#interchangerule)*

## AvailabilityCondition 
*→ [see ServiceCalendarFrame](./08_service_calendars.md#availabilitycondition)*

## Timeband 
*→ [see ServiceCalendarFrame](./08_service_calendars.md#timeband)*


## NoticeAssignment
*→ [see Common elements](./07_service.md#noticeassignment)*


## ServiceFacilitySet
*→ [see Common elements](./10_common.md#servicefacilityset)*

