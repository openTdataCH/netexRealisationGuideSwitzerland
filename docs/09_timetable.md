# Timetables
In this chapter:
- [TimetableFrame](09_timetable.md#TimetableFrame)
- [ServiceJourney](09_timetable.md#ServiceJourney)
- [TemplateServiceJourney](09_timetable.md#TemplateServiceJourney)
- [OccupancyView](09_timetable.md#OccupancyView)
- [TrainNumber](09_timetable.md#TrainNumber)
- [TimetabledPassingTime](09_timetable.md#TimetabledPassingTime)
- [InterchangeRule](09_timetable.md#InterchangeRule)
- [InterchangeRuleParameter](09_timetable.md#InterchangeRuleParameter)
- [InterchangeRuleTiming](09_timetable.md#InterchangeRuleTiming)

In Service: 
- [NoticeAssignment](07_service.md#NoticeAssignment)
- [ServiceFacilitySet](10_common.md#ServiceFacilitySet)

In ServiceCalender:
- [AvailabilityCondition](08_service_calendars.md#AvailabilityCondition)
- [Timeband](08_service_calendars.md#Timeband)



## TimetableFrame
*→ [Glossary definition](A4_annex_glossary.md#timetableframe)*

### Purpose

A `TimetableFrame` contains the operational journey definitions — the actual trips that run on the network. It groups `ServiceJourney`s, `TemplateServiceJourney`s, and `InterchangeRules` that together describe the timetabled service offering.

### Contained Elements
- `vehicleJourneys`– collection of journey types:
  -  `ServiceJourney`- describes an individual timetabled journey
  -  `TemplateServiceJourney`- describes a set of journeys repeating at a certain frequency
  -  The Swiss profile only models journeys that are available to the passengers
- `TrainNumber`- each `(Template)ServiceJourney` is mapped one-to-one to exactly one train number
- `PassingTimes`- describe the times of vehicles at points in their journey
- `InterchangeRule`s- describe interchanges between journeys
- `NoticeAssignment`s- link *Notices* to specific journeys or stop points within journeys
- `ServiceFacilitySet`s- describe the various services and facilities offered by the vehicles of a journey


### Table
[Swiss profile NeTEx definition](../generated/markdown-examples/TimetableFrame.md)

*→ [General NeTEx definition ](../generated/xcore/TimetableFrame.html)*

### Example
[Example snippet](../generated/xml-snippets/TimetableFrame.xml)

*→ [Template](../templates/TimetableFrame.xml)*

### Frame Relationships
TimetableFrame depends on `ServiceFrame`for JourneyPatterns and Lines referenced by ServiceJourneys. It depends on `ResourceFrame` for Operator definitions. `VehicleScheduleFrame` may reference journeys defined here for block and duty scheduling. `TimetableFrame` is typically wrapped in a `CompositeFrame`within a `PublicationDelivery`.

## ServiceJourney
*→ [Glossary definition](A4_annex_glossary.md#ServiceFrame)*

### Purpose
A `ServiceJourney` represents a planned trip in the timetable operating on a recurring schedule. It defines the stop sequence via reference to a `JourneyPattern`, includes scheduled passing times, and specifies operational details such as operator and days of operation. Unlike `DatedServiceJourney`, which represents a concrete instance on a specific date, `ServiceJourney` is the reusable template used across multiple dates via `DayType` definitions

### Table
TODO INSERT [Swiss profile NeTEx definition](../generated/markdown-examples/ServiceJourney.md)

*→ [General NeTEx definition ](../generated/xcore/ServiceJourney.html)*

### Example
[Example snippet](../generated/xml-snippets/ServiceJourney.xml)

*→ [Template](../templates/ServiceJourney.xml)*


### Usage Notes

- **Template vs. Instance:** `ServiceJourney` is the template; `DatedServiceJourney` represents concrete daily instances.
- **Consistency:** A `ServiceJourney` must reference exactly one `JourneyPattern`. The pattern's stop sequence is authoritative.
- **Stop Times:** Each stop in the referenced `JourneyPattern` must have exactly one `TimetabledPassingTime` entry with `ArrivalTime` and/or `DepartureTime`.
- **Day Governance:** DayType references control on which days the journey operates; per-date deviations belong to `DatedServiceJourney`.
- **Validation:** Ensure `JourneyPatternRef`, `LineRef`, and `OperatorRef` are consistent and reference existing objects.

## TemplateServiceJourney

### Purpose
A `TemplateServiceJourney` represents a sequence of planned trips. It is similar to the `ServiceJourney`, but it is used if there is a frequency defined at which the trips are scheduled on an operating day. 

### Table

[Swiss profile NeTEx definition](../generated/markdown-examples/TemplateServiceJourney.md)

*→ [General NeTEx definition ](../generated/xcore/TemplateServiceJourney.html)*

### Example

[Example snippet](../generated/xml-snippets/TemplateServiceJourney.xml)

*→ [Template](../templates/TemplateServiceJourney.xml)*

## OccupancyView

### Purpose

`OccupancyView`can be used on the `Journey`, `JourneyPart`, and `TimetabledPassingTime` elements. Used for predicted and planned occupancies of vehicles.

### Table

[Swiss profile NeTEx definition](../generated/markdown-examples/OccupancyView.md)

*→ [General NeTEx definition ](../generated/xcore/OccupancyView.html)*

### Example

- [Example snippet](../generated/xml-snippets/OccupancyView.xml)
*→ [Template](../templates/OccupancyView.xml)*


## TrainNumber

### Purpose

Codes assigned to particular journeys (`ServiceJourney`, `TemplateServiceJourney`) when operated by trains. `ServiceJourney`s can in principle have multiple different `TrainNumber`s whereas a `JourneyPart` can only reference a single one.

### Table
[Swiss profile NeTEx definition](../generated/markdown-examples/TrainNumber.md)

*→ [General NeTEx definition ](../generated/xcore/TrainNumber.html)*

 ### Example
[Example snippet](../generated/xml-snippets/TrainNumber.xml)

*→ [Template](../templates/TrainNumber.xml)*


## TimetabledPassingTime

### Purpose

Long-term planned time data concerning public transport vehicles passing a particular `PointInJourneyPattern` on a specified vehicle journey for a certain `DayType`. 

### Table
[Swiss profile NeTEx definition](../generated/markdown-examples/TimetabledPassingTime.md)

*→ [General NeTEx definition ](../generated/xcore/TimetabledPassingTime.html)*

### Example
[Example snippet](../generated/xml-snippets/TimetabledPassingTime.xml)

*→ [Template](../templates/TimetabledPassingTime.xml)*

### Usage Notes

- Note that for journeys lasting more than one day, `DayOffset` is available.
- If `DepartureTime` is not on the same day as `ArrivalTime` this information will be provided using `WaitingTime`.


## InterchangeRule

### Purpose

An `InterchangeRule`defines the possibility of interchanging between two `ServiceJourney`s at the same or different `ScheduledStopPoint*` — where at least one journey is specified indirectly via `Direction`, `Line` or the VEHICLE JOURNEY (? TODO), rather than as an explicit journey pair. The rule specifies criteria (e.g. `Mode`, `Line`, `Direction`) that a candidate feeder or distributor journey must fulfil.

### Table

[Swiss profile NeTEx definition](../generated/markdown-examples/InterchangeRule.md)

*→ [General NeTEx definition ](../generated/xcore/InterchangeRule.html)*


### Examples

*→ [General NeTEx definition ](../generated/xcore/InterchangeRule.html)*

#### Interchanges between ServiceJourneys
[Example snippet](../generated/xml-snippets/InterchangeRule_UMSTEIGZ.xml)

#### Interchange between Lines/Directions/Operators
[Example snippet](../generated/xml-snippets/InterchangeRule_UMSTEIGL.xml)


### Usage Notes
- The `ScheduledStopPoint` is defined separately for the feeder and distributor side.
- [See use case Durchbindung](uc01_durchbindung.md)
- [See use case transfers](uc03_transfers.md)

## InterchangeRuleParameter
> **TODO** Finish it.

### Purpose
> **TODO** Finish it.

### Table
[Swiss profile NeTEx definition](../generated/markdown-examples/InterchangeRule_UMTEIGZ.md)

*→ [General NeTEx definition ](../generated/xcore/InterchangeRuleParameter.html)*

### Example
[Example snippet](../generated/xml-snippets/InterchangeRule_UMSTEIGZ.xml)

*→ [Template](../templates/InterchangeRule.xml))*


## InterchangeRuleTiming
> **TODO** Finish it.

### Purpose
> **TODO** Finish it.

Conditions for considering JOURNEYs to meet or not to meet, specified indirectly: by a particular MODE, DIRECTION or LINE. Such conditions may alternatively be specified directly, indicating the corresponding services. In this case they are either a SERVICE JOURNEY PATTERN INTERCHANGE or a SERVICE JOURNEY INTERCHANGE. 

### Table
[Swiss profile NeTEx definition](../generated/markdown-examples/InterchangeRule_UMTEIGZ.md)

- [General NeTEx definition ](../generated/xcore/InterchangeRuleTiming.html)
- 
### Example

[Example snippet](../generated/xml-snippets/InterchangeRule_UMSTEIGZ.xml)

*→ [Template](../templates/InterchangeRule.xml)*

## AvailabilityCondition 
[see ServiceCalenderFrame](./08_service_calendars.md#AvailabilityCondition)

## Timeband 
[see ServiceCalenderFrame](./08_service_calendars.md#Timeband)


## NoticeAssignment -> TODO: move to Common
[see Common elements](./07_service.md#NoticeAssignment)



## ServiceFacilitySet -> TODO: move to Common
[see Common elements](./10_common.md#ServiceFacilitySet)

Set of FACILITies available for a SERVICE JOURNEY or a JOURNEY PART. The set may be available only for a specific VEHICLE TYPE within the SERVICE (e.g. carriage equipped with low floor). 

## JourneyMeeting -> TODO: Probably to be removed
[//]: # (TODO: Add JourneyMeeting links)

### Table
[Swiss profile NeTEx definition](../generated/markdown-examples/JourneyMeeting.md)

*→ [General NeTEx definition ](../generated/xcore/JourneyMeeting.html)*

### Example
[Example snippet](../generated/xml-snippets/JourneyMeeting.xml)

*→ [Template](../templates/JourneyMeeting.xml))*



### Usage Notes
* [See use case Joining and splitting](uc02_joining_splitting.md)

