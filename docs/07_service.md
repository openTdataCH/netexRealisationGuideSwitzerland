# ServiceFrame

The service related elements of the Network Description model can be grouped into a SER-VICE FRAME which holds a coherent set of elements for data exchange.

The Service Frame model comprises among others:
-	Route model: fixed LINEs and ROUTEs of a transport network.
-	Flexible Network model: flexible LINEs and ROUTEs of a demand responsive transport network.
-	Line Network model: overall topology of the LINEs and LINE SECTIONs that make up a transport network.
-	Service Pattern model: SCHEDULED STOP POINTs and SERVICE LINKs, i.e., points and links referenced by schedules.

Other important classes of the SERVICE FRAME include:
-	PASSENGER STOP ASSIGNMENTs and TRAIN STOP ASSIGNMENTs which model the relationship between stops in the timetable and the physical platforms of an actual station or other stop.
-	CONNECTIONs as the topological model of INTERCHANGES. They model the possi-bility of a transfer between two SCHEDULED STOP POINTs.
-	NOTICEs which are then assigned to JOURNEYs and CALLs of the TIMETABLE FRAME through NOTICE ASSIGNMENTs. They model the association of footnotes and passenger information content such as stop announcements and the network.

See the following class diagram for the most important objects of the RESOURCE FRAME and their relationships to the other frames.
<img width="604" height="434" alt="ServiceModel" src="media/ServiceModel.png" />


- [Swiss profile NeTEx definition](../generated/markdown-examples/ServiceFrame.md)
- [Example snippet](../generated/xml-snippets/ServiceFrame.xml)
- [General NeTEx definition](../generated/xcore/ServiceFrame.html)

## Direction

**TBD** DO we use Direction. 
<Direction version="any" id="ch:1:Direction:H">
<Direction-Type>outbound</DirectionType></Direction>


## Line 
Transmodel defines a LINE as a grouping of ROUTEs that is generally known to the public by a similar name or number. These ROUTEs are usually very similar to each other from the top-ological point of view.
Each LINE has a unique number  PrivateCode, a ShortName and a Name.  Passengers rec-ognise a LINE by its published “PublicCode”. The transport mode is specified in  “TransportMode”, e.g  metro, tram, bus etc.. 
The assignement of a LINE to an ORGANISATION is done by the element OperatorRef and to the operationalContext with OperationalContextRef.
Note that there exist journeys in Switzerland and neighbouring countries that are not associat-ed with a Line. In NeTEx, however, the ServiceJourneys corresponding to such journeys must still reference something in LineRef. To ensure this, we introduce a placeholder Line called "NoLine" for each Operator that has journeys without a Line. 
For more information about SwissLineID: see https://www.xn--v-info-vxa.ch/sites/default/files/2023-06/slnid-spezifikation_v1.25_0.pdf
Be aware that there might be for mixed lines multiple lines in NeTEx. Otherwise the relevant operator must at least be set on the ServiceJourney.

- [Swiss profile NeTEx definition](../generated/markdown-examples/Line.md)
- [Example snippet](../generated/xml-snippets/Line.xml)
- [General NeTEx definition](../generated/xcore/ServiceFrame.html)

## DestinationDisplay
(NeTEx-1, 8.4.5.8.4)
The DESTINATION DISPLAY is an advertised destination of a specific LINE, usually displayed on a head-sign 

**TODO We need to discuss this in a lot more detail **

- [Swiss profile NeTEx definition](../generated/markdown-examples/DestinationDisplay.md)
- [Example snippet](../generated/xml-snippets/DestinationDisplay.xml)
- [General NeTEx definition](../generated/xcore/DestinationDisplay.html)

## ScheduledStopPoint
(NeTEx-1, 8.6.3.4.2)
A POINT where passengers can board or alight from vehicles. Where a STOP PLACE models stop points with the desired level of topographic details (areas, entrances, paths etc.), a SCHEDULED STOP POINT corresponds to the simpler network representation used for LINEs, STOP ASSIGNMENTs, JOURNEYs and so on. The connection of these network points with their respective STOP PLACEs is done via STOP ASSIGNEMTNs.

ScheduledStopPoint is a core concept. It is the “Point” used in the timetable for the services to stop. A ScheduledStopPoint can refer to a Quay or only a StopPlace. So the level of hierarchy is not determined by the element (see PassengerStopAssignment).

A ScheduledStopPoint can represent two types of stop points:
-	In most cases, the ScheduledStopPoint is the station named in the timetable, especial-ly as some organisations don’t have a full physical model of their StopPlaces. 
-	In some cases, the ScheduledStopPoint may be mapped to the Quay. The more de-tailed mapping is also done with the PassengerStopAssignment.

- [Swiss profile NeTEx definition](../generated/markdown-examples/ScheduledStopPoint.md)
- [Example snippet](../generated/xml-snippets/ScheduledStopPoint.xml)
- [General NeTEx definition](../generated/xcore/ScheduledStopPoint.html)

## PassengerStopAssignment
(NeTEx-1, 8.6.6.4.2)
The allocation of a SCHEDULED STOP POINT to a specific STOP PLACE for a PASSENGER SERVICE and, also possibly, a QUAY or BOARDING POSITION.
PassengerStopAssignments bring the SiteModel and the ServiceModel in alignment. We have two general cases:
-	A ScheduledStopPoint in a Call is linked to a StopPlace for arrival and departure.
-	A ScheduledStopPoint in a Call is linked to a Quay for arrival and departure.

Suppose a vehicle arrives on QUAY 2A and departs on QUAY 2D. In this case we model only the SCHEDULED STOP POINT for QUAY 2 but assign this STOP POINT to both QUAYs by using two different PASSENGER STOP ASSIGNMENTS.

- [Swiss profile NeTEx definition](../generated/markdown-examples/PassengerStopAssignment.md)
- [Example snippet](../generated/xml-snippets/PassengerStopAssignment.xml)
- [General NeTEx definition](../generated/xcore/PassengerStopAssignment.html)

## DefaultConnection
(NeTEx-1, 8.5.14)
A CONNECTION expresses that there is a possible walking link  that is suitable for a passen-ger to interchange from one public transport vehicle to another between two specified SCHEDULED STOP POINTs and the time allocated for a passenger to traverse the link. Soft-ware used to control guaranteed interchanges can use the time information given to use a CONNECTION link as to assist calculating how long a distributor SERVICE JOURNEY needs to wait after a fetcher SERVICE JOURNEY has arrived before it can depart. If no specific CONNECTION link is available, timings from a DEFAULT CONNECTION must be used.

DefaultConnections are used to transmit the ConnectionTimes for the following constellations:
-	between 2 ProductCategories
-	between 2 Operators
-	In a defined StopPlace
-	In a defined StopPlace and 2 Operators
-	in a defined StopPlace, 2 Operators and 2 ProductCategories
For more Detail see 11 Appendix **TODO**

**TODO**: Needs to be updated by Adrian. !! Here we will have variants of templates that we need to use!

- [Swiss profile NeTEx definition](../generated/markdown-examples/DefaultConnection.md)
- [Example snippet](../generated/xml-snippets/DefaultConnection.xml)
- [General NeTEx definition](../generated/xcore/DefaultConnection.html)

The following variants exist:

- [Swiss profile NeTEx definition](../generated/markdown-examples/DefaultConnection_Modes.md)

- - [Swiss profile NeTEx definition](../generated/markdown-examples/DefaultConnection_Operators.md)


## SiteConnection
(NeTEx-1, 8.5.14.7.3)
The physical (spatial) possibility for a passenger to change from one public transport vehicle to another to continue the trip. The ends of connection can be specified STOP PLACE or STOP AREA.

The SiteConnection describes the transfer times between two adjacent StopPlaces 
For more Detail see 11 Appendix

- [Swiss profile NeTEx definition](../generated/markdown-examples/SiteConnection.md)
- [Example snippet](../generated/xml-snippets/SiteConnection.xml)
- [General NeTEx definition](../generated/xcore/SiteConnection.html)


# Notice
(NeTEx-1, 7.7.18.4.1)
The NOTICE Model defines reusable text note elements that may be attached to timetables as footnotes, used as announcements, etc. NOTICES are associated with other entities using a NOTICE ASSIGNMENT. NOTICES may be classified with a TYPE OF NOTICE.

- [Swiss profile NeTEx definition](../generated/markdown-examples/Notice.md)
- [Example snippet](../generated/xml-snippets/Notice.xml)
- [General NeTEx definition](../generated/xcore/Notice.html)
