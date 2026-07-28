# ResourceFrame

This chapter describes the `ResourceFrame` and all its elements as it is a container holding data that can be referred to from multiple other frames.

In this chapter:
- [ResourceFrame](#resourceframe)
  - [ResponsibilitySet](#responsibilityset)
  - [TypeOfValue / Valuesets](#typeof--valueset)
    - [TypeOfProductCategory](#typeofproductcategory)
    - [TypeOfService](#typeofservice)
  - [Organisation / Operator / Authority](#organisation--operator--authority)
  - [ServiceFacilitySet](#servicefacilityset)
  - [SiteFacilitySet](#sitefacilityset)
  - [VehicleType](#vehicletype)


## ResourceFrame

*→ [Glossary definition](A4_annex_glossary.md#resourceframe)*

### Purpose
Contains shared resources used / referenced in other frames - organisations (`Operator`s), `VehicleType`s, codespaces, and other common reference data.

See the following class diagram for the most important objects of the RESOURCE FRAME and their relationships to the other frames.

### Contained Elements

- ResponsibilitySet
- TypeOfValue / ValueSets
  - TypeOfNotice
  - TypeOfProductCategory
  - TypeOfService
- Organisation / Operator / Authority
- ServiceFacilitySet
- SiteFacilitySet

### Table
- [Swiss profile NeTEx definition](../site/tables/ResourceFrame.md)

*→ - [General NeTEx definition](../site/netex-html/ResourceFrame.html)*

### Example
- [XML Snippet](../site/xml-snippets/ResourceFrame.xml)

*→ - [Template](./templates/ResourceFrame.xml)*

### Frame Relationships

Elements of the `ResourceFrame` can be referenced in other frames like `SiteFrame`, `ServiceFrame`, `ServiceCalendarFrame` 
and/or `TimetableFrame`.

## ResponsibilitySet

*→ [Glossary definition](A4_annex_glossary.md#responsibilityset)*

### Purpose
The set of roles and organisations responsible for managing data, operations, or contractual obligations within a defined scope.
We use this element to  describe the different roles of the participating companies. For the most part, the company code is used to fully identify the provided services. 


| value of `StakeholderRoleType` | Description                                                                        |
|--------------------------------|------------------------------------------------------------------------------------|
| `EntityLegalOwnership`         | Role of the **concession company** holding the concession for the original service |
| `Operation`                    | role of the **operator company** responsible for providing the transport service   |

*Table: Allowed StakeholderRoleType*

### Table
- [Swiss profile NeTEx definition](../site/tables/ResponsibilitySet.md)

*→ - [General NeTEx definition](../site/netex-html/ResponsibilitySet.html)*

### Example
- [XML Snippet](../site/xml-snippets/ResponsibilitySet.xml)

*→ - [Template](./templates/ResponsibilitySet.xml)*

### Usage Notes
Services (e.g. replacement services) can be associated with different roles. These roles can be defined inside the `ResponsibilitySet` element.

Only the values defined below are allowed in Switzerland for `StakeholderRoleType` in `ResponsbilityRoleAssignment`:
-	`Operation`
-	`EntityLegalOwnership`

We might add at some point:
-	`FareManagement`
-	`Planning`

id-attribute should be kept stable between exports.

## TypeOf... / ValueSet
*→ [Glossary definition: TypeOf...](A4_annex_glossary.md#typeof)*\
*→ [Glossary definition: ValueSet](A4_annex_glossary.md#valueset)*

### Purpose
TypeOf... (examples: `TypeOfNotice`, `TypeOfProductCategory`, `TypeOfService`) are used for classification of NeTEx entities.  They are listed in `ValueSet`s as part of the `ResourceFrame`. 

### Usage Notes
We use TypeOfValue references in various Frames in objects including:
-	`Notice`: references `TypeOfNotice`
-	`Line` and `ServiceJourney`: references `TypeOfProductCategory`
- id-attribute needs to be kept stable between exports.

## TypeOfNotice

### Purpose
`TypeOfNotice` is used within a [Notice](07_service.md#notice) to give information, what it is about. The table below shows the `TypeOfNotice` we use in Switzerland.

| PrivateCode | Name                | Description                                                                                                                                                                                                                                                      |
|-------------|---------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1           | Allgemeiner Hinweis | General information text                                                                                                                                                                                                                                         |
| 2           | ~~Zugname~~         | Name of the train. Is not used, as this is stored in `ServiceJourney`/`Name`.                                                                                                                                                                                        |
| 3           | ~~Gleis-Angabe~~    | Quay and Quay section information. Is no longer used. Is put into Quay.                                                                                                                                                                                          |
| 10          | Angebot             | Most of the `ServiceFacilitySet` are also transmitted as `Notice`. On top of that we have multiple services and facilities in Switzerland that cannot be mapped to `ServiceFacilitySets`. This `TypeOfNotice` is used to deliver those special cases as Notices. |
| 11          | ~~Region~~          | Postauto is divided into several regions. Will be omitted. We will add a `privateCodes/PrivateCode` with `type="rn"` to the `ServiceJourney` or `TemplateServiceJourney`.                                                                                       |

*Table: Allowed TypeOfNotice in Switzerland*

The following snippet is **all** that is defined for `TypeOfNotice`:
``` xml
<ValueSet id="ch:1:ValueSet:notices" version="1" nameOfClass="TypeOfNotice">
  <values>
    <TypeOfNotice id="ch:1:TypeOfNotice:1" version="1">
      <Name>Allgemeiner Hinweis</Name>
      <PrivateCode>1</PrivateCode>
    </TypeOfNotice>
    <TypeOfNotice id="ch:1:TypeOfNotice:10" version="1">
      <Name>Angebot</Name>
      <PrivateCode>10</PrivateCode>
    </TypeOfNotice>
  </values>
</ValueSet>
```
## TypeOfProductCategory

### Purpose

For the ServiceJourneys exclusively provided in Switzerland, only the ProductCategories defined in the document [06 Harmonisierung Verkehrsmittel](https://www.allianceswisspass.ch/de/tarife-vorschriften/uebersicht/V580/Produkte-der-V580-FIScommun-1) may be referenced. 
For ServiceJourneys provided in other countries or partially in Switzerland, there are no restrictions, provided that the category does not overlap with the ProductCategories defined for Switzerland.

### Table
- [Swiss profile NeTEx definition](../site/tables/TypeOfProductCategory.md)

*→ [General NeTEx definition](../xcore/netex/elements/TypeOfProductCategory.html)*


###  Example
- [XML Snippet](../site/xml-snippets/TypeOfProductCategory.xml)

*→ [Template](./templates/TypeOfProductCategory.xml)*

## TypeOfService
`TypeOfService` is to be found within `TimetableFrame`.

## Organisation / Operator / Authority

*→ [Glossary definition: Operator](A4_annex_glossary.md#operator)*\
*→ [Glossary definition: Authority](A4_annex_glossary.md#authority)*

### Purpose
A legally incorporated body associated with any aspect of public transportation. `Authority` and `Operator` are `Organisation`s. An `Operator` provides public transport services under contract with an `Authority`. We don't use `Authority`.


### Table
- [Swiss profile NeTEx definition](../site/tables/Operator.md)

*→ [General NeTEx definition](../xcore/netex/elements/Operator.html)*

### Example
- [XML Snippet](../site/xml-snippets/Operator.xml)

*→ - [Template](./templates/Operator.xml)*

### Usage Notes
* `Organisation`s located in Switzerland are identified by their [SBOIDs](https://transportdatamanagement.ch/content/uploads/2021/05/SwissBusinessOrganisationID_DE_1_2.pdf)  (earlier [GO-number](https://opentransportdata.swiss/de/dataset/didok/resource/d66259a0-a77c-4aee-b7bd-e4fba99dcbb1) ).
in Switzerland. The TU-Code is to be used for operators of other countries. 
* The SBOID and GO number shall always also be stored in the `KeyList` and in `privateCodes/PrivateCode`.
* `OperatorRef` on a `Line` is always the "Konzessionär". 
* If a different `Operator` is running a given `ServiceJourney`, then this is reflected in the `ServiceJourney` having 
a different `OperatorRef`.
* `Authority`  and `Organisation` are not used.
- id-attribute needs to be kept stable between exports.

## ServiceFacilitySet
*→ [Glossary definition](A4_annex_glossary.md#servicefacilityset)*

### Purpose
Set of `Facility`'s available for a `ServiceJourney` or a `JourneyPart`. 

### Table
- [Swiss profile NeTEx definition](../site/tables/ServiceFacilitySet.md)

*→ [General NeTEx definition](../xcore/netex/elements/ServiceFacilitySet.html)*

### Example
- [XML Snippet](../site/xml-snippets/ServiceFacilitySet.xml)

*→ - [Template](./templates/ServiceFacilitySet.xml)*

### Usage Notes
* SKI uses the following groups to classify `ServiceFacility`s:
  -	Accommodation facility
  -	Catering facility
  -	Fare classes
  -	Group booking facility
  -	Luggage carriage facility
  -	Mobility facility
  -	Nuisance facility
  -	Passenger communications facility
  -	Service reservation facility
  -	Ticketing facility
  -	Uic train rate

* The list is from time to time revised. The values and lists from the NeTEx standard are not updated.
* This means that a given Facility (e.g. restaurant or diaper changing table) is shown in the appropriate 
subcategory `MealFacilityList` or `FamilyFacilityList`, and a passenger information system can show these categories in 
a reasonable order. The categories themselves are from type `xsd:list`, meaning that the values of a category are a 
separated list of elements. 
* When transforming from HRDF to NeTEx. The `Facility` is often also copied as a `Notice` in textual form.
* The details of the usage are defined in the [mapping table for NeTEX 2.0](media/Mappingtabellen_NeTEx_v2.0.xlsx).
* See also [Use case on service facilities](uc04_service_facilities.md).
- id-attribute should be kept stable between exports.

## SiteFacilitySet
*→ [Glossary definition](A4_annex_glossary.md#servicefacilityset)*

### Purpose
Set of `Facility`s available at a `StopPlace`, `Quay` or other site elements.

A `SiteFacilitySet` defines a set of facilities like sanitary facilities, ticket service, lockers etc. that can be 
referenced to define facilities of a site.

### Table
- [Swiss profile NeTEx definition](../site/tables/SiteFacilitySet.md)

*→ [General NeTEx definition](../xcore/netex/elements/SiteFacilitySet.html)*

### Example
- [XML Snippet](../site/xml-snippets/SiteFacilitySet.xml)

*→ - [Template](./templates/SiteFacilitySet.xml)*

### Usage Notes
* Make sure to not generate identical SiteFacilitySets. Reuse them.
* We currently don't have many `SiteFacilitySet` as this is not done in timetables yet. With accessibility and more information from Atlas, this may change. 
* We will keep the list of relevant values updated in [mapping table for NeTEX 2.0](media/Mappingtabellen_NeTEx_v2.0.xlsx).
* There may be an overlap between `SiteFacilitySet` and `ServiceFacilitySet`. However, they reference very different things: site elements and vehicles.
* Sometimes "capabilities"/"limitations" are defined through combinations of what a stop and what a vehicle can do.
* In future also the use of `Equipment` and `EquipmentPlace` may become more important. These are then actual pieces of equipment. This also means that the `Vehicle` must be known and referenced. 
- id-attribute should be kept stable between exports.

## VehicleType
*→ [Glossary definition](A4_annex_glossary.md#vehicletype)*

### Purpose
A typified vehicle configuration (model or series) defining reusable characteristics such as capacity, dimensions, propulsion, and accessibility features.


### Table
- [Swiss profile NeTEx definition](../site/tables/VehicleType.md)

*→ [General NeTEx definition](../xcore/netex/elements/VehicleType.html)*

### Example
- [XML Snippet](../site/xml-snippets/VehicleType.xml)

*→ - [Template](./templates/VehicleType.xml)*

### Usage Notes
* We currently use `VehicleType` but not `VehicleModel`.
* We express accessibility partially through it.
* See more details in the [mapping excel](media/Mappingtabellen_NeTEx_v2.0.xlsx).


