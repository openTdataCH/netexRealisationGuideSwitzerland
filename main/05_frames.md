# The Frames Structure
In this chapter:
- [PublicationDelivery](#PublicationDelivery)
- [Frames](#Frames)
- [CompositeFrame](#CompositeFrame)

## PublicationDelivery
*→ [Glossary definition](A4_annex_glossary.md#publicationdelivery)*

### Purpose
Any valid XML document must start with one root element.
`PublicationDelivery` is the root element of NeTEx XML. 

In addition to linking to the NeTEx XML schema, this element is used to specify the publication timestamp and the 
participant's identifier. 

### Table



For PublicationDelivery have a good look at how the attributes must be done in the provided examples.

*Table: PublicationDelivery*

| Sub | Element | Usage | Card | Type | Description | Note |
|-----|---------|-------|------|------|-------------|------|
|  | @xmlns | mandatory | 1..1 | xsd:string | Attribute xmlns | |
|  | @xlmns:xsi | mandatory | 1..1 | xsd:string | Attribute xlmns:xsi | |
|  | @version | mandatory | 1..1 | xsd:string | Attribute version | |
|  | @xsi:schemaLocation | mandatory | 1..1 | xsd:string | Attribute xsi:schemaLocation | |
|  | @xmlns:gml | mandatory | 1..1 | xsd:string | Attribute xmlns:gml | |
|  | @xmlns:siri | mandatory | 1..1 | xsd:string | Attribute xmlns:siri | |
|  | PublicationTimestamp | mandatory | 1..1 | xsd:dateTime | Time of output of data. |  |
|  | ParticipantRef | mandatory | 1..1 | siri:ParticipantCodeType | Identifier of system requesting Data. |  |
|  | Description | optional | 0..* | MultilingualString | Description of contents. |  |
|  | dataObjects | mandatory | 0..1 | dataObjects | NeTEx Entities of any type. |  |
| + | [CompositeFrame](./tables/CompositeFrame.md) | mandatory | 1..1 | CompositeFrame | A container VERSION FRAME that groups a set of content VERSION FRAMsE to which the same VALIDITY CONDITIONs have been assigned. |  |




*→ [Original NeTEx table](../xcore/netex/elements/PublicationDelivery.html)*

### Example


```xml
<?xml version="1.0" encoding="UTF-8"?>
<PublicationDelivery version="2.1" {http://www.w3.org/2001/XMLSchema-instance}schemaLocation="http://www.netex.org.uk/netex ../../xsd/xsd/NeTEx_publication.xsd">
  <!-- For PublicationDelivery have a good look at how the attributes must be done in the provided examples. -->
  <PublicationTimestamp>2026-03-30T12:00:00</PublicationTimestamp>
  <ParticipantRef>SKI-Templates</ParticipantRef>
  <Description>Standard export 2027-06-02 for Bernmobil.</Description>
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



*→ [Template](./templates/PublicationDelivery.xml)*

### Usage Notes
* We use the standard `frames` of NeTEx
* Which file needs to contain what `Frame` and with what content is defined in the  [files](04_files.md) chapter.
 
## Frames

NeTEx is divided into [frames](#frames), containers for elements of a specific domain. These frames are introduced below.

We use the following frames in Switzerland:

| Frame                                                                | Description                                                                                                                                                                                                                                                                    |
|----------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [CompositeFrame](#CompositeFrame)                                    | Container for the `FrameDefaults` and the other frames.                                                                                                                                                                                                                        |
| [ResourceFrame](10_common.md#resourceframe)                          | General purpose elements such as `ResponsibilitySet`, `Organisation`, `Operator`, `SiteFacilitySet` and `ServiceFacilitySet`. `TypeOfProductCategory` and `TypeOfNotice` are to be defined in a `ValueSet`.                                                                    |
| [SiteFrame](06_stops.md#siteframe)                                   | Contains the physical infrastructure model: Encloses elements describing locations like `Site`, `StopPlace`, `Quay` and `TopographicPlace`.                                                                                                                                    |
| [ServiceFrame](07_service.md#serviceframe)                           | Contains, among other, the network model with elements such as `Line` and `Route`, the service pattern model with `ScheduledStopPoint`, `ServiceJourneyPattern` and `TimingLink`, and the topological model of interchanges with `DefaultConnection`,                                                                          `SiteConnection`. |
| [ServiceCalendarFrame](08_service_calendars.md#servicecalendarframe) | Contains calendar specific elements like `AvailabilityConditions`, `ServiceCalendar` and `DayType` that are referenced in other frames like the `TimetableFrame`.                                                                                                              |
| [TimetableFrame](09_timetable.md#timetableframe)                     | Contains the operational journey definitions with elements like `ServiceJourney`, `TimeDemandType`, `ServiceJourneyInterchange` and others.                                                                                                                                    |

*Table: Content of the frames*

> The following frames are **not to be used** in Switzerland:
> - `GeneralFrame`
> - `InfrastructureFrame`
> - `VehicleScheduleFrame`
> - `DriverScheduleFrame`
> - `FareFrame`

## CompositeFrame
*→ [Glossary definition](A4_annex_glossary.md#compositeframe)*

### Purpose
The `CompositeFrame` is the container for the `FrameDefaults` and the other frames like `ResourceFrame`, `SiteFrame`, `ServiceFrame`, `ServiceCalendarFrame` and `TimetableFrame`, 
appearing in this order.

Their full documentation can be found here: [ResourceFrame](10_common.md#resourceframe), [SiteFrame](06_stops.md#siteframe), [ServiceFrame](07_service.md#serviceframe), [ServiceCalendarFrame](08_service_calendars.md#servicecalendarframe), [TimetableFrame](09_timetable.md#timetableframe)  

### Table



*Table: CompositeFrame*

| Sub | Element | Usage | Card | Type | Description | Note |
|-----|---------|-------|------|------|-------------|------|
|  | ValidBetween | expected | 1..1 | ValidBetween | OPTIMISATION. Simple version of a VALIDITY CONDITION. Comprises a simple period. NO UNIQUENESS CONSTRAINT. | This defines which timetable year is meant. We don't support partial delivery. |
| + | FromDate | expected | 0..1 | xsd:dateTime | Start date of AVAILABILITY CONDITION. |  |
| + | ToDate | expected | 0..1 | xsd:dateTime | End of AVAILABILITY CONDITION. Date is INCLUSIVE. |  |
|  | Description | optional | 0..* | MultilingualString | Description of contents. | A description of the delivery can be provided. |
|  | [FrameDefaults](./tables/FrameDefaults.md) | expected | 0..1 | VersionFrameDefaultsStructure | Default values to use on elements in the frame that do not explicitly state a value. |  |
|  | frames | mandatory | 0..1 | frames_RelStructure | Content frames in COMPOSITE FRAME. |  |
| + | [ResourceFrame](./tables/ResourceFrame.md) | expected | 1..1 | ResourceFrame | A coherent set of reference values for TYPE OF VALUEs , ORGANISATIONs, VEHICLE TYPEs etc that have a common validity, as specified by a set of frame VALIDITY CONDITIONs. Used to define common resources that will be referenced by other types of FRAME. |  |
| + | [SiteFrame](./tables/SiteFrame.md) | expected | 1..1 | SiteFrame | A coherent set of SITE data to which the same frame VALIDITY CONDITIONs have been assigned. |  |
| + | [ServiceFrame](./tables/ServiceFrame.md) | expected | 1..1 | ServiceFrame | A coherent set of Service data to which the same frame VALIDITY CONDITIONs have been assigned. |  |
| + | [ServiceCalendarFrame](./tables/ServiceCalendarFrame.md) | expected | 1..1 | ServiceCalendarFrame | A SERVICE CALENDAR. A coherent set of OPERATING DAYS and DAY TYPES comprising a Calendar. That may be used to state the temporal VALIDITY of other NeTEx entities such as Timetables, STOP PLACEs, etc. Covers a PERIOD with a collection of assignments of OPERATING DAYS to DAY TYPES. |  |
| + | [TimetableFrame](./tables/TimetableFrame.md) | expected | 1..1 | TimetableFrame | A coherent set of timetable data (VEHICLE JOURNEYs and BLOCKs) to which the same VALIDITY CONDITIONs have been assigned. |  |




*→ [General NeTEx definition](../xcore/netex/elements/CompositeFrame.html)*

### Example


```xml
<?xml version="1.0" encoding="UTF-8"?>
<CompositeFrame id="ch:1:CompositeFrame" version="1">
  <ValidBetween>
  <!-- This defines which timetable year is meant. We don't support partial delivery. -->
  <FromDate>2026-01-01T00:00:00</FromDate>
  <ToDate>2026-12-31T00:00:00</ToDate>
  </ValidBetween>
  <Description>
  <!-- A description of the delivery can be provided. -->
  </Description>
  <FrameDefaults>
  <DefaultLocale>
  <TimeZoneOffset>1</TimeZoneOffset>
  <TimeZone>Europe/Berlin</TimeZone>
  <SummerTimeZoneOffset>2</SummerTimeZoneOffset>
  <DefaultLanguage>de</DefaultLanguage>
  </DefaultLocale>
  <DefaultLocationSystem>urn:ogc:def:crs:EPSG::4326</DefaultLocationSystem>
  </FrameDefaults>
  <frames>
  <ResourceFrame id="ch:1:ResourceFrame" version="1"/>
  <SiteFrame id="ch:1:SiteFrame" version="1"/>
  <ServiceFrame id="ch:1:ServiceFrame" version="1"/>
  <ServiceCalendarFrame id="ch:1:ServiceCalendarFrame" version="1"/>
  <TimetableFrame id="ch:1:TimetableFrame:j23" version="1"/>
  </frames>
</CompositeFrame>
```



*→ [Template](./templates/CompositeFrame.xml)*
