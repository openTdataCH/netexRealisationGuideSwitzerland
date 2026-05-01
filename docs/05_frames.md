# The NeTEx Structure


## PublicationDelivery

`PublicationDelivery` is the root element of NeTEx XML.

### Purpose
NeTEx is divided into [frames](#frames), containers for elements of a specific domain. These frames are introduced below.

### Tables
[Swiss profile tables](../generated/markdown-examples/PublicationDelivery.md)

*→ [Original NeTEx table](../generated/xcore/PublicationDelivery.xml)*

### Example
[XML Snippet](../generated/xml-snippets/PublicationDelivery.xml)

*→ [Template](../templates/PublicationDelivery.xml)*

### Usage Hints
- Basically, the containers could be defined arbitrarily. We are using the most common used version.

## Frames

We use the following frames in Switzerland:

| Frame                                                                | Description                                                                                                                             |
|----------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------|
| [CompositeFrame](#CompositeFrame)                                    | Container for the FrameDefaults and the other frames.                                                                                   |
| [ResourceFrame](10_common.md#ResourceFrame)                          | General purpose components such as ORGANISATIONSs VEHICLE TYPEs and code values. VEHICLE TYPE is not used.                              |
| [SiteFrame](06_stops.md#SiteFrame)                                   | SITEs, STOP PLACEs. POINTS OF INTEREST and other fixed objects.                                                                         |
| [ServiceFrame](07_service.md#ServiceFrame)                           | Network description elements such as LINEs, ROUTEs, etc. and Tactical Planning elements such as SCHEDULED STOP POINTs, JOURNEY PATTERNs |
| [ServiceCalendarFrame](08_service_calendars.md#ServiceCalendarFrame) | SKI uses principally `AvailabilyConditions`                                                                                             |
| [TimetableFrame](09_timetable.md#TimeTableFrame)                     | Timetable elements: SERVICE JOURNEYs with timings.                                                                                      |

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

[Swiss profile NeTEx definition](../generated/markdown-examples/CompositeFrame.md)

*→ [General NeTEx definition](../generated/xcore/CompositeFrame.html)*

#### Example

[Example snippet](../generated/xml-snippets/CompositeFrame.xml)

*→ [Template](../templates/CompositeFrame.xml)*









