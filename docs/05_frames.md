# The NeTEx Structure

> [!WARNING]\
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
- [Swiss profile tables](../generated/markdown-examples/PublicationDelivery.md)
- [XML Snippet](../generated/xml-snippets/PublicationDelivery.xml)
- [Original NeTEx table](tbd)

## Frames

We use the following frames in Switzerland:

> [!WARNING]\
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

- [Swiss profile tables](../generated/markdown-examples/CompositeFrame.md)
- [XML Snippet](../generated/xml-snippets/CompositeFrame.xml)
- [Original NeTEx table](tbd)







