# Comparison of the NeTEx Profiles of Switzerland, France and Norway

This comparison is focused on the actual productive data rather than on the documentation

## Comparison of the File Structure

### France

The national access point offers NeTEx data feeds from several different regions and/or transport organisations:
![NAP France](./media/France/FranceNAP.png)

The file structure of the data feeds is not totally identical. Ile de France Mobilite provides:
![IDFM](./media/France/FranceDirectoryTree.png)

There are common files
- arrets.xml: Stop places and quays
- commun.xml: Common reference data
- lignes.xml: A directory of the LINEs contained in the dataset
There are subdirectories per operator. These contain a  NeTEx file for each LINE run by the operator. These files contain routes, servicepatterns and journey. 
![OFFRE](./media/France/FranceDataSet.png)
The subdirectories also contain a "calendrier" file containig the service calendar for the LINEs contained in the directory.

The data feeld of Nouvelle Aquitaine is similar in structure, but has file naming variants:
![NAQ](./media/France/FrandeDataSetVariantNAQ.png)
Instead of using subdirectories, the region name of the data is coded into the file name, e.g BORDEAUX_METROPOLE_calendriers.xml. However, the principle is the same.

Aditionally, the SNCF publishes a feed containing accessibility on stations. The SNCF timetable datset is not separated into files per LINE. They publish a dataset containing several LINEs.

### Norway

The Norwegian NAP provides datasets for each region / operator. There is also a dataset for the whole of Norway, but this just contains all files of the individual data sets.
![NAP_NORWAY](./media/Norway/NorwayNAP.png)

Each Dataset contains a "shared data" file and individual files per LINE. The same applies for flexible services.

The SiteFrame containing stops and quays can also be downloaded either as one file containing all norwegian stops or as separate files per region.

![Norway dataset](./media/Norway/NorwayDataset.png)

### Future Swiss Profile 2.0

There will be 
- one file containing the SiteFrame with all stops and quays 
- NETWORK_OFFER files containing ServiceFrame and Timetable for a certain region and data provider. Common reference data are contained in the files
- a file containing ServiceInterchange between lines and service journeys.


### Summary
- While file naming conventions differ, both NO and FR provide files per LINE to make file size more manageable. Common reference data are put into extra files per data feed / data provider, but there is no common reference dataset for the whole country.
- The CH profile is also aimed at making file size more manageable, but places more emphasis on having self-contained files where all reference data are contained and can be validated.
- In Norway and Switzerland, the file naming convention makes sure that the file name is unique across all datasets.
  
  
## Comparison of the Resource Frame - Common Reference Data

### France

The french profile does not use the predefined NeTEx Frames like ResourceFrame, SiteFrame, ServiceFrame etc., but uses GeneralFrame with TypeOfFrameRef indicating the content.

A GeneralFrame with TypeOfFrameRef "NETEX_COMMUN" may contain elements such as:
- Operator
- Authority
- Network
- Line
- Notice
- BookingContact (for flexible services)

Note that the frame content can still be split into different files

### Norway

The ResourceFrame contains the elements
 - Operator
 - Authority
 - typesOfValue/Branding

However, the "shared" files also contain ServiceFrame and ServiceCalendarFrame. 

ServiceFrame contains:
- Network
- Route
- RoutePoint with projection to ScheduledStopPoint
- ScheduledStopPoint
- PassengerStopAssignment
- Notice
  
ServiceCalenderFrame contains:
- DayType
- DayTypeAssignment

These elements are treated as general reference data which can be used by different TimetableFrames containing the actual services


### Future Swiss Profile 2.0

The ResourceFrame contains the following main elements:
- ResponsibilitySet
- TypeOfValue / ValueSets
- TypeOfNotice
- TypeOfProductCategory
- TypeOfService
- Organisation / Operator / Authority
- ServiceFacilitySet
- SiteFacilitySet
- VehicleType (not confirmed yet)

While a ResourceFrame is included in each NETWORK_OFFER file, the actual element keys and values are the same for all datasets.

### Summary

The Swiss profile places more emphasis on having a consolidated and mandatory set of reference data for all data providers.



## Comparison of the SiteFrame - Stops and Quays

### France

The french profile does not use SiteFrame for information on stops and quays, but uses GeneralFrame with TypeOfFrameRef "NETEX_ARRET" instead

Elements contained are
- TopographicPlace
- StopPlace
- Quay
- TariffZone
- Authority

Stop places may be nested. Monomodal stops are grouped into multimodal stops. Quay elements are not child elements of StopPlace, but are referenced by StopPlace/QuayRef. Quay elements can also be nested. TypeOfQuay is not provided.

Stop and quay coordinates are either WGS84 or the french national projection (EPSG 2154), examples for both can be found.

AccessibilityAssessment is provided for stops and quays.

### Norway

Norway provides a SiteFrame containing all StopPlaces of Norway and also used stops from neighbour countries. 
Elements contained in the SiteFrame are:

- TopographicPlace
- StopPlace
- Quay
- GroupOfStopPlace
- Parking
- TariffZone
- GroupOfTariffZones

Stops can be nested and grouped. Grouping is used to indicate the central stops of a city. TopographicPlaces are provided in great detail including ParentTopographicPlace and border coordinates.


### Future Swiss Profile 2.0

The main elements contained in SiteFrame are:
- [StopPlace](#stopplace)
- [Quay](#quay)
- [TopographicPlace](#topographicplace)

Quays can be nested in order to model rail island platforms and tracks. TopographicPlace contains the hierarchy canton to district to locality. Default connection times for stops are provided in ServiceFrame. All stops originate from the Swiss central stop register and are identified by the SLOID (Swiss Location ID)

### Summary

Even though there are some differneces in detail, the model of stops and quays is relatively similar in the three profiles.


## Comparison of the Service Frame - Lines, Routes and JourneyPatterns

### France

The french profile does not use ServiceFrame, but a GeneralFrame with typeOfFrameRef "NETEX_STRUCTURE"

The Frame contains the main elements:
- Route including pointsInSequence/PointOnRoute
- RoutePoint
- Direction
- ServiceJourneyPattern
- DestinationDisplay
- ScheduledStopPoint
- PassengerStopAssignment
- DataSource

Surprisingly the Line element is not contained. It is contained in the NETEX_COMMUN frame. 
DirectionType is used to distinguish between inbound/outbound, whereas Direction indicates the name of the final destination of the Route.

### Norway

The Frame contains the main elements:
- Network (including additionalNetworks)
- GroupOfLines
- Line
- FlexibleLine
- Route including pointsInSequence/PointOnRoute
- RoutePoint
- PointProjection
- Direction
- ServiceJourneyPattern
- DestinationDisplay
- ScheduledStopPoint
- ServiceLink
- PassengerStopAssignment
- FlexibleStopAssignment
- Notice
- NoticeAssignment (to StopPointInJourneyPattern)
  

The norwegian profile separates between route and journeypattern, but it additionally uses the PointProjection element to map RoutePoint to ScheduledStopPoint. ServiceLinks are treated as shared data between different Lines and ServiceJourneyPatterns. ServiceLinks contain the coordinate sequence of the roads or tracks travelled. The Route element does not seem to provide any additional information except that it enables the link between ServiceJourneyPattern and Line.

### Future Swiss Profile 2.0

The future Swiss profile contains the elements:
- ServiceFrame
- Line
- GroupOfLines
- DestinationDisplay
- ScheduledStopPoint
- PassengerStopAssignment
- DefaultConnection
- SiteConnection
- TimingLink
- ServiceJourneyPattern
- TimeDemandType
- Notice
- NoticeAssignment

GroupOfLines is used to group lines which the same line from a passenger perspective, but are operated by different operators and which are therefore split into different technical lines.
TimeDemandType and TimingLink provide information on scheduled running times between stops of a ServiceJourneyPattern and scheduled waiting times at stops.

### Summary

The main differences between CH and NO,FR are
- The Swiss profile does not use the Route element
- The Swiss profile provides relative running times between stops. This enables consumers to calculate PassingTimes themselves and allows for more compact timetable files.
- The Swiss profile will not provide ServiceLinks / coordinates of the route run. This may be added in a later version.


## Comparison of the TimetableFrame - Journeys and Interchanges

### France
The french profile does not use the TimetableFrame, it uses a GeneralFrame with TypeOfFrameRef "NETEX_HORAIRE"

The frame contains only ServiceJourney Elements. The main child elements are
- Name: Obviously contains a journey number
- dayTypes/daytypeRef
- JourneyPatternRef
- trainNumbers/TrainNumber
- passingTime


### Norway

The TimetableFrame contains the elements
- ServiceJourney
- DatedServiceJourney
- ServiceJourneyInterchange
- NoticeAssignment

The child elements of ServiceJourney are:

- DepartureTime
- Name
- dayTypes/daytypeRef
- LineRef
- JourneyPatternRef
- OperatorRef
- trainNumbers/TrainNumber
- passingTime

### Future Swiss Profile 2.0

The main elements contained in a TimetableFrame are:

- ServiceJourney
- TemplateServiceJourney: describes a set of journeys repeating at a certain frequency. Used e.g. for cable cars.
- ServiceJourneyInterchange: Describes cases where standard interchange times are overriden or where passengers may remain in the same vehicle
- NoticeAssignment
- ServiceFacilitySet: various services and facilities offered by the vehicles of a journey

The main child elements of ServiceJourney and TemplateServiceJourney are:
- ResponsibilitySetRef: Detailed assignment of organisations and their roles
- OperatorRef: operator running the journey
- DepartureTime
- ServiceJourneyPatternRef
- AvailabilityConditionRef: Operating days of journey
- privateCodes/privateCode: Swiss journey id (SYID)
- TransportMode
- TypeOfProductCategoryRef
- TrainNumber
- NoticeAssignment
- OccupancyView
- VehicleTypeRef
- JourneyPartRef: Used where properties change within the journey

ServiceJourneys and TemplateServiceJourneys refer to a ServiceJourneyPattern and a TimeDemandType. They do not contain a PassingTimes child element. Consumers of the data need to calculate the passing times on the fly.
Validity of ServiceJourneys is given by a reference to an AvailabilityCondition 

### Summary

There are two main conceptual differences between the Swiss profile and NO/FR:
- passingTimes are not provided, the consumer needs to calculate them (not difficult)
- Operating Days of journeys are not provided by DayType, but by reference to an AvailabilityCondition element

## Comparison of the ServiceCalendarFrame - Daytypes and Operating Days

### France
The french profile does not use ServiceCalendarFrame, but uses a GeneralFrame with TypeOfFrame "NETEX_CALENDRIER" instead.

The main elements contained in the frame are
- Daytype
- DaytypeAssignment

Daytypes have in part meaningful names and "property of day" is often set

### Norway
The main elements contained in ServiceCalendarFrame are
- Daytype
- OperatingPeriod
- DaytypeAssignment

Daytypes can be either assigned to OperatingPeriods or to Dates. Both variants can be found in the same file.

### Future Swiss Profile 2.0
The elements contained in ServiceCalendarFrame are
- ServiceCalendar: Only one element spanning the entire annual timetable
- DayType: There is one DayType for each Swiss public holiday, but DayTypes are NOT used for operating periods of journeys.
- AvailabilityCondition: Used for describing operating days of journeys. The ValidDayBits element is used to express OperatingDays in a compact manner.
- TimeBand: Used for operating time intervals of TemplateServiceJourneys
  
## Summary
The main difference here is thet FR and NO use DayType and DayTypeAssignment for expressing operating days of journeys, whereas the Swiss profile uses AvailabilityCondition

## Comparison of DemandResponsiveServices
> *Draft!!!*

### France

According to the documentation, the following elements are used
- FlexibleLine
- BookingContact
- FlexibleStopPlace
- FlexiblePointProperties
- FlexibleServiceProperties

Alas no complete examples have been found yet which show the usage of all elements together
*TODO:* Find meaningful examples actually using FlexibleStopPlace

### Norway

Norway uses the FlexibleLine element to indicate flexible services:

![FlexibleLine](./media/Norway/NorwayFlexibleLine.png)

The ServicePattern describes a sequence of ScheduledStopPoints which stand for the individual FlexibleStopPlaces:

![ServiceJourneyPattern](./media/Norway/NorwayFlexibleJourneyPattern.png)

The "BookingContact" is repeated at every area served. 

ScheduledStopPoints are assigned to a FlexibleStopPlace:
![FlexibleStopAssignment](./media/Norway/NorwayFlexibleStopAssignment.png)

The FlexibleStop itsself contains a FlexibleArea with a poligon describing the area of operation:

![FlexibleStopPlace](./media/Norway/NorwayFlexibleStopPlace.png)

The ServiceJourney element contains PassingTimes with a time range (EarliestDeparture and LatestArrival)

![FlexibleJourney](./media/Norway/NorwayFlexibleJourney.png)

The FlexibleServiceProperties element describes booking conditions.

*TODO:* 
- FlexibleStopPlaces containing regular stops or virtual stop points? 
- Journeys without fixed departures but just a time range of operaton?


### Future Swiss Profile 2.0

## References
The following references were used to compile this document.

### France

Profile documentation:
https://normes.transport.data.gouv.fr/


Github:
https://github.com/etalab/transport-profil-netex-fr

Sample data:
https://transport.data.gouv.fr/datasets/reseau-urbain-et-interurbain-dile-de-france-mobilites


### Norway

Profile documentation:
https://entur.atlassian.net/wiki/spaces/PUBLIC/pages/728891481/Nordic+NeTEx+Profile


Github:
https://github.com/entur/nordic-netex-documentation 
https://github.com/entur/profile-examples
https://github.com/entur/nordic-netex-ontology


Sample data (examples):
https://entur.atlassian.net/wiki/spaces/PUBLIC/pages/728891505/NeTEx+examples+catalogue

Sample data (Productive data feed)
https://developer.entur.no/open-data/timetable
