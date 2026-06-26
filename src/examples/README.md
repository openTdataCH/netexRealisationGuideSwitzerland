# Examples
This  folder contains the relevant examples for the realisation guide 2.0 based on NeTEX 2.0.

### Basic train with PassingTime
Example of a normal rail journey train Spiez - Interlaken Ost with various quay combinations.

[Link to example](NeTEx_Spiez_Interlaken_Ost_PassingTime.xml)

### Basic bus
Swiss NeTEx 2.0 models repeated stops within a journey using PassingTimes and JourneyPattern references, enabling quay-level differentiation (e.g. opposite sides of the road) without duplicating journeys or introducing additional segmentation structures

[Link to example](NeTEx_CH_PAG_11929.xml)

Another bus i an example from Nyon.

[Link to example](NeTEx_CH_PAG_11929.xml)

### Bus with some DRT properties
We modeled some `ServiceJourney` from the following bus: https://github.com/user-attachments/files/26309155/50.110.pdf

[Link to example](NeTEx_CH_DRT_Line_50.110.xml)

## Bus where there must be passengers present at the start
Als drittes Beispiel eignet sich die Fahrt 11957 auf der Linie 50.119. Diese Fahrt ist fahrplanmässig fix (kein Rufbus, keine Voranmeldung), weist jedoch entlang der gesamten Strecke ausschliesslich Haltestellen zum Ausstieg auf. Sofern niemand an der Starthaltestelle einsteigt, wird die Fahrt auch nicht gefahren.

[Link to example](NeTEx_CH_DRT_Line_Dependent_on_Passengers_At_Start.xml)

### Example splitting train Bern - Zweisimmen | Brig
A simple splitting train without any additional information.
Bern - Thun - Spiez - (Zweisimmen | Brig)

> **TODO**: Check if this really is the full example with the latest version JourneyMeeting or the improved InterchangeRule also 3 parts and one stays in Brig

[Link to example](NeTEx_CH_Bern_Spiez_Zweisimmen_Passingtime.xml)

## Basic ThroughJourney
This example demonstrates a Swiss NeTEx 2.0 modelling of an international ThroughJourney (Durchbindung) extending beyond Swiss borders, highlighting the use of TimetabledPassingTimes, consistent KeyList and PrivateCode usage, and a complete mapping between ScheduledStopPoints and PassengerStopAssignments to ensure both temporal and spatial consistency.

[Link to example](NeTEx_CH_Interlaken_BS_Freiburg_Breisach_Durchbindung.xml)

## Train with ServiceFacilities and Notes
This example shows the usage of ServiceFacilities. It also shows when the ServiceFacility is
- not available on all operating days
- is restricted to a part of the journey (here the bistro is not open between Olten and Zürich)

[Link to example](NeEX_CH_Bern_Olten_ZuerichHB_Winterthur_StGallen_with_Facilities.xml)

## Using a platform for a train
This is and example of a rail journey from Niederhasli Zürich HB Zürich Stadelhofen Uster, where Zürich HB is mapped via PassengerStopAssignment to a shared platform Quay “33/34”
This shows the problems with sloid.

We model a train that has the following stops Fribourg - Bern - Zürich. Zürich it uses Zürich Löwenstrasse 33/34

![img.png](media/fribourg_zuerich.png)

[Link to example](NeTEx_CH_Fribourg_Bern_Zuerich_Perron.xml)

## Special case: Destination changed
We use a BLS train from Bern to Luzern. Due to construction it is terminated at Wolhusen.
We assume that in Bern, Konolfingen and Langnau i.E. we want to show Destination Luzern. On the ServiceJourney we want to show Wolhusen. And in the stops after Langnau i.E. we show Wolhusen as destination.

![img.png](media/DestinationChange_Bern_Luzern.png)

[Link to example](NeTEx_CH_BLS_Bern_Luzern_DestinationChange.xml)


In a second modeling we want to model the change in the train number as also shown in the example. In this version the train goes to Luzern exactly as shown in the image.

[Link to example](NeTEx_CH_BLS_Bern_Luzern_Change_TrainNumber_and_other_stuff.xml)


## Special case: Destination display in a round trip
>**TODO** LATER


## Journey relationships
>**TODO** Examples from Adrian

## Full content of a minimal export
Only few lines with some interaction to show all elements in action and the different files. The file names are already done as they should be.

>**TODO** Later by MENTZ when file structure is defined

## Special case: Umsteigebeziehungen und Metastations
>**TODO** by Adrian

## Postauto with Anhänger
>**TODO** to be provided by PAG

## Formation for trains
>**TODO** Will be done by Matthias in June

## carTransportRail
>**TODO** Later

### rail replacement
>**TODO** Later

### Frequency based traffic
>**TODO** needs to be improved

#### Draglift
>**TODO** needs to be improved

#### Cabin
>**TODO** needs to be improved


## Other Demand Responsive Traffic (DRT)
Swiss NeTEx 2.0 replaces Call-based, order-dependent modelling with a flat, PassingTime-driven structure that separates stop sequence, timing, and operational semantics more clearly than previous version

We already have seen line-based DRT. Here we deal with area based DRT.

> **TODO** Later

## Accessibility
For NeTEx 2.0 EPIAP (European Passsenger accessibility Profile, NeTEx Part 6) Chur was used as an example. 
We don't do accessibility modeling in NeTEx even for RG 2.0

[Accessibility example in the main NeTEx repo](https://github.com/NeTEx-CEN/NeTEx/tree/v2.0/examples/standards/epiap)

## Experimental
The following examples are experimental. They are NOT to be used as of now as good templates for modeling stuff

### Minimalistic data for import into INFO+
We consider to use a minimalistic version for importation in INFO+. All basic data (Line, site model, operators) are already known to SKI / Atlas. So we don't need them in the import. We still want valid files.

[Minimal Template Journey](Experimental_Minimal_TemplateJourney_Passingtime.xml)


