# Common Elements

## Rules for common Attributes

The following rules apply to common attributes:

| Attribute     | Rule                                                  |
|---------------|-------------------------------------------------------|
| `id`          | See description regarding [technical IDs](#ids) below |
| `version`     | is always set to `"1"`                                |
| `responsibilitySetRef`     | We use `responsibilitySetRef` in the following elements xxx |
| `nameOfClass` | We use `nameOfClass` in the XXXRef elements.          |

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
The time format consists only of the hours, minutes (and seconds) of a 24 hour clock, e.g. `23:55:00`. 
Times that pass midnight of the current `OperatingDay` are marked with a `DayOffset` element. 
If a `ServiceJourney` (in a particular `Call`) runs over midnight, then `DayOffset` must be set to `1`.

## FrameDefaults
With the FrameDefaults we set some basic parameters. When they are not set, we still assume the values that we present 
in the XML snippet.


| Sub | Element | Usage | Card | Type | Description | Note |
|-----|---------|-------|------|------|-------------|------|
|  | FrameDefaults | expected | 0..1 | VersionFrameDefaultsStructure | Default values to use on elements in the frame that do not explicitly state a value. |  |
| + | DefaultLocale | mandatory | 0..1 | LocaleStructure | Default LOCAL for frame elements. Assume this value for timezone and language of elements if not specified on individual elements. | The default locale is German (de) for SBB and Swiss public transport. |
| ++ | TimeZoneOffset | mandatory | 0..1 | TimeZoneOffsetType | Timezone offset from Greenwich at LOCALE. | We prefer times without the suf-fix "+hh:mm". Instead we specify a default TimeZoneOffset (+2) and SummerTimeZoneOffset (+1) |
| ++ | SummerTimeZoneOffset | mandatory | 0..1 | TimeZoneOffsetType | Summer timezone offset if different from Time zone offset. | We prefer times without the suf-fix "+hh:mm". Instead we specify a default TimeZoneOffset (+2) and SummerTimeZoneOffset (+1) |
| ++ | DefaultLanguage | mandatory | 0..1 | xsd:language | Default Language for LOCALE. Assume language use is "normally used" | Is always set to “de” for SKI and Swiss public transport. |




```xml
<?xml version="1.0" encoding="UTF-8"?>
<FrameDefaults >
  <DefaultLocale>
    <!-- The default locale is German (de) for SBB and Swiss public transport. -->
    <TimeZoneOffset>1</TimeZoneOffset>
    <!-- We prefer times without the suf-fix "+hh:mm". Instead we specify a default TimeZoneOffset (+2) and SummerTimeZoneOffset (+1) -->
    <SummerTimeZoneOffset>2</SummerTimeZoneOffset>
    <!-- We prefer times without the suf-fix "+hh:mm". Instead we specify a default TimeZoneOffset (+2) and SummerTimeZoneOffset (+1) -->
    <DefaultLanguage>de</DefaultLanguage>
    <!-- Is always set to “de” for SKI and Swiss public transport. -->
  </DefaultLocale>
</FrameDefaults>

```


- [Original NeTEx table](tbd)

## AlternativeName
> **Original NeTEx Definition:**\
> The ALTERNATIVE NAME Model defines reusable texts. For example, we use it to distinguish between two places with the same name in different countries. It complements the ALTERNATIVE TEXT entity, which is used to provide translations for individual text attribues of elements.

As a general rule: further names (aliases) of `StopPlace` or `Organisation` elements are modelled with `AlternativeName`, 
whereas direct translations of content (for example of `Notice` texts) are modelled with AlternativeText.
For names of `Organisation` and `StopPlace` elements etc., we use `AlternativeName`. 
For text translations, however, [AlternativeText](#AlternativeText) is used.

We only allow the following values for `NameType`: 
- `alias`
- `translation`

``` xml 
<alternativeNames>
  <AlternativeName id="ch:1:AlternativeName:StopPlace:8500010_5" version="1">
    <NameType>alias</NameType>
    <TypeOfName>offical</TypeOfName>
    <Name lang="de">Basilea FFS</Name>
  </AlternativeName>
  <AlternativeName id="ch:1:AlternativeName:StopPlace:8500010_8" version="1">
    <NameType>alias</NameType>
    <TypeOfName>offical</TypeOfName>
    <Name lang="de">Bale</Name>
  </AlternativeName>
<alternativeNames>
```



| Sub | Element | Usage | Card | Type | Description | Note |
|-----|---------|-------|------|------|-------------|------|
|  | AlternativeName | mandatory | 1..1 | unknown | Alternative Name. | In some cases we need translations or alias of the Name element. This is done with AlternativeName. |
| + | TypeOfName | optional | 0..1 | xsd:normalizedString | Type of Name - open value. |  |
| + | Name | mandatory | 0..1 | MultilingualString | Name of Traveller |  |
| + | @lang | mandatory | 1..1 | xsd:string | Attribute lang | |




```xml
<?xml version="1.0" encoding="UTF-8"?>
<AlternativeName >
  <!-- In some cases we need translations or alias of the Name element. This is done with AlternativeName. -->
  <NameType>alias</NameType>
  <TypeOfName>offical</TypeOfName>
  <Name lang="de">Die Übersetzung des Namens.</Name>
</AlternativeName>

```



## AlternativeText
> **Original NeTEx Definition:** <br>
> It is sometime necessary to provide seval variants of a single text, in particular if the infor-mation is required in several national languages. 
> The AlternativeText element is a generic way of providing such variants for any text attribute of a DataManagedObject. 
> It can be seen as a complement to the AlternativeName mechanism, and can be used to provide an alias for any description or text attribute.

> [!CAUTION] 
> US: term attribute is confusing. Text is in an element.

The `AlternativeText` is part of a `DataManagedObject` and references the name of the attribute (in terms of the NeTEx 
Metamodel), for which it provides an alternative. 
It contains the alternative text as an attribute of type `MultilingualString` which indicates the language. 

In addition, the `AlternativeText` element may have a `useForLanguage` attribute to indicate a second language for which it may be used as 
an acceptable presentation, if there is no native language alternative; normally this will be the same as the language 
of the string, but might be different.

As a general rule: further names (aliases) of a `StopPlace` or `Organisation` are modelled with [AlternativeNames](#AlternativeName), whereas 
direct translations of content (for example of `Notice` texts) are modelled with `AlternativeTexts`.

> [!CAUTION] 
> **TODO** 5.2

<notices>
    <Notice id=”ch:1:Notice:Hin-1229900” version=”1”>
      <alternativeTexts>
        <AlternativeText id=”ch:1:AlternativeText:Notice-Hin_1229900-fr” version=”1” attributeName=”Text” useForLanguage=”fr”>
          <Text>Départ de la voie 2.</Text>
        </AlternativeText>
        <AlternativeText id=”ch:1:AlternativeText:Notice-Hin_1229900-it” version=”1” attributeName=”Text” useForLanguage=”it”>
          <Text>Partenza dal binario 2.</Text>
        </AlternativeText>
        <AlternativeText id=”ch:1:AlternativeText:Notice-Hin_1229900-en” version=”1” attributeName=”Text” useForLanguage=”en”>
          <Text>Departure on platform 2.</Text>
        </AlternativeText>
      </alternativeTexts>
      <Text lang="de">Abfahrt auf Gleis 2.</Text>
      <TypeOfNoticeRef ref="ch:1:TypeOfNotice:3" version="1" />
    </Notice>
</notices>
```

``` xml
<AlternativeText attributeName="Name">
  <Text lang="it">Train Express Regional</Text>
</AlternativeText>
```



| Sub | Element | Usage | Card | Type | Description | Note |
|-----|---------|-------|------|------|-------------|------|
|  | AlternativeText | mandatory | 1..1 | unknown | Alternative Text. +v1.1 |  |
| + | Text | mandatory | 0..1 | MultilingualString | Text content of NOTICe. |  |




```xml
<?xml version="1.0" encoding="UTF-8"?>
<AlternativeText  id="ch:1:AlternativeText:Notice-Hin_1229900-fr" version="1" attributeName="Text" useForLanguage="fr">
  <!--  -->
  <Text>Départ de la voie 2.</Text>
</AlternativeText>

```



# ResourceFrame
The RESOURCE FRAME is a coherent set of resource data to which the same VALIDITY CONDITIONs have been assigned. Used to define common resources that will be referenced by other types of FRAME.

See the following class diagram for the most important objects of the RESOURCE FRAME and their relationships to the other frames.

![ResourceFrame](./media/ResourceFrame.png)



| Sub | Element | Usage | Card | Type | Description | Note |
|-----|---------|-------|------|------|-------------|------|
|  | ResourceFrame | mandatory | 1..1 | unknown | A coherent set of reference values for TYPE OF VALUEs , ORGANISATIONs, VEHICLE TYPEs etc that have a common validity, as specified by a set of frame VALIDITY CONDITIONs. Used to define common resources that will be referenced by other types of FRAME. |  |
| + | responsibilitySets | mandatory | 0..1 | responsibilitySetsInFrame_RelStructure | RESPONSIBILITY SETs used in frame. | RESPONSIBILITY SETs contained in RESOURCE FRAME. ResponsibilitySets are used for the cases in which the LegalEntity, the Operator and the organisation selling the tickets are different. |
| ++ | [ResponsibilitySet](ResponsibilitySet.md) | mandatory | 1..1 | unknown | A set of responsibility roles assignments that can be associated with a DATA MANAGED OBJECT. A Child ENTITY has the same responsibilities as its parent. | Each combination of Authority and Operator needs a ResponsibilitySet. |
| + | typesOfValue | mandatory | 0..1 | typesOfValueInFrame_RelStructure | VALUE SETs and TYPE OF VALUEs in frame. | Sets of TYPE OF VALUE con-tained in the RESOURCE FRAME. |
| ++ | ValueSet | mandatory | 1..1 | unknown | An extensible set of code values which may be added to by user applications and is used to validate the properties of Entities. |  |
| + | organisations | mandatory | 0..1 | organisationsInFrame_RelStructure | ORGANISATIONs in frame. | ORGANISATIONs contained in RESOURCE FRAME. Contains the relevant Operators and other Organisations. We currently face a problem that the same sboid might be reused for Operator and Authority. We will have to check, if we only define Operators, but ue them in Authority as well. TBD |
| ++ | [Operator](Operator.md) | mandatory | 1..1 | unknown | A company providing public transport services. | We will use this organisation also in AuthorityRef. The problem is that the sboid can be used only once. |
| + | siteFacilitySets | optional | 0..1 | siteFacilitySetsInFrame_RelStructure |  | Depending on the export/import part, there will be SiteFacilitySets to be included or not. |
| ++ | [SiteFacilitySet](SiteFacilitySet.md) | optional | 1..1 | unknown | Set of enumerated FACILITY values that are relevant to a SITE (names based on TPEG classifications, augmented with UIC etc.). |  |
| ++ | [ServiceFacilitySet](ServiceFacilitySet.md) | optional | 1..1 | unknown | Service FACILITY. Set of enumerated FACILITY values (Where available names are based on TPEG classifications, augmented with UIC etc.). |  |




```xml
<?xml version="1.0" encoding="UTF-8"?>
<ResourceFrame  id="ch:1:ResourceFrame" version="any">
  <responsibilitySets>
    <!-- RESPONSIBILITY SETs contained in RESOURCE FRAME. ResponsibilitySets are used for the cases in which the LegalEntity, the Operator and the organisation selling the tickets are different. -->
    <ResponsibilitySet id="ch:1:ResponsbilitySet-gen" version="1">
      <!-- Each combination of Authority and Operator needs a ResponsibilitySet. -->
    </ResponsibilitySet>
  </responsibilitySets>
  <typesOfValue>
    <!-- Sets of TYPE OF VALUE con-tained in the RESOURCE FRAME. -->
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
    <ValueSet id="ch:1:ValueSet:TypesOfProductCategory" version="1" nameOfClass="TypeOfProductCategory">
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
  </typesOfValue>
  <organisations>
    <!-- ORGANISATIONs contained in RESOURCE FRAME. Contains the relevant Operators and other Organisations. We currently face a problem that the same sboid might be reused for Operator and Authority. We will have to check, if we only define Operators, but ue them in Authority as well. TBD -->
    <Operator id="sboid" version="1">
      <!-- We will use this organisation also in AuthorityRef. The problem is that the sboid can be used only once. -->
    </Operator>
  </organisations>
  <siteFacilitySets>
    <!-- Depending on the export/import part, there will be SiteFacilitySets to be included or not. -->
    <SiteFacilitySet id="generated" version="1"/>
  </siteFacilitySets>
  <serviceFacilitySets>
    <!-- Depending on the export/import part, there will be ServiceFacilitySets to be included. If there are ServiceJourneys we expect there to be some. -->
    <ServiceFacilitySet id="generated" version="1"/>
  </serviceFacilitySets>
</ResourceFrame>

```



## ResponsibilitySet

> [!CAUTION] 
> US: Why is there an exception for the PAG? Is it still needed?

We use this model to  describe the different roles of the participating companies. For the most part, the company code is used to fully identify the services provided. 
For the PAG company (801), the attribute `ResponsibleArea(Ref)` must also be taken into account.

Services (e.g. replacement services) can be associated with different roles. These roles can be defined inside the `ResponsibilitySet` element.

| value of `StakeholderRoleType` | Description                                                                      |
| ----- |----------------------------------------------------------------------------------|
| `EntityLegalOwnership` | Role of the **conession company** holding the concession for the original service |
| `Operation` | role of the **operator company** responsible for providing the transport service  |



| Sub | Element | Usage | Card | Type | Description | Note |
|-----|---------|-------|------|------|-------------|------|
|  | [ResponsibilitySet](ResponsibilitySet.md) | mandatory | 1..1 | unknown | A set of responsibility roles assignments that can be associated with a DATA MANAGED OBJECT. A Child ENTITY has the same responsibilities as its parent. | Each combination of Authority and Operator needs a ResponsibilitySet. |




```xml
<?xml version="1.0" encoding="UTF-8"?>
<ResponsibilitySet  id="ch:1:ResponsbilitySet-gen" version="1">
  <!-- Each combination of Authority and Operator needs a ResponsibilitySet. -->
</ResponsibilitySet>

```



``` xml
<responsibilitySets>
    <ResponsibilitySet id="ch:1:ResponsibilitySet:33_801-5678" version="1">
        <!-- For Journey from BLS with replacement Journey by PAG -->
        <Name lang="de">BLS AG (bls)</Name>
        <PrivateCode>BLS</PrivateCode>
        <roles>
            <ResponsibilityRoleAssignment id="ch:1:ResponsibilityRoleAssignment:33_801-5678:1" version="1">
                <StakeholderRoleType>EntityLegalOwnership</StakeholderRoleType>
                <ResponsibleOrganisationRef ref="ch:1:Operator:33" version="1"/>
            </ResponsibilityRoleAssignment>
            <ResponsibilityRoleAssignment id="ch:1:ResponsibilityRoleAssignment:33_801-5678:2" version="1">
                <StakeholderRoleType>Operation</StakeholderRoleType>
                <ResponsibleOrganisationRef ref="ch:1:Operator:801" version="1"/>
                <ResponsibleAreaRef ref="ch:1:TransportAdministrativeZone:801-5678" version="1"/>
            </ResponsibilityRoleAssignment>
        </roles>
    </ResponsibilitySet>
</responsibilitySets>
```
> [!CAUTION] 
> **TODO** to be checked with ...\
> **TODO** 6.5.3 Postauto needs to be checked

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
`TypeOfNotice` is used within a [Notice](#Notice) to give information, what it is about. The table below shows the `TypeOfNotice` we use in Switzerland.

> [!CAUTION]
> **TODO** Rework table and example xml\
> **COMMENT** US: remove things that are no longer used, e.g. values 2, 3?

| PrivateCode | Name               | Description                                                                                                                                                                                                                                                    |
|-------------|--------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1           | Allgemeiner Hinweis | General information text                                                                                                                                                                                                                                       |
| 2           | ~~Zugname~~            | Name of the train. Is not used, as this is stored in ServiceJourneyName.                                                                                                                                                                                       |
| 3           | ~~Gleis-Angabe~~   | Quay and Quay section information. Is no longer used. Is put into Quay.                                                                                                                                                                                        |
| 10          | Angebot            | Most of the `ServiceFacilitySet` are also transmitted as `Notice`. On top of that we have multiple services and facilities in Switzerland that cannot be mapped to `ServiceFacilitySets`. This `TypeOfNotice` is used to deliver those special cases as Notices. |
| 11          | ~~Region~~             | Postauto is divided into several regions. Will be omitted. If anything this will be done with different constructs.                                                                                                                                            |

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
For the ServiceJourneys exclusively provided in Switzerland, only the ProductCategories defined in the document [06 Harmonisierung Verkehrsmittel](https://www.allianceswisspass.ch/de/tarife-vorschriften/uebersicht/V580/Produkte-der-V580-FIScommun-1) may be referenced. 
For ServiceJourneys provided in other countries or partially in Switzerland, there are no restrictions, provided that the category does not overlap with the ProductCategories defined for Switzerland.

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

### TypeOfService
The container for `typesOfService` is in TimetableFrame. But it is rather general, so we describe it here.

> [!CAUTION] 
> **TODO** link?\
> **TODO** remove table as it shows TypeOfServices not used in Switzerland?

`TypeOfService` indicates the purpose of a `ServiceJourney`, for example, whether if it is a passenger transport or a garage run-in. The following types are currently used:

| Name	          | Description                                                                                                                                               |
|----------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------|
| PublicJourney	 | A public passenger transport                                                                                                                              |
| ~~GarageRunOut~~	  | A garage run-out                                                                                                                                          |
| ~~GarageRunIn~~	   | A garage run-in                                                                                                                                           |
| ~~ThroughCoach~~   | 	A special type of public passenger transport that is used if a ServiceJourney is comprised of JourneyParts of other ServiceJourneys because of coupling. |

Actually there is only one allowed value that we use in the Swiss profile: Only the `PublicJourney` are to be exchanged.

So, this is what needs to be in the TimetableFrame:

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
The ORGANISATION is a need to describe a concrete organisation like operator.
The Organisations are identified by their [GO-number](https://opentransportdata.swiss/de/dataset/didok/resource/d66259a0-a77c-4aee-b7bd-e4fba99dcbb1) 
in Switzerland. The TU-Code is to be used for operators of other countries. 

> [!NOTE] From 2024, organisations will also be identified 
> by [SBOIDs](https://transportdatamanagement.ch/content/uploads/2021/05/SwissBusinessOrganisationID_DE_1_2.pdf).

The list contains all transport enterprises for which timetable information is delivered. 
The Operators are identified by their GO-number in Switzerland. The TU-Code is to be used for operators of other countries. 

>The **PAG company** (GO = 801) is organised in different parts for managing and identifying journeys. 
>These parts are represented by the `OrganisationPart` and `TransportAdministrativeZone` elements. 

> [!CAUTION] 
> **COMMENT** US: I would remove this sentence as it should be obvious from tables.

~~The operators must be set.~~ 

The SBOID and GO number will always be mainly stored in the `KeyList`.

> [!CAUTION] 
> **TODO**: `OrganisationPart` needs to be studied! 6.4.1

`OperatorRef` on a `Line` is always the "Konzessionär". 
If a different `Operator` is running a given `ServiceJourney`, then this is reflected in the `ServiceJourney` having 
a different `OperatorRef`.


| Sub | Element | Usage | Card | Type | Description | Note |
|-----|---------|-------|------|------|-------------|------|
|  | Operator | mandatory | 1..1 | unknown | A company providing public transport services. | We will use this organisation also in AuthorityRef. The problem is that the sboid can be used only once. |




```xml
<?xml version="1.0" encoding="UTF-8"?>
<Operator  id="sboid" version="1">
  <!-- We will use this organisation also in AuthorityRef. The problem is that the sboid can be used only once. -->
</Operator>

```



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
