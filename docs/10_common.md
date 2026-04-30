# Common Elements

This chapter deals with elements that are commonly used. They belong into different frames.

In this chapter:
- Rules for id 
- `MultilingualString`
- `FrameDefaults` (in every frame)
- Time formatting and journey after midnight
- `AlternativeName` (in `TODOFrame`)
- `AlternativeText` (in `TODOFrame`)
- `ResourceFrame`
  - `ResponsibilitySet`
  - `TypeOfValue /Valuesets`
    - `TypeOfProductCategory`
    - `TypeOfService`
  - `Organisation` / `Operator` / `Authority`
  - `ServiceFacilitySet`
  - `SiteFacilitySet`

> **TODO** make links in the toc correct

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
This information will be also transmitted separately in a `KeyList`. 

> [!CAUTION] 
> **TODO** Must be revisited and updated.

All other defined attributes like `created`, `changed`, `modification` are not used. If we need one, we will inform about it in the table associated with the element.

## MultilingualString

NeTEx uses the type `MultilingualString` for descriptive text elements (e.g. `Notice` text, `Name`, `ShortName` etc.).
However, only one language can be set for a given element (e.g. `<MultilingualString lang=”fr”>`). 
Additional languages are introduced through the [AlternativeName](#alternativename) and [AlternativeText](#alternativetext) element.

For [Organisations](#organisation--operator--authority) e.g. there are all languages present.

The `StopPlace` names in Switzerland are language-independent.

## Time Formatting and Journey after Midnight
The time format consists only of the hours, minutes (and seconds) of a 24-hour clock, e.g. `23:55:00`. 
Times that pass midnight of the current `OperatingDay` are marked with a `DayOffset` element. 
If a `ServiceJourney` (in a particular `Call`) runs over midnight, then `DayOffset` must be set to `1`.

## FrameDefaults

### Purpose
With the FrameDefaults we set some basic parameters. When they are not set, we still assume the values that we present 
in the XML snippet.
### Table
 
[Swiss profile tables](../generated/markdown-examples/FrameDefaults.md)

*-> [Original NeTEx table](../generated/xcore/FrameDefaults.html)*


### Example

[XML Snippet](../generated/xml-snippets/FrameDefaults.xml)

*-> [Template](../templates/FrameDefaults.xml)*

## AlternativeName
**TODO** Link to Glossary

### Purpose

**TODO**

### Table

[Swiss profile tables](../generated/markdown-examples/AlternativeName.md)

*-> - [NeTEx](../generated/xcore/AlternativeName.html)*
 
### Example

[XML Snippet](../generated/xml-snippets/AlternativeName.xml)

*-> - [Template](../templates/AlternativeName.xml)*

### Usage Notes

As a general rule: further names (aliases) of `StopPlace` or `Organisation` elements are modelled with `AlternativeName`, 
whereas direct translations of content (for example of `Notice` texts) are modelled with AlternativeText.
For names of `Organisation` and `StopPlace` elements etc., we use `AlternativeName`. 
For text translations, however, [AlternativeText](#AlternativeText) is used.

We only allow the following values for `NameType`: 
- `alias`
- `translation`




## AlternativeText
**TODO** Link to Glossary

### Purpose
The AlternativeText element is a generic way of providing such variants for any text attribute of a DataManagedObject. 

It can be seen as a complement to the AlternativeName mechanism, and can be used to provide an alias for any element.

**TODO**

### Table

[Swiss profile tables](../generated/markdown-examples/AlternativeText.md)

*-> - [NeTEx](../generated/xcore/AlternativeText.html)*
 
### Example

[XML Snippet](../generated/xml-snippets/AlternativeText.xml)

*-> - [Template](../templates/AlternativeText.xml)*

## Usage Notes
The `AlternativeText` is part of a `DataManagedObject` and references the name of the attribute (in terms of the NeTEx 
Metamodel), for which it provides an alternative. 
It contains the alternative text as an attribute of type `MultilingualString` which indicates the language. 

In addition, the `AlternativeText` element may have a `useForLanguage` attribute to indicate a second language for which it may be used as 
an acceptable presentation, if there is no native language alternative; normally this will be the same as the language 
of the string, but might be different.

As a general rule: further names (aliases) of a `StopPlace` or `Organisation` are modelled with [AlternativeNames](#AlternativeName), whereas 
direct translations of content (for example of `Notice` texts) are modelled with `AlternativeTexts`.

# ResourceFrame
**TODO** Link to Glossary

## Purpose
See the following class diagram for the most important objects of the RESOURCE FRAME and their relationships to the other frames.

![ResourceFrame](./media/ResourceFrame.png)
## Contained Elements
**TODO** 

## Table

[Swiss profile tables](../generated/markdown-examples/ResourceFrame.md)

*-> - [NeTEx](../generated/xcore/ResourceFrame.html)*

## Example

[XML Snippet](../generated/xml-snippets/ResourceFrame.xml)

*-> - [Template](../templates/ResourceFrame.xml)*


## Frame Relationships
** TODO**

## ResponsibilitySet
**TODO** Link to Glossary

### Purpose
We use this model to  describe the different roles of the participating companies. For the most part, the company code is used to fully identify the services provided. 


| value of `StakeholderRoleType` | Description                                                                        |
|--------------------------------|------------------------------------------------------------------------------------|
| `EntityLegalOwnership`         | Role of the **concession company** holding the concession for the original service |
| `Operation`                    | role of the **operator company** responsible for providing the transport service   |
## Table

[Swiss profile tables](../generated/markdown-examples/ResponsibilitySet.md)

*-> - [NeTEx](../generated/xcore/ResponsibilitySet.html)*

## Example

[XML Snippet](../generated/xml-snippets/ResponsibilitySet.xml)

*-> - [Template](../templates/ResponsibilitySet.xml)*

## Usage Notes

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

### TypeOfNotice
`TypeOfNotice` is used within a [Notice](07_service.md#Notice) to give information, what it is about. The table below shows the `TypeOfNotice` we use in Switzerland.

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
### TypeOfProductCategory

#### Purpose

For the ServiceJourneys exclusively provided in Switzerland, only the ProductCategories defined in the document [06 Harmonisierung Verkehrsmittel](https://www.allianceswisspass.ch/de/tarife-vorschriften/uebersicht/V580/Produkte-der-V580-FIScommun-1) may be referenced. 
For ServiceJourneys provided in other countries or partially in Switzerland, there are no restrictions, provided that the category does not overlap with the ProductCategories defined for Switzerland.

#### Table
``` xml
<ValueSet id="ch:1:ValueSet:TypeOfProductCategory" version="1" nameOfClass="TypeOfProductCategory">
  <Name>ProductCategories</Name>
  <values>
    <TypeOfProductCategory id="ch:1:TypeOfProductCategory:TER" version="1">
      <alternativeTexts>
        <AlternativeText attributeName="Name">
          <Text lang="it">Train Express Regional</Text>
        </AlternativeText>
        <AlternativeText attributeName="Name">
          <Text lang="en">Train Express Regional</Text>
        </AlternativeText>
        <AlternativeText attributeName="Name">
          <Text lang="fr">Train Express Regional</Text>
        </AlternativeText>
      </alternativeTexts>
      <Name lang="de">TER</Name>
      <ShortName>TER</ShortName>
    </TypeOfProductCategory>
  </values>
</ValueSet>
```

####  Example


### TypeOfService

#### Purpose
The container for `typesOfService` is in TimetableFrame. But it is rather general, so we describe it here.

#### Table
> [!CAUTION] 
> **TODO** link?\

#### Example

``` xml
<typesOfService>
    <TypeOfService id="ch:1:TypeOfService:1" version="1">
        <Name lang="en">PublicJourney</Name>
        <ShortName lang="en">N</ShortName>
        <PrivateCode>1</PrivateCode>
    </TypeOfService>
</typesOfService>
```
#### Usage Notes

`TypeOfService` indicates the purpose of a `ServiceJourney`, for example, whether if it is a passenger transport or a garage run-in. The following types are currently used:

| Name	             | Description                                                                                                                                               |
|-------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------|
| PublicJourney	    | A public passenger transport                                                                                                                              |
| ~~GarageRunOut~~	 | A garage run-out                                                                                                                                          |
| ~~GarageRunIn~~	  | A garage run-in                                                                                                                                           |
| ~~ThroughCoach~~  | 	A special type of public passenger transport that is used if a ServiceJourney is comprised of JourneyParts of other ServiceJourneys because of coupling. |

Actually there is only one allowed value that we use in the Swiss profile: Only the `PublicJourney` are to be exchanged.

So, this is what needs to be in the TimetableFrame:



## Organisation / Operator / Authority


### Purpose

The ORGANISATION is a need to describe a concrete organisation like operator.
The Organisations are identified by their [GO-number](https://opentransportdata.swiss/de/dataset/didok/resource/d66259a0-a77c-4aee-b7bd-e4fba99dcbb1) 
in Switzerland. The TU-Code is to be used for operators of other countries. 

### Table

[Swiss profile tables](../generated/markdown-examples/Operator.md)

### Example

[XML Snippet](../generated/xml-snippets/Operator.xml)

### Usage Notes

> [!NOTE] From 2024, organisations will also be identified 
> by [SBOIDs](https://transportdatamanagement.ch/content/uploads/2021/05/SwissBusinessOrganisationID_DE_1_2.pdf).

The list contains all transport enterprises for which timetable information is delivered. 
The Operators are identified by their GO-number in Switzerland. The TU-Code is to be used for operators of other countries. 

>The **PAG company** (GO = 801) is organised in different parts for managing and identifying journeys. 
>These parts are represented by the `OrganisationPart` and `TransportAdministrativeZone` elements. 

The SBOID and GO number will always be mainly stored in the `KeyList`.

> [!CAUTION] 
> **TODO**: `OrganisationPart` needs to be studied! 6.4.1

`OperatorRef` on a `Line` is always the "Konzessionär". 
If a different `Operator` is running a given `ServiceJourney`, then this is reflected in the `ServiceJourney` having 
a different `OperatorRef`.


## ServiceFacilitySet

>**Original NeTEx definition:**\
>Set of `ServiceFacilitySet` objects available for a `ServiceJourney`. 
>The set may be available only for a specific VEHICLE TYPE within the SERVICE (e.g. carriage equipped with low floor). 
>`ServiceFacilitySets` are listed in the `TimetableFrame` (between trainNumbers and notices). 
>They are referenced in the facilities object of a `ServiceJourney`.

The assignment of `facilities` to `ServiceJourney` or `JourneyPart` is made by using `FacilitySet` elements.

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

> [!CAUTION] 
> **TODO** 10.13.2ff

``` xml
<ServiceFacilitySet id="ch:1:ServiceFacilitySet:A___2" version="1">
  <alternativeTexts>
    <AlternativeText attributeName="Description">
      <Text lang="en">2nd class only</Text>
    </AlternativeText>
    <AlternativeText attributeName="Description">
      <Text lang="fr">Seulement 2e classe</Text>
    </AlternativeText>
    <AlternativeText attributeName="Description">
      <Text lang="it">Solo 2a classe</Text>
    </AlternativeText>
  </alternativeTexts>
  <Extensions>
    <Priority>1</Priority>
    <Condition>4</Condition>
  </Extensions>
  <Description lang="de">Nur 2. Klasse</Description>
  <FareClasses>secondClass</FareClasses>
</ServiceFacilitySet>
```
> [!CAUTION] 
> **TODO** a lot more detail needed. But probably in uc

## SiteFacilitySet

> [!CAUTION] 
> **TODO** not decribed in RG 1.01. What do we do
