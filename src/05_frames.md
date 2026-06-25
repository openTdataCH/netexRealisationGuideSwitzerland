# The NeTEx Structure
In this chapter:
- [PublicationDelivery](#PublicationDelivery)
- [Frames](#Frames)
- [CompositeFrame](#CompositeFrame)

## PublicationDelivery
*→ [Glossary definition](A4_annex_glossary.md#PublicationDelivery)*

### Purpose
Any valid XML document must start with one root element.
`PublicationDelivery` is the root element of NeTEx XML. 

In addition to linking to the NeTEx XML schema, this element is used to specify the publication timestamp and the 
participant's identifier. 

### Table
- [Swiss profile tables](../site/tables/PublicationDelivery.md)

*→ [Original NeTEx table](../generated/netex-html/PublicationDelivery.html)*

### Example
- [XML Snippet](../site/xml-snippets/PublicationDelivery.xml)

*→ [Template](./templates/PublicationDelivery.xml)*

### Usage Notes

* Basically, the containers could be defined arbitrarily. We are using the most common used version.
* Be aware that what should be in a Frame in a given file is defined by the organisation of files that are defined in chapter on the [files](04_files.md).

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
| [TimetableFrame](09_timetable.md#TimeTableFrame)                     | Contains the operational journey definitions with elements like `ServiceJourney`, `PassingTimes`, `ServiceJourneyInterchange` and others.                                                                                              |

> The following frames are **not to be used** in Switzerland:
> - `GeneralFrame`
> - `InfrastructureFrame`
> - `VehicleScheduleFrame`
> - `DriverScheduleFrame`
> - `FareFrame`

## CompositeFrame
*→ [Glossary definition](A4_annex_glossary.md#compositeframe)*

### Purpose
The `CompositeFrame` is the container for the `FrameDefaults` and the other frames like `ResourceFrame`, `SiteFrame`, `ServiceFrame`, `ServiceCalendarFrame` and `TimeTableFrame`, 
appearing in this order.

### Table
- [Swiss profile NeTEx definition](../site/tables/CompositeFrame.md)

*→ [General NeTEx definition](../generated/netex-html/CompositeFrame.html)*

### Example
- [Example snippet](../site/xml-snippets/CompositeFrame.xml)

*→ [Template](./templates/CompositeFrame.xml)*









