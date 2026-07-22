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
|  | vehicleJourneys | expected | 0..1 | journeysInFrame_RelStructure | VEHICLE JOURNEYs in frame. | Contains the ServiceJourneys and TemplateServiceJourneys. |
| + | [ServiceJourney](./tables/ServiceJourney.md) | expected | 1..* | ServiceJourney | A passenger carrying VEHICLE JOURNEY for one specified DAY TYPE. The pattern of working is in principle defined by a SERVICE JOURNEY PATTERN. The VIEW includes derived ancillary data from referenced entities. | ServiceJourney is used for common Journeys. |
| + | [TemplateServiceJourney](./tables/TemplateServiceJourney.md) | expected | 1..* | TemplateServiceJourney | A VEHICLE JOURNEY with a set of frequencies that may be used to represent a set of similar journeys differing only by their time of departure. | TemplateServiceJourney is only to be used if a line is serviced at a certain frequency. |
|  | trainNumbers | expected | 0..1 | trainNumbersInFrame_RelStructure | TRAIN NUMBERs in frame. |  |
| + | [TrainNumber](./tables/TrainNumber.md) | mandatory | 1..* | TrainNumber | Specification of codes assigned to particular VEHICLE JOURNEYs when operated by TRAINs of COMPOUND TRAINs according to a functional purpose (passenger information, operation follow-up, etc). |  |
|  | serviceFacilitySets | optional | 0..1 | serviceFacilitySetsInFrame_RelStructure | SERVICE FACILITies in frame. |  |
| + | [ServiceFacilitySet](./tables/ServiceFacilitySet.md) | expected | 1..* | ServiceFacilitySet | Service FACILITY. Set of enumerated FACILITY values (Where available names are based on TPEG classifications, augmented with UIC etc.). |  |
|  | typesOfService | expected | 0..1 | typesOfServiceInFrame_RelStructure | TYPEs of SERVICE in frame. |  |
| + | TypeOfService | optional | 1..* | TypeOfService | Classification of a Service. | This is exactly how the TypeOfService should be defined for Switzerland. Attention: Only once per file. |
| ++ | Name | expected | 0..1 | MultilingualString | Name of Traveller |  |
| +++ | @lang | mandatory | 1..1 | xsd:string | Attribute lang | |
| ++ | ShortName | expected | 0..1 | MultilingualString | Short Name for service |  |
| +++ | @lang | mandatory | 1..1 | xsd:string | Attribute lang | |
| ++ | PrivateCode | optional | 1..1 | PrivateCodeStructure | A private code that uniquely identifies the element. May be used for inter-operating with other (legacy) systems. |  |
| + | [ServiceJourneyInterchange](./tables/ServiceJourneyInterchange.md) | expected | 1..1 | ServiceJourneyInterchange | The scheduled possibility for transfer of passengers between two SERVICE JOURNEYs at the same or different STOP POINTs. | For modeling many forms of interchanges |




*→ [General NeTEx definition ](../generated/netex-html/TimetableFrame.html)*

### Example


```xml
<?xml version="1.0" encoding="UTF-8"?>
<TimetableFrame  id="ch:1:TimetableFrame:j23" version="1">
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
|  | validityConditions | mandatory | 1..1 | validityConditions_RelStructure | VALIDITY CONDITIONs conditioning entity. | Used to specify a set of temporal conditions that can be associated with the ServiceJourney, for example that the corresponding journey only applies on particular days of a period (indicated by ValidDayBits, “Verkehrstagebitfeld”). |
| + | AvailabilityConditionRef | mandatory | 1..* | AvailabilityConditionRefStructure | Reference to an AVAILABILITY CONDITION. A VALIDITY CONDITION defined in terms of temporal attributes. | Only a single AvailabilityConditionRef is allowed. |
|  | keyList | expected | 1..1 | KeyListStructure | A list of alternative Key values for an element. | KEY LIST with the KEY VALUEs belonjing to the SERVICE JOURNEY. Will contain the SJYID. |
| + | KeyValue | mandatory | 1..* | KeyValueStructure | Key value pair for Entity. | A KeyValue pair with the Key SJYID must exist. The Value contains a valid Swiss Journey ID. |
| ++ | Key | mandatory | 1..1 | xsd:normalizedString | Identifier of value e.g. System. |  |
| ++ | Value | mandatory | 0..1 | xsd:anyType | Value associated with QUALITY STRUCTURE FACTOR. |  |
|  | privateCodes | expected | 1..1 | PrivateCodesStructure | A list of private codes that uniquely identifiy the element. May be used for inter-operating with other (legacy) systems. +v2.0 |  |
| + | PrivateCode | expected | 1..1 | PrivateCodeStructure | A private code that uniquely identifies the element. May be used for inter-operating with other (legacy) systems. | The following types are possible: sjyid and rn. rn is the type used for the Postauto region. |
| ++ | @type | mandatory | 1..1 | xsd:string | Attribute type | |
|  | TransportMode | optional | 0..1 | AllModesEnumeration | MODE. |  |
|  | TypeOfProductCategoryRef | mandatory | 1..1 | TypeOfProductCategoryRefStructure | Reference to a TYPE OF PRODUCT CATEGORY. Product of a JOURNEY. e.g. ICS, Thales etc See ERA B.4 7037 Characteristic description code. | Relevant elements are defined in the mapping excel. |
|  | TypeOfServiceRef | optional | 1..1 | TypeOfServiceRefStructure | Reference to a TYPE OF SERVICE. | Should always be ch:1:TypeOfService:1 |
|  | noticeAssignments | optional | 0..1 | noticeAssignments_RelStructure | NOTICEs relevant for the whole GROUP OF SINGLE JOURNEYs. | The complete set of all applicable Notices. Attention: Notices may be restricted to a a part of the journey (by defining the first and last stop). |
| + | [NoticeAssignment](./tables/NoticeAssignment.md) | optional | 1..* | NoticeAssignment | The assignment of a NOTICE showing an exception in a JOURNEY PATTERN, a COMMON SECTION, or a VEHICLE JOURNEY, possibly specifying at which POINT IN JOURNEY PATTERN the validity of the NOTICE starts and ends respectively. |  |
|  | occupancies | optional | 0..1 | OccupancyView_RelStructure | OCCUPANCYs associated with this journey. +v2.0 |  |
| + | [OccupancyView](./tables/OccupancyView.md) | optional | 1..* | OccupancyView_VersionStructure |  | Currently not available |
|  | ServiceAlteration | mandatory | 0..1 | ServiceAlterationEnumeration | Whether journey is as planned, a cancellation or an extra journey. Default is as Planned. | Only the value planned is allowed. We might add the others, like cancelled, later. |
|  | DepartureTime | expected | 0..1 | xsd:time | Departure time. |  |
|  | DepartureDayOffset | optional | 0..1 | DayOffsetType | Departure Time Day Offset. | 0 for current operating day. Could also be negative. |
|  | JourneyPatternRef | mandatory | 1..1 | JourneyPatternRefStructure | Reference to a JOURNEY PATTERN. | The reference to the ServiceJourneyPattern. |
| + | @nameOfRefClass | mandatory | 1..1 | xsd:string | Attribute nameOfRefClass | |
|  | TimeDemandTypeRef | mandatory | 0..1 | TimeDemandTypeRefStructure | Reference to a TIME DEMAND TYPE used at start of JOURNEY. | The timing behaviour is defined here. We allow only one TimeDemandType per ServiceJourney. |
|  | VehicleTypeRef | expected | 1..1 | VehicleTypeRefStructure | Reference to a VEHICLE TYPE. | Mostly used for accessibility information like NF. Relevant definitions in the mapping excel. |
|  | LineRef | mandatory | 1..1 | LineRefStructure | Reference to a LINE. |  |
|  | DirectionType | mandatory | 0..1 | RelativeDirectionEnumeration | For fares for DISTANCE MATRIXE LEMENTs, DIRECTION in which price applies. | Allowed are: inbound, outbound |
|  | trainNumbers | mandatory | 0..1 | trainNumbersInFrame_RelStructure | TRAIN NUMBERs in frame. |  |
| + | TrainNumberRef | mandatory | 1..* | TrainNumberRefStructure | Reference to a TRAIN NUMBER. |  |
|  | [Destination](./tables/Destination.md) | expected | 0..1 | TravelSpecificationSummaryEndpointStructure | Destination of Travel. Note that for a point-to-point TARIFF the origin is assigned with a DISTANCE MATRIX ELEMENT. |  |
|  | parts | optional | 0..1 | blockParts_RelStructure | BLOCK PARTs which make up COMPOUND BLOCK. | For some use cases e.g. change of Facilities during ServiceJourney |
| + | JourneyPartRef | expected | 1..* | JourneyPartRefStructure | Reference to a JOURNEY PART. |  |
|  | checkConstraints | optional | 0..1 | checkConstraints_RelStructure | CHECK CONSTRAINTs which apply to SERVICE JOURNEY, e.g. check in time, security time. These are advisory only and not for use in journey planning. |  |
| + | CheckConstraint | optional | 1..* | CheckConstraint | Characteristics of a SITE COMPONENT representing a process, such as check-in, security screening, ticket control or immigration, that may potentially incur a time penalty that should be allowed for when journey planning. Used to mark PATH LINKs to determine transit routes through interchanges. | CheckConstraints are used for different use cases |




*→ [General NeTEx definition ](../generated/netex-html/ServiceJourney.html)*

### Example


```xml
<?xml version="1.0" encoding="UTF-8"?>
<ServiceJourney  id="generated" version="1">
  <validityConditions>
    <!-- Used to specify a set of temporal conditions that can be associated with the ServiceJourney, for example that the corresponding journey only applies on particular days of a period (indicated by ValidDayBits, “Verkehrstagebitfeld”). -->
    <AvailabilityConditionRef ref="generated" version="1">
      <!-- Only a single AvailabilityConditionRef is allowed. -->
    </AvailabilityConditionRef>
  </validityConditions>
  <keyList>
    <!-- KEY LIST with the KEY VALUEs belonjing to the SERVICE JOURNEY. Will contain the SJYID. -->
    <KeyValue>
      <!-- A KeyValue pair with the Key SJYID must exist. The Value contains a valid Swiss Journey ID. -->
      <Key>SJYID</Key>
      <Value>ch:1:sjyid:100001:71707-003</Value>
    </KeyValue>
  </keyList>
  <privateCodes>
    <PrivateCode type="sjyid">ch:1:sjyid:100001:71707-003</PrivateCode>
    <!-- The following types are possible: sjyid and rn. rn is the type used for the Postauto region. -->
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
  <ServiceAlteration>planned</ServiceAlteration>
  <!-- Only the value planned is allowed. We might add the others, like cancelled, later. -->
  <DepartureTime>06:21:00</DepartureTime>
  <DepartureDayOffset>0</DepartureDayOffset>
  <!-- 0 for current operating day. Could also be negative. -->
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
  <DirectionType>outbound</DirectionType>
  <!-- Allowed are: inbound, outbound -->
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
- **Stop Times:** Each stop in the referenced `JourneyPattern` must have exactly one `TimetabledPassingTimes` entry with `ArrivalTime` and/or `DepartureTime`.
- **Day Governance:** Operating days are controlled via `AvailabilityConditionRef` (`ValidDayBits`), not via `DayType`. `DayType`/`DayTypeAssignment` are reserved for flagging national holidays only (see [ServiceCalendarFrame](08_service_calendars.md#daytype)). `DatedServiceJourney` is not used in the Swiss profile.
- **Validation:** Ensure `JourneyPatternRef`, `LineRef`, and `OperatorRef` are consistent and reference existing objects.
- We assume that a Swiss Journey ID exists for almost every `ServiceJourney`. In those cases the `id` is also set to the `sjyid`. Possible problematic cases: some cableways, when the frequency group is not done right (we try to remove those cases), foreign journeys. In those cases the `id` will contain a `_gen`
- substring.
- A `ServiceJourney`can be associated with exactly one `ServiceJourneyPattern` and `TimeDemandType`.
- id-attribute needs to be kept stable between exports.

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
|  | validityConditions | mandatory | 1..1 | validityConditions_RelStructure | VALIDITY CONDITIONs conditioning entity. | Used to specify a set of temporal conditions that can be associated with the ServiceJourney, for example that the corresponding journey only applies on particular days of a period (indicated by ValidDayBits, “Verkehrstagebitfeld”). |
| + | AvailabilityConditionRef | mandatory | 1..* | AvailabilityConditionRefStructure | Reference to an AVAILABILITY CONDITION. A VALIDITY CONDITION defined in terms of temporal attributes. | Only a single AvailabilityConditionRef is allowed. |
|  | keyList | mandatory | 1..1 | KeyListStructure | A list of alternative Key values for an element. | Key list for the repeating journeys. Contains the SJYID. |
| + | KeyValue | mandatory | 1..* | KeyValueStructure | Key value pair for Entity. | A KeyValue pair with the key SJYID must exist. The Value contains a valid Swiss Journey ID. |
| ++ | Key | mandatory | 1..1 | xsd:normalizedString | Identifier of value e.g. System. |  |
| ++ | Value | mandatory | 0..1 | xsd:anyType | Value associated with QUALITY STRUCTURE FACTOR. |  |
|  | privateCodes | expected | 1..1 | PrivateCodesStructure | A list of private codes that uniquely identifiy the element. May be used for inter-operating with other (legacy) systems. +v2.0 | Replaces the single PrivateCode. The following types are possible: sjyid and rn. rn is the type used for the Postauto region |
| + | PrivateCode | expected | 1..1 | PrivateCodeStructure | A private code that uniquely identifies the element. May be used for inter-operating with other (legacy) systems. |  |
|  | TransportMode | optional | 0..1 | AllModesEnumeration | MODE. |  |
|  | TypeOfProductCategoryRef | expected | 1..1 | TypeOfProductCategoryRefStructure | Reference to a TYPE OF PRODUCT CATEGORY. Product of a JOURNEY. e.g. ICS, Thales etc See ERA B.4 7037 Characteristic description code. |  |
|  | TypeOfServiceRef | optional | 1..1 | TypeOfServiceRefStructure | Reference to a TYPE OF SERVICE. |  |
|  | noticeAssignments | optional | 0..1 | noticeAssignments_RelStructure | NOTICEs relevant for the whole GROUP OF SINGLE JOURNEYs. | The complete set of all applicable notices. Attention: Notices may be restricted to a given set of stops. |
| + | [NoticeAssignment](./tables/NoticeAssignment.md) | optional | 1..* | NoticeAssignment | The assignment of a NOTICE showing an exception in a JOURNEY PATTERN, a COMMON SECTION, or a VEHICLE JOURNEY, possibly specifying at which POINT IN JOURNEY PATTERN the validity of the NOTICE starts and ends respectively. |  |
|  | occupancies | optional | 0..1 | OccupancyView_RelStructure | OCCUPANCYs associated with this journey. +v2.0 |  |
| + | [OccupancyView](./tables/OccupancyView.md) | optional | 1..* | OccupancyView_VersionStructure |  |  |
|  | ServiceAlteration | mandatory | 0..1 | ServiceAlterationEnumeration | Whether journey is as planned, a cancellation or an extra journey. Default is as Planned. | Only the value planned is allowed. |
|  | DepartureTime | optional | 0..1 | xsd:time | Departure time. | Departure of the first journey. |
|  | DepartureDayOffset | optional | 0..1 | DayOffsetType | Departure Time Day Offset. | DayOffset if relevant. |
|  | JourneyPatternRef | mandatory | 1..1 | JourneyPatternRefStructure | Reference to a JOURNEY PATTERN. | The reference to the ServiceJourneyPattern |
| + | @nameOfRefClass | mandatory | 1..1 | xsd:string | Attribute nameOfRefClass | |
|  | TimeDemandTypeRef | mandatory | 0..1 | TimeDemandTypeRefStructure | Reference to a TIME DEMAND TYPE used at start of JOURNEY. | The timing behaviour is defined here. We allow only one TimeDemandType per ServiceJourney. |
|  | VehicleTypeRef | expected | 1..1 | VehicleTypeRefStructure | Reference to a VEHICLE TYPE. | Mostly used for accessibility information |
|  | LineRef | mandatory | 1..1 | LineRefStructure | Reference to a LINE. |  |
|  | DirectionType | optional | 0..1 | RelativeDirectionEnumeration | For fares for DISTANCE MATRIXE LEMENTs, DIRECTION in which price applies. | Allowed are: inbound, outbound |
|  | trainNumbers | mandatory | 0..1 | trainNumbersInFrame_RelStructure | TRAIN NUMBERs in frame. |  |
| + | TrainNumberRef | mandatory | 1..* | TrainNumberRefStructure | Reference to a TRAIN NUMBER. |  |
|  | [Destination](./tables/Destination.md) | expected | 0..1 | TravelSpecificationSummaryEndpointStructure | Destination of Travel. Note that for a point-to-point TARIFF the origin is assigned with a DISTANCE MATRIX ELEMENT. |  |
|  | parts | optional | 0..1 | blockParts_RelStructure | BLOCK PARTs which make up COMPOUND BLOCK. | For some use cases e.g. change of Facilities during ServiceJourney |
| + | JourneyPartRef | expected | 1..* | JourneyPartRefStructure | Reference to a JOURNEY PART. |  |
|  | TemplateVehicleJourneyType | expected | 0..1 | TemplateVehicleJourneyTypeEnumeration | Type of TEMPLATE VEHICLE JOURNEY. |  |
|  | frequencyGroups | mandatory | 0..1 | frequencyGroupsInFrame_RelStructure | FREQUENCY GROUPs In frame. Can be used to template VEHICLE JOURNEYs. | We strictly map one frequency to the TemplateServiceJourney. |
| + | HeadwayJourneyGroup | mandatory | 1..* | HeadwayJourneyGroup | A group of VEHICLE JOURNEYs following the same JOURNEY PATTERN and having the same headway interval between a specified start and end time (for example, ‘every 10 minutes’). This is especially useful for presenting passenger information. |  |
| ++ | ScheduledHeadwayInterval | mandatory | 0..1 | xsd:duration | Scheduled normal headway interval. |  |
| ++ | HeadwayDisplay | optional | 0..1 | HeadwayUseEnumeration | How headway value should be displayed to public. | Allowed values: displayPassingTimesOnly displayInsteadOfPassingTimes displayAsWellAsPassingTimes. We only export displayPassingTimesOnly. |




*→ [General NeTEx definition ](../generated/netex-html/TemplateServiceJourney.html)*

### Example


```xml
<?xml version="1.0" encoding="UTF-8"?>
<TemplateServiceJourney  id="generated" version="1">
  <!-- TemplateServiceJourney is used for journeys repeating at a certain frequency. -->
  <validityConditions>
    <!-- Used to specify a set of temporal conditions that can be associated with the ServiceJourney, for example that the corresponding journey only applies on particular days of a period (indicated by ValidDayBits, “Verkehrstagebitfeld”). -->
    <AvailabilityConditionRef ref="generated" version="1">
      <!-- Only a single AvailabilityConditionRef is allowed. -->
    </AvailabilityConditionRef>
  </validityConditions>
  <keyList>
    <!-- Key list for the repeating journeys. Contains the SJYID. -->
    <KeyValue>
      <!-- A KeyValue pair with the key SJYID must exist. The Value contains a valid Swiss Journey ID. -->
      <Key>SJYID</Key>
      <Value>ch:1:sjyid:100001:71707-003</Value>
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
  <ServiceAlteration>planned</ServiceAlteration>
  <!-- Only the value planned is allowed. -->
  <DepartureTime>06:21:00</DepartureTime>
  <!-- Departure of the first journey. -->
  <DepartureDayOffset>0</DepartureDayOffset>
  <!-- DayOffset if relevant. -->
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
  <DirectionType>inbound</DirectionType>
  <!-- Allowed are: inbound, outbound -->
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
      <HeadwayDisplay>DisplayInsteadOfPassingTimes</HeadwayDisplay>
      <!-- Allowed values: displayPassingTimesOnly displayInsteadOfPassingTimes displayAsWellAsPassingTimes. We only export displayPassingTimesOnly. -->
    </HeadwayJourneyGroup>
  </frequencyGroups>
</TemplateServiceJourney>

```



*→ [Template](./templates/TemplateServiceJourney.xml)*

### Usage Notes
- `HeadwayJourneyGroup` holds all the frequency-based information of the journey, as for example when the stops of the journey are serviced the first/last time and in what interval (or at which frequency, respectively). 
- Note that in addition to `HeadwayJourneyGroup`, standard NeTEx also features `RhythmicalJourneyGroup` to specifiy, e.g., departures at 15, 27 and 40 minutes past the hour - this is not used in the Swiss profile.
- For sjyid see information about [frequencies](uc14_frequencies.md).
- id-attribute needs to be kept stable between exports.

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
|  | dayTypeRefs | optional | 0..1 | dayTypeRefs | DAY TYPEs for BLOCK. |  |
| + | DayTypeRef | optional | 1..* | DayTypeRefStructure | The DAY TYPE of all the services in this group. |  |
|  | dayTypes | expected | 0..1 | dayTypeRefs_RelStructure | DAY TYPEs for BLOCK. |  |
| + | [DayType](./tables/DayType.md) | expected | 1..1 | DayType | A type of day characterized by one or more properties which affect public transport operation. For example: weekday in school holidays. |  |
|  | FareClass | expected | 0..1 | FareClassEnumeration | Fare class in VEHICLE for which occupancy or capacities are specified. |  |
|  | OccupancyLevel | expected | 0..1 | OccupancyEnumeration | An approximate figure of how occupied or full a VEHICLE and its parts are, e.g. 'manySeatsAvailable' or 'standingRoomOnly'. More accurate data can be provided by the individual occupancies or capacities below. | Niedrige Belegung: empty; mittlere Belegung: manySeatsAvailable; hohe Belegung: fewSeatsAvailable |
|  | GroupReservation | optional | 0..* | GroupReservationStructure | Reservations of travel groups, i.e., name of group and number of seats booked. |  |
| + | NameOfGroup | expected | 1..1 | MultilingualString | Name for which the travel group has made the reservation. |  |
| + | NumberOfReservedSeats | expected | 1..1 | NumberOfPassengers | Number of seats that the group has booked. |  |




*→ [General NeTEx definition ](../generated/netex-html/OccupancyView.html)*

### Example


```xml
<?xml version="1.0" encoding="UTF-8"?>
<OccupancyView  id="generated" version="1">
  <dayTypeRefs>
    <DayTypeRef ref="generated" version="1"/>
  </dayTypeRefs>
  <dayTypes>
    <DayType id="generated" version="1"/>
  </dayTypes>
  <FareClass>firstClass</FareClass>
  <OccupancyLevel>seatsAvailable</OccupancyLevel>
  <!-- Niedrige Belegung: empty; mittlere Belegung: manySeatsAvailable; hohe Belegung: fewSeatsAvailable -->
  <GroupReservation>
    <NameOfGroup lang="fr">Gymnase français de Bienne&gt;</NameOfGroup>
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
|  | ForAdvertisement | expected | 0..1 | xsd:normalizedString | TRAIN NUMBER to use when advertising Train -If different from Id. | TrainNumber to use for advertisement to public. Use if different from ID. |
|  | ForProduction | optional | 0..1 | xsd:normalizedString | TRAIN NUMBER to use for production -If different from Id. | TrainNumber to use for production purposes, for instance towards technical systems that require an odd or even value according to safety regulations. Use iff different from ID. |




*→ [General NeTEx definition ](../generated/netex-html/TrainNumber.html)*

### Example


```xml
<?xml version="1.0" encoding="UTF-8"?>
<TrainNumber  id="71707" version="1">
  <!-- The TrainNumber are currently a maximum of 6 digits long. TrainNumber for advertisment und production are identical. It is the number from *Z in HRDF. Must be unique per operating day in Switzerland. -->
  <ForAdvertisement>12311A</ForAdvertisement>
  <!-- TrainNumber to use for advertisement to public. Use if different from ID. -->
  <ForProduction>12311A</ForProduction>
  <!-- TrainNumber to use for production purposes, for instance towards technical systems that require an odd or even value according to safety regulations. Use iff different from ID. -->
</TrainNumber>

```



*→ [Template](./templates/TrainNumber.xml)*

### Usage Note
- id-attribute needs to be kept stable between exports.

## TypeOfService

### Purpose

`TypeOfService` indicates the purpose of a `ServiceJourney`, for example, whether if it is a passenger transport or a garage run-in. We only use `ch:1:TypeOfService:1`

### Table



*Table: TypeOfService*

| Sub | Element | Usage | Card | Type | Description | Note |
|-----|---------|-------|------|------|-------------|------|
|  | Name | expected | 0..1 | MultilingualString | Name of Traveller |  |
| + | @lang | mandatory | 1..1 | xsd:string | Attribute lang | |
|  | ShortName | expected | 0..1 | MultilingualString | Short Name for service |  |
| + | @lang | mandatory | 1..1 | xsd:string | Attribute lang | |
|  | PrivateCode | expected | 1..1 | PrivateCodeStructure | A private code that uniquely identifies the element. May be used for inter-operating with other (legacy) systems. |  |




*→ [General NeTEx definition](../generated/netex-html/TypeOfService.html)*

### Example


```xml
<?xml version="1.0" encoding="UTF-8"?>
<TypeOfService  id="ch:1:TypeOfService:1" version="1">
  <Name lang="en">PublicJourney</Name>
  <ShortName lang="en">N</ShortName>
  <PrivateCode>1</PrivateCode>
</TypeOfService>

```



*→ - [Template](./templates/TypeOfService.xml)*

### Usage Notes
- id-attribute needs to be kept stable between exports.

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
|  | validityConditions | expected | 1..1 | validityConditions_RelStructure | VALIDITY CONDITIONs conditioning entity. |  |
| + | AvailabilityConditionRef | expected | 1..* | AvailabilityConditionRefStructure | Reference to an AVAILABILITY CONDITION. A VALIDITY CONDITION defined in terms of temporal attributes. |  |
|  | Description | optional | 0..1 | MultilingualString | Description of contents. |  |
|  | StaySeated | mandatory | 0..1 | xsd:boolean | Whether the passenger can remain in vehicle (i.e. block linking). Default is false: the passenger must change vehicles for this INTERCHANGE. Default is false. |  |
|  | CrossBorder | optional | 0..1 | xsd:boolean | Whether interchanging crosses a border. |  |
|  | ChangeWithinVehicle | optional | 0..1 | xsd:boolean | In case of train splitting, the passenger may have to change to a different part of the train to continue the journey. Default is false. +v2.1 | Set to true for train splitting (Flügelzug) when the passenger may have to move to a different coach. Default is false. |
|  | Planned | optional | 0..1 | xsd:boolean | Whether INTERCHANGE is planned in a timetable. Default is true. |  |
|  | Guaranteed | optional | 0..1 | xsd:boolean | Whether INTERCHANGE is guaranteed. Default is false. |  |
|  | MaximumWaitTime | optional | 0..1 | xsd:duration | Maximum wait time for JOURNEY MEETING. | If not set or PT0M, it is guaranteed. |
|  | FromPointRef | mandatory | 1..1 | VehicleMeetingPointRefStructure | Identifier of VEHICLE MEETING POINT from which Link starts. |  |
| + | @nameOfRefClass | mandatory | 1..1 | xsd:string | Attribute nameOfRefClass | |
|  | FromVisitNumber | optional | 0..1 | xsd:nonNegativeInteger | Visit number to distinguish which visit to FROM SCHEDULED STOP POINT this is. Default is one. Only needed for circular routes with connections at the same stop on different visits. |  |
|  | ToPointRef | mandatory | 1..1 | VehicleMeetingPointRefStructure | Identifier of VEHICLE MEETING POINT at which Link ends. |  |
| + | @nameOfRefClass | mandatory | 1..1 | xsd:string | Attribute nameOfRefClass | |
|  | FromServiceJourneyRef | mandatory | 1..1 | ServiceJourneyRefStructure | SERVICE JOURNEY that feeds the INTERCHANGE. +v2.0 |  |
|  | ToServiceJourneyRef | mandatory | 1..1 | ServiceJourneyRefStructure | SERVICE JOURNEY that distributes from the INTERCHANGE. +v2.0 |  |




*→ [General NeTEx definition ](../generated/netex-html/ServiceJourneyInterchange.html)*

### Example


```xml
<?xml version="1.0" encoding="UTF-8"?>
<ServiceJourneyInterchange  version="1" id="ch:1:ServiceJourneyInterchange:91014I-THU-17-1-5100_91030L-THU-80-1-7200">
  <validityConditions>
    <AvailabilityConditionRef ref="ch:1:AvailabilityCondition:2K" version="1"/>
  </validityConditions>
  <Description>LineChange</Description>
  <StaySeated>true</StaySeated>
  <CrossBorder>false</CrossBorder>
  <ChangeWithinVehicle>false</ChangeWithinVehicle>
  <!-- Set to true for train splitting (Flügelzug) when the passenger may have to move to a different coach. Default is false. -->
  <Planned>true</Planned>
  <Guaranteed>false</Guaranteed>
  <MaximumWaitTime>PT9M</MaximumWaitTime>
  <!-- If not set or PT0M, it is guaranteed. -->
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
- id-attribute should be kept stable between exports.

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

