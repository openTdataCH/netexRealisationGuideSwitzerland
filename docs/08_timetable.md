# Timetables




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
- [General NeTEx definition ](generated/xcore/TimetableFrame.html)
- [Swiss profile NeTEx definition](generated/markdown-examples/TimetableFrame.md)
- [Example snippet](generated/xml-snippets/TimetableFrame.xml)

> [Template](../templates/TimetableFrame.xml)

## ServiceJourney

A SERVICE JOURNEY is a VEHICLE JOURNEY on which passengers will be allowed to board or alight from vehicles at stops. It describes the service between an origin and a destination, as advertised to the public.

[//]: # (TODO: Add ServiceJourney links)
- [General NeTEx definition ](generated/xcore/ServiceJourney.html)
- [Swiss profile NeTEx definition](generated/markdown-examples/ServiceJourney.md)
- [Example snippet](generated/xml-snippets/ServiceJourney.xml)

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
- [General NeTEx definition ](generated/xcore/ServiceJourney.html)
- [Swiss profile NeTEx definition](generated/markdown-examples/ServiceJourney.md)

> [Template](../templates/ServiceJourney.xml)

### 3. Example

[//]: # (TODO: Add ServiceJourney links)
- [Example snippet](generated/xml-snippets/ServiceJourney.xml)


### 4. Usage Notes / Pitfalls

- **Template vs. Instance:** ServiceJourney is the template; DatedServiceJourney represents concrete daily instances.
- **Consistency:** A ServiceJourney must reference exactly one JourneyPattern. The pattern's stop sequence is authoritative.
- **Stop Times:** Each stop in the referenced JourneyPattern must have exactly one TimetabledPassingTime entry with ArrivalTime and/or DepartureTime.
- **Day Governance:** DayType references control on which days the journey operates; per-date deviations belong to DatedServiceJourney.
- **Validation:** Ensure journeyPatternRef, lineRef, and operatorRef are consistent and reference existing objects.


## TemplateServiceJourney

A TEMPLATE SERVICE JOURNEY is a VEHICLE JOURNEY on which passengers will be allowed to board or alight from vehicles at stops and that reapeats with a certain frequency. It describes the service between an origin and a destination, as advertised to the public. Only to be used if a frequency has been specified for the JOURNEY. 

[//]: # (TODO: Add TemplateServiceJourney links)
- [General NeTEx definition ](generated/xcore/TemplateServiceJourney.html)
- [Swiss profile NeTEx definition](generated/markdown-examples/TemplateServiceJourney.md)
- [Example snippet](generated/xml-snippets/TemplateServiceJourney.xml)

> [Template](../templates/TemplateServiceJourney.xml)



## AvailabilityCondition -> TODO: move to Common

A specific type of VALIDITY CONDITION used to specify a set of temporal conditions that can be associated with an ENTITY, for example that a STOP PLACE is open on a particular DAY TYPE.

[//]: # (TODO: Add AvailabilityCondition links)
- [General NeTEx definition ](generated/xcore/AvailabilityCondition.html)
- [Swiss profile NeTEx definition](generated/markdown-examples/AvailabilityCondition.md)
- [Example snippet](generated/xml-snippets/AvailabilityCondition.xml)

> [Template](../templates/AvailabilityCondition.xml)



## Timeband -> TODO: move to Common


[//]: # (TODO: Add Timeband links)
- [General NeTEx definition ](generated/xcore/Timeband.html)
- [Swiss profile NeTEx definition](generated/markdown-examples/Timeband.md)
- [Example snippet](generated/xml-snippets/Timeband.xml)

> [Template](../templates/Timeband.xml)



## NoticeAssignment -> TODO: move to Common

The assignment of a NOTICE to any model element. Can be used in particular to show an exception in a JOURNEY PATTERN, a COMMON SECTION, or a VEHICLE JOURNEY, possibly specifying at which POINT IN JOURNEY PATTERN the validity of the NOTICE starts and ends respectively.

[//]: # (TODO: Add NoticeAssignment links)
- [General NeTEx definition ](generated/xcore/NoticeAssignment.html)
- [Swiss profile NeTEx definition](generated/markdown-examples/NoticeAssignment.md)
- [Example snippet](generated/xml-snippets/NoticeAssignment.xml)

> [Template](../templates/NoticeAssignment.xml)


## OccupancyView

The OccupancyView element can be used on the JOURNEY, JOURNEY PART, and TIMETABLED PASSING TIME elements. Used for predicted and planned occupancies of vehicles.

[//]: # (TODO: Add OccupancyView links)
- [General NeTEx definition ](generated/xcore/OccupancyView.html)
- [Swiss profile NeTEx definition](generated/markdown-examples/OccupancyView.md)
- [Example snippet](generated/xml-snippets/OccupancyView.xml)

> [Template](../templates/OccupancyView.xml)



## TrainNumber

Codes assigned to particular VEHICLE JOURNEYs when operated by TRAINs or COMPOUND TRAINs. ServiceJourneys can in principle have multiple different TrainNumbers whereas a JourneyPart can only reference a single one.

[//]: # (TODO: Add TrainNumber links)
- [General NeTEx definition ](generated/xcore/TrainNumber.html)
- [Swiss profile NeTEx definition](generated/markdown-examples/TrainNumber.md)
- [Example snippet](generated/xml-snippets/TrainNumber.xml)

> [Template](../templates/TrainNumber.xml)



## TimetabledPassingTime

Long-term planned time data concerning public transport vehicles passing a particular POINT IN JOURNEY PATTERN on a specified VEHICLE JOURNEY for a certain DAY TYPE. Note that for Journeys lasting more than one day, DayOffset is available. If DepartureTime is not on the same day as ArrivalTime this information will be provided using WaitingTime.

[//]: # (TODO: Add TimetabledPassingTime links)
- [General NeTEx definition ](generated/xcore/TimetabledPassingTime.html)
- [Swiss profile NeTEx definition](generated/markdown-examples/TimetabledPassingTime.md)
- [Example snippet](generated/xml-snippets/TimetabledPassingTime.xml)

> [Template](../templates/TimetabledPassingTime.xml)

## ServiceFacilitySet -> TODO: move to Common

Set of FACILITies available for a SERVICE JOURNEY or a JOURNEY PART. The set may be available only for a specific VEHICLE TYPE within the SERVICE (e.g. carriage equipped with low floor). 

[//]: # (TODO: Add ServiceFacilitySet links)
- [General NeTEx definition ](generated/xcore/ServiceFacilitySet.html)
- [Swiss profile NeTEx definition](generated/markdown-examples/ServiceFacilitySet.md)
- [Example snippet](generated/xml-snippets/ServiceFacilitySet.xml)

> [Template](../templates/ServiceFacilitySet.xml)

## JourneyMeeting
tbd

[//]: # (TODO: Add JourneyMeeting links)
- [General NeTEx definition ](generated/xcore/JourneyMeeting.html)
- [Swiss profile NeTEx definition](generated/markdown-examples/JourneyMeeting.md)
- [Example snippet](generated/xml-snippets/JourneyMeeting.xml)

> [Template](../templates/JourneyMeeting.xml)


## InterchangeRule

An INTERCHANGE RULE defines the possibility of interchanging between two SERVICE JOURNEYs at the same or different SCHEDULED STOP POINTs — where at least one journey is specified indirectly via DIRECTION, LINE or VEHICLE JOURNEY, rather than as an explicit journey pair.
The rule specifies criteria (e.g. MODE, LINE, DIRECTION) that a candidate feeder or distributor SERVICE JOURNEY must fulfil. The SCHEDULED STOP POINT is defined separately for the feeder and distributor side.

- [General NeTEx definition ](generated/xcore/InterchangeRule.html)
- [Swiss profile NeTEx definition](https://github.com/openTdataCH/netexRealisationGuideSwitzerland/blob/3825500c6a13a9a2cc1e89f3f6993acf881a3507/generated/markdown-examples/InterchangeRule_UMTEIGZ.md)
- [Example snippet](https://github.com/openTdataCH/netexRealisationGuideSwitzerland/blob/c543acb1750e60bb369f53e3cbd10e1fac884ab0/generated/xml-snippets/InterchangeRule_UMTEIGZ.xml)

## InterchangeRuleParameter
(NeTEx-2, 7.2.8.3.2) 
Type for INTERCHANGE RULE PARAMETER of the InterchangeRuleFilteringGroup. 
- [General NeTEx definition ](generated/xcore/InterchangeRule.html)
- [Swiss profile NeTEx definition](todo)
- [Example snippet](todo)




