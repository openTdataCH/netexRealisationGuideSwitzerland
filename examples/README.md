# Examples
This  folder contains the relevante examples for the realisation guide 2.0 based on NeTEX 2.0.

## Call Based (DEPRECIATED)
The 1.x series of the Swiss profile were CALL based. 


## Basic Rail Journey

### Example of a normal rail jounrney train Spiez - Interlaken Ost with various quay combinations
[link](examples/Netex_Spiez_Interlaken_Ost_Version1.2.xml)

### Example splitting train Bern - Zweisimmen | Brig
A simple splitting train without any additional information.
Bdern - Thun - Spiez - (Zweisimmen | Brig)

[Link](NeTEx-Bern-Spiez-Zweisimmen-o-Brig.xml)

## Basic PassingTime

### Example splitting train Bern - Zweisimmen | Brig
This example models the basic splitting of a train with 3 'ServiceJourney'

[Link](NeTEx-Bern-Spiez-Zweisimmen-o-Brig-PassingTime.xml)

### Example with international connection
<description>
  
## ServiceFacilities

### Example of a rail jounrney with ServiceFacilities from Bern to Zürich
This example contains a rail jounrey with a variety of ServiceFacilities

[Link](examples/Netex_Bern_Olten_Zürich3.xml)

## Basic ThroughJourney

### Example of an international rail with through journey Interlanken | Basel SBB | Basel Bad | Freiburg in Breisach (D) 
This is an example of a "ThroughJourney" or "Durchbindung" traversering two countries

[Link](examples/Netex_Interlaken_BS_Freiburg_Breisach_Durchbindung_V.3.xml)

## Shared Quay

### This is and example of a rail jounrey from Niederhasli Zürich HB Zürich Stadelhofen Uster, where Zürich HB is mapped via PassengerStopAssignment to a shared platform Quay “41/42”

This example uses shared quays 41/42, stop‑specific NoticeAssignments, and passingTimes in the Timetable Frame. Also notice that Calls and Order are no longer being used. It separates operational vs. passenger-facing platforms and enables precise notice placement of the platforms via Start/EndPointInPatternRef in the noticeAssignments. Other specific differences from the Swiss Netex 2.0 is the usage of Order and Calls are no longer being used. 
 

[Link] 


## More complete examples


## Full use of SID4PT
<Description>

### Bus
<Description>

### Tram
<Description>


## Special cases
<Description>

### Destination display in a round trip
<Description>

### Umsteigebeziehungen und Metastations
<Description>

### Postauto with Anhänger
<Description>

### Formation for trains
<Description>

### carTransportRail
<Description>

### Journey relationships
<Description>

### rail replacement
<Description>

### Frequency based traffic
<Description>

#### Draglift
<Description>

#### Cabin
<Description>


## Demand Responsive Traffic (DRT)

## Accessibility
For NeTEx 2.0 EPIAP (European Passsenger accessibility Profile, NeTEx Part 6) Chur was used as ann example. 
We don't do accessibility modeling in NeTEx even for RG 2.0

[Accessibility examples in the main repo](https://github.com/NeTEx-CEN/NeTEx/tree/v2.0/examples/standards/epiap)

## Experimental
The following examples are experimental. They are NOT to be used as of now as good templates for modeling stuff

### Minimalistic data for import into INFO+
We consider to use a minimalistic version for importation in INFO+. All basic data (Line, site model, operators) are already known to SKI / Atlas. So we don't need them in the import. We still want valid files.

[Minimal Template Journey](Experimental_Minimal_TemplateJourney_Passingtime.xml)

