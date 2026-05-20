# Examples
This  folder contains the relevant examples for the realisation guide 2.0 based on NeTEX 2.0.


### Basic train with PassingTime
Example of a normal rail journey train Spiez - Interlaken Ost with various quay combinations.

[Link to example](NeTEx_CH_Spiez_Interlaken_Ost.xml)

### Basic bus
Swiss NeTEx 2.0 models repeated stops within a journey using PassingTimes and JourneyPattern references, enabling quay-level differentiation (e.g. opposite sides of the road) without duplicating journeys or introducing additional segmentation structures

We modeled some `ServiceJourney` from the following bus: https://github.com/user-attachments/files/26309155/50.110.pdf

[Link to example](../examples/NeTEx_CH_DRT_Line_50.110.xml)

### Example splitting train Bern - Zweisimmen | Brig
A simple splitting train without any additional information.
Bern - Thun - Spiez - (Zweisimmen | Brig)

[Link to example](NeTEx_CH_Bern_Spiez_Zweisimmen_Passingtime.xml)

## Bus where there must be passengers present at the start
> **TODO** were is the definition?
> 

[Link to example](../examples/NeTEx_CH_DRT_Line_Dependent_on_Passengers_At_Start.xml)


## Basic ThroughJourney
In the case of international connections a "Durchbindung" is needed.
[Link to example](NeTEx_CH_Interlaken_BS_Freiburg_Breisach_Durchbindung.xml)


## Train with ServiceFacilities and Notes
This example shows the usage of ServiceFacilities. It also shows when the ServiceFacility is
- not available on all operating days
- is restricted to a part of the journey

I would like to suggest the following text for this xml example: Swiss NeTEx 2.0 uses PassingTimes for precise stop timing and models ServiceFacilities per operating day and journey segment, replacing Call-based structures and avoiding additional segmentation layers like JourneyParts.

[Link to example](NeTEx_CH_Bern_Olten_Zürich_Notes_Facilities.xml)

>**TODO** needs to be improved


## Using a platform for a train
This is and example of a rail journey from Niederhasli Zürich HB Zürich Stadelhofen Uster, where Zürich HB is mapped via PassengerStopAssignment to a shared platform Quay “41/42”
This shows the problems with sloid.

>**TODO** needs to be improved

## Special case: Destination changed
>**TODO** needs to be improved

## Special case: Destination display in a round trip
>**TODO** needs to be improved


## Journey relationships
>**TODO** needs to be improved

## Full content of a minimal export
Only few lines with some interaction to show all elements in action and the different files. The file names are already done as they should be.
>**TODO** needs to be improved



## Special case: Umsteigebeziehungen und Metastations
>**TODO** needs to be improved

## Postauto with Anhänger
>**TODO** needs to be improved

## Formation for trains
>**TODO** needs to be improved

## carTransportRail
>**TODO** needs to be improved

### rail replacement
>**TODO** needs to be improved

### Frequency based traffic
>**TODO** needs to be improved

#### Draglift
>**TODO** needs to be improved

#### Cabin
>**TODO** needs to be improved


## Demand Responsive Traffic (DRT)
Swiss NeTEx 2.0 replaces Call-based, order-dependent modelling with a flat, PassingTime-driven structure that separates stop sequence, timing, and operational semantics more clearly than previous version

## Accessibility
For NeTEx 2.0 EPIAP (European Passsenger accessibility Profile, NeTEx Part 6) Chur was used as ann example. 
We don't do accessibility modeling in NeTEx even for RG 2.0

[Accessibility examples in the main repo](https://github.com/NeTEx-CEN/NeTEx/tree/v2.0/examples/standards/epiap)

## Experimental
The following examples are experimental. They are NOT to be used as of now as good templates for modeling stuff

### Minimalistic data for import into INFO+
We consider to use a minimalistic version for importation in INFO+. All basic data (Line, site model, operators) are already known to SKI / Atlas. So we don't need them in the import. We still want valid files.

[Minimal Template Journey](Experimental_Minimal_TemplateJourney_Passingtime.xml)


## No longer used
>**TODO** probably removed in the end.
