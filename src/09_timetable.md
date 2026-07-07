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

In ServiceCalender:
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
- `passingTimes`- describe the times of vehicles at points in their journey
- `journeyInterchanges` – collection of ServiceJourneyInterchanges describing planned connections and through-services between journeys
- `NoticeAssignment`s- link `Notice`s to specific journeys or stop points within journeys
- `ServiceFacilitySet`s- describe the various services and facilities offered by the vehicles of a journey


### Table
- [Swiss profile NeTEx definition](../site/tables/TimetableFrame.md)

*→ [General NeTEx definition ](../generated/netex-html/TimetableFrame.html)*

### Example
- [Example snippet](../site/xml-snippets/TimetableFrame.xml)

*→ [Template](./templates/TimetableFrame.xml)*

### Frame Relationships
`TimetableFrame` depends on `ServiceFrame`for `JourneyPattern`s and `Line`s referenced by `ServiceJourney`s. It depends on `ResourceFrame` for `Operator` definitions. `VehicleScheduleFrame` may reference journeys defined here for block and duty scheduling. `TimetableFrame` is typically wrapped in a `CompositeFrame`within a `PublicationDelivery`.

## ServiceJourney
*→ [Glossary definition](A4_annex_glossary.md#servicejourney)*

### Purpose
A `ServiceJourney` represents a planned trip in the timetable operating on a recurring schedule. It defines the stop sequence via reference to a `JourneyPattern`, includes scheduled passing times, and specifies operational details such as operator and days of operation. Unlike `DatedServiceJourney`, which represents a concrete instance on a specific date, `ServiceJourney` is the reusable template used across multiple dates via `DayType` definitions

### Table
- [Swiss profile NeTEx definition](../site/tables/ServiceJourney.md)

*→ [General NeTEx definition ](../generated/netex-html/ServiceJourney.html)*

### Example
- [Example snippet](../site/xml-snippets/ServiceJourney.xml)

*→ [Template](./templates/ServiceJourney.xml)*


### Usage Notes

- **Template vs. Instance:** `ServiceJourney` is the template; `DatedServiceJourney` represents concrete daily instances.
- **Consistency:** A `ServiceJourney` must reference exactly one `JourneyPattern`. The pattern's stop sequence is authoritative.
- **Stop Times:** Each stop in the referenced `JourneyPattern` must have exactly one `TimetabledPassingTimes` entry with `ArrivalTime` and/or `DepartureTime`.
- **Day Governance:** `DayType` references control on which days the journey operates; per-date deviations belong to `DatedServiceJourney`.
- **Validation:** Ensure `JourneyPatternRef`, `LineRef`, and `OperatorRef` are consistent and reference existing objects.
- We assume that a swiss journey exists for almost every `ServiceJourney`. In those cases the `id` is also set to the `sjyid`. Possible problematic cases: some cableways, when the frequency group is not done right (we try to remove those cases), foreign journeys. In those cases the `id` will contain a `_gen` substring.
- A `ServiceJourney`can be associated with exactly one `ServiceJourneyPattern` and `TimeDemandType`.
- id-attribute needs to be kept stable between exports.

## TemplateServiceJourney
*→ [Glossary definition](A4_annex_glossary.md#templateservicejourney)*
### Purpose
A `TemplateServiceJourney` represents a sequence of planned trips. It is similar to the `ServiceJourney`, but it is used if there is a frequency defined at which the trips are scheduled on an operating day. 

A frequency is specified in a `HeadwayJourneyGroup` (e.g. every 20 minutes). The `TemplateServiceJourney` may thus represent multiple journeys or it could be used simply as a template for adding extra date journeys after the planning phase. 

### Table
- [Swiss profile NeTEx definition](../site/tables/TemplateServiceJourney.md)

*→ [General NeTEx definition ](../generated/netex-html/TemplateServiceJourney.html)*

### Example
- [Example snippet](../site/xml-snippets/TemplateServiceJourney.xml)

*→ [Template](./templates/TemplateServiceJourney.xml)*

### Usage Notes
- `HeadwayJourneyGroup` holds all the frequency-based information of the journey, as for example when the stops of the journey are serviced the first/last time and in what interval (or at which frequency, respectively). 
- Note that in addition to `HeadwayJourneyGroup`, standard NeTEx also features `RhythmicalJourneyGroup` to specifiy, e.g., departures at 15, 27 and 40 minutes past the hour - this is not used in the Swiss profile.
- For sjyid see information about [frequencies](uc14_frequencies.md).
- id-attribute needs to be kept stable between exports.


## OccupancyView

### Purpose
`OccupancyView`can be used on the `Journey`, `JourneyPart`, and `TimetabledPassingTime` elements. Used for predicted and planned occupancies of vehicles.

### Table
- [Swiss profile NeTEx definition](../site/tables/OccupancyView.md)

*→ [General NeTEx definition ](../generated/netex-html/OccupancyView.html)*

### Example
- [Example snippet](../site/xml-snippets/OccupancyView.xml)

*→ [Template](./templates/OccupancyView.xml)*

### Usage Notes
We currently don't use OccupancyView.


## TrainNumber
*→ [Glossary definition](A4_annex_glossary.md#trainnumber)*

### Purpose

Codes assigned to particular journeys (`ServiceJourney`, `TemplateServiceJourney`) when operated by trains. `ServiceJourney`s can in principle have multiple different `TrainNumber`s whereas a `JourneyPart` can only reference a single one.

### Table
- [Swiss profile NeTEx definition](../site/tables/TrainNumber.md)

*→ [General NeTEx definition ](../generated/netex-html/TrainNumber.html)*

### Example
- [Example snippet](../site/xml-snippets/TrainNumber.xml)

*→ [Template](./templates/TrainNumber.xml)*

### Usage Note
- id-attribute needs to be kept stable between exports.

## TypeOfService

### Purpose

`TypeOfService` indicates the purpose of a `ServiceJourney`, for example, whether if it is a passenger transport or a garage run-in. We only use `ch:1:TypeOfService:1`

### Table
- [Swiss profile NeTEx definition](../site/tables/TypeOfService.md)

*→ [General NeTEx definition](../generated/netex-html/TypeOfService.html)*

### Example
- [XML Snippet](../site/xml-snippets/TypeOfService.xml)

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
*→ [Glossary definition](A4_annex_glossary.md#timetabledpassingtime)*
> We don't use TimetabledPassingTime. We will remove this. We use TimeDemandType now.

### Purpose

Long-term planned time data concerning public transport vehicles passing a particular `PointInJourneyPattern` on a specified vehicle journey for a certain `DayType`. 

### Table
- [Swiss profile NeTEx definition](../site/tables/TimetabledPassingTime_deprecated.md)

*→ [General NeTEx definition ](../generated/netex-html/TimetabledPassingTime.html)*

### Example
- [Example snippet](../site/xml-snippets/TimetabledPassingTime_deprecated.xml)

*→ [Template](./templates/TimetabledPassingTime_deprecated.xml)*

### Usage Notes
- Note that for journeys lasting more than one day, `DayOffset` is available.
- If `DepartureTime` is not on the same day as `ArrivalTime` this information will be provided using `WaitingTime`.
- We use sjyid whenever possible as the attribute. However, there are different types of `ServiceJourney`s that don't have one:
  - foreign `ServiceJourney`s
  - perhaps some touristic offers
  - frequency-based journeys that are wrongly modeled in HRDF (will be removed)
- We store the sjyid in different places `id`, `privateCodes/PrivateCode`, `KeyList`. This allows different importing systems to find the sjyid.


## ServiceJourneyInterchange
*→ [Glossary definition](A4_annex_glossary.md#servicejourneyinterchange)*

### Purpose
The standard states: "In some cases, a SERVICE JOURNEY INTERCHANGE expresses an interchange between two SERVICE JOURNEYs specifically planned to be operated by the same physical vehicle. This concept is for instance used for circular lines and coupled journeys. This means that passenger information should be adapted to the fact that the passenger should not change vehicle as the transfer is implicit. In this case it is also important that operation control staff is aware of the consequences to passengers if the operation is altered in such a way that two different vehicles are used for the two involved SERVICE JOURNEYs."

`StaySeated=true` should be used for through-services (Durchbindung) and joining (Vereinigung). While splitting (Flügelzug) technically involves different vehicle parts, the passenger does not leave the train — however, they may need to move to the correct coach. For splitting, `StaySeated=false` combined with `ChangeWithinVehicle=true` is therefore the correct modelling. See [uc02 Joining and splitting](uc02_joining_splitting.md).

### Table

- [Swiss profile NeTEx definition](../site/tables/ServiceJourneyInterchange.md)

*→ [General NeTEx definition ](../generated/netex-html/ServiceJourneyInterchange.html)*

### Example
- [Example snippet](../site/xml-snippets/ServiceJourneyInterchange.xml)

*→ [Template](./templates/ServiceJourneyInterchange.xml)*

### Usage Notes
- `ServiceJourneyInterchange` is placed in the `TimetableFrame` within the `journeyInterchanges` collection.
- `StaySeated=true` indicates that the passenger remains in the vehicle — typically used for through-services (Durchbindung), splitting (Flügelzug) and joining (Vereinigung). See [uc01 Durchbindung](uc01_durchbindung.md).
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
*→ [see ServiceCalenderFrame](./08_service_calendars.md#availabilitycondition)*

## Timeband 
*→ [see ServiceCalenderFrame](./08_service_calendars.md#timeband)*


## NoticeAssignment
*→ [see Common elements](./07_service.md#noticeassignment)*


## ServiceFacilitySet
*→ [see Common elements](./10_common.md#servicefacilityset)*

