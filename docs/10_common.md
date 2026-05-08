> [!CAUTION]\
> **COMMENT** @tuxalp I renamed the title because "Comment Element" seemed me ambigous/unprecise.

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
    - [TypeOfService](#typeofproductcategory)
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
> **TODO** Must be revisited and updated.

All other defined attributes like `created`, `changed`, `modification` are not used. If we need one, we will inform about it in the table associated with the element.

## Common Types

### MultilingualString

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

### Purpose
In the element `FrameDefaults` we set some basic parameters. When they are not set, we still assume the values that we present 
in the XML snippet.

### Table
- [Swiss profile NeTEx definition](../generated/markdown-examples/FrameDefaults.md)

*→ [General NeTEx definition](../generated/xcore/FrameDefaults.html)*

### Example

- [XML Snippet](../generated/xml-snippets/FrameDefaults.xml)

*→ [Template](../templates/FrameDefaults.xml)*

## AlternativeName

*→ [Glossary definition](A4_annex_glossary.md#alternativetext)*

### Purpose

As the name of the element states, the `AlternativeName` is used to provide an alternative (alias or translation) of a name, e.g. of 
a `StopPlace` or `Organisation`. 

For all other alternative texts use `AlternativeText`.

> **Original NeTEx Definition:**\
> The ALTERNATIVE NAME Model defines reusable texts. For example, we use it to distinguish between two places with the 
> same name in different countries.

### Table
- [Swiss profile NeTEx definition](../generated/markdown-examples/AlternativeName.md)

*→ - [General NeTEx definition](../generated/xcore/AlternativeName.html)*
 
### Example
- [XML Snippet](../generated/xml-snippets/AlternativeName.xml)

*→ - [Template](../templates/AlternativeName.xml)*

### Usage Notes

We only allow the following values for `NameType`: 
- `alias`
- `translation`

## AlternativeText

*→ [Glossary definition](A4_annex_glossary.md#alternativetext)*

### Purpose

The `AlternativeText` is a generic way to provide an alternative text (translation or alias).
For example, it can be used for the translation of `Notice` texts.

### Table
- [Swiss profile NeTEx definition](../generated/markdown-examples/AlternativeText.md)

*→ - [General NeTEx definition](../generated/xcore/AlternativeText.html)*
 
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

The ResourceFrame is used to define common resources referenced in other FRAMEs.

> **Original NeTEx Definition:**\
> The RESOURCE FRAME is used to group reusable components for exchange, for example to declare the local code values 
> used in a given data set (VALUE SETs and TYPE OF VALUEs.), or entities common to many frames such as ORGANISATIONs 
> and RESPONSIBILITY SETs. A RESOURCE FRAME can be grouped with other frames using a COMPOSITE FRAME. 

See the following class diagram for the most important objects of the RESOURCE FRAME and their relationships to the other frames.

![ResourceFrame](./media/ResourceFrame.png)

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

*→ - [General NeTEx definition](../generated/xcore/ResourceFrame.html)*

## Example
- [XML Snippet](../generated/xml-snippets/ResourceFrame.xml)

*→ - [Template](../templates/ResourceFrame.xml)*

## Frame Relationships

Elements of the `ResourceFrame` can be referenced in other frames like `SiteFrame`, `ServiceFrame`, `ServiceCalendarFrame` 
and/or `TimetableFrame`.

## ResponsibilitySet

*→ [Glossary definition](A4_annex_glossary.md#responsibilityset)*

### Purpose
We use this element to  describe the different roles of the participating companies. For the most part, the company code is used to fully identify the provided services. 


| value of `StakeholderRoleType` | Description                                                                        |
|--------------------------------|------------------------------------------------------------------------------------|
| `EntityLegalOwnership`         | Role of the **concession company** holding the concession for the original service |
| `Operation`                    | role of the **operator company** responsible for providing the transport service   |
### Table
- [Swiss profile NeTEx definition](../generated/markdown-examples/ResponsibilitySet.md)

*→ - [General NeTEx definition](../generated/xcore/ResponsibilitySet.html)*

### Example
- [XML Snippet](../generated/xml-snippets/ResponsibilitySet.xml)

*→ - [Template](../templates/ResponsibilitySet.xml)*

### Usage Notes

> [!CAUTION] 
> US: Why is there an exception for the PAG? Is it still needed?

For the PAG company (801), the attribute `ResponsibleArea(Ref)` must also be taken into account.

Services (e.g. replacement services) can be associated with different roles. These roles can be defined inside the `ResponsibilitySet` element.

Only the values defined below are allowed in Switzerland for `StakeholderRoleType` in `ResponsbilityRoleAssignment`:
-	`Operation`
-	`EntityLegalOwnership`
-	`FareManagement`
-	`Planning`

`FareManagement` and `Planning` are currently not used. Not all roles must be filled.

> [!CAUTION] 
> **TODO** put this into template as well as a check for enums.

## TypeOfValue / ValueSets
The ResourceFrame contains all the `ValueSets` and `TypeOfValues`. These are used for classification of NeTEx entities like `Notice`, `ProductCategory` etc.
It is preferred that the `TypeOfValue` are copied from the SKI files and no individual `TypeOfValue` are created.

> [!CAUTION] 
> **TODO** add more examples for TypeOfValue usage

`TypeOfValue` elements are stored in `ValueSets` as part of the ResourceFrame. We use TypeOfValue references in various Frames in objects including:
-	`Notice`: references `TypeOfNotice`
-	`ServiceJourney`: references `TypeOfProductCategory`

## TypeOfNotice

`TypeOfNotice` is used within a [Notice](07_service.md#notice) to give information, what it is about. The table below shows the `TypeOfNotice` we use in Switzerland.

> [!CAUTION]
> **TODO** Rework table and example xml\
> **COMMENT** US: remove things that are no longer used, e.g. values 2, 3?

| PrivateCode | Name                | Description                                                                                                                                                                                                                                                      |
|-------------|---------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1           | Allgemeiner Hinweis | General information text                                                                                                                                                                                                                                         |
| 2           | ~~Zugname~~         | Name of the train. Is not used, as this is stored in ServiceJourneyName.                                                                                                                                                                                         |
| 3           | ~~Gleis-Angabe~~    | Quay and Quay section information. Is no longer used. Is put into Quay.                                                                                                                                                                                          |
| 10          | Angebot             | Most of the `ServiceFacilitySet` are also transmitted as `Notice`. On top of that we have multiple services and facilities in Switzerland that cannot be mapped to `ServiceFacilitySets`. This `TypeOfNotice` is used to deliver those special cases as Notices. |
| 11          | ~~Region~~          | Postauto is divided into several regions. Will be omitted. If anything this will be done with different constructs.                                                                                                                                              |

``` xml
<ValueSet id="ch:1:ValueSet:notices" version="1" nameOfClass="TypeOfNotice">
  <values>
    <TypeOfNotice id="ch:1:TypeOfNotice:11" version="1">
      <Name>Region</Name>
      <PrivateCode>11</PrivateCode>
    </TypeOfNotice>
    <TypeOfNotice id="ch:1:TypeOfNotice:1" version="1">
      <Name>Allgemeiner Hinweis</Name>
      <PrivateCode>1</PrivateCode>
    </TypeOfNotice>
    <TypeOfNotice id="ch:1:TypeOfNotice:10" version="1">
      <Name>Angebot</Name>
      <PrivateCode>10</PrivateCode>
    </TypeOfNotice>
    <TypeOfNotice id="ch:1:TypeOfNotice:3" version="1">
      <Name>Gleis-Angabe</Name>
      <PrivateCode>3</PrivateCode>
    </TypeOfNotice>
    <TypeOfNotice id="ch:1:TypeOfNotice:2" version="1">
      <Name>Zugname</Name>
      <PrivateCode>2</PrivateCode>
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

*→ [General NeTEx definition](../generated/xcore/TypeOfProductCategory.html)*


###  Example
- [XML Snippet](../generated/xml-snippets/TypeOfProductCategory.xml)

*→ [Template](../templates/TypeOfProductCategory.xml)*

## TypeOfService

> [!CAUTION]\
> **COMMENT**: @tuxalp This element appears in both frames, ResourceFrame AND TimeTableFrame. This is somewhat confusing... 
> Can I define it at both places? Why don't we describe it under ResourceFrame?
> 
### Purpose

`TypeOfService` indicates the purpose of a `ServiceJourney`, for example, whether if it is a passenger transport or a garage run-in.

> **Original NeTEx description:**\
> A classification for VEHICLE JOURNEYs and SPECIAL SERVICEs to express some common properties of journeys to be taken 
> into account in the scheduling and/or operations control process.

> Not to be confused with TYPE OF SERVICE (FEATURE) of the LOCAL SERVICE and FACILITY model in NeTEx-1, which determines 
> if a LOCAL SERVICE or FACILITY is, for example, a RETAIL SERVICE or TICKETING FACILITY.

### Table
- [Swiss profile NeTEx definition](../generated/markdown-examples/TypeOfService.md)

*→ [General NeTEx definition](../generated/xcore/TypeOfService.html)*

### Example
- [XML Snippet](../generated/xml-snippets/TypeOfService.xml)

*→ - [Template](../templates/TypeOfService.xml)*

### Usage Notes

The following types are currently used:

| Name	             | Description                                                                                                                                               |
|-------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------|
| PublicJourney	    | A public passenger transport                                                                                                                              |
| ~~GarageRunOut~~	 | A garage run-out                                                                                                                                          |
| ~~GarageRunIn~~	  | A garage run-in                                                                                                                                           |
| ~~ThroughCoach~~  | 	A special type of public passenger transport that is used if a ServiceJourney is comprised of JourneyParts of other ServiceJourneys because of coupling. |

Actually there is only one allowed value that we use in the Swiss profile: Only the `PublicJourney` is to be exchanged.

This element can also be defined in the `TimetableFrame` as a child of `typesOfService`:
``` xml
<typesOfService>
    <TypeOfService id="ch:1:TypeOfService:1" version="1">
        <Name lang="en">PublicJourney</Name>
        <ShortName lang="en">N</ShortName>
        <PrivateCode>1</PrivateCode>
    </TypeOfService>
</typesOfService>
```

## Organisation / Operator / Authority

*→ [Glossary definition: Operator](A4_annex_glossary.md#operator)*\
*→ [Glossary definition: Authority](A4_annex_glossary.md#authority)*

### Purpose

The ORGANISATION is a need to describe a concrete organisation like operator.
The Organisations are identified by their [GO-number](https://opentransportdata.swiss/de/dataset/didok/resource/d66259a0-a77c-4aee-b7bd-e4fba99dcbb1) 
in Switzerland. The TU-Code is to be used for operators of other countries. 

### Table
- [Swiss profile NeTEx definition](../generated/markdown-examples/Operator.md)

*→ [General NeTEx definition](../generated/xcore/Operator.html)*

### Example
- [XML Snippet](../generated/xml-snippets/Operator.xml)

*→ - [Template](../templates/Operator.xml)*

### Usage Notes

> [!NOTE] From 2024, organisations will also be identified 
> by [SBOIDs](https://transportdatamanagement.ch/content/uploads/2021/05/SwissBusinessOrganisationID_DE_1_2.pdf).

The list contains all transport enterprises for which timetable information is delivered. 
The Operators are identified by their GO-number in Switzerland. The TU-Code is to be used for operators of other countries. 

>The **PAG company** (GO = 801) is organised in different parts for managing and identifying journeys. 
>These parts are represented by the `OrganisationPart` and `TransportAdministrativeZone` elements. 

The SBOID and GO number shall always also be stored in the `KeyList`.

> [!CAUTION]\
> **TODO**: `OrganisationPart` needs to be studied! 6.4.1

`OperatorRef` on a `Line` is always the "Konzessionär". 
If a different `Operator` is running a given `ServiceJourney`, then this is reflected in the `ServiceJourney` having 
a different `OperatorRef`.

## ServiceFacilitySet

### Purpose

> **Original NeTEx definition:**\
> Set of `ServiceFacilitySet` objects available for a `ServiceJourney`. 
> The set may be available only for a specific VEHICLE TYPE within the SERVICE (e.g. carriage equipped with low floor). 
> `ServiceFacilitySets` are listed in the `TimetableFrame` (between trainNumbers and notices). 
> They are referenced in the facilities object of a `ServiceJourney`.

The assignment of `facilities` to `ServiceJourney` or `JourneyPart` is made by using `ServiceFacilitySet`elements.

> [!CAUTION]\
> **TODO** 10.13.2ff

> [!CAUTION]\
> **TODO** a lot more detail needed. But probably in uc

### Table
- [Swiss profile NeTEx definition](../generated/markdown-examples/ServiceFacilitySet.md)

*→ [General NeTEx definition](../generated/xcore/ServiceFacilitySet.html)*

### Example
- [XML Snippet](../generated/xml-snippets/ServiceFacilitySet.xml)

*→ - [Template](../templates/ServiceFacilitySet.xml)*

### Usage Notes

SKI uses the following groups to classify `facilities`:
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

If necessary, this list can be revised. In case of additions, this can be done, as long as the desired category is defined in the NeTEx specifications. 

This means that a given Facility (e.g. restaurant or diaper changing table) is shown in the appropriate 
subcategory `MealFacilityList` or `FamilyFacilityList`, and a passenger information system can show these categories in 
a reasonable order. The categories themselves are from type `xsd:list`, meaning that the values of a category are a 
separated list of elements. 

## SiteFacilitySet

### Purpose

> [!CAUTION]\
> **COMMENT** @tuxalp not decribed in RG 1.01.\
> **COMMENT** @tuxalp missing in glossary\
> **COMMENT** @tuxalp missing elements in template.

A `SiteFacilitySet` defines a set of facilities like sanitary facilities, ticket service, lockers etc. that can be 
referenced to define facilities of a site.

### Table
- [Swiss profile NeTEx definition](../generated/markdown-examples/SiteFacilitySet.md)

*→ [General NeTEx definition](../generated/xcore/SiteFacilitySet.html)*

### Example
- [XML Snippet](../generated/xml-snippets/SiteFacilitySet.xml)

*→ - [Template](../templates/SiteFacilitySet.xml)*

### Usage Notes

Make sure to not generate identical SiteFacilitySets. Reuse them.

## VehicleType
**TODO**
