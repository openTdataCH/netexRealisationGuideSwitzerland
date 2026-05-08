# The NeTEx Structure

## PublicationDelivery

Any valid XML document must start with one root element.
`PublicationDelivery` is the root element of NeTEx XML. 

### Purpose

In addition to linking to the NeTEx XML schema, this element is used to specify the publication timestamp and the 
participant's identifier. 

### Tables
- [Swiss profile tables](../generated/markdown-examples/PublicationDelivery.md)

*→ [Original NeTEx table](../generated/netex-html/PublicationDelivery.html)*

### Example
- [XML Snippet](../generated/xml-snippets/PublicationDelivery.xml)

*→ [Template](../templates/PublicationDelivery.xml)*

### Usage Hints

Basically, the containers could be defined arbitrarily. We are using the most common used version.

## Frames

NeTEx is divided into [frames](#frames), containers for elements of a specific domain. These frames are introduced below.

We use the following frames in Switzerland:

| Frame                                                                | Description                                                                                                                                                                                                                            |
|----------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [CompositeFrame](#CompositeFrame)                                    | Container for the `FrameDefaults` and the other frames.                                                                                                                                                                                |
| [ResourceFrame](10_common.md#ResourceFrame)                          | General purpose elements such as `ResponsibilitySet`, `Organisation`, `Operator`, `SiteFacilitySet` and `ServiceFacilitySet`. `TypeOfProductCategory` and `TypeOfNotice` are to be defined in a `ValueSet`. `VehicleType` is not used. |
|                                                                      |                                                                                                                                                                                                                                        |
| [SiteFrame](06_stops.md#SiteFrame)                                   | Contains the physical infrastructure model: Encloses elements describing locations like `Site`, `StopPlace`, `Quay` and `TopographicPlace`.                                                                                            |
| [ServiceFrame](07_service.md#ServiceFrame)                           | Contains, among other, the network model with elements such as `Line` and `Route`, the service pattern model with `ScheduledStopPoint` and `JourneyPattern` and `Connection` elements for the topological model of interchanges.       |
| [ServiceCalendarFrame](08_service_calendars.md#ServiceCalendarFrame) | Contains calendar specific elements like `AvailabilityConditions`, `ServiceCalendar` and `DayType` that are referenced in other frames like the `TimetableFrame`.                                                                      |
| [TimetableFrame](09_timetable.md#TimeTableFrame)                     | Contains the operational journey definitions with elements like `ServiceJourney`, `PassingTimes`, `InterchangeRule` and others.                                                                                                          |

> The following frames are **not to be used** in Switzerland:
> - `GeneralFrame`
> - `InfrastructureFrame`
> - `VehicleScheduleFrame`
> - `DriverScheduleFrame`
> - `FareFrame`

### CompositeFrame

#### Purpose
The `CompositeFrame` is the container for the `FrameDefaults` and the other frames like `ResourceFrame`, `SiteFrame`, `ServiceFrame`, `ServiceCalendarFrame` and `TimeTableFrame`, 
appearing in this order.

#### Table
- [Swiss profile NeTEx definition](../generated/markdown-examples/CompositeFrame.md)

*→ [General NeTEx definition](../generated/netex-html/CompositeFrame.html)*

#### Example
- [Example snippet](../generated/xml-snippets/CompositeFrame.xml)

*→ [Template](../templates/CompositeFrame.xml)*









