# Common Elements

## id/version and other Attributs

* `version` is generally always set to `"1"`
* We use `responsibilitySetRef` in the following elements xxx
* We use `nameOfClass` in the XXXRef elements.

All other defined attributes like `created`, `changed`, `modification` are not used. If we need one we will inform about it in the table associated with the element.

## MultilingualString
NeTEx uses the type `MultilingualString` for descriptive text elements (e.g. Notice text, Name, ShortName etc.).
However, only one language can be set for a given element (`<MultilingualString lang=”xx”>`). 
Additional languages are introduced through the `AlternativeName` and `AlternativeText` object described in tbd and tbd.

For the organisations e.g. there are all languages present.

The StopPlace names in Switzerland are langugage-independent. 

## IDs
It is important to note that internal or artificially generated IDs should not be used to extract content whenever business keys and attributes are available. For readability and easy referencing, we will use the following principles:
-	We will use attributes to build the technical IDs.
-	The class of the object is the beginning of the technical ID in general.
-	Where there is a compelling need for global stability, the ID will be a global ID. This information will be also transmitted separately in a `KeyList`. 

IDs must be globally unique during importation. 
IDs may also be partially or completely artificially generated. The persistence of ID between exports is then usually not guaranteed. Important business level keys are stored in elements not in IDs (PublicKey, PrivateKey, KeyList). They must be communicated as attribute in the elements.

tbd: Must be revisited and updated.

## Time Formatting and Journey after Midnight
The time format consists only of the hour, minutes (and seconds) of a 24 hour clock, e.g. `23:55:00`. Times that pass midnight of the current OperatingDay are marked with a DayOffset element. If a ServiceJourney (in a particular Call) runs over midnight, then DayOffset must be set to `1`.

## FrameDefaults
With the FrameDefaults we set some basic parameters. When they are not set, we still assume the values that we present in the XML snippet.
- [Swiss profile tables](../generated/markdown-examples/FrameDefaults.md)
- [XML Snippet](../generated/xml-snippets/FrameDefaults.xml)
- [Original NeTEx table](tbd)

## AlternativeName
Original NeTEx definition: "The ALTERNATIVE NAME Model defines reusable texts. For example, we use it to distinguish between two places with the same name in different countries. It complements the ALTERNATIVE TEXT entity, which is used to provide translations for individual text attribues of elements.".

As a general rule: further names (alias) of a StopPlace or Organisation are modelled with AlternativeNames, whereas direct translations of content (for example of Notice texts) are modelled with AlternativeText.
For names of ORGANISATIONs and STOP PLACEs etc., we use AlternativeName. For text translations, however, [AlternativeText](#AlternativeText) is used.

We only allow the following values for `NameType`: 
- `alias`
- `translation`

``` xml 
<alternativeNames>
  <AlternativeName id="ch:1:AlternativeName:StopPlace:8500010_5" ver-sion="any">
    <NameType>alias</NameType>
    <TypeOfName>offical</TypeOfName>
    <Name lang="de">Basilea FFS</Name>
  </AlternativeName>
  <AlternativeName id="ch:1:AlternativeName:StopPlace:8500010_8" ver-sion="any">
    <NameType>alias</NameType>
    <TypeOfName>offical</TypeOfName>
    <Name lang="de">Bale</Name>
  </AlternativeName>
<alternativeNames>
```

- [Swiss profile tables](generated/markdown-examples/AlternativeName.md)
- [XML Snippet](generated/xml-snippets/AlternativeName.xml)

## AlternativeText
Original definition: "It is sometime necessary to provide seval variants of a single text, in particular if the infor-mation is required in several national languages. The AlternativeText element is a generic way of providing such variants for any text attribute of a DataManagedObject. It can be seen as a complement to the AlternativeName mechanism, and can be used to provide an alias for any description or text attribute.

The AlternativeText is part of a DataManagedObject and references the name of the attribute in the NeTEx Metamodel) for which it is providing an alternative. It contains the alternative text as an attribute of type MultilingualString which indicates the language. In addition the text may have a ‘Use for’ language attribute to indicate a second language for which it may be used as an acceptable presentation if there is no native language alternative; normally this will be the same as the language of the string, but might be different."

As a general rule: further names (alias) of a StopPlace or Organisation are modelled with [AlternativeNames](#AlternativeName), whereas direct translations of content (for example of Notice Texts) are modelled with AlternativeTexts.
tbd 5.2
```
<notices>
    <Notice id=”ch:1:Notice:Hin-1229900” version=”any”>
      <alternativeTexts>
        <AlternativeText id=”ch:1:AlternativeText:Notice-Hin_1229900-fr” version=”any” attributeName=”Text” useForLanguage=”fr”>
          <Text>Départ de la voie 2.</Text>
        </AlternativeText>
        <AlternativeText id=”ch:1:AlternativeText:Notice-Hin_1229900-it” version=”any” attributeName=”Text” useForLanguage=”it”>
          <Text>Partenza dal binario 2.</Text>
        </AlternativeText>
        <AlternativeText id=”ch:1:AlternativeText:Notice-Hin_1229900-en” version=”any” attributeName=”Text” useForLanguage=”en”>
          <Text>Departure on platform 2.</Text>
        </AlternativeText>
      </alternativeTexts>
      <Text lang="de">Abfahrt auf Gleis 2.</Text>
      <TypeOfNoticeRef ref="ch:1:TypeOfNotice:3" version="any" />
    </Notice>
</notices>
```

```
<AlternativeText attributeName="Name">
  <Text lang="it">Train Express Regional</Text>
</AlternativeText>

```

- [Swiss profile tables](../generated/markdown-examples/AlternativeText.md)
- [XML Snippet](../generated/xml-snippets/AlternativeText.xml)

# ResourceFrame
The RESOURCE FRAME is a coherent set of resource data to which the same VALIDITY CONDITIONs have been assigned. Used to define common resources that will be referenced by other types of FRAME.
See the following class diagram for the most important objects of the RESOURCE FRAME and their relationships to the other frames.
<img width="615" height="435" alt="ResourceFrame_structure" src="https://github.com/user-attachments/assets/219600b4-5e5b-47ab-99a6-89b95784b266" />
tbd image to be moved to docs/include subfolder.

- [Swiss profile tables](../generated/markdown-examples/ResourceFrame.md)
- [XML Snippet](../generated/xml-snippets/ResourceFrame.xml)


## ResponsibilitySet
We use this model to  describe the different roles of the participating companies. For the most part, the company code is used to fully identify the services provided. For the PAG company (801), the attribute ResponsibleArea(Ref) must also be taken into account.


For some replacement services, the public transport sector has decided that the different roles of the companies should be represented when defining the services:
- the role of the company holding the concession for the original service
- the role of the company responsible for providing the transport service

These 2 roles are represented in the ResponsibilitySet element. 
- the role of the concession company is represented by the EntityLegalOwnership value of the StakeholderRoleType attribute
- the role of the company responsible for carrying out the transport is represented by the Op-eration value of the StakeholderRoleType attribute.

- [Swiss profile tables](../generated/markdown-examples/ResponsibilitySet.md)
- [XML Snippet](../generated/xml-snippets/ResponsibilitySet.xml)

```
<responsibilitySets>
    <ResponsibilitySet id="ch:1:ResponsibilitySet:33_801-5678" version="any">
        <!-- For Journey from BLS with replacement Journey by PAG -->
        <Name lang="de">BLS AG (bls)</Name>
        <PrivateCode>BLS</PrivateCode>
        <roles>
            <ResponsibilityRoleAssignment id="ch:1:ResponsibilityRoleAssignment:33_801-5678:1" version="any">
                <StakeholderRole-Type>EntityLegalOwnership</StakeholderRoleType>
                <ResponsibleOrganisationRef ref="ch:1:Operator:33" ver-sion="any"/>
            </ResponsibilityRoleAssignment>
            <ResponsibilityRoleAssignment id="ch:1:ResponsibilityRoleAssignment:33_801-5678:2" version="any">
                <StakeholderRoleType>Operation</StakeholderRoleType>
                <ResponsibleOrganisationRef ref="ch:1:Operator:801" ver-sion="any"/>
                <ResponsibleAreaRef ref="ch:1:TransportAdministrativeZone:801-5678" version="any"/>
            </ResponsibilityRoleAssignment>
        </roles>
    </ResponsibilitySet>
</responsibilitySets>
```
tbd to be checked with.
tbd 6.5.3 Postauto needs to be checked

Only the values defined below are allowed in Switzerland for `StakeholderRoleType` in `ResponsbilityRoleAssignment`:
-	`Operation`
-	`EntityLegalOwnership`
-	`FareManagement`
-	`Planning`
and `FareManagement` and `Planning` are currently not used. Not all roles must be filled.
tbd put this into template as well as a check for enums.


## TypeOfValue / ValueSets
The ResourceFrame contains all the `ValueSets` and `TypeOfValues`. That are used for classifi-cation of NeTEx entities like Notice, ProductCategory etc.
It is preferred that the TypeOfValue are copied from the SKI files and no individual TypeOfValue are created.

TypeOfValue’s are stored in ValueSets as part of the ResourceFrame. We use TypeOfValue references in various Frames in objects including:
-	Notice: references TypeOfNotice
-	ServiceJourney: references TypeOfProductCategory
- tbd

### TypeOfNotice
TypeOfNotice is used within a [Notice](#Notice) to give information, what it is about.  

| Value | Name | Description |
|--|--|--|
|1|Allgemeiner Hinweis|General information text|
|2|Zugname|Name|Name of the train. Is not used, as this is stored in ServiceJourneyName |
|3|Gleis-Angabe|Quay and Quay section information. Will be put into Quay|
|10|Angebot|Most of the ServiceFacilitySet are also transmitted as Notice. On top of that we have multiple services and facilities in Switzerland that cannot be mapped to ServiceFacilitySets. To deliver those special cases as Notices we need an additional TypeOfNotice.|
|11|Region|Postauto is divided into several regions.|

```
<ValueSet id="ch:1:ValueSet:notices" version="any" nameOfClass="TypeOfNotice">
  <values>
    <TypeOfNotice id="ch:1:TypeOfNotice:11" version="any">
      <Name>Region</Name>
      <PrivateCode>11</PrivateCode>
    </TypeOfNotice>
    <TypeOfNotice id="ch:1:TypeOfNotice:1" version="any">
      <Name>Allgemeiner Hinweis</Name>
      <PrivateCode>1</PrivateCode>
    </TypeOfNotice>
    <TypeOfNotice id="ch:1:TypeOfNotice:10" version="any">
      <Name>Angebot</Name>
      <PrivateCode>10</PrivateCode>
    </TypeOfNotice>
    <TypeOfNotice id="ch:1:TypeOfNotice:3" version="any">
      <Name>Gleis-Angabe</Name>
      <PrivateCode>3</PrivateCode>
    </TypeOfNotice>
    <TypeOfNotice id="ch:1:TypeOfNotice:2" version="any">
      <Name>Zugname</Name>
      <PrivateCode>2</PrivateCode>
    </TypeOfNotice>
  </values>
</ValueSet>
```
### TypeOfProductCategory
For the ServiceJourneys exclusively provided in Switzerland, only the ProductCategories de-fined in the document "06 Harmonisierung Verkehrsmittel" (see https://www.allianceswisspass.ch/de/tarife-vorschriften/uebersicht/V580/Produkte-der-V580-FIScommun-1) may be referenced. 
For ServiceJourneys provided in other countries or partially in Switzerland, there are no re-strictions, provided that the category does not overlap with the ProductCategories defined for Switzerland.
```
<ValueSet id="ch:1:ValueSet:TypeOfProductCategory" version="any" nameOfClass="TypeOfProductCategory">
  <Name>ProductCategories</Name>
  <values>
    <TypeOfProductCategory id="ch:1:TypeOfProductCategory:TER" ver-sion="any">
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
The container for typesOfService is in TimetableFrame. But it is rather general, so we describe it here.
tbd link

TypeOfService indicates the purpose of a ServiceJourney, for example, whether if it is a passenger transport or a garage run-in. The following types are currently used:

|TypeOfService	|Description|
|--|--|
|PublicJourney	|A public passenger transport|
|GarageRunOut	|A garage run-out|
|GarageRunIn	|A garage run-in|
|ThroughCoach|	A special type of public passenger transport that is used if a ServiceJourney is comprised of JourneyParts of other ServiceJourneys because of coupling.|

Actually there is only one allowed value that we use in the Swiss profile: Only the PublicJourney are to be exchanged.

So, this is what needs to be in the TimetableFrame:
```
<typesOfService>
    <TypeOfService id="ch:1:TypeOfService:1" version="any">
        <Name lang="en">PublicJourney</Name>
        <ShortName lang="en">N</ShortName>
        <PrivateCode>1</PrivateCode>
    </TypeOfService>
</typesOfService>
```
tbd

## Organisation / Operator / Authority
The ORGANISATION is a need to describe a concrete organisation like operator.
The Organisations are identified by their GO-number in Switzerland (see the https://opentransportdata.swiss/de/dataset/didok/resource/d66259a0-a77c-4aee-b7bd-e4fba99dcbb1). The TU-Code is to be used for operators of other countries. To be noted:  From 2024, organisations will also be identified by SBOIDs. For more infor-mations, see document https://transportdatamanagement.ch/content/uploads/2021/05/SwissBusinessOrganisationID_DE_1_2.pdf

The list contains all transport enterprises for which timetable information is delivered. 
The Operators are identified by their GO-number in Switzerland. The TU-Code is to be used for operators of other countries. 
The PAG company (GO = 801) is organised in different parts for managing and identifying journeys.  These parts are represented by the OrganisationPart and TransportAdministrative-Zone elements.
To be noted:  From 2024, organisations will also be identified by SBOIDs.
The operators must be set. 

The sboid and GO number will always be mainly stored in the KeyList.

tbd: OrganisationPart needs to be studied! 6.4.1

- [Swiss profile tables](../generated/markdown-examples/Operator.md)
- [XML Snippet](../generated/xml-snippets/Operator.xml)

## ServiceFacilitySet
From the original NeTEx definition:
"Set of ServiceFacilitySet objects available for a ServiceJourney. The set may be available only for a specific VEHICLE TYPE within the SERVICE (e.g. carriage equipped with low floor). Ser-viceFacilitySets are listed in the TimetableFrame (between trainNumbers and notices). They are referenced in the facilities object of a ServiceJourney. In the following table are listed only the elements we currently use in the example. "
The assignment of facilities to ServiceJourney or JourneyPart is made by using FacilitySet elements.
SKI uses the following groups to classify facilities:
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

This means that a given Facility (e.g. restaurant or diaper changing table) is shown in the ap-propriate sub category MealFacilityList or FamilyFacilityList and a passenger information sys-tem can show these categories in a reasonable order. The categories themselves are from type "xsd:list“, meaning that the values of a cateogry are a separated list of elements. 

tbd 10.13.2ff

```
<ServiceFacilitySet id="ch:1:ServiceFacilitySet:A___2" version="any">
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
tbd a lot more detail needed. But probably in uc

## SiteFacilitySet
tbd not decribed in RG 1.01. What do we do
