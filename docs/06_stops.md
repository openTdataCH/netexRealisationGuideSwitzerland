# Stop Modelling

- [SiteFrame](06_stops.md#SiteFrame)
- [StopPlace](06_stops.md#StopPlace)
- [Quay](06_stops.md#Quay)
- [TopographicPlace](06_stops.md#TopographicPlace)

## SiteFrame 

> *→ [Glossary definition](A4_annex_glossary.md#siteframe)*

### 1. Purpose

A ***SiteFrame*** contains the physical infrastructure model for public transport — *StopPlace*s, *Quay*s, and topographic context. It defines the spatial elements that passengers interact with and that other frames reference for stop assignments.


### 2. Contained Elements

- ***StopPlace***s – stations and stops 
  - ***Quay***s - platforms where passengers can board a vehicle
- ***TopographicPlace***s - points of interest, geographical and administrative area context for stops
- Not currently modelled: entrances, levels, equipments, paths, accessibility properties

### 3. Table (TODO)

> *→ [General NeTEx definition ](generated/xcore/SiteFrame.html)*

TODO INSERT: [Swiss profile NeTEx definition](generated/markdown-examples/SiteFrame.md)

> *→ [Template](../templates/SiteFrame.xml)*

### 4. Example
TODO INSERT: [Example snippet](generated/xml-snippets/SiteFrame.xml)


### 5. Frame Relationships
***SiteFrame*** is independent of other frames but provides the physical stop infrastructure that ***ServiceFrame*** references through *PassengerStopAssignments*. ***TimetableFrame*** indirectly depends on ***SiteFrame*** through the *JourneyPattern* stop sequence. ***SiteFrame*** is typically wrapped in a *CompositeFrame* within a *PublicationDelivery*.

## StopPlace
> *→ [Glossary definition](A4_annex_glossary.md#StopPlace)*

### 1. Purpose

A named physical or virtual location where passengers can board or alight from public transport, containing one or more *Quays*.
Note that a *StopPlace* is a distinct concept from the representation of the stop in a timetable – the *ScheduledStopPoint*. The two can be connected using a *StopPointAssignment*. 


### 2. Table (TODO)

> *→ [General NeTEx definition ](generated/xcore/StopPlace.html)*

TODO INSERT: [Swiss profile NeTEx definition](generated/markdown-examples/StopPlace.md)

> *→ [Template](../templates/StopPlace.xml)*

### 3. Example
TODO INSERT: [Example snippet](generated/xml-snippets/StopPlace.xml)


### 4. Usage Notes (TODO)

In Switzerland all these StopPlace codes are defined in Didok by order of the Department of Transport (BAV). If the BAV will regulate also “Haltepunkte” and “Haltekante” then also the Quays will be regulated. Foreign StopPlaces may be mapped to Swiss Didok codes. 
 
It is important to notice that the main connection between Didok codes and the NeTEx export are the ScheduledStopPoints. Those will have the same Id (besides the different <Element Name> as the StopPlace in many cases. Exceptions are meta stations and local public transport that already uses assignment to “Haltekanten”. In that case the ScheduledStopPoint is more refined than the DiDok UIC like codes. 
 
There will be meta-stations added with their own code. In some cases these are added for operational or searching reasons. 


> The **Centroid** always contains a location:
> - The main coordinates are given as WSG84.
> - The Swiss coordinates are added as well, when available (see below) 
> - INFO+ will not use the data from the import. Always the DIDOK master data will be used for all Swiss coordinates. INFO+ will use the data of foreign places.

## Quay

> *→ [Glossary definition](A4_annex_glossary.md#Quay)*

### 1. Purpose
A specific boarding or alighting position (platform, stand, bay) within a *StopPlace* where passengers physically meet vehicles. 


### 2. Table (TODO)

> *→ [General NeTEx definition ](generated/xcore/StopPlace.html)*

TODO INSERT: [Swiss profile NeTEx definition](generated/markdown-examples/StopPlace.md)

> *→ [Template](../templates/StopPlace.xml)*

### 3. Example
TODO INSERT: [Example snippet](generated/xml-snippets/StopPlace.xml)



### 4. Usage Notes (TODO)

A QUAY may serve one or more VEHICLE STOPPING PLACEs and be associated with one or more STOP POINTs.  
 
A QUAY may contain other sub QUAYs. A child QUAY must be physically contained within its parent QUAY.  

Further more: 
- A nested QUAY is always physically contiguous with its parent and so has the same accessibility characteristics 
as it parents. 
- Nested QUAYs should not be used to mark individual positions on a platform – BOARDING POSITIONs service this function. 
- Nested QUAYs and ACCESS PLACES must always be on the same LEVEL as their parent

#### Business Requirements   

QUAYs are mapped with the following resolution: 
- No hierarchy between the different definitions of quays is foreseen at the moment 
- All combinations between sectors of the same quay are considered as independent quays. 
- Combinations of several quays are considered as independent quays. 
 
In future the modelling of the Quays might adhere to EPIAP (NeTEx part 6) more to make sure that accessibility features can be modelled 
correctly.. 

## TopographicPlace
> *→ [Glossary definition](A4_annex_glossary.md#TopographicPlace)*

### 1. Purpose
A named geographic area such as a city, municipality, county, or region - used to provide spatial context for *StopPlaces*, for example when interactively searching for the origin or destination of a trip.



### 2. Table (TODO)

> *→ [General NeTEx definition ](generated/xcore/TopographicPlace.html)*

TODO INSERT: [Swiss profile NeTEx definition](generated/markdown-examples/TopographicPlace.md)

> *→ [Template](../templates/TopographicPlace.xml)*

### 3. Example
TODO INSERT: [Example snippet](generated/xml-snippets/TopographicPlace.xml)

### 4. Usage Notes (TODO)

#### Business Requirements

The TopograficPlace represent the cantons and communes in Switzerland. The value will be set to the cantons for stops. 

[//]: # (TODO: Comment to Centroid is repeated.)
Comment to Centroid:

The “Centroid” always contains a location. 
- The main coordinates are given as WSG84. 
- The Swiss coordinates are added as well, when available (see below) 
- INFO+ will not use the data from the import. Always the DIDOK master data will be used for all Swiss coordinates. INFO+ will use the data of foreign places. 
