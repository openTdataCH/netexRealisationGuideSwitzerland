# The NeTEx Structure

> [!CAUTION]\
> **TODO** 4.1

## PublicationDelivery

`PublicationDelivery` is the root element of NeTEx XML.

(NeTEX-1, p. 220)
NeTEx is divided into [frames](#frames), containers for elements of a specific domain. These frames are introduced below.

``` xml
<?xml version="1.0" encoding="UTF-8"?>
<PublicationDelivery xmlns="http://www.netex.org.uk/netex" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" version="1.0" xsi:schemaLocation="http://www.netex.org.uk/netex ../xsd/xsd/NeTEx_publication.xsd">
	<PublicationTimestamp>2026-03-30T12:00:00</PublicationTimestamp>
	<ParticipantRef>SKI-Templates</ParticipantRef>
	<dataObjects>
		<CompositeFrame id="ch:1:CompositeFrame" version="1">
			<FrameDefaults>
				<!-- ch-see -->
			</FrameDefaults>
			<frames>
				<ResourceFrame id="ch:1:ResourceFrame" version="1">
					<!-- General components such as ORGANISATIONSs VEHICLE TYPEs and code values -->
				</ResourceFrame>
				<SiteFrame id="ch:1:SiteFrame" version="1">
					<!-- SITEs, STOP PLACEs. POINTS OF INTEREST and other fixed objects. -->
				</SiteFrame>
				<ServiceFrame id="ch:1:ServiceFrame" version="1">
					<!-- Network elements such as LINEs, ROUTEs and elements such as SCHEDULED STOP POINTs, JOURNEY PATTERNs, etc. -->
				</ServiceFrame>
				<ServiceCalendarFrame id="ch:1:ServiceCalendarFrame" version="1">
					<!-- ch-see -->
				</ServiceCalendarFrame>
				<TimetableFrame id="ch:1:TimetableFrame:j23" version="1">
					<!-- Timetable elements: SERVICE JOURNEYs with timings. -->
				</TimetableFrame>
			</frames>
		</CompositeFrame>
	</dataObjects>
</PublicationDelivery>
```


| Sub | Element | Usage | Card | Type | Description | Note |
|-----|---------|-------|------|------|-------------|------|
|  | PublicationDelivery | mandatory | 1..1 | PublicationDeliveryStructure | A set of NeTEx objects as assembled by a publication request or other service. Provides a general purpose wrapper for NeTEx data content. |  |
| + | PublicationTimestamp | mandatory | 1..1 | xsd:dateTime | Time of output of data. |  |
| + | ParticipantRef | mandatory | 1..1 | siri:ParticipantCodeType | Identifier of system requesting Data. |  |
| + | dataObjects | mandatory | 0..1 | unknown | NeTEx Entities of any type. |  |
| ++ | [CompositeFrame](CompositeFrame.md) | mandatory | 1..1 | unknown | A container VERSION FRAME that groups a set of content VERSION FRAMsE to which the same VALIDITY CONDITIONs have been assigned. |  |




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


- [Original NeTEx table](tbd)

## Frames

We use the following frames in Switzerland:

> [!CAUTION]\
> **TODO** Make sure that hyperlinks work when single page is generated from markdown files.\
> **COMMENT** Links cannot not work in this source document. I assume that anchors will be available and hyperlinks will work as soon as the final document is put together.

| Frame                                         | Description                                                                                                                             |
|-----------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------|
| [CompositeFrame](#CompositeFrame)             | Container for the FrameDefaults and the other frames.                                                                                   |
| [ResourceFrame](#ResourceFrame)               | General purpose components such as ORGANISATIONSs VEHICLE TYPEs and code values. VEHICLE TYPE is not used.                              |
| [SiteFrame](#SiteFrame)                       | SITEs, STOP PLACEs. POINTS OF INTEREST and other fixed objects.                                                                         |
| [ServiceFrame](#ServiceFrame)                 | Network description elements such as LINEs, ROUTEs, etc. and Tactical Planning elements such as SCHEDULED STOP POINTs, JOURNEY PATTERNs |
| [ServiceCalendarFrame](#ServiceCalendarFrame) | SKI uses principaly `AvailabilyConditions`                                                                                              |
| [TimetableFrame](#TimeTableFrame)             | Timetable elements: SERVICE JOURNEYs with timings.                                                                                      |

> The following frames are **not to be used** in Switzerland:
> - GeneralFrame
> - InfrastructureFrame
> - VehicleScheduleFrame
> - DriverScheduleFrame
> - FareFrame

### CompositeFrame

The `CompositeFrame` is the container for the `FrameDefaults` and the other frames like `ResourceFrame`, `SiteFrame`, `ServiceFrame`, `ServiceCalendarFrame` and `TimeTableFrame`, 
appearing in this order.



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


- [Original NeTEx table](tbd)







