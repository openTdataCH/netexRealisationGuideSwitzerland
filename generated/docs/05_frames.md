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


| Sub | Element | Usage | Card | Type | Description | Note |
|-----|---------|-------|------|------|-------------|------|
|  | PublicationDelivery | mandatory | 1..1 | PublicationDeliveryStructure | A set of NeTEx objects as assembled by a publication request or other service. Provides a general purpose wrapper for NeTEx data content. |  |
| + | PublicationTimestamp | mandatory | 1..1 | xsd:dateTime | Time of output of data. |  |
| + | ParticipantRef | mandatory | 1..1 | siri:ParticipantCodeType | Identifier of system requesting Data. |  |
| + | dataObjects | mandatory | 0..1 | unknown | NeTEx Entities of any type. |  |
| ++ | [CompositeFrame](CompositeFrame.md) | mandatory | 1..1 | unknown | A container VERSION FRAME that groups a set of content VERSION FRAMsE to which the same VALIDITY CONDITIONs have been assigned. |  |



*→ [Original NeTEx table](../generated/netex-html/PublicationDelivery.html)*

### Example


```xml
<?xml version="1.0" encoding="UTF-8"?>
<PublicationDelivery  xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" version="1.0" xsi:schemaLocation="http://www.netex.org.uk/netex ../xsd/xsd/NeTEx_publication.xsd">
  <PublicationTimestamp>2026-03-30T12:00:00</PublicationTimestamp>
  <ParticipantRef>SKI-Templates</ParticipantRef>
  <dataObjects>
    <CompositeFrame id="ch:1:CompositeFrame" version="1">
      <FrameDefaults/>
      <frames>
        <ResourceFrame id="ch:1:ResourceFrame" version="1"/>
        <SiteFrame id="ch:1:SiteFrame" version="1"/>
        <ServiceFrame id="ch:1:ServiceFrame" version="1"/>
        <ServiceCalendarFrame id="ch:1:ServiceCalendarFrame" version="1"/>
        <TimetableFrame id="ch:1:TimetableFrame:j23" version="1"/>
      </frames>
    </CompositeFrame>
  </dataObjects>
</PublicationDelivery>

```



*→ [Template](../templates/PublicationDelivery.xml)*

### Usage Notes

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

## CompositeFrame
*→ [Glossary definition](A4_annex_glossary.md#compositeframe)*

### Purpose
The `CompositeFrame` is the container for the `FrameDefaults` and the other frames like `ResourceFrame`, `SiteFrame`, `ServiceFrame`, `ServiceCalendarFrame` and `TimeTableFrame`, 
appearing in this order.

### Table


| Sub | Element | Usage | Card | Type | Description | Note |
|-----|---------|-------|------|------|-------------|------|
|  | CompositeFrame | mandatory | 1..1 | unknown | A container VERSION FRAME that groups a set of content VERSION FRAMsE to which the same VALIDITY CONDITIONs have been assigned. |  |
| + | [FrameDefaults](FrameDefaults.md) | expected | 0..1 | VersionFrameDefaultsStructure | Default values to use on elements in the frame that do not explicitly state a value. |  |
| + | frames | mandatory | 0..1 | frames_RelStructure | Content frames in COMPOSITE FRAME. |  |
| ++ | [ResourceFrame](ResourceFrame.md) | expected | 1..1 | unknown | A coherent set of reference values for TYPE OF VALUEs , ORGANISATIONs, VEHICLE TYPEs etc that have a common validity, as specified by a set of frame VALIDITY CONDITIONs. Used to define common resources that will be referenced by other types of FRAME. |  |
| ++ | [SiteFrame](SiteFrame.md) | expected | 1..1 | unknown | A coherent set of SITE data to which the same frame VALIDITY CONDITIONs have been assigned. |  |
| ++ | [ServiceFrame](ServiceFrame.md) | expected | 1..1 | unknown | A coherent set of Service data to which the same frame VALIDITY CONDITIONs have been assigned. |  |
| ++ | [ServiceCalendarFrame](ServiceCalendarFrame.md) | expected | 1..1 | unknown | A SERVICE CALENDAR. A coherent set of OPERATING DAYS and DAY TYPES comprising a Calendar. That may be used to state the temporal VALIDITY of other NeTEx entities such as Timetables, STOP PLACEs, etc. Covers a PERIOD with a collection of assignments of OPERATING DAYS to DAY TYPES. |  |
| ++ | [TimetableFrame](TimetableFrame.md) | expected | 1..1 | unknown | A coherent set of timetable data (VEHICLE JOURNEYs and BLOCKs) to which the same VALIDITY CONDITIONs have been assigned. |  |



*→ [General NeTEx definition](../generated/netex-html/CompositeFrame.html)*

### Example


```xml
<?xml version="1.0" encoding="UTF-8"?>
<CompositeFrame  id="ch:1:CompositeFrame" version="1">
  <FrameDefaults/>
  <frames>
    <ResourceFrame id="ch:1:ResourceFrame" version="1"/>
    <SiteFrame id="ch:1:SiteFrame" version="1"/>
    <ServiceFrame id="ch:1:ServiceFrame" version="1"/>
    <ServiceCalendarFrame id="ch:1:ServiceCalendarFrame" version="1"/>
    <TimetableFrame id="ch:1:TimetableFrame:j23" version="1"/>
  </frames>
</CompositeFrame>

```



*→ [Template](../templates/CompositeFrame.xml)*









