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
- [ServiceFacilitySet](10_common.md#ServiceFacilitySet)

In ServiceCalender:
- [AvailabilityCondition](08_service_calendars.md#availabilitycondition)
- [Timeband](08_service_calendars.md#timeband)



## TimetableFrame
*→ [Glossary definition](A4_annex_glossary.md#timetableframe)*

### Purpose

A `TimetableFrame` contains the operational journey definitions — the actual trips that run on the network. It groups `ServiceJourney`s, `TemplateServiceJourney`s, and `InterchangeRules` that together describe the timetabled service offering.

### Contained Elements
- `vehicleJourneys`– collection of journey types:
  -  `ServiceJourney`- describes an individual timetabled journey
  -  `TemplateServiceJourney`- describes a set of journeys repeating at a certain frequency
  -  The Swiss profile only models journeys that are available to the passengers
- `TrainNumber`- each `ServiceJourney` and `TemplateServiceJourney` is mapped one-to-one to exactly one train number
- `PassingTimes`- describe the times of vehicles at points in their journey
- `InterchangeRule`s- describe interchanges between journeys
- `NoticeAssignment`s- link `Notice`s to specific journeys or stop points within journeys
- `ServiceFacilitySet`s- describe the various services and facilities offered by the vehicles of a journey


### Table


| Sub | Element | Usage | Card | Type | Description | Note |
|-----|---------|-------|------|------|-------------|------|
| + | vehicleJourneys | expected | 0..1 | journeysInFrame_RelStructure | VEHICLE JOURNEYs in frame. | Contains the ServiceJourneys and TemplateServiceJourneys. |
| ++ | [ServiceJourney](ServiceJourney.md) | expected | 1..1 | unknown | A passenger carrying VEHICLE JOURNEY for one specified DAY TYPE. The pattern of working is in principle defined by a SERVICE JOURNEY PATTERN.



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
    <ServiceJourneyInterchange id="ch:1:sji:generated-1" version="1">
      <!-- For modeling many forms of interchanges -->
      <FromJourneyRef ref="sjyid-1" version="1"/>
      <ToJourneyRef ref="sjyid-2" version="1"/>
    </ServiceJourneyInterchange>
  </journeyInterchanges>
  <interchangeRules>
    <InterchangeRule id="ch:1:InterchangeRule:1" version="1"/>
  </interchangeRules>
</TimetableFrame>

```



*→ [Template](../templates/TimetableFrame.xml)*

### Frame Relationships
`TimetableFrame` depends on `ServiceFrame`for `JourneyPattern`s and `Line`s referenced by `ServiceJourney`s. It depends on `ResourceFrame` for `Operator` definitions. `VehicleScheduleFrame` may reference journeys defined here for block and duty scheduling. `TimetableFrame` is typically wrapped in a `CompositeFrame`within a `PublicationDelivery`.

## ServiceJourney
*→ [Glossary definition](A4_annex_glossary.md#ServiceFrame)*

### Purpose
A `ServiceJourney` represents a planned trip in the timetable operating on a recurring schedule. It defines the stop sequence via reference to a `JourneyPattern`, includes scheduled passing times, and specifies operational details such as operator and days of operation. Unlike `DatedServiceJourney`, which represents a concrete instance on a specific date, `ServiceJourney` is the reusable template used across multiple dates via `DayType` definitions

### Table


| Sub | Element | Usage | Card | Type | Description | Note |
|-----|---------|-------|------|------|-------------|------|
| + | validityConditions | mandatory | 1..1 | validityConditions_RelStructure | VALIDITY CONDITIONs conditioning entity. | Used to specify a set of temporal conditions that can be associated with the ServiceJourney, for example that the corresponding journey only applies on particular days of a period (indicated by ValidDayBits, “Verkehrstagebitfeld”). |
| ++ | [AvailabilityCondition](AvailabilityCondition.md) | mandatory | 1..1 | unknown | VALIDITY CONDITION stated in terms of DAY TYPES and PROPERTIES OF DAYs. | Only a single occurence is allowed. The following elements are mandatory here, any other elements of AvailabilityCondition are not allowed or will be ignored. |
| + | keyList | expected | 1..1 | KeyListStructure | A list of alternative Key values for an element. | KEY LIST with the KEY VALUEs belonjing to the SERVICE JOURNEY. Will contain the SJYID. |
| ++ | KeyValue | mandatory | 1..* | KeyValueStructure | Key value pair for Entity. | A KeyValue pair with the Key SJYID must exist. The Value contains a valid Swiss Journey ID. |
| +++ | Key | mandatory | 1..1 | xsd:normalizedString | Identifier of value e.g. System. |  |
| +++ | Value | mandatory | 0..1 | xsd:anyType | Value associated with QUALITY STRUCTURE FACTOR. |  |
| + | privateCodes | expected | 1..1 | PrivateCodesStructure | A list of private codes that uniquely identifiy the element. May be used for inter-operating with other (legacy) systems. +v2.0 |  |
| ++ | PrivateCode | expected | 1..1 | PrivateCodeStructure | A private code that uniquely identifies the element. May be used for inter-operating with other (legacy) systems. |  |
| + | Extensions | optional | 1..1 | ExtensionsStructure | User defined Extensions to ENTITY in schema. (Wrapper tag used to avoid problems with handling of optional 'any' by some validators). | Used to indicate Facility changes. |
| ++ | facilities | optional | 0..1 | serviceFacilitySets_RelStructure | FACILITies available associated with JOURNEY. |  |
| +++ | Facility | optional | 1..1 | unknown |  |  |
| ++++ | ServiceFacilitySetRef | mandatory | 1..1 | ServiceFacilitySetRefStructure | Reference to a SERVICE FACILITY SET. |  |
| + | TransportMode | optional | 0..1 | AllModesEnumeration | MODE. |  |
| + | TypeOfProductCategoryRef | mandatory | 1..1 | TypeOfProductCategoryRefStructure | Reference to a TYPE OF PRODUCT CATEGORY. Product of a JOURNEY. e.g. ICS, Thales etc



*→ [General NeTEx definition ](../generated/netex-html/ServiceJourney.html)*

### Example


```xml
<?xml version="1.0" encoding="UTF-8"?>
<ServiceJourney  id="generated" version="1">
  <validityConditions>
    <!-- Used to specify a set of temporal conditions that can be associated with the ServiceJourney, for example that the corresponding journey only applies on particular days of a period (indicated by ValidDayBits, “Verkehrstagebitfeld”). -->
    <AvailabilityCondition id="generated" version="1">
      <!-- Only a single occurence is allowed. The following elements are mandatory here, any other elements of AvailabilityCondition are not allowed or will be ignored. -->
      <FromDate>2026-05-17T00:00:00Z</FromDate>
      <!-- Is equal to the start date of the timetable year or, more generally, the period in which the ValidDayBits apply. -->
      <ToDate>2026-05-17T00:00:00Z</ToDate>
      <!-- Is equal to the end date of the timetable year or, more generally, the period in which the ValidDayBits apply. -->
      <ValidDayBits>01010111</ValidDayBits>
    </AvailabilityCondition>
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
  </privateCodes>
  <Extensions>
    <!-- Used to indicate Facility changes. -->
    <facilities>
      <Facility id="ch:1:facility:f1" version="1">
        <validityConditions>
          <AvailabilityConditionRef ref="ch:1:AvailabilityCondition:c3" version="1"/>
        </validityConditions>
        <ServiceFacilitySetRef ref="ch:1:ServiceFacilitySet:A___1" version="1"/>
      </Facility>
    </facilities>
  </Extensions>
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
  <DepartureDayOffset>0</DepartureDayOffset>
  <LineRef ref="ch:2:Line:11.IR.90" version="1"/>
  <DirectionType>outbound</DirectionType>
  <!-- Allowed are: inbound, outbound -->
  <trainNumbers>
    <TrainNumberRef ref="ch:1:TrainNumber:71707" version="1"/>
  </trainNumbers>
  <Destination>
    <ScheduledStopPointRef ref="ch:1:sloid:3412" version="1"/>
  </Destination>
  <passingTimes>
    <TimetabledPassingTime id="generated" version="1">
      <PointInJourneyPatternRef ref="generated" version="1"/>
    </TimetabledPassingTime>
  </passingTimes>
</ServiceJourney>

```



*→ [Template](../templates/ServiceJourney.xml)*


### Usage Notes

- **Template vs. Instance:** `ServiceJourney` is the template; `DatedServiceJourney` represents concrete daily instances.
- **Consistency:** A `ServiceJourney` must reference exactly one `JourneyPattern`. The pattern's stop sequence is authoritative.
- **Stop Times:** Each stop in the referenced `JourneyPattern` must have exactly one `TimetabledPassingTimes` entry with `ArrivalTime` and/or `DepartureTime`.
- **Day Governance:** `DayType` references control on which days the journey operates; per-date deviations belong to `DatedServiceJourney`.
- **Validation:** Ensure `JourneyPatternRef`, `LineRef`, and `OperatorRef` are consistent and reference existing objects.

## TemplateServiceJourney
*→ [Glossary definition](A4_annex_glossary.md#templateservicejourney)*
### Purpose
A `TemplateServiceJourney` represents a sequence of planned trips. It is similar to the `ServiceJourney`, but it is used if there is a frequency defined at which the trips are scheduled on an operating day. 

A frequency is specified in a `HeadwayJourneyGroup` (e.g. every 20 minutes). The `TemplateServiceJourney` may thus represent multiple journeys or it could be used simply as a template for adding extra date journeys after the planning phase. 

### Table


| Sub | Element | Usage | Card | Type | Description | Note |
|-----|---------|-------|------|------|-------------|------|
| + | validityConditions | expected | 1..1 | validityConditions_RelStructure | VALIDITY CONDITIONs conditioning entity. | Used to specify a set of temporal conditions that can be associated with the TemplateServiceJourney, for example that the corresponding journey only applies on particular days of a period (indicated by ValidDayBits, “Verkehrstagebitfeld”). |
| ++ | [AvailabilityCondition](AvailabilityCondition.md) | mandatory | 1..1 | unknown | VALIDITY CONDITION stated in terms of DAY TYPES and PROPERTIES OF DAYs. | More spacific requirements than standard AvailabilityCondition. Only a single occurence is allowed. The following elements are mandatory here, any other elements of AvailabilityCondition are not allowed or will be ignored. |
| + | keyList | mandatory | 1..1 | KeyListStructure | A list of alternative Key values for an element. | Key list for the repeating journeys. Contains the SJYID. |
| ++ | KeyValue | mandatory | 1..* | KeyValueStructure | Key value pair for Entity. | A KeyValue pair with the key SJYID must exist. The Value contains a valid Swiss Journey ID. |
| +++ | Key | mandatory | 1..1 | xsd:normalizedString | Identifier of value e.g. System. |  |
| +++ | Value | mandatory | 0..1 | xsd:anyType | Value associated with QUALITY STRUCTURE FACTOR. |  |
| + | privateCodes | expected | 1..1 | PrivateCodesStructure | A list of private codes that uniquely identifiy the element. May be used for inter-operating with other (legacy) systems. +v2.0 | Replaces the single PrivateCode. |
| ++ | PrivateCode | expected | 1..1 | PrivateCodeStructure | A private code that uniquely identifies the element. May be used for inter-operating with other (legacy) systems. |  |
| + | Extensions | optional | 1..1 | ExtensionsStructure | User defined Extensions to ENTITY in schema. (Wrapper tag used to avoid problems with handling of optional 'any' by some validators). | Used to indicate Facility changes. |
| ++ | facilities | optional | 0..1 | serviceFacilitySets_RelStructure | FACILITies available associated with JOURNEY. |  |
| +++ | Facility | optional | 1..1 | unknown |  |  |
| ++++ | ServiceFacilitySetRef | mandatory | 1..1 | ServiceFacilitySetRefStructure | Reference to a SERVICE FACILITY SET. |  |
| + | TransportMode | optional | 0..1 | AllModesEnumeration | MODE. |  |
| + | TypeOfProductCategoryRef | expected | 1..1 | TypeOfProductCategoryRefStructure | Reference to a TYPE OF PRODUCT CATEGORY. Product of a JOURNEY. e.g. ICS, Thales etc



*→ [General NeTEx definition ](../generated/netex-html/TemplateServiceJourney.html)*

### Example


```xml
<?xml version="1.0" encoding="UTF-8"?>
<TemplateServiceJourney  id="generated" version="1">
  <!-- TemplateServiceJourney is used for journeys repeating at a certain frequency. -->
  <validityConditions>
    <!-- Used to specify a set of temporal conditions that can be associated with the TemplateServiceJourney, for example that the corresponding journey only applies on particular days of a period (indicated by ValidDayBits, “Verkehrstagebitfeld”). -->
    <AvailabilityCondition id="generated" version="1">
      <!-- More spacific requirements than standard AvailabilityCondition. Only a single occurence is allowed. The following elements are mandatory here, any other elements of AvailabilityCondition are not allowed or will be ignored. -->
      <FromDate>2026-05-17T00:00:00Z</FromDate>
      <!-- Is equal to the start date of the timetable year or, more generally, the period in which the ValidDayBits apply. -->
      <ToDate>2026-05-17T00:00:00Z</ToDate>
      <!-- Is equal to the end date of the timetable year or, more generally, the period in which the ValidDayBits apply. -->
      <ValidDayBits>01010111</ValidDayBits>
    </AvailabilityCondition>
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
    <!-- Replaces the single PrivateCode. -->
    <PrivateCode type="sjyid">ch:1:sjyid:100001:71707-003</PrivateCode>
  </privateCodes>
  <Extensions>
    <!-- Used to indicate Facility changes. -->
    <facilities>
      <Facility id="ch:1:facility:f1" version="1">
        <validityConditions>
          <AvailabilityConditionRef ref="ch:1:AvailabilityCondition:c3" version="1"/>
        </validityConditions>
        <ServiceFacilitySetRef ref="ch:1:ServiceFacilitySet:A___1" version="1"/>
      </Facility>
    </facilities>
  </Extensions>
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
  <LineRef ref="ch:2:Line:11.IR.90" version="1"/>
  <DirectionType>inbound</DirectionType>
  <!-- Allowed are: inbound, outbound -->
  <trainNumbers>
    <TrainNumberRef ref="ch:1:TrainNumber:71707" version="1"/>
  </trainNumbers>
  <Destination>
    <Name lang="de">Wollishofen</Name>
    <ScheduledStopPointRef ref="ch:1:sloid:3412" version="1"/>
    <DestinationDisplayRef ref="generated" version="1"/>
    <PlaceRef ref="ch:1:sloid:3412" version="1"/>
  </Destination>
  <passingTimes>
    <TimetabledPassingTime id="generated" version="1">
      <PointInJourneyPatternRef ref="generated" version="1"/>
    </TimetabledPassingTime>
  </passingTimes>
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



*→ [Template](../templates/TemplateServiceJourney.xml)*

### Usage Notes
- `HeadwayJourneyGroup` holds all the frequency-based information of the journey, as for example when the stops of the journey are serviced the first/last time and in what interval (or at which frequency, respectively). 
- Note that in addtion to `HeadwayJourneyGroup`, standard NeTEx also features `RhythmicalJourneyGroup` to specifiy, e.g., departures at 15, 27 and 40 minutes past the hour - this is not used in the Swiss profile.
- For sjyid see information about [frequencies](uc14_frequencies.md).


## OccupancyView

### Purpose
`OccupancyView`can be used on the `Journey`, `JourneyPart`, and `TimetabledPassingTime` elements. Used for predicted and planned occupancies of vehicles.

### Table


| Sub | Element | Usage | Card | Type | Description | Note |
|-----|---------|-------|------|------|-------------|------|
| + | dayTypeRefs | optional | 0..1 | unknown | DAY TYPEs for BLOCK. |  |
| ++ | DayTypeRef | optional | 1..* | DayTypeRefStructure | The DAY TYPE of all the services in this group. |  |
| + | dayTypes | expected | 0..1 | unknown | DAY TYPEs for BLOCK. |  |
| ++ | [DayType](DayType.md) | expected | 1..1 | unknown | A type of day characterized by one or more properties which affect public transport operation. For example: weekday in school holidays. |  |
| + | FareClass | expected | 0..1 | FareClassEnumeration | Fare class in VEHICLE for which occupancy or capacities are specified. |  |
| + | OccupancyLevel | expected | 0..1 | OccupancyEnumeration | An approximate figure of how occupied or full a VEHICLE and its parts are, e.g. 'manySeatsAvailable' or 'standingRoomOnly'.  



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



*→ [Template](../templates/OccupancyView.xml)*

### Usage Notes
We currently don't use OccupancyView.


## TrainNumber
*→ [Glossary definition](A4_annex_glossary.md#trainnumber)*

### Purpose

Codes assigned to particular journeys (`ServiceJourney`, `TemplateServiceJourney`) when operated by trains. `ServiceJourney`s can in principle have multiple different `TrainNumber`s whereas a `JourneyPart` can only reference a single one.

### Table


| Sub | Element | Usage | Card | Type | Description | Note |
|-----|---------|-------|------|------|-------------|------|
| + | Description | optional | 0..1 | MultilingualString | Description of contents. |  |
| + | ForAdvertisement | optional | 0..1 | xsd:normalizedString | TRAIN NUMBER to use when advertising Train -If different from Id. | TRAIN NUMBER to use for advertisement to public. Use iff different from ID. |
| + | ForProduction | optional | 0..1 | xsd:normalizedString | TRAIN NUMBER to use for production -If different from Id. | TRAIN NUMBER to use for production purposes, for instance towards technical systems that require an odd or even value according to safety regulations. Use iff different from ID. |



*→ [General NeTEx definition ](../generated/netex-html/TrainNumber.html)*

 ### Example


```xml
<?xml version="1.0" encoding="UTF-8"?>
<TrainNumber  id="71707" version="1">
  <!-- The TRAIN NUMBERs are currently a maximum of 6 digits long. TRAIN NUMBERs for advertisment und production are identical. -->
  <Description>Information about the train</Description>
  <ForAdvertisement>12311A</ForAdvertisement>
  <!-- TRAIN NUMBER to use for advertisement to public. Use iff different from ID. -->
  <ForProduction>12311A</ForProduction>
  <!-- TRAIN NUMBER to use for production purposes, for instance towards technical systems that require an odd or even value according to safety regulations. Use iff different from ID. -->
</TrainNumber>

```



*→ [Template](../templates/TrainNumber.xml)*

## TypeOfService

### Purpose

`TypeOfService` indicates the purpose of a `ServiceJourney`, for example, whether if it is a passenger transport or a garage run-in. We only use `ch:1:TypeOfService:1`

### Table


| Sub | Element | Usage | Card | Type | Description | Note |
|-----|---------|-------|------|------|-------------|------|
|  | TypeOfService | expected | 1..1 | unknown | Classification of a Service. |  |
| + | Name | mandatory | 0..1 | MultilingualString | Name of Traveller |  |
| + | ShortName | mandatory | 0..1 | MultilingualString | Short Name for service |  |
| + | PrivateCode | mandatory | 1..1 | PrivateCodeStructure | A private code that uniquely identifies the element. May be used for inter-operating with other (legacy) systems. |  |



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



*→ - [Template](../templates/TypeOfService.xml)*

### Usage Notes

The following types are currently used:

| Name	             | Description                                                                                                                                               |
|-------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------|
| PublicJourney	    | A public passenger transport                                                                                                                              |
| ~~GarageRunOut~~	 | A garage run-out                                                                                                                                          |
| ~~GarageRunIn~~	  | A garage run-in                                                                                                                                           |
| ~~ThroughCoach~~  | 	A special type of public passenger transport that is used if a ServiceJourney is comprised of JourneyParts of other ServiceJourneys because of coupling. |

Actually there is only one allowed value that we use in the Swiss profile: Only the `PublicJourney` is to be exchanged.


## TimetabledPassingTime
*→ [Glossary definition](A4_annex_glossary.md#timetabledpassingtime)*

### Purpose

Long-term planned time data concerning public transport vehicles passing a particular `PointInJourneyPattern` on a specified vehicle journey for a certain `DayType`. 

### Table


| Sub | Element | Usage | Card | Type | Description | Note |
|-----|---------|-------|------|------|-------------|------|
| ++ | CheckConstraint | optional | 1..1 | unknown | Characteristics of a SITE COMPONENT representing a process, such as check-in, security



*→ [General NeTEx definition ](../generated/netex-html/TimetabledPassingTime.html)*

### Example


```xml
<?xml version="1.0" encoding="UTF-8"?>
<TimetabledPassingTime  id="generated" version="1">
  <!-- Long-term planned time data concerning public transport vehicles passing a particular POINT IN JOURNEY PATTERN on a specified VEHICLE JOURNEY for a certain DAY TYPE. -->
  <Extensions>
    <CheckConstraint id="generated" version="1">
      <!-- **TODO - Planned for V2.1** Allows for specifying delays due to longer boarding times. -->
    </CheckConstraint>
    <IsFlexible>false</IsFlexible>
    <!-- **TODO - Planned for V2.1** Stop is only served upon prior request (e.g., booking by phone). -->
  </Extensions>
  <AlightAndReboard>false</AlightAndReboard>
  <StopPointInJourneyPatternRef ref="generated" version="1"/>
  <ArrivalTime>08:00:00</ArrivalTime>
  <!-- Not used if departure only. -->
  <ArrivalDayOffset>0</ArrivalDayOffset>
  <DepartureTime>08:01:00</DepartureTime>
  <!-- Not used if arrival only. -->
  <DepartureDayOffset>0</DepartureDayOffset>
  <WaitingTime>PT1M</WaitingTime>
  <LatestArrivalTime>08:05:00</LatestArrivalTime>
  <LatestArrivalDayOffset>0</LatestArrivalDayOffset>
  <EarliestDepartureTime>07:58:00</EarliestDepartureTime>
  <EarliestDepartureDayOffset>0</EarliestDepartureDayOffset>
</TimetabledPassingTime>

```



*→ [Template](../templates/TimetabledPassingTime.xml)*

### Usage Notes

- Note that for journeys lasting more than one day, `DayOffset` is available.
- If `DepartureTime` is not on the same day as `ArrivalTime` this information will be provided using `WaitingTime`.
- We use sjyid whenever possible as the attribute. However, there are different types of `ServiceJourney`s that don't have one:
  - foreign `ServiceJourney`s
  - **TODO** which other cases don't have sjyid #83
- We store the sjyid in different places `id`, `privateCodes/PrivateCode`, `KeyList`. This allows different importing systems to find the sjyid.


## ServiceJourneyInterchange
*→ [Glossary definition](A4_annex_glossary.md#servicejourneyinterchange)*

### Purpose
The standard say: "In some cases, a SERVICE JOURNEY INTERCHANGE expresses an interchange between two SERVICE JOURNEYs specifically planned to be operated by the same physical vehicle. This concept is for instance used for circular lines and coupled journeys. This means that passenger information should be adapted to the fact that the passenger should not change vehicle as the transfer is implicit. In this case it is also im-portant that operation control staff is aware of the consequences to passengers if the operation is altered in such a way that two different vehicles are used for the two involved SERVICE JOURNEYs."

StaySeated can and should be modeled this way (especially if one uses EPIP as basis. Splitting is very technically not the same vehicle, but on on a higher level for the passenger it is. So we can indicate the splitting there.

### Table


| Sub | Element | Usage | Card | Type | Description | Note |
|-----|---------|-------|------|------|-------------|------|
|  | ServiceJourneyInterchange | mandatory | 1..1 | unknown | The scheduled possibility for transfer of passengers between two SERVICE JOURNEYs at the same or different STOP POINTs. |  |
| + | validityConditions | expected | 1..1 | validityConditions_RelStructure | VALIDITY CONDITIONs conditioning entity. |  |
| ++ | AvailabilityConditionRef | expected | 1..1 | AvailabilityConditionRefStructure | Reference to an AVAILABILITY CONDITION. A VALIDITY CONDITION defined in terms of temporal attributes. |  |
| + | Description | optional | 0..1 | MultilingualString | Description of contents. |  |
| + | StaySeated | mandatory | 0..1 | xsd:boolean | Whether the passenger can remain in vehicle (i.e. block linking). Default is false: the passenger must change vehicles for this INTERCHANGE.



*→ [General NeTEx definition ](../generated/netex-html/ServiceJourneyInterchange.html)*

### Example


```xml
<?xml version="1.0" encoding="UTF-8"?>
<ServiceJourneyInterchange  version="2.0" id="ch:1:ServiceJourneyInterchange:91014I-THU-17-1-5100_91030L-THU-80-1-7200">
  <validityConditions>
    <AvailabilityConditionRef ref="ch:1:AvailabilityCondition:2K" version="1"/>
  </validityConditions>
  <Description>LineChange</Description>
  <StaySeated>true</StaySeated>
  <CrossBorder>false</CrossBorder>
  <Planned>true</Planned>
  <Guaranteed>false</Guaranteed>
  <MaximumWaitTime>PT9M</MaximumWaitTime>
  <!-- If not set or PT0M, it is guaranteed. -->
  <FromPointRef ref="ch:1:ScheduledStopPoint:8506105:3" version="1"/>
  <FromVisitNumber>1</FromVisitNumber>
  <ToPointRef ref="ch:1:ScheduledStopPoint:8506105:3" version="1"/>
  <FromServiceJourneyRef ref="ch:1:ServiceJourney:ch:1:sjyid:100046:30467-003_91014I.j26_17" version="1"/>
  <ToServiceJourneyRef ref="ch:1:ServiceJourney:ch:1:sjyid:100046:13602-002_91030L.j26_80" version="1"/>
</ServiceJourneyInterchange>

```



*→ [Template](../templates/ServiceJourneyInterchange.xml))*

### Usage Notes
> **TODO*** Adrian pls add some descriptions here. #63

## InterchangeRule
*→ [Glossary definition](A4_annex_glossary.md#interchangerule)*
> **TODO** will probably be removed and replaced by ServiceJourneyInterchange #63
### Purpose

An `InterchangeRule`defines the possibility of interchanging between two `ServiceJourney`s at the same or different `ScheduledStopPoint*` — where at least one journey is specified indirectly via `Direction`, `Line` or the VEHICLE JOURNEY (? **TODO** #63), rather than as an explicit journey pair. The rule specifies criteria (e.g. `Mode`, `Line`, `Direction`) that a candidate feeder or distributor journey must fulfil.

### Table


| Sub | Element | Usage | Card | Type | Description | Note |
|-----|---------|-------|------|------|-------------|------|
|  | InterchangeRule | mandatory | 1..1 | unknown | Conditions for considering journeys to meet or not to meet, specified indirectly: by a particular MODE, DIRECTION or LINE. Such conditions may alternatively be specified directly, indicating the corresponding services. In this case they are either a SERVICE JOURNEY PATTERN INTERCHANGE or a SERVICE JOURNEY INTERCHANGE. | transfer times between Line/Directions at a given stop (UMSTEIGL) |
| ++ | AvailabilityConditionRef | expected | 1..1 | AvailabilityConditionRefStructure | Reference to an AVAILABILITY CONDITION. A VALIDITY CONDITION defined in terms of temporal attributes. |  |
| + | StaySeated | mandatory | 0..1 | xsd:boolean | Whether the passenger can remain in vehicle (i.e. block linking). Default is false: the passenger must change vehicles for this INTERCHANGE.



*→ [General NeTEx definition ](../generated/netex-html/InterchangeRule.html)*


### Examples

#### Interchanges between ServiceJourneys


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



#### Interchange between Lines/Directions/Operators


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




### Usage Notes
- The `ScheduledStopPoint` is defined separately for the feeder and distributor side.
- [See use case Durchbindung](uc01_durchbindung.md)
- [See use case transfers](uc03_transfers.md)


## AvailabilityCondition 
*→ [see ServiceCalenderFrame](./08_service_calendars.md#AvailabilityCondition)*

## Timeband 
*→ [see ServiceCalenderFrame](./08_service_calendars.md#Timeband)*


## NoticeAssignment
*→ [see Common elements](./07_service.md#NoticeAssignment)*


## ServiceFacilitySet
*→ [see Common elements](./10_common.md#servicefacilityset)*


### Usage Notes
* [See use case Joining and splitting](uc02_joining_splitting.md)

