# Timetables




## TimetableFrame
> *→ [Glossary definition](A4_annex_glossary.md#timetableframe)*

### 1. Purpose

A ***TimetableFrame*** contains the operational journey definitions — the actual trips that run on the network. It groups *ServiceJourneys*, *TemplateServiceJourneys*, and *InterchangeRules* that together describe the timetabled service offering.


### 2. Contained Elements

- ***vehicleJourneys*** – collection of journey types:
  -  ***ServiceJourney*** - describes an individual timetabled journey
  -  **TemplateServiceJourney** - describes a set of journeys repeating at a certain frequency
  -  The Swiss profile only models journeys that are available to the passengers
- ***TrainNumber*** - each *(Template)ServiceJourney* is mapped one-to-one to exactly one *TrainNumber*
- ***PassingTimes*** - describe the times of vehicles at points in their journey
- ***InterchangeRule***s - describe interchanges between journeys
- ***NoticeAssignment***s - link *Notices* to specific journeys or stop points within journeys
- ***ServiceFacilitySet***s - describe the various services and facilities offered by the vehicles of a journey


### 3. Table

[//]: # (TODO: Add TimetableFrame links)
> *→ [General NeTEx definition ](generated/xcore/TimetableFrame.html)*

TODO INSERT: [Swiss profile NeTEx definition](generated/markdown-examples/TimetableFrame.md)

> *→ [Template](../templates/TimetableFrame.xml)*

### 4. Example
TODO INSERT: [Example snippet](generated/xml-snippets/TimetableFrame.xml)


### 5. Frame Relationships

TimetableFrame depends on **ServiceFrame** for JourneyPatterns and Lines referenced by ServiceJourneys. It depends on **ResourceFrame** for Operator definitions. **VehicleScheduleFrame** may reference journeys defined here for block and duty scheduling. TimetableFrame is typically wrapped in a **CompositeFrame** within a PublicationDelivery.




## ServiceJourney
> *→ [Glossary definition](A4_annex_glossary.md#ServiceFrame)*

### 1. Purpose

A **ServiceJourney** represents a planned trip in the timetable operating on a recurring schedule. It defines the stop sequence via reference to a *JourneyPattern*, includes scheduled passing times, and specifies operational details such as operator and days of operation. Unlike *DatedServiceJourney*, which represents a concrete instance on a specific date, *ServiceJourney* is the reusable template used across multiple dates via *DayType* definitions

### 2. Table

> *→ [General NeTEx definition ](generated/xcore/ServiceJourney.html)*

TODO INSERT [Swiss profile NeTEx definition](generated/markdown-examples/ServiceJourney.md)

> *→ [Template](../templates/ServiceJourney.xml)*

### 3. Example

TODO INSERT[Example snippet](generated/xml-snippets/ServiceJourney.xml)


### 4. Usage Notes

- **Template vs. Instance:** *ServiceJourney* is the template; *DatedServiceJourney* represents concrete daily instances.
- **Consistency:** A *ServiceJourney* must reference exactly one *JourneyPattern*. The pattern's stop sequence is authoritative.
- **Stop Times:** Each stop in the referenced *JourneyPattern* must have exactly one *TimetabledPassingTime* entry with *ArrivalTime* and/or *DepartureTime*.
- **Day Governance:** DayType references control on which days the journey operates; per-date deviations belong to *DatedServiceJourney*.
- **Validation:** Ensure *journeyPatternRef*, *lineRef*, and *operatorRef* are consistent and reference existing objects.


## TemplateServiceJourney

### 1. Purpose

A ***TemplateServiceJourney*** represents a sequence of planned trips. It is similar to the *ServiceJourney*, but it is used if there is a frequency defined at which the trips are scheduled on an operating day. 

### 2. Table

[//]: # (TODO: Add TemplateServiceJourney links)
> *→ [General NeTEx definition ](generated/xcore/TemplateServiceJourney.html)*

TODO INSERT [Swiss profile NeTEx definition](generated/markdown-examples/TemplateServiceJourney.md)

> *→ [Template](../templates/TemplateServiceJourney.xml)*


### 3. Example

TODO INSERT [Example snippet](generated/xml-snippets/TemplateServiceJourney.xml)

## OccupancyView

### 1. Purpose

***OccupancyView*** can be used on the *Journey*, *JourneyPart*, and *TimetabledPassingTime* elements. Used for predicted and planned occupancies of vehicles.

### 2. Table

> *→ [General NeTEx definition ](generated/xcore/OccupancyView.html)*

TODO INSERT [Swiss profile NeTEx definition](generated/markdown-examples/OccupancyView.md)

> *→ [Template](../templates/OccupancyView.xml)*

### 3. Example

- [Example snippet](generated/xml-snippets/OccupancyView.xml)




## TrainNumber

### 1. Purpose

Codes assigned to particular journeys (*ServiceJourney*, *TemplateServiceJourney*) when operated by trains. *ServiceJourney*s can in principle have multiple different *TrainNumber*s whereas a *JourneyPart* can only reference a single one.

### 2. Table

> *→ [General NeTEx definition ](generated/xcore/TrainNumber.html)*

TODO INSERT [Swiss profile NeTEx definition](generated/markdown-examples/TrainNumber.md)

> *→ [Template](../templates/TrainNumber.xml)*

 ### 3. Example
 
 TODO INSERT [Example snippet](generated/xml-snippets/TrainNumber.xml)



## TimetabledPassingTime

### 1. Purpose

Long-term planned time data concerning public transport vehicles passing a particular *PointInJourneyPattern* on a specified vehicle journey for a certain *DayType*. 

### 2. Table

> *→ [General NeTEx definition ](generated/xcore/TimetabledPassingTime.html)*

 TODO INSERT [Swiss profile NeTEx definition](generated/markdown-examples/TimetabledPassingTime.md)

> *→ [Template](../templates/TimetabledPassingTime.xml)*

### 3. Example

[Example snippet](generated/xml-snippets/TimetabledPassingTime.xml)


### 4. Usage Notes

- Note that for journeys lasting more than one day, *DayOffset* is available.
- If *DepartureTime* is not on the same day as *ArrivalTime* this information will be provided using *WaitingTime*.


## InterchangeRule

### 1. Purpose

An ***InterchangeRule*** defines the possibility of interchanging between two *ServiceJourney*s at the same or different *ScheduledStopPoint*s — where at least one journey is specified indirectly via *Direction*, *Lne* or the VEHICLE JOURNEY (? TODO), rather than as an explicit journey pair. The rule specifies criteria (e.g. mode, *Line*, *Direction*) that a candidate feeder or distributor journey must fulfil.

### 2. Table

> *→ [General NeTEx definition ](generated/xcore/InterchangeRule.html)*

TODO INSERT [Swiss profile NeTEx definition](https://github.com/openTdataCH/netexRealisationGuideSwitzerland/blob/3825500c6a13a9a2cc1e89f3f6993acf881a3507/generated/markdown-examples/InterchangeRule_UMTEIGZ.md)

> *→ [Template]*

### 3. Example

[Example snippet](https://github.com/openTdataCH/netexRealisationGuideSwitzerland/blob/c543acb1750e60bb369f53e3cbd10e1fac884ab0/generated/xml-snippets/InterchangeRule_UMTEIGZ.xml)

### 4. Usage Notes

- The *ScheduledStopPoint* is defined separately for the feeder and distributor side.


## InterchangeRuleParameter -> TODO
(NeTEx-2, 7.2.8.3.2) 
Type for INTERCHANGE RULE PARAMETER of the InterchangeRuleFilteringGroup. 
- [General NeTEx definition ](generated/xcore/InterchangeRuleParameter.html)
- [Swiss profile NeTEx definition](todo)
- [Example snippet](todo)

## InterchangeRuleTiming -> TODO
(NeTEx-2, 7.2.8.3.3) 
Conditions for considering JOURNEYs to meet or not to meet, specified indirectly: by a particular MODE, DIRECTION or LINE. Such conditions may alternatively be specified directly, indicating the corresponding services. In this case they are either a SERVICE JOURNEY PATTERN INTERCHANGE or a SERVICE JOURNEY INTERCHANGE. 
- [General NeTEx definition ](generated/xcore/InterchangeRuleTiming.html)
- [Swiss profile NeTEx definition](todo)
- [Example snippet](todo)




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



## ServiceFacilitySet -> TODO: move to Common

Set of FACILITies available for a SERVICE JOURNEY or a JOURNEY PART. The set may be available only for a specific VEHICLE TYPE within the SERVICE (e.g. carriage equipped with low floor). 

[//]: # (TODO: Add ServiceFacilitySet links)
- [General NeTEx definition ](generated/xcore/ServiceFacilitySet.html)
- [Swiss profile NeTEx definition](generated/markdown-examples/ServiceFacilitySet.md)
- [Example snippet](generated/xml-snippets/ServiceFacilitySet.xml)

> [Template](../templates/ServiceFacilitySet.xml)

## JourneyMeeting -> TODO: Probably to be removed
tbd

[//]: # (TODO: Add JourneyMeeting links)
- [General NeTEx definition ](generated/xcore/JourneyMeeting.html)
- [Swiss profile NeTEx definition](generated/markdown-examples/JourneyMeeting.md)
- [Example snippet](generated/xml-snippets/JourneyMeeting.xml)

> [Template](../templates/JourneyMeeting.xml)


