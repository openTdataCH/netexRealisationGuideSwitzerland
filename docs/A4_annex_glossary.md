# Glossary

Core terms used in this NeTEx profile, organised alphabetically.
Each entry includes the definition (adapted to the context of the profile), the official NeTEx XSD annotation, and (where applicable) the Transmodel (EN 12896) definition.

Note that not all elements are used in the profile. Where the element exists and is documented, a link (→ [Full documentation](10_common.md#AlternativeName)) points to the appropriate section in the realisation guide. 

<!-- entur-terms-ready: format maps to SKOS prefLabel + definition -->

---

## AlternativeName

Additional name variant for a NeTEx object - such as an official registration, translation, or abbreviation.

> **NeTEx XSD:** Alternative Name.
>
> **Transmodel:** Alternative name for an ENTITY.

→ [Full documentation](10_common.md#AlternativeName)

---

## AlternativeText

Supplementary textual description attached to any NeTEx object.

> **NeTEx XSD:** Alternative Text.
>
> **Transmodel:** Alternative text for any textual attribute of an ENTITY.

→ [Full documentation](10_common.md#AlternativeText)

---

## Authority

A public transport organisation responsible for planning, organising, and managing public transport services within a specific geographical area.

> **NeTEx XSD:** The ORGANISATION under which the responsibility of organising the transport service in a certain area is placed.
>
> **Transmodel:** The ORGANISATION on which the responsibility of organising the transport service in a certain area is placed.

→ [Full documentation](10_common.md#organisation--operator--authority)

---

## AvailabilityCondition

Temporal availability in terms of, e.g., Dates, Timebands, ValidDayBits.

> **NeTEx XSD:** A specific type of VALIDITY CONDITION used to specify a set of temporal conditions that can be associated with an ENTITY, for example that a STOP PLACE is open on a particular DAY TYPE.
>
> **Transmodel:** A VALIDITY CONDITION expressed in terms of temporal parameters and referring to DAY TYPEs.

→ [Full documentation](08_service_calendars.md#AvailabilityCondition)

---


## Codespace

The namespace definition used for all NeTEx `@id` and `@ref` values within a dataset, ensuring identifier uniqueness across producers.

> **NeTEx XSD:** A system for uniquely identifying objects of a given type. Used for the distributed management of objects from many different sources.

---

## CompositeFrame

A container frame that groups multiple typed frames (ServiceFrame, TimetableFrame, etc.) into a single coherent delivery.

> **NeTEx XSD:** A container VERSION FRAME that groups a set of content VERSION FRAMEs to which the same VALIDITY CONDITIONs have been assigned.
>
> **Transmodel:** A set of VERSION FRAMEs to which the same VALIDITY CONDITIONs have been assigned.

→ [Full documentation](05_frames.md#CompositeFrame)

---

## Contract

A legal or commercial agreement governing responsibilities between an Authority (contractee) and an Operator (contractor) for providing public transport services.

> **NeTEx XSD / Transmodel:** A CONTRACT between ORGANISATIONs to supply services or goods.

---

## DatedServiceJourney

A specific operational instance of a ServiceJourney on a particular calendar day, including day-specific modifications such as cancellations, replacements, or reinforcements. DatedServiceJourney is a NeTEx specialisation of the Transmodel concept DATED VEHICLE JOURNEY.

> **NeTEx XSD:** A particular SERVICE JOURNEY of a vehicle on a particular OPERATING DAY including all modifications possibly decided by the control staff.
>
> **Transmodel:** A particular journey of a vehicle on a particular OPERATING DAY including all modifications possibly decided by the control staff. *(Transmodel: DATED VEHICLE JOURNEY)*

---

## DayType

A classification of days on which a specific set of transport services operates (e.g., Weekdays, Saturdays, Public Holidays).

> **NeTEx XSD:** A type of day characterized by one or more properties which affect public transport operation. For example: weekday in school holidays.
>
> **Transmodel:** A type of day characterised by one or more properties which affect public transport operation (for example: working day, sunday, weekday in school holidays, etc.).

→ [Full documentation](08_service_calendars.md#DayType)

---

## DayTypeAssignment

The binding between a DayType and a specific date or date range (OperatingPeriod), determining when that DayType is active - including exception handling via `isAvailable=false`.

> **NeTEx XSD:** Associates a DAY TYPE with an OPERATING DAY within a specific Calendar. A specification of a particular DAY TYPE which will be valid during a TIME BAND on an OPERATING DAY.
>
> **Transmodel:** The assignment of operational characteristics, expressed by DAY TYPEs, to particular OPERATING DAYs within a SERVICE CALENDAR.

→ [Full documentation](08_service_calendars.md#DayTypeAssignment)

---

## DefaultConnection

Specifies default times for various transfer situations (within a StopPlace, between different Operators, between different ProductCategorys, etc.).

> **NeTEx XSD:** Specifies default times to be used to change from one mode of transport or another at an area or national level as specified by a TOPOGRAPHIC PLACE or SITE. May be restricted to a specific MODE or OPERATOR or only apply in a particular direction of transfer, e.g. bus to rail may have a different time as rail to bus.
>
> **Transmodel:** The physical (spatial) possibility for a passenger to change from one public transport vehicle to another to continue the trip. NOTE1: It specifies default times to be used to change from one mode of transport to another at an area or national level as specified by a TOPOGRAPHIC PLACE, STOP AREA or SITE
ELEMENT. NOTE2: It may be further restricted to a specific MODE or OPERATOR or only apply in a particular direction of transfer, e.g., bus to rail may have a different time for rail to bus.

→ [Full documentation](07_service.md#DefaultConnection)

---

## DestinationDisplay

The text shown on the front or side of a public transport vehicle to indicate its destination, including via-points and variant labels.

> **NeTEx XSD / Transmodel:** An advertised destination of a specific JOURNEY PATTERN, usually displayed on a headsign or at other on-board locations.

→ [Full documentation](07_service.md#DestinationDisplay)

---

## FareContract

A customer-facing agreement for the right to travel and consume fare products, defined within a SalesTransactionFrame (NeTEx Part 3 - Sales).

> **NeTEx XSD / Transmodel:** A contract with a particular (but possibly anonymous) customer, ruling the consumption of transport services (and joint services). A FARE CONTRACT may be designed for a fixed SALES OFFER PACKAGE (e.g. ticket) or to allow successive purchases of SALES OFFER PACKAGEs.

---

## FareFrame

Contains fare data, products, and pricing rules - tariffs, validable elements, preassigned fare products, and sales offer packages.

> **NeTEx XSD:** A coherent set of Fare data to which the same VALIDITY CONDITIONs have been assigned.
> 
---

## FareZone

A geographic zone used to determine ticket prices in public transport, grouping stop points for fare calculation.

> **NeTEx XSD / Transmodel:** A specialization of TARIFF ZONE to include FARE SECTIONs.

---

## FlexibleServiceProperties

The scheduling and operational characteristics of a flexible (demand-responsive) transport service, attached to a ServiceJourney.

> **NeTEx XSD:** FLEXIBLE SERVICE PROPERTIES in frame.
>
> **Transmodel:** Flexibility characteristics of a SERVICE JOURNEY, e.g., cancelled unless ordered and/or timing may be adjusted at time of booking or even later for service optimisation purposes.

---

## FrameDefaults

Holds default values for certain basic parameters.

> **NeTEx XSD:** The FrameDefaults element specifies default values for certain common properties of elements in the frame, such as DATA SOURCE, time-zone etc., to be applied to elements in the frame for which an explicit value has not been specifed. The use of defaults can both simplify export and reduce the size of documents.

→ [Full documentation](10_common.md#FrameDefaults)

---

## GroupOfLines

A logical grouping of multiple Line objects for common management, branding, distribution, or filtering.

> **NeTEx XSD / Transmodel:** A grouping of LINEs which will be commonly referenced for a specific purpose.

---

## Interchange

A planned transfer opportunity between two ServiceJourneys at a shared stop point, modelled as `ServiceJourneyInterchange` in XML.

> **NeTEx XSD:** The scheduled possibility for transfer of passengers between two SERVICE JOURNEYs at the same or different STOP POINTs.
>
> **Transmodel:** The scheduled possibility for transfer of passengers between two SERVICE JOURNEYs at the same or different SCHEDULED STOP POINTs.

---

## InterchangeRule

An InterchangeRule defines the possibility of interchanging between two ServiceJourneys at the same or different ScheduledStopPoints - where at least one journey is specified indirectly via Direction, Line, or the VehicleJourney, rather than as an explicit journey pair. The rule specifies criteria (e.g. Mode, Line, Direction) that a candidate feeder or distributor journey must fulfil.

> **NeTEx XSD:** INTERCHANGE RULE specifies conditions governing the possibility of interchanging between two SERVICE JOURNEYs, stopping at the same or different SCHEDULED STOP POINTs, where at least one of the two SERVICE JOURNEYs is indicated indirectly by a DIRECTION, LINE or VEHICLE JOURNEY.
> Such conditions may alternatively be specified directly, indicating the corresponding services. In this case, they are either a SERVICE JOURNEY PATTERN INTERCHANGE or a SERVICE JOURNEY INTERCHANGE.
>
> **Transmodel:** Conditions governing the possibility of interchanging between two SERVICE JOURNEYs, stopping at the same or different SCHEDULED STOP POINTs, where at least one of the two SERVICE</font>
<font color="#f79646">JOURNEYs is indicated indirectly by a DIRECTION, LINE or VEHICLE JOURNEY.

→ [Full documentation](09_timetable.md#InterchangeRule)

---

## JourneyPattern

The ordered sequence of ScheduledStopPoints that a transport service follows for a specific variant of a Route.

> **NeTEx XSD:** An ordered list of SCHEDULED STOP POINTs and TIMING POINTs on a single ROUTE, describing the pattern of working for public transport vehicles. A JOURNEY PATTERN may pass through the same POINT more than once. The first point of a JOURNEY PATTERN is the origin. The last point is the destination.
>
> **Transmodel:** An ordered list of SCHEDULED STOP POINTs and TIMING POINTs on a single ROUTE, describing the pattern of working for public transport vehicles.

→ [Full documentation](07_service.md#ServiceJourneyPattern)

---

## Line

A public transport service line, representing a marketed route with a name, transport mode, and operator.

> **NeTEx XSD / Transmodel:** A group of ROUTEs which is generally known to the public by a similar name or number.

→ [Full documentation](07_service.md#Line)

---

## LinkSequenceProjection

The geographic representation of a ServiceLink, carrying GML geometry (typically a LineString) describing the spatial path between two consecutive ScheduledStopPoints.

> **NeTEx XSD:** A Projection of a whole LINK SEQUENCE as an ordered series of POINTs.

---

## MultilingualString

NeTEx type used to define a string in one or more natural languages. 

> **NeTEx XSD:** `MultilingualString` allows the definition of a string in one or more natural languages.

→ [Full documentation](10_common.md#multilingualstring)

---

## Notice

Informational or regulatory text associated with public transport services, displayed to passengers.

> **NeTEx XSD:** A note or footnote about any aspect of a service, e.g. an announcement, notice, etc. May have different DELIVERY VARIANTs for different media.
>
> **Transmodel:** A text for informational purposes on exceptions in a LINE, a JOURNEY PATTERN, etc. The information may be usable for passenger or driver information.

→ [Full documentation](07_service.md#Notice)

---

## NoticeAssignment

Assign a `Notice` to an element.

> **NeTEx XSD:** The assignment of a NOTICE to any model element. Can be used in particular to show an exception in a JOURNEY PATTERN, a COMMON SECTION, or a VEHICLE JOURNEY, possibly specifying at which POINT IN JOURNEY PATTERN the validity of the NOTICE starts and ends respectively.
>
> **Transmodel:** The assignment of a NOTICE showing an exception in a JOURNEY PATTERN, a COMMON SECTION, or a VEHICLE JOURNEY, possibly specifying at which POINT IN JOURNEY PATTERN the
validity of the NOTICE starts and ends respectively.

→ [Full documentation](07_service.md#NoticeAssignment)

---

## OperatingDay

A specific calendar date on which transport services operate, referenced by DatedServiceJourney to anchor a journey to a concrete day.

> **NeTEx XSD:** A day of public transport operation in a specific calendar. An OPERATING DAY may last more than 24 hours.
>
> **Transmodel:** A day of public transport operation of which the characteristics are defined within in a specific SERVICE CALENDAR. An OPERATING DAY may last more than 24 hours.

---

## OperatingPeriod

A continuous date range (FromDate-ToDate) during which a set of transport services may operate, used by DayTypeAssignment.

> **NeTEx XSD / Transmodel:** A continuous interval of time between two OPERATING DAYs which will be used to define validities.

---

## Operator

An organisation that provides public transport services under contract with an Authority.

> **NeTEx XSD / Transmodel:** A company providing public transport services.

→ [Full documentation](10_common.md#organisation--operator--authority)

---

## Organisation

A legally incorporated body associated with any aspect of public transportation. Authority and Operator are Organisations.

> **NeTEx XSD / Transmodel:** A legally incorporated body associated with any aspect of public transportation.

→ [Full documentation](10_common.md#organisation--operator--authority)

---


## Parking

A parking facility associated with public transport - such as a park-and-ride lot, bike parking, or car park at a station.

> **NeTEx XSD:** A named place where Parking may be accessed. May be a building complex (e.g. a station) or an on-street location.
>
> **Transmodel:** Designated locations for leaving vehicles such as cars, motorcycles and bicycles.

---

## PassengerStopAssignment

The bridge linking a logical ScheduledStopPoint to a physical Quay within a StopPlace, connecting timetable planning with physical infrastructure.

> **NeTEx XSD:** The default allocation of a SCHEDULED STOP POINT to a specific STOP PLACE, and also possibly a QUAY and BOARDING POSITION.
>
> **Transmodel:** The default allocation of a SCHEDULED STOP POINT to a specific STOP PLACE, and also possibly a QUAY.

→ [Full documentation](07_service.md#PassengerStopAssignment)

---

## placeEquipments

A container within a StopPlace or Quay holding equipment items (shelters, waiting rooms, sanitary facilities, ticketing machines) that describe the physical amenities at the stop.

---

## PublicationDelivery

The root element of every NeTEx XML document, wrapping one or more frames with metadata (timestamp, participant, description).

> **NeTEx XSD:** A set of NeTEx objects as assembled by a publication request or other service. Provides a general purpose wrapper for NeTEx data content.

→ [Full documentation](05_frames.md#PublicationDelivery)

---

## PurposeOfGrouping

A classifier for the reason why NeTEx objects are grouped together (e.g., for presentation, regulation, or contract scope).

> **NeTEx XSD / Transmodel:** Functional purpose for which GROUPs of elements are defined. The PURPOSE OF GROUPING may be restricted to one or more types of the given object.

---

## Quay

A specific boarding or alighting position (platform, stand, bay) within a StopPlace where passengers physically meet vehicles.

> **NeTEx XSD:** A place such as platform, stance, or quayside where passengers have access to PT vehicles, Taxi cars or other means of transportation. A QUAY may contain other sub QUAYs. A child QUAY must be physically contained within its parent QUAY.
>
> **Transmodel:** A place such as platform, stance, or quay side where passengers have access to PT vehicles, Taxis, cars or other means of transportation.

→ [Full documentation](06_stops.md#Quay)

---

## ResponsibilitySet

The set of roles and organisations responsible for managing data, operations, or contractual obligations within a defined scope.

> **NeTEx XSD:** A set of responsibility roles assignments that can be associated with a DATA MANAGED OBJECT. A Child ENTITY has the same responsibilities as its parent.
>
> **Transmodel:** A list of possible responsibilities over one or more ENTITies IN VERSION, resulting from the process of the assignment of RESPONSIBILITY ROLEs (such as data origination, ownership, etc.) on specific data (instances) to ORGANISATIONs or ORGANISATION PARTs.

→ [Full documentation](10_common.md#ResponsibilitySet)

---

## ResourceFrame

Contains shared resources used across other frames - organisations (Authorities and Operators), vehicle types, vehicles, codespaces, and other common reference data.

> **NeTEx XSD:** A coherent set of reference values for TYPE OF VALUEs, ORGANISATIONs, VEHICLE TYPEs etc that have a common validity. Used to define common resources that will be referenced by other types of FRAME.

→ [Full documentation](10_common.md#ResourceFrame)

---

## Route

The logical geographic path definition for a Line with a specific direction.

> **NeTEx XSD / Transmodel:** An ordered list of located POINTs defining one single path through the road (or rail) network. A ROUTE may pass through the same POINT more than once.

---

## SalesTransactionFrame

Contains sales-related data including fare contracts and their entries, representing the commercial agreements between passengers and transport providers.

> **NeTEx XSD:** A coherent set of Sales Transaction data to which the same VALIDITY CONDITIONs have been assigned.

---

## SanitaryEquipment

Sanitary facilities (toilets, washrooms) available at a stop place, station, or onboard a vehicle.

> **NeTEx XSD:** A SANITARY FACILITY, e.g. WC, Shower, baby change.
>
> **Transmodel:** Specialisation of PASSENGER EQUIPMENT describing sanitary facilities (WC, shower, etc.).

---

## ScheduledStopPoint

A logical stopping point in the timetable, used by JourneyPatterns and ServiceJourneys to define where vehicles stop.

> **NeTEx XSD / Transmodel:** A POINT where passengers can board or alight from vehicles.

→ [Full documentation](07_service.md#ScheduledStopPoint)

---

## ServiceAlteration

An enumeration on DatedServiceJourney indicating the deviation type. Allowed values: `planned`, `cancellation`, `replaced`, `extraJourney`. Omitted implies `planned`.

→ [DatedServiceJourney table](09_timetable.md#ServiceJourney)

---

## ServiceCalendar

Long-term planning uses calendar days that are classified as specific DayTypes (example: weekday in school holidays). A ServiceCalendar defines a mapping between DayTypes and OperatingDays

> **NeTEx XSD:** A collection of assignments of OPERATING DAYs to DAY TYPEs.

→ [Full documentation](08_service_calendars.md#ServiceCalendar)

---

## ServiceCalendarFrame

Groups calendar definitions that describe when services operate - day types, operating periods, and day-type assignments.

> **NeTEx XSD:** A SERVICE CALENDAR. A coherent set of OPERATING DAYS and DAY TYPES comprising a Calendar, used to state the temporal VALIDITY of other NeTEx entities such as Timetables and STOP PLACEs.

→ [Full documentation](08_service_calendars.md#ServiceCalendarFrame)

---

## ServiceFacilitySet

Set of facilities available for a ServiceJourney or a JourneyPart.

> **NeTEx XSD:** Set of FACILITies available for a SERVICE JOURNEY or a JOURNEY PART. The set may be available only for a specific VEHICLE TYPE within the SERVICE (e.g. carriage equipped with low floor).
>
> **Transmodel:** Set of FACILITies available for a specific VEHICLE TYPE (e.g., carriage equipped with low floor) possibly only for a service (or for a SERVICE JOURNEY or a JOURNEY).

→ [Full documentation](10_common.md#servicefacilityset)

---

## ServiceFrame

Contains the network and route definitions - Lines, Routes, JourneyPatterns, ScheduledStopPoints, DestinationDisplays, and PassengerStopAssignments.

> **NeTEx XSD:** A coherent set of Service data to which the same frame VALIDITY CONDITIONs have been assigned.

→ [Full documentation](07_service.md#ServiceFrame)

---

## ServiceJourney

A planned trip in the timetable operating on a recurring schedule, defining the stop sequence via a JourneyPattern, passing times, operator, and days of operation.

> **NeTEx XSD / Transmodel:** A passenger carrying VEHICLE JOURNEY for one specified DAY TYPE. The pattern of working is in principle defined by a SERVICE JOURNEY PATTERN.

→ [Full documentation](09_timetable.md#ServiceJourney)

---

## ServiceJourneyPattern

ServiceJourneyPattern is used to describe the journey pattern (sequence and times of ScheduledStopPoints) of ServiceJourney.

> **NeTEx XSD / Transmodel:** The JOURNEY PATTERN for a (passenger carrying) SERVICE JOURNEY.

→ [Full documentation](07_service.md#ServiceJourneyPattern)

---

## ShelterEquipment

Weather shelter facilities available at a stop place or quay, with properties such as seating, step-free access, and enclosure.

> **NeTEx XSD:** Specialisation of WAITING EQUIPMENT for a SHELTER.
>
> **Transmodel:** Specialisation of WAITING EQUIPMENT describing a shelter.

---

## SiteConnection

Sanitary facilities (toilets, washrooms) available at a stop place, station, or onboard a vehicle.

> **NeTEx XSD:** The physical (spatial) possibility for a passenger to change from one public transport vehicle to another to continue the trip. The ends of connection can be specified as SCHEDULED STOP POINT or STOP AREA. Optionally this may be additionally qualified with physical STOP PLACE. Different times may be necessary to cover this link, depending on the kind of passenger.
>
> **Transmodel:** The physical (spatial) possibility for a passenger to change from one public transport vehicle to another to continue the trip, determined by physical locations, such as SITEs and/or its
components and/or ENTRANCEs, in particular STOP PLACEs and/or its components. NOTE: Different times may be necessary to cover the resulting distance, depending on the kind of passenger.

→ [Full documentation](07_service.md#SiteConnection)

---

## SiteFacilitySet

Set of facilities available at a StopPlace, Quay or other site elements.

> **NeTEx XSD:** Set of FACILITies available for a SITE or SITE ELEMENT.
>
> **Transmodel:** Set of FACILITies available for a SITE ELEMENT. 

→ [Full documentation](10_common.md#sitefacilityset)

---

## SiteFrame

Contains the physical infrastructure model for public transport - stop places, quays, entrances, parking facilities, and topographic context.

> **NeTEx XSD:** A coherent set of SITE data to which the same frame VALIDITY CONDITIONs have been assigned.

→ [Full documentation](06_stops.md#SiteFrame)

---

## StopPlace

A named physical or virtual location where passengers can board or alight from public transport, containing one or more Quays.

> **NeTEx XSD:** A named place where public transport may be accessed. May be a building complex (e.g. a station) or an on-street location.
>
> **Transmodel:** A place comprising one or more locations where vehicles may stop and where passengers may board or leave vehicles or prepare their trip. A STOP PLACE will usually have one or more well-known names.

→ [Full documentation](06_stops.md#StopPlace)

---

## TariffZone

A geographic fare zone used for ticketing and pricing, grouping stops and areas into zones that determine ticket prices.

> **NeTEx XSD / Transmodel:** A ZONE used to define a zonal fare structure in a zone-counting or zone-matrix system.

---

## TemplateServiceJourney

A TemplateServiceJourney represents a sequence of planned trips. It is similar to the ServiceJourney, but it is used if there is a frequency or a rhythmical pattern defined at which the trips are scheduled on an operating day.

> **NeTEx XSD:** A repeating SERVICE JOURNEY for which a frequency has been specified, either as a HEADWAY JOURNEY GROUP (e.g. every 20 minutes) or a RHYTHMICAL JOURNEY GROUP (e.g. at 15, 27 and 40 minutes past the hour). It may thus represent multiple journeys or it could be used simply as a template for adding single extra DATED VEHICLE JOURNEYs after the planning phase.
>
> **Transmodel:** A passenger carrying TEMPLATE VEHICLE JOURNEY. NOTE: It may represent multiple journeys.

→ [Full documentation](09_timetable.md#TemplateServiceJourney)

---

## TicketingEquipment

Ticket machines, validators, or other ticketing infrastructure available at a stop place or station.

> **NeTEx XSD / Transmodel:** Specialisation of PASSENGER EQUIPMENT for ticketing.

---

## Timeband

A period of time within a day, usually defined by a start and end time.

> **NeTEx XSD / Transmodel:** A period in a day, significant for some aspect of public transport, e.g. similar traffic conditions or fare category.

→ [Full documentation](08_service_calendars.md#timeband)

---

## TimeDemandType

An indicator of traffic conditions or other factors which may affect vehicle run or wait times.

> **NeTEx XSD / Transmodel:** An indicator of traffic conditions or other factors which may affect vehicle run or wait times. It may be entered directly by the scheduler or defined by the use of TIME BANDs.

→ [Full documentation](08_service_calendars.md#timedemandtype)

---

## TimetabledPassingTime

Long-term planned time data concerning public transport vehicles passing a particular PointInJourneyPattern on a specified vehicle journey for a certain DayType.

> **NeTEx XSD:** PASSING TIME indicates the time of a vehicle at a point in a journey pattern. There can be different types of time (arrival, departure, estimated, observed, etc.). TIMETABLED PASSING TIME represents  scheduled information.
>
> **Transmodel:** Long-term planned time data concerning public transport vehicles passing a particular POINT IN JOURNEY PATTERN on a specified VEHICLE JOURNEY for a certain DAY TYPE.

→ [Full documentation](09_timetable.md#TimetabledPassingTime)

---

## TimetableFrame

Contains operational journey definitions - ServiceJourneys, DatedServiceJourneys, dead runs, coupled journeys, and interchange rules.

> **NeTEx XSD:** A coherent set of timetable data (VEHICLE JOURNEYs and BLOCKs) to which the same VALIDITY CONDITIONs have been assigned.

→ [Full documentation](09_timetable.md#TimetableFrame)

---

## TimingLink

An ordered pair of TimingPoints for which run times may be recorded.

> **NeTEx XSD / Transmodel:** An ordered pair of TIMING POINTs for which run times may be recorded.

→ [Full documentation](08_service_calendars.md#timinglink)

---

## TimingPoint

A (geographic) point against which the timing information necessary to build schedules may be recorded.

> **NeTEx XSD / Transmodel:** A POINT against which the timing information necessary to build schedules may be recorded.

→ [Full documentation](08_service_calendars.md#timingpoint)

---

## TopographicPlace

A named geographic area such as a city, municipality, county, or region - used to provide spatial context for StopPlaces.

> **NeTEx XSD:** A town, city, village, suburb, quarter or other name settlement within a country. Provides a Gazetteer of Transport related place names.
>
> **Transmodel:** A type of PLACE providing the topographical context when searching for or presenting travel information, for example as the origin or destination of a trip.

→ [Full documentation](06_stops.md#TopographicPlace)

---

## TrainBlock

A rail-specific specialisation of Block that represents an operational grouping for a single train on a given operating day.

> **NeTEx XSD:** The vehicle work required by a train-based JOURNEY or sequence of JOURNEYs, from the time it leaves a PARKING POINT after parking until its next return to park at a PARKING POINT.
>
> **Transmodel:** The work required to be done by a vehicle from the time it leaves a PARKING POINT after parking until its next return to park at a PARKING POINT. *(Transmodel: BLOCK)*

---

## TrainNumber

Codes assigned to particular journeys (ServiceJourney, TemplateServiceJourney) when operated by trains. 

> **NeTEx XSD:** Specification of codes assigned to particular VEHICLE JOURNEYs when operated by TRAINs or COMPOUND TRAINs according to a functional purpose (passenger information, operation follow-up, etc.).
>
> **Transmodel:** A specification of codes assigned to particular VEHICLE JOURNEYs or JOURNEY PARTs when operated by TRAINs or COMPOUND TRAINs according to a functional purpose (passenger information, operation follow-up, etc.)

→ [Full documentation](09_timetable.md#TrainNumber)

---

## TypeOf...

Used for classification of NeTEx entities.

> **NeTEx XSD:** Classification of ENTITies, for instance according to the domain in which they are defined or used.
>
> **Transmodel:** TYPE OF VALUE - an ENTITY that serves to classify another entry, using as a list of simple code values, each with a name.

→ [Full documentation](10_common.md#typeof--valueset)

---

## ValueSet

A collection of classification codes of a particular NeTEx entity (e.g., a list of TypeOfNotice values).

> **NeTEx XSD:** A grouping of instances of a specific TYPE OF VALUE instances for the purposes of exchange (i.e. a list of codes).

→ [Full documentation](10_common.md#ValueSet)

---

## Vehicle

A specific physical vehicle in the fleet used to operate public transport services.

> **NeTEx XSD / Transmodel:** A public transport vehicle used for carrying passengers.

---

## VehicleScheduleFrame

Contains operational vehicle schedules - blocks, vehicle services, and duty assignments defining how vehicles are allocated to journeys.

> **NeTEx XSD:** A coherent set of Vehicle Scheduling data to which the same VALIDITY CONDITIONs have been assigned.

---

## VehicleType

A typified vehicle configuration (model or series) defining reusable characteristics such as capacity, dimensions, propulsion, and accessibility features.

> **NeTEx XSD:** A classification of public transport vehicles according to the vehicle scheduling requirements in mode and capacity (e.g. standard bus, double-deck).
>
> **Transmodel:** A classification of public transport vehicles according to the vehicle scheduling requirements in mode and capacity (e.g., standard bus, double-decker, etc.).

→ [Full documentation](10_common.md#VehicleType)

---

## WaitingRoomEquipment

Enclosed indoor waiting room facilities available at a stop place or station, with properties such as seating, step-free access, and heating.

> **NeTEx XSD:** Specialisation of WAITING EQUIPMENT for WAITING ROOMs, classified by TYPE OF WAITING ROOM.
>
> **Transmodel:** Specialisation of WAITING EQUIPMENT describing waiting rooms (number of seats, type, FACILITIEs, etc.).

---

## View

In this profile, "View" is used in two complementary senses:

1. **Publication view** - The way data is selected and packaged inside a NeTEx PublicationDelivery for a specific purpose or audience (e.g., a Timetable publication view).
2. **Thematic view** - A conceptual grouping used in the profile to scope content and requirements (e.g., Timetable, Network, Fares).

Clarifications:
- DatedCalls are not a separate "view" - they are child elements of a DatedServiceJourney within a TimetableFrame.
- When in doubt, prefer the precise NeTEx model terms (PublicationDelivery, TimetableFrame, DatedServiceJourney).

