# Timetables


![Timetable model](media/TimetableModel.png)

## TimetableFrame

A set of timetable data (VEHICLE JOURNEYs, etc.) to which the same VALIDITY CONDITIONs have been assigned. 
A TIMETABLE FRAME holds a coherent set of timetable related elements for data exchange. 
The primary component exchanged by a TIMETABLE FRAME in NeTEx / Transmodel terms is the VEHICLE JOURNEY. The Swiss profile only uses the more specific SERVICE JOURNEY (which describes an individual journey) and the TEMPLATE SERVICE JOURNEY (which describes a set of journeys repeating at a certain frequency). 


The `TimetableFrame` contains the following allowed elements:
* `ServiceJourney` and `TemplateServiceJourney`
  * `TemplateServiceJourney` is only used for frequency traffic
  * We only model journeys that are available for passenger  
* `TrainNumber`
  * Each (TEMPLATE) SERVICE JOURNEY is mapped one-to-one to exactly one TRAIN NUMBER
* `PassingTime`s describe the times of vehicles at points in their journey
* `InterchangeRule`s describe interchanges between journeys
* `JourneyMeeting`s and `JourneyPart`s describe multipart journeys which join and split **TODO**
* `ServiceFacilitySet`s describe the various services and facilities offered by the vehicles of a journey



[//]: # (TODO: Add TimetableFrame links)
- [Swiss profile NeTEx definition](../generated/markdown-examples/TimetableFrame.md)
- [Example snippet](../generated/xml-snippets/TimetableFrame.xml)
- [General NeTEx definition ](../generated/xcore/TimetableFrame.html)


> [Template](../templates/TimetableFrame.xml)

## ServiceJourney

A SERVICE JOURNEY is a VEHICLE JOURNEY on which passengers will be allowed to board or alight from vehicles at stops. It describes the service between an origin and a destination, as advertised to the public.

[//]: # (TODO: Add ServiceJourney links)
- [General NeTEx definition ](../generated/xcore/ServiceJourney.html)
- [Swiss profile NeTEx definition](../generated/markdown-examples/ServiceJourney.md)
- [Example snippet](../generated/xml-snippets/ServiceJourney.xml)

> [Template](../templates/ServiceJourney.xml)

((The following restrictions occur:
* DONE: The attributs id, version and responsibilitySetRef must be set.
* DONE: The validityConditions contain only one AvailablityCondition that contains only the elements FromDate, ToDate and ValidDayBits.
* DONE: In the keyList a KeyValue pair with the Key `sjyid` must exists. The Value contains a valid Swiss Journey ID.
* privateCodes: tbd
* TransportMode: tbd
* TypeOfProductCategoryRef: tbd
* TypeOfServiceRef is always set to tbd
* DONE: noticeAssignments contain all notices. Attention: they may be restricted to a given set of stops.
* DONE: ServiceAlteration is set.
* DepartureTime:
* DepartureDayOffset:
* DONE: LineRef is mandatory.
* DONE: DirectionType is only inbound or outbound
* DONE: trainNumbers contains at least one TrainNumberRef. TrainNumber i not allowed in it.
* Destination: xxx
* passingTimes: ddd
* DONE: calls are not to be used.

## ServiceJourney (alternative to previous section)

### 1. Purpose

A **ServiceJourney** represents a planned trip in the timetable operating on a recurring schedule. It defines the stop sequence via reference to a JourneyPattern, includes scheduled passing times, and specifies operational details such as operator and days of operation. Unlike DatedServiceJourney, which represents a concrete instance on a specific date, ServiceJourney is the reusable template used across multiple dates via DayType definitions

### 2. Table

[//]: # (TODO: Add ServiceJourney links)

- [Swiss profile NeTEx definition](../generated/markdown-examples/ServiceJourney.md)
- [General NeTEx definition ](../generated/xcore/ServiceJourney.html)

> [Template](../templates/ServiceJourney.xml)

### 3. Example

[//]: # (TODO: Add ServiceJourney links)
- [Example snippet](../generated/xml-snippets/ServiceJourney.xml)


### 4. Usage Notes / Pitfalls

- **Template vs. Instance:** ServiceJourney is the template; DatedServiceJourney represents concrete daily instances.
- **Consistency:** A ServiceJourney must reference exactly one JourneyPattern. The pattern's stop sequence is authoritative.
- **Stop Times:** Each stop in the referenced JourneyPattern must have exactly one TimetabledPassingTime entry with ArrivalTime and/or DepartureTime.
- **Day Governance:** DayType references control on which days the journey operates; per-date deviations belong to DatedServiceJourney.
- **Validation:** Ensure journeyPatternRef, lineRef, and operatorRef are consistent and reference existing objects.


## TemplateServiceJourney

A TEMPLATE SERVICE JOURNEY is a VEHICLE JOURNEY on which passengers will be allowed to board or alight from vehicles at stops and that reapeats with a certain frequency. It describes the service between an origin and a destination, as advertised to the public. Only to be used if a frequency has been specified for the JOURNEY. 

[//]: # (TODO: Add TemplateServiceJourney links)

- [Swiss profile NeTEx definition](../generated/markdown-examples/TemplateServiceJourney.md)
- [Example snippet](../generated/xml-snippets/TemplateServiceJourney.xml)
- [General NeTEx definition ](../generated/xcore/TemplateServiceJourney.html)

> [Template](../templates/TemplateServiceJourney.xml)



## AvailabilityCondition -> TODO: move to Common

A specific type of VALIDITY CONDITION used to specify a set of temporal conditions that can be associated with an ENTITY, for example that a STOP PLACE is open on a particular DAY TYPE.

[//]: # (TODO: Add AvailabilityCondition links)

- [Swiss profile NeTEx definition](../generated/markdown-examples/AvailabilityCondition.md)
- [Example snippet](../generated/xml-snippets/AvailabilityCondition.xml)
- [General NeTEx definition ](../generated/xcore/AvailabilityCondition.html)

> [Template](../templates/AvailabilityCondition.xml)



## Timeband -> TODO: move to Common


[//]: # (TODO: Add Timeband links)

- [Swiss profile NeTEx definition](../generated/markdown-examples/Timeband.md)
- [Example snippet](../generated/xml-snippets/Timeband.xml)
- [General NeTEx definition ](../generated/xcore/Timeband.html)

> [Template](../templates/Timeband.xml)



## NoticeAssignment -> TODO: move to Common

The assignment of a NOTICE to any model element. Can be used in particular to show an exception in a JOURNEY PATTERN, a COMMON SECTION, or a VEHICLE JOURNEY, possibly specifying at which POINT IN JOURNEY PATTERN the validity of the NOTICE starts and ends respectively.

[//]: # (TODO: Add NoticeAssignment links)

- [Swiss profile NeTEx definition](../generated/markdown-examples/NoticeAssignment.md)
- [Example snippet](../generated/xml-snippets/NoticeAssignment.xml)
- [General NeTEx definition ](../generated/xcore/NoticeAssignment.html)

> [Template](../templates/NoticeAssignment.xml)


## OccupancyView

The OccupancyView element can be used on the JOURNEY, JOURNEY PART, and TIMETABLED PASSING TIME elements. Used for predicted and planned occupancies of vehicles.

[//]: # (TODO: Add OccupancyView links)

- [Swiss profile NeTEx definition](../generated/markdown-examples/OccupancyView.md)
- [Example snippet](../generated/xml-snippets/OccupancyView.xml)
- [General NeTEx definition ](../generated/xcore/OccupancyView.html)

> [Template](../templates/OccupancyView.xml)



## TrainNumber

Codes assigned to particular VEHICLE JOURNEYs when operated by TRAINs or COMPOUND TRAINs. ServiceJourneys can in principle have multiple different TrainNumbers whereas a JourneyPart can only reference a single one.

[//]: # (TODO: Add TrainNumber links)

- [Swiss profile NeTEx definition](../generated/markdown-examples/TrainNumber.md)
- [Example snippet](../generated/xml-snippets/TrainNumber.xml)
- [General NeTEx definition ](../generated/xcore/TrainNumber.html)

> [Template](../templates/TrainNumber.xml)



## TimetabledPassingTime

Long-term planned time data concerning public transport vehicles passing a particular POINT IN JOURNEY PATTERN on a specified VEHICLE JOURNEY for a certain DAY TYPE. Note that for Journeys lasting more than one day, DayOffset is available. If DepartureTime is not on the same day as ArrivalTime this information will be provided using WaitingTime.

[//]: # (TODO: Add TimetabledPassingTime links)

- [Swiss profile NeTEx definition](../generated/markdown-examples/TimetabledPassingTime.md)
- [Example snippet](../generated/xml-snippets/TimetabledPassingTime.xml)
- [General NeTEx definition ](../generated/xcore/TimetabledPassingTime.html)

> [Template](../templates/TimetabledPassingTime.xml)

## ServiceFacilitySet -> TODO: move to Common

Set of FACILITies available for a SERVICE JOURNEY or a JOURNEY PART. The set may be available only for a specific VEHICLE TYPE within the SERVICE (e.g. carriage equipped with low floor). 

[//]: # (TODO: Add ServiceFacilitySet links)

- [Swiss profile NeTEx definition](../generated/markdown-examples/ServiceFacilitySet.md)
- [Example snippet](../generated/xml-snippets/ServiceFacilitySet.xml)
- [General NeTEx definition ](../generated/xcore/ServiceFacilitySet.html)

> [Template](../templates/ServiceFacilitySet.xml)

## JourneyMeeting
**todo** we will have to check if we continue to use it

(NeTEx-2, 7.2.7.3.5)
A JOURNEY MEETING describes the possibility to plan the schedules according to various interchange possibilities:
•	Interchange with another service, of which only the arrival or departure time is known.
•	More generally, service scheduled according to the time fixed for an external event, which will feed, or be fed by, this service.
•	Organisation of a meeting (hub) between several services, during a defined time band; this is a simplified specification of several interchanges. If needed this could be de-scribed in detail using several INTERCHANGE RULEs or SERVICE JOURNEY IN-TERCHANGEs.
•	Specification of a rendez-vous (time and place) for any journey that can meet the ap-pointment.

A JOURNEY MEETING may be related to one or several SERVICE JOURNEYs, which are planned according to this JOURNEY MEETING. It may be timed by an earliest time (e.g. the arrival time of a feeder line, plus the duration of a possible transfer) or by a latest time (e.g. the opening hour of the school served by the journey), or both (e.g. the time band of a hub).

A JOURNEY MEETING is located at one or several STOP POINTs, which shall be also clas-sified as TIMING POINTs. It is planned in principle for VEHICLE JOURNEYs specified for the same DAY TYPE. The timing reference of these VEHICLE JOURNEYs will probably be chosen according to the JOURNEY MEETING specified.

In NeTEx consequences of any DEFAULT INTERCHANGE or JOURNEY MEETING used in the planning phase that needs to be exchanged should be expressed as the resulting SERVICE JOURNEY timings, INTERCHANGE RULEs and/or SERVICE JOURNEY INTERCHANGEs.
InterchangeRules are used to connect different ServiceJourney

[//]: # (TODO: Add JourneyMeeting links)

- [Swiss profile NeTEx definition](../generated/markdown-examples/JourneyMeeting.md)
- [Example snippet](../generated/xml-snippets/JourneyMeeting.xml)
- [General NeTEx definition ](../generated/xcore/JourneyMeeting.html)
- 
> [Template](../templates/JourneyMeeting.xml)


## InterchangeRule

An INTERCHANGE RULE defines the possibility of interchanging between two SERVICE JOURNEYs at the same or different SCHEDULED STOP POINTs — where at least one journey is specified indirectly via DIRECTION, LINE or VEHICLE JOURNEY, rather than as an explicit journey pair.
The rule specifies criteria (e.g. MODE, LINE, DIRECTION) that a candidate feeder or distributor SERVICE JOURNEY must fulfil. The SCHEDULED STOP POINT is defined separately for the feeder and distributor side.


- [Swiss profile NeTEx definition](https://github.com/openTdataCH/netexRealisationGuideSwitzerland/blob/3825500c6a13a9a2cc1e89f3f6993acf881a3507/generated/markdown-examples/InterchangeRule_UMTEIGZ.md)
- [Example snippet](https://github.com/openTdataCH/netexRealisationGuideSwitzerland/blob/c543acb1750e60bb369f53e3cbd10e1fac884ab0/generated/xml-snippets/InterchangeRule_UMTEIGZ.xml)
- [General NeTEx definition ](../generated/xcore/InterchangeRule.html)
## InterchangeRuleParameter
(NeTEx-2, 7.2.8.3.2) 
Type for INTERCHANGE RULE PARAMETER of the InterchangeRuleFilteringGroup. 

- [Swiss profile NeTEx definition](todo)
- [Example snippet](todo)
- [General NeTEx definition ](../generated/xcore/InterchangeRuleParameter.html)
## InterchangeRuleTiming
(NeTEx-2, 7.2.8.3.3) 
Conditions for considering JOURNEYs to meet or not to meet, specified indirectly: by a particular MODE, DIRECTION or LINE. Such conditions may alternatively be specified directly, indicating the corresponding services. In this case they are either a SERVICE JOURNEY PATTERN INTERCHANGE or a SERVICE JOURNEY INTERCHANGE. 

- [Swiss profile NeTEx definition](todo)
- [Example snippet](todo)
- - [General NeTEx definition ](../generated/xcore/InterchangeRuleTiming.html)


