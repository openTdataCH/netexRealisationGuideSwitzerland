# Common Building Blocks

This chapter deals with the elements, attributes, formats and types that are commonly used.

In this chapter:
- [Rules for common Attributes ](#rules-for-common-attributes)
  - [Rules for IDs](#ids)
- Common Types
  - [MultilingualString](#multilingualstring)
- [FrameDefaults](#framedefaults)
- [Time formatting and journey after midnight](#time-formatting-and-journey-after-midnight)
- [AlternativeName](#alternativename)
- [AlternativeText](#alternativetext)
- [ResourceFrame](#resourceframe)
  - [ResponsibilitySet](#responsibilityset)
  - [TypeOfValue / Valuesets](#typeofvalue--valuesets)
    - [TypeOfProductCategory](#typeofproductcategory)
    - [TypeOfService](#typeofservice)
  - [Organisation / Operator / Authority](#organisation--operator--authority)
  - [ServiceFacilitySet](#servicefacilityset)
  - [SiteFacilitySet](#servicefacilityset)

## Rules for common Attributes

The following rules apply to common attributes:

| Attribute              | Rule                                                        |
|------------------------|-------------------------------------------------------------|
| `id`                   | See description regarding [technical IDs](#ids) below       |
| `version`              | is always set to `"1"`                                      |
| `responsibilitySetRef` | We use `responsibilitySetRef` in the following elements xxx |
| `nameOfClass`          | We use `nameOfClass` in the XXXRef elements.                |

### IDs
IDs must be globally unique during importation. 
They may also be partially or completely artificially generated. The persistence of these IDs between exports is then 
usually not guaranteed. 
Important business level keys are stored in elements (`PublicKey`, `PrivateKey`, `KeyList`), not in IDs.

It is important to note that internal or artificially generated IDs should not be used to extract content whenever 
business keys and attributes are available. 

For readability and easy referencing, we will use the following principles:
-	We use the class of the object to prefix the technical ID like `ch:1:TypeOfNotice:3"` for a `TypeOfNotice` element.
-   We use appropriate business values to build technical IDs where available, e.g. `ch:1:TypeOfProductCategory:TER` 
where the value of `ShortName` of the `TypeOfProductCategory` is used to build the ID, or `ch:1:Operator:11`.
-	Where there is a compelling need for global stability, the ID will be a global ID. 
This information will be also provided separately in a `KeyList`. 

> [!CAUTION] 
> **TODO** Must be revisited and updated. #83

All other defined attributes like `created`, `changed`, `modification` are not used. If we need one, we will inform about it in the table associated with the element.

## Common Types

### MultilingualString
*→ [Glossary definition](A4_annex_glossary.md#multilingualstring)*

#### Purpose

NeTEx uses the type `MultilingualString` for descriptive text elements (e.g. `Notice` text, `Name`, `ShortName` etc.).
However, only one language can be set for a given element (e.g. `<MultilingualString lang=”fr”>`). 
Additional languages are introduced through the [AlternativeName](#alternativename) and [AlternativeText](#alternativetext) element.

#### Usage Notes

- For [Organisations](#organisation--operator--authority) e.g. there are all languages present.
- The `StopPlace` names in Switzerland are language-independent.

## Time Formatting and Journey after Midnight

The time format consists only of the hours, minutes (and seconds) of a 24-hour clock, e.g. `23:55:00`. 

Times that pass midnight of the current `OperatingDay` are marked with a `DayOffset` element. 
If a `ServiceJourney` (in a particular `Call`) runs over midnight, then `DayOffset` must be set to `1`.

## FrameDefaults
*→ [Glossary definition](A4_annex_glossary.md#framedefaults)*

### Purpose
Holds default values for certain basic parameters. 

### Table
- [Swiss profile NeTEx definition](../generated/markdown-examples/FrameDefaults.md)

*→ [General NeTEx definition](../generated/netex-html/FrameDefaults.html)*

### Example

- [XML Snippet](../generated/xml-snippets/FrameDefaults.xml)

*→ [Template](../templates/FrameDefaults.xml)*

### Usage Notes
For values not set in `FrameDefaults` we use the values as indicated in the table and example above.

## AlternativeName

*→ [Glossary definition](A4_annex_glossary.md#alternativetext)*

### Purpose

`AlternativeName` is used to provide an alternative (alias or translation) of a name, e.g. of 
a `StopPlace` or `Organisation`. 

For all other alternative texts use `AlternativeText`.

### Table
- [Swiss profile NeTEx definition](../generated/markdown-examples/AlternativeName.md)

*→ - [General NeTEx definition](../generated/netex-html/AlternativeName.html)*
 
### Example
- [XML Snippet](../generated/xml-snippets/AlternativeName.xml)

*→ - [Template](../templates/AlternativeName.xml)*

### Usage Notes

We only allow the following values for `NameType`: 
- `alias`
- `translation`

## AlternativeText
> **TODO** remove AlternativeText with MultilanguageString
 

*→ [Glossary definition](A4_annex_glossary.md#alternativetext)*

### Purpose

The `AlternativeText` is a generic way to provide an alternative text (translation or alias).
For example, it can be used for the translation of `Notice` texts.

### Table
- [Swiss profile NeTEx definition](../generated/markdown-examples/AlternativeText.md)

*→ - [General NeTEx definition](../generated/netex-html/AlternativeText.html)*
 
### Example
- [XML Snippet](../generated/xml-snippets/AlternativeText.xml)

*→ - [Template](../templates/AlternativeText.xml)*

## Usage Notes

The `AlternativeText` is part of a `DataManagedObject` and references the name of the node, for which it provides an alternative. 
It contains the alternative text as an attribute of type `MultilingualString` which indicates the language. 

In addition, the `AlternativeText` element may have a `useForLanguage` attribute to indicate a second language for which it may be used as 
an acceptable presentation, if there is no native language alternative; normally this will be the same as the language 
of the string, but might be different.

Alternative names (translations or aliases) of a `StopPlace` or `Organisation` are modelled with [AlternativeNames](#AlternativeName).

# ResourceFrame

*→ [Glossary definition](A4_annex_glossary.md#resourceframe)*

## Purpose
Contains shared resources used / referenced in other frames - organisations (`Authoritiy`s and `Operator`s), `VehicleType`s, codespaces, and other common reference data.

See the following class diagram for the most important objects of the RESOURCE FRAME and their relationships to the other frames.

![ResourceFrame](./media/ResourceFrame.png)
> **TODO** replace image with a mermaid diagram

## Contained Elements

- ResponsabilitySet
- TypeOfValue / ValueSets
  - TypeOfNotice
  - TypeOfProductCategory
  - TypeOfService
- Organisation / Operator / Authority
- ServiceFacilitySet
- SiteFacilitySet

## Table
- [Swiss profile NeTEx definition](../generated/markdown-examples/ResourceFrame.md)

*→ - [General NeTEx definition](../generated/netex-html/ResourceFrame.html)*

## Example
- [XML Snippet](../generated/xml-snippets/ResourceFrame.xml)

*→ - [Template](../templates/ResourceFrame.xml)*

## Frame Relationships

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

### Table
- [Swiss profile NeTEx definition](../generated/markdown-examples/ResponsibilitySet.md)

*→ - [General NeTEx definition](../generated/netex-html/ResponsibilitySet.html)*

### Example
- [XML Snippet](../generated/xml-snippets/ResponsibilitySet.xml)

*→ - [Template](../templates/ResponsibilitySet.xml)*

### Usage Notes

> **TODO** see if we still need the Organisation part 

For the PAG company (801), the attribute `ResponsibleArea(Ref)` must also be taken into account.

Services (e.g. replacement services) can be associated with different roles. These roles can be defined inside the `ResponsibilitySet` element.

Only the values defined below are allowed in Switzerland for `StakeholderRoleType` in `ResponsbilityRoleAssignment`:
-	`Operation`
-	`EntityLegalOwnership`
-	`FareManagement`
-	`Planning`

`FareManagement` and `Planning` are currently not used. Not all roles must be filled.

## TypeOf... / ValueSet
*→ [Glossary definition: TypeOf...](A4_annex_glossary.md#typeof...)*\
*→ [Glossary definition: ValueSet](A4_annex_glossary.md#valueset)*

### Purpose
TypeOf... (examples: `TypeOfNotice`, `TypeOfProductCategory`, `TypeOfService`) are used for classification of NeTEx entities.  They are listed in `ValueSet`s as part of the `ResourceFrame`. 

### Usage Notes
We use TypeOfValue references in various Frames in objects including:
-	`Notice`: references `TypeOfNotice`
-	`Line` and `ServiceJourney`: references `TypeOfProductCategory`

## TypeOfNotice

### Purpose
`TypeOfNotice` is used within a [Notice](07_service.md#notice) to give information, what it is about. The table below shows the `TypeOfNotice` we use in Switzerland.

| PrivateCode | Name                | Description                                                                                                                                                                                                                                                      |
|-------------|---------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1           | Allgemeiner Hinweis | General information text                                                                                                                                                                                                                                         |
| 2           | ~~Zugname~~         | Name of the train. Is not used, as this is stored in ServiceJourneyName.                                                                                                                                                                                         |
| 3           | ~~Gleis-Angabe~~    | Quay and Quay section information. Is no longer used. Is put into Quay.                                                                                                                                                                                          |
| 10          | Angebot             | Most of the `ServiceFacilitySet` are also transmitted as `Notice`. On top of that we have multiple services and facilities in Switzerland that cannot be mapped to `ServiceFacilitySets`. This `TypeOfNotice` is used to deliver those special cases as Notices. |
| 11          | ~~Region~~          | Postauto is divided into several regions. Will be omitted. If anything this will be done with different constructs.                                                                                                                                              |

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
- [Swiss profile NeTEx definition](../generated/markdown-examples/TypeOfProductCategory.md)

*→ [General NeTEx definition](../generated/netex-html/TypeOfProductCategory.html)*


###  Example
- [XML Snippet](../generated/xml-snippets/TypeOfProductCategory.xml)

*→ [Template](../templates/TypeOfProductCategory.xml)*

## TypeOfService
`TypeOfService` is to be found within `TimetableFrame`.

## Organisation / Operator / Authority

*→ [Glossary definition: Operator](A4_annex_glossary.md#operator)*\
*→ [Glossary definition: Authority](A4_annex_glossary.md#authority)*

### Purpose
A legally incorporated body associated with any aspect of public transportation. `Authority` and `Operator` are `Organisation`s. An `Operator` provides public transport services under contract with an `Authority`. We don't use `Authority`.


### Table
- [Swiss profile NeTEx definition](../generated/markdown-examples/Operator.md)

*→ [General NeTEx definition](../generated/netex-html/Operator.html)*

### Example
- [XML Snippet](../generated/xml-snippets/Operator.xml)

*→ - [Template](../templates/Operator.xml)*

### Usage Notes
* `Organisation`s located in Switzerland are identified by their [SBOIDs](https://transportdatamanagement.ch/content/uploads/2021/05/SwissBusinessOrganisationID_DE_1_2.pdf)  (earlier [GO-number](https://opentransportdata.swiss/de/dataset/didok/resource/d66259a0-a77c-4aee-b7bd-e4fba99dcbb1) ).
in Switzerland. The TU-Code is to be used for operators of other countries. 
* The SBOID and GO number shall always also be stored in the `KeyList` and in `privateCodes\PrivateCode`.
`* OperatorRef` on a `Line` is always the "Konzessionär". 
* If a different `Operator` is running a given `ServiceJourney`, then this is reflected in the `ServiceJourney` having 
a different `OperatorRef`.
* `Authority`  and `Organisation` are not used.


> **TODO** The **PAG company** (GO = 801) is organised in different parts for managing and identifying journeys. 
>These parts are represented by the `OrganisationPart` and `TransportAdministrativeZone` elements. 
> **TODO**#67: `OrganisationPart` needs to be studied! 6.4.1

## ServiceFacilitySet
*→ [Glossary definition](A4_annex_glossary.md#servicefacilityset)*

### Purpose
Set of `Facilitiy`s available for a `ServiceJourney` or a `JourneyPart`. 

### Table
- [Swiss profile NeTEx definition](../generated/markdown-examples/ServiceFacilitySet.md)

*→ [General NeTEx definition](../generated/netex-html/ServiceFacilitySet.html)*

### Example
- [XML Snippet](../generated/xml-snippets/ServiceFacilitySet.xml)

*→ - [Template](../templates/ServiceFacilitySet.xml)*

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

* The list is fromtime to time revised. The values and lists from the NeTEx standard are not updated.
* This means that a given Facility (e.g. restaurant or diaper changing table) is shown in the appropriate 
subcategory `MealFacilityList` or `FamilyFacilityList`, and a passenger information system can show these categories in 
a reasonable order. The categories themselves are from type `xsd:list`, meaning that the values of a category are a 
separated list of elements. 
* When transforming from HRDF to NeTEx. The `Facility` is often also copied as a `Notice` in textual form.
* The details of the usage are defined in the [mapping table for NeTEX 2.0](media/Mappingtabellen_NeTEx_v2.0.xlsx).
* See also [Use case on service facilities](uc04_service_facilities.md).

## SiteFacilitySet
*→ [Glossary definition](A4_annex_glossary.md#servicefacilityset)*

### Purpose
Set of `Facilitiy`s available at a `StopPlace`, `Quay` or other site elements.

A `SiteFacilitySet` defines a set of facilities like sanitary facilities, ticket service, lockers etc. that can be 
referenced to define facilities of a site.

### Table
- [Swiss profile NeTEx definition](../generated/markdown-examples/SiteFacilitySet.md)

*→ [General NeTEx definition](../generated/netex-html/SiteFacilitySet.html)*

### Example
- [XML Snippet](../generated/xml-snippets/SiteFacilitySet.xml)

*→ - [Template](../templates/SiteFacilitySet.xml)*

### Usage Notes
* Make sure to not generate identical SiteFacilitySets. Reuse them.
* We currently don't have many `SiteFacilitySet` as this is not done in timetables yet. With accessibility and more information from Atlas, this may change. 
* We will keep the list of relevant values updated in [mapping table for NeTEX 2.0](media/Mappingtabellen_NeTEx_v2.0.xlsx).
* There may be an overlap between `SiteFacilitySet` and `ServiceFacilitySet`. However, they reference very different things: site elements and vehicles.
* Sometimes "capabilities"/"limitations" are defined through combinations of what a stop and what a vehicle can do.
* In future also the use of `Equipment` and `EquipmentPlace` may become more important. These are then actual pieces of equipment. This also means that the `Vehicle` must be known and referenced. 

## VehicleType
*→ [Glossary definition](A4_annex_glossary.md#vehicletype)*

### Purpose
A typified vehicle configuration (model or series) defining reusable characteristics such as capacity, dimensions, propulsion, and accessibility features.

### Usage Notes
We currently don't use `VehicleType` or `VehicleModel`. We will need those at some point.

