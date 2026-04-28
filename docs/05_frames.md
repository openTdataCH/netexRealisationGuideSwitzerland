# The Frames

(NeTEX-1, p. 220)
NeTEx is divided into frames. In this section we describe the frames we use in Switzerland, and which frames are not to be used.

> [!WARNING]\
> **TODO** Make sure that hyperlinks work when single page is generated from markdown files.\
> **COMMENT** Links cannot not work in this source document. I assume that anchors will be available and hyperlinks will work as soon as the final document is put together.

## Frames used in Switzerland

We use the following frames in Switzerland:

| Frame                                         | Description                                                                                                                                          |
|-----------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------|
| [CompositeFrame](#CompositeFrame)             | Frame to group other VERSION FRAMEs                                                                                                                  |
| [ResourceFrame](#ResourceFrame)               | General purpose components such as ORGANISATIONSs VEHICLE TYPEs and code values. VEHICLE TYPE is not used.                                           |
| [SiteFrame](#SiteFrame)                       | SITEs, STOP PLACEs. POINTS OF INTEREST and other fixed objects.                                                                                      |
| [ServiceFrame](#ServiceFrame)                 | Network description elements such as LINEs, ROUTEs, etc., Tactical Planning elements such as SCHEDULED STOP POINTs, JOURNEY PATTTERNs, etc. pattern. |
| [ServiceCalendarFrame](#ServiceCalendarFrame) | SKI uses principaly `AvailabilyConditions`                                                                                                             |
| [TimetableFrame](#TimeTableFrame)             | Timetable elements: SERVICE JOURNEYs with timings.                                                                                                   |

The following frames are **not to be used**:

- GeneralFrame
- InfrastructureFrame
- VehicleScheduleFrame
- DriverScheduleFrame
- FareFrame

# The main Structure and the needed Schemas
TBD: 4.1

# CompositeFrame
*![](../10_common.md)
