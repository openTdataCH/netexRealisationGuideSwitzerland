# Timetables

```mermaid
sequenceDiagram
Alice -> Bob: Authentication Request
Bob --> Alice: Authentication Response
Alice -> Bob:Another authentication Response
Bob --> Alice: Another authentication Response
```

## TimetableFrame

A set of timetable data (VEHICLE JOURNEYs, etc.) to which the same VALIDITY CONDITIONs have been assigned. 
A TIMETABLE FRAME holds a coherent set of timetable related elements for data exchange. 
The primary component exchanged by a TIMETABLE FRAME in NeTEx / Transmodel terms is the VEHICLE JOURNEY. The Swiss profile only uses the more specific SERVICE JOURNEY (which describes an individual journey) and the TEMPLATE SERVICE JOURNEY (which describes a set of journeys repeating at a certain frequency). 


The `TimeTableFrame` contains the following allowed elements:
* `ServiceJourney` and `TemplateServiceJourney`
  * `TemplateServiceJourney` is only used for frequency traffic
  * We only model journeys that are available for passenger  
* `TrainNumber`
  * Each (TEMPLATE) SERVICE JOURNEY is mapped one-to-one to exactly one TRAIN NUMBER
* `PassingTime`s describe the times of vehicles at points in their journey
* `InterchangeRule`s describe interchanges between journeys
* `JourneyMeeting`s and `JourneyPart`s describe multipart journeys which join and split **TODO**
* `ServiceFacilitySet`s describe the various services and facilities offered by the vehicles of a journey


[//]: # (TODO: Add TimetableFrame links)
- [General NeTEx definition ](generated/xcore/TimetableFram.html)
- [Swiss profile NeTEx definition](generated/markdown-examples/TimetableFrame.md)
- [Example snippet](generated/xml-snippets/TimetableFrame.xml)

> [Template](../templates/TimetableFrame.xml)

## ServiceJourney

A SERVICE JOURNEY is a VEHICLE JOURNEY on which passengers will be allowed to board or alight from vehicles at stops. It describes the service between an origin and a destination, as advertised to the public.

[//]: # (TODO: Add ServiceJourney links)
- [General NeTEx definition ](generated/xcore/ServiceJourney.html)
- [Swiss profile NeTEx definition](generated/markdown-examples/ServiceJourney.md)
- [Example snippet](generated/xml-snippets/ServiceJourney.xml)

> [Template](../templates/ServiceJourney.xml)

The following restrictions occur:
* The attributs id, version and responsibilitySetRef must be set.
* The validityConditions contain only one AvailablityCondition that contains only the elements FromDate, ToDate and ValidDayBits.
* In the keyList a KeyValue pair with the Key `sjyid` must exists. The Value contains a valid Swiss Journey ID.
* privateCodes: tbd
* TransportMode: tbd
* TypeOfProductCategoryRef: tbd
* TypeOfServiceRef is always set to tbd
* noticeAssignments contain all notices. Attention: they may be restricted to a given set of stops.
* ServiceAlteration is set.
* DepartureTime:
* DepartureDayOffset:
* LineRef is mandatory.
* DirectionType is only inbound or outbound
* trainNumbers contains at least one TrainNumberRef. TrainNumber i not allowed in it.
* Destination: xxx
* passingTimes: ddd
* calls are not to be used.

## TemplateServiceJourney

A TEMPLATE SERVICE JOURNEY is a (repeating) VEHICLE JOURNEY on which passengers will be allowed to board or alight from vehicles at stops. It describes the service between an origin and a destination, as advertised to the public. Only to be used if a frequency has been specified for the JOURNEY. 

[//]: # (TODO: Add TemplateServiceJourney links)
- [General NeTEx definition ](generated/xcore/TemplateServiceJourney.html)
- [Swiss profile NeTEx definition](generated/markdown-examples/TemplateServiceJourney.md)
- [Example snippet](generated/xml-snippets/TemplateServiceJourney.xml)




## PassingTime
tbd
