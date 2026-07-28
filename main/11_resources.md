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



*Table: ResourceFrame*

| Sub | Element | Usage | Card | Type | Description | Note |
|-----|---------|-------|------|------|-------------|------|
|  | @id | mandatory | 1..1 | xsd:string | Attribute id | |
|  | @version | mandatory | 1..1 | xsd:string | Attribute version | |
|  | responsibilitySets | mandatory | 0..1 | responsibilitySetsInFrame_RelStructure | RESPONSIBILITY SETs used in frame. | RESPONSIBILITY SETs contained in RESOURCE FRAME. ResponsibilitySets are used for the cases in which the LegalEntity, the Operator and the organisation selling the tickets are different. |
| + | [ResponsibilitySet](./tables/ResponsibilitySet.md) | mandatory | 1..1 | ResponsibilitySet | A set of responsibility roles assignments that can be associated with a DATA MANAGED OBJECT. A Child ENTITY has the same responsibilities as its parent. | Each combination of Authority and Operator needs a ResponsibilitySet. |
|  | typesOfValue | mandatory | 0..1 | typesOfValueInFrame_RelStructure | VALUE SETs and TYPE OF VALUEs in frame. | Sets of TYPE OF VALUE contained in the RESOURCE FRAME. |
| + | ValueSet | expected | 1..1 | ValueSet | An extensible set of code values which may be added to by user applications and is used to validate the properties of Entities. | We need a TypeOfNotice ValueSet. |
| ++ | values | expected | 0..1 | typesOfValue_RelStructure | Values in Set. |  |
| +++ | TypeOfNotice | expected | 1..1 | TypeOfNotice | A classification of a NOTICE according to its functional purpose. |  |
| + | ValueSet | expected | 1..1 | ValueSet | An extensible set of code values which may be added to by user applications and is used to validate the properties of Entities. | We need a TypeOfProductCategory ValueSet |
| + | ValueSet | expected | 1..1 | ValueSet | An extensible set of code values which may be added to by user applications and is used to validate the properties of Entities. | We expect a TypsOfPlace Valueset |
|  | organisations | mandatory | 0..1 | organisationsInFrame_RelStructure | ORGANISATIONs in frame. | ORGANISATIONs contained in RESOURCE FRAME. Contains the relevant Operators and other Organisations. We currently face a problem that the same sboid might be reused for Operator and Authority. We will have to check, if we only define Operators, but ue them in Authority as well. TBD |
| + | [Operator](./tables/Operator.md) | mandatory | 1..1 | Operator | A company providing public transport services. | We will use this organisation also in AuthorityRef. The problem is that the sboid can be used only once. |
|  | siteFacilitySets | optional | 0..1 | siteFacilitySetsInFrame_RelStructure | SITE FACILITY SETs in frame . +v1.2.2 | Depending on the export/import part, there will be SiteFacilitySets to be included or not. |
| + | [SiteFacilitySet](./tables/SiteFacilitySet.md) | optional | 1..1 | SiteFacilitySet | Set of enumerated FACILITY values that are relevant to a SITE (names based on TPEG classifications, augmented with UIC etc.). |  |
|  | serviceFacilitySets | optional | 0..1 | serviceFacilitySetsInFrame_RelStructure | SERVICE FACILITies in frame. | Depending on the export/import part, there will be ServiceFacilitySets to be included. If there are ServiceJourneys we expect there to be some. |
| + | [ServiceFacilitySet](./tables/ServiceFacilitySet.md) | optional | 1..1 | ServiceFacilitySet | Service FACILITY. Set of enumerated FACILITY values (Where available names are based on TPEG classifications, augmented with UIC etc.). |  |
|  | vehicleTypes | optional | 0..1 | transportTypeRefs_RelStructure | Opnen specifcation of VEHICLE TYPEs + v1.1 |  |
| + | [VehicleType](./tables/VehicleType.md) | optional | 1..1 | VehicleType | A classification of public transport vehicles according to the vehicle scheduling requirements in mode and capacity (e.g. standard bus, double-deck, ...). |  |




*→ - [General NeTEx definition](../site/netex-html/ResourceFrame.html)*

### Example


```xml
<?xml version="1.0" encoding="UTF-8"?>
<ResourceFrame id="ch:1:ResourceFrame" version="1">
  <responsibilitySets>
  <!-- RESPONSIBILITY SETs contained in RESOURCE FRAME. ResponsibilitySets are used for the cases in which the LegalEntity, the Operator and the organisation selling the tickets are different. -->
  <ResponsibilitySet id="ch:1:ResponsbilitySet-gen" version="1">
  <!-- Each combination of Authority and Operator needs a ResponsibilitySet. -->
  </ResponsibilitySet>
  </responsibilitySets>
  <typesOfValue>
  <!-- Sets of TYPE OF VALUE contained in the RESOURCE FRAME. -->
  <ValueSet id="ch:1:ValueSet:notices" version="1" nameOfClass="TypeOfNotice">
  <!-- We need a TypeOfNotice ValueSet. -->
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
  <ValueSet id="ch:1:ValueSet:TypesOfProductCategory" version="1" nameOfClass="TypeOfProductCategory">
  <!-- We need a TypeOfProductCategory ValueSet -->
  <values>
  <TypeOfProductCategory id="ch:1:TypeOfProductCategory:TER" version="1">
  <Name lang="de">Train Express Regional
  <Text lang="it">Train Express Regional</Text>
  <Text lang="en">Train Express Regional</Text>
  <Text lang="fr">Train Express Regional</Text>
  </Name>
  <ShortName>TER</ShortName>
  </TypeOfProductCategory>
  </values>
  </ValueSet>
  <ValueSet id="ch:1:ValueSet:TypesOfPlace" version="1" nameOfClass="TypeOfPlace">
  <!-- We expect a TypsOfPlace Valueset -->
  <values>
  <TypeOfPlace id="drtCollectionPoint" version="1">
  <Name lang="de">Sammelpunkt
  <Text lang="en">Collection Point</Text>
  </Name>
  </TypeOfPlace>
  <TypeOfPlace id="regularStop" version="1">
  <Name lang="de">Reguläre Haltestelle
  <Text lang="en">Regular Stop</Text>
  </Name>
  </TypeOfPlace>
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
  <vehicleTypes>
  <VehicleType id="tbd" version="1"/>
  </vehicleTypes>
</ResourceFrame>
```



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



Each combination of Authority and Operator needs a ResponsibilitySet. EntitiyLegalOwnership ismandatory. All other roles are optional. However, we prefer to have the Operation part as well. If given Journeys are operated by a different Operator, then a different ResponsibilitySet should be referenced in the ServiceJourney from the Line.

*Table: ResponsibilitySet*

| Sub | Element | Usage | Card | Type | Description | Note |
|-----|---------|-------|------|------|-------------|------|
|  | @id | mandatory | 1..1 | xsd:string | Attribute id | |
|  | @version | mandatory | 1..1 | xsd:string | Attribute version | |
|  | Name | mandatory | 0..* | MultilingualString | Name of Traveller |  |
| + | @lang | mandatory | 1..1 | xsd:string | Attribute lang | |
|  | PrivateCode | expected | 1..1 | PrivateCodeStructure | A private code that uniquely identifies the element. May be used for inter-operating with other (legacy) systems. |  |
|  | roles | mandatory | 0..1 | responsibilityRoleAssignments_RelStructure | Roles defined by this RESPONSIBILITY SET. |  |
| + | ResponsibilityRoleAssignment | mandatory | 1..1 | ResponsibilityRoleAssignment | Assignment of a specific RESPONSIBILITY ROLE to a specific organisation and/or subdivision. |  |
| ++ | StakeholderRoleType | mandatory | 0..1 | StakeholderRoleTypeListOfEnumerations | Stakeholder roles which this assignment assigns. | "EntityLegalOwnership" must be defined once and "Operator" should be too. |
| ++ | ResponsibleOrganisationRef | mandatory | 0..1 | OrganisationRefStructure | Responsible ORGANISATION. |  |




*→ - [General NeTEx definition](../site/netex-html/ResponsibilitySet.html)*

### Example


```xml
<?xml version="1.0" encoding="UTF-8"?>
<ResponsibilitySet id="ch:1:ResponsbilitySet-gen" version="1">
  <!-- Each combination of Authority and Operator needs a ResponsibilitySet. EntitiyLegalOwnership ismandatory. All other roles are optional. However, we prefer to have the Operation part as well. If given Journeys are operated by a different Operator, then a different ResponsibilitySet should be referenced in the ServiceJourney from the Line. -->
  <Name lang="de">Basler Verkehrsbetriebe</Name>
  <PrivateCode>BVB</PrivateCode>
  <roles>
  <ResponsibilityRoleAssignment id="ch:1:ResponsibilityRoleAssignment:823_823:1" version="1">
  <StakeholderRoleType>EntityLegalOwnership
  <!-- "EntityLegalOwnership" must be defined once and "Operator" should be too. -->
  </StakeholderRoleType>
  <ResponsibleOrganisationRef ref="ch:1:sboid:100622" version="1"/>
  </ResponsibilityRoleAssignment>
  <ResponsibilityRoleAssignment id="ch:1:ResponsibilityRoleAssignment:823_823:2" version="1">
  <StakeholderRoleType>Operation</StakeholderRoleType>
  <ResponsibleOrganisationRef ref="ch:1:sboid:100622" version="1"/>
  </ResponsibilityRoleAssignment>
  </roles>
</ResponsibilitySet>
```



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



*Table: TypeOfProductCategory*

| Sub | Element | Usage | Card | Type | Description | Note |
|-----|---------|-------|------|------|-------------|------|
|  | @id | mandatory | 1..1 | xsd:string | Attribute id | |
|  | @version | mandatory | 1..1 | xsd:string | Attribute version | |
|  | Name | mandatory | 0..* | MultilingualString | Name of Traveller |  |
| + | @lang | mandatory | 1..1 | xsd:string | Attribute lang | |
| + | Text | optional | 0..* | MultilingualString | Text content of NOTICe. |  |
| ++ | @lang | mandatory | 1..1 | xsd:string | Attribute lang | |
|  | ShortName | mandatory | 0..* | MultilingualString | Short Name for service |  |




*→ [General NeTEx definition](../xcore/netex/elements/TypeOfProductCategory.html)*


###  Example


```xml
<?xml version="1.0" encoding="UTF-8"?>
<TypeOfProductCategory id="ch:1:TypeOfProductCategory:TER" version="1">
  <alternativeTexts>
  <!-- Is done with MultilanguageString now -->
  </alternativeTexts>
  <Name lang="de">TER
  <Text lang="en">Train Express Regional</Text>
  <Text lang="it">Train Express Regional</Text>
  <Text lang="fr">Train Express Regional</Text>
  </Name>
  <ShortName>TER</ShortName>
</TypeOfProductCategory>
```



*→ [Template](./templates/TypeOfProductCategory.xml)*

## TypeOfService
`TypeOfService` is to be found within `TimetableFrame`.

## Organisation / Operator / Authority

*→ [Glossary definition: Operator](A4_annex_glossary.md#operator)*\
*→ [Glossary definition: Authority](A4_annex_glossary.md#authority)*

### Purpose
A legally incorporated body associated with any aspect of public transportation. `Authority` and `Operator` are `Organisation`s. An `Operator` provides public transport services under contract with an `Authority`. We don't use `Authority`.


### Table



We will use this organisation also in AuthorityRef. The problem is that the sboid can be used only once.

*Table: Operator*

| Sub | Element | Usage | Card | Type | Description | Note |
|-----|---------|-------|------|------|-------------|------|
|  | @id | mandatory | 1..1 | xsd:string | Attribute id | |
|  | @version | mandatory | 1..1 | xsd:string | Attribute version | |
|  | keyList | expected | 1..1 | KeyListStructure | A list of alternative Key values for an element. |  |
| + | KeyValue | expected | 1..* | KeyValueStructure | Key value pair for Entity. |  |
| ++ | Key | expected | 1..1 | xsd:normalizedString | Identifier of value e.g. System. |  |
| ++ | Value | expected | 0..1 | xsd:anyType | Value associated with QUALITY STRUCTURE FACTOR. |  |
|  | privateCodes | expected | 1..1 | PrivateCodesStructure | A list of private codes that uniquely identifiy the element. May be used for inter-operating with other (legacy) systems. +v2.0 |  |
| + | PrivateCode | expected | 0..* | PrivateCodeStructure | A private code that uniquely identifies the element. May be used for inter-operating with other (legacy) systems. | Busines organisation |
|  | PrivateCode | expected | 1..1 | PrivateCodeStructure | A private code that uniquely identifies the element. May be used for inter-operating with other (legacy) systems. |  |
|  | Name | expected | 0..* | MultilingualString | Name of Traveller |  |
|  | ShortName | expected | 0..* | MultilingualString | Short Name for service | there may be cases, when it can't be set. However, when no sboid is there, then ShortName must be filled (especially for foreign operators. |
|  | parts | optional | 0..1 | blockParts_RelStructure | BLOCK PARTs which make up COMPOUND BLOCK. |  |
| ++ | administrativeZones | optional | 0..1 | administrativeZones_RelStructure | Zones managed by ORGANISATION PART. |  |
| +++ | TransportAdministrativeZone | optional | 1..1 | TransportAdministrativeZone | A ZONE relating to the management responsibilities of an ORGANISATION. For example to allocate bus stop identifiers for a region. |  |
| ++++ | PrivateCode | optional | 1..1 | PrivateCodeStructure | A private code that uniquely identifies the element. May be used for inter-operating with other (legacy) systems. |  |




*→ [General NeTEx definition](../xcore/netex/elements/Operator.html)*

### Example


```xml
<?xml version="1.0" encoding="UTF-8"?>
<Operator id="ch:1:sboid:100602" version="1">
  <!-- We will use this organisation also in AuthorityRef. The problem is that the sboid can be used only once. -->
  <keyList>
  <KeyValue>
  <Key>GO</Key>
  <Value>801</Value>
  </KeyValue>
  <KeyValue>
  <Key>SBOID</Key>
  <Value>ch:1:sboid:100602</Value>
  </KeyValue>
  </keyList>
  <privateCodes>
  <PrivateCode type="GO">801
  <!-- Busines organisation -->
  </PrivateCode>
  <PrivateCode type="sboid">ch:1:sboid:100602</PrivateCode>
  </privateCodes>
  <PrivateCode>801</PrivateCode>
  <Name>PostAuto AG</Name>
  <ShortName>PAG
  <!-- there may be cases, when it can't be set. However, when no sboid is there, then ShortName must be filled (especially for foreign operators. -->
  </ShortName>
  <parts>
  <OrganisationPart id="ch:1:OrganisationPart:801-5678" version="1">
  <administrativeZones>
  <TransportAdministrativeZone id="ch:1:TransportAdministrativeZone:801-5678" version="1">
  <PrivateCode>5678</PrivateCode>
  </TransportAdministrativeZone>
  </administrativeZones>
  </OrganisationPart>
  </parts>
</Operator>
```



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



List of ServiceFacility. Be careful: not all are supported. Consult profile. Make sure to not generate identical ServiceFacilitySets. Reuse them. Details in the mapping excel.

*Table: ServiceFacilitySet*

| Sub | Element | Usage | Card | Type | Description | Note |
|-----|---------|-------|------|------|-------------|------|
|  | @id | mandatory | 1..1 | xsd:string | Attribute id | |
|  | @version | mandatory | 1..1 | xsd:string | Attribute version | |
|  | Extensions | expected | 1..1 | ExtensionsStructure | User defined Extensions to ENTITY in schema. (Wrapper tag used to avoid problems with handling of optional 'any' by some validators). | Two elements used in HRDF for ordering facilities |
| + | Priority | expected | 0..1 | InterchangePriorityType | Priority to assign to this INTERCHANGE. |  |
|  | Description | expected | 0..* | MultilingualString | Description of contents. |  |
| + | @lang | mandatory | 1..1 | xsd:string | Attribute lang | |
| + | Text | optional | 0..* | MultilingualString | Text content of NOTICe. |  |
| ++ | @lang | mandatory | 1..1 | xsd:string | Attribute lang | |
|  | FareClasses | optional | 1..1 | FareClassListOfEnumerations | List of FARE CLASSes. |  |
|  | MobilityFacilityList | optional | 1..1 | MobilityFacilityListOfEnumerations | List of MOBILITY FACILITies. |  |
|  | NuisanceFacilityList | optional | 1..1 | NuisanceFacilityListOfEnumerations | List of NUISANCE FACILITies. |  |
|  | PassengerCommsFacilityList | optional | 1..1 | PassengerCommsFacilityListOfEnumerations | List of PASSENGER COMMS FACILITies. |  |
|  | SanitaryFacilityList | optional | 1..1 | SanitaryFacilityListOfEnumerations | List of SANITARY FACILITies. |  |
|  | CouchetteFacilityList | optional | 1..1 | CouchetteFacilityListOfEnumerations | List of COUCHETTE FACILITies. |  |
|  | GroupBookingFacility | optional | 1..1 | GroupBookingEnumeration | Classification of GROUP FACILITY type - TPEG pti23. |  |




*→ [General NeTEx definition](../xcore/netex/elements/ServiceFacilitySet.html)*

### Example


```xml
<?xml version="1.0" encoding="UTF-8"?>
<ServiceFacilitySet id="ch:1:ServiceFacilitySet:A___2" version="1">
  <!-- List of ServiceFacility. Be careful: not all are supported. Consult profile. Make sure to not generate identical ServiceFacilitySets. Reuse them. Details in the mapping excel. -->
  <Extensions>
  <!-- Two elements used in HRDF for ordering facilities -->
  <Priority>1</Priority>
  <Condition>4</Condition>
  </Extensions>
  <Description lang="de">Nur 2. Klasse
  <Text lang="en">2nd class only</Text>
  <Text lang="fr">Seulement 2e classe</Text>
  <Text lang="it">Solo 2a classe</Text>
  </Description>
  <FareClasses>secondClass</FareClasses>
  <MobilityFacilityList>stepFreeAccess lowFloor</MobilityFacilityList>
  <NuisanceFacilityList>animalsAllowed</NuisanceFacilityList>
  <PassengerCommsFacilityList>publicWifi</PassengerCommsFacilityList>
  <SanitaryFacilityList>toilet</SanitaryFacilityList>
  <CouchetteFacilityList>wheelchair</CouchetteFacilityList>
  <GroupBookingFacility>groupsAllowed</GroupBookingFacility>
</ServiceFacilitySet>
```



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



List of SiteFacility. Be careful: not all are supported. Consult profile. Make sure to not generate identical SiteFacilitySets. Reuse them. There might be an overlap to ServiceFacilitySet, but they are used for different purposes.

*Table: SiteFacilitySet*

| Sub | Element | Usage | Card | Type | Description | Note |
|-----|---------|-------|------|------|-------------|------|
|  | @id | mandatory | 1..1 | xsd:string | Attribute id | |
|  | @version | mandatory | 1..1 | xsd:string | Attribute version | |
|  | validityConditions | optional | 1..1 | validityConditions_RelStructure | VALIDITY CONDITIONs conditioning entity. |  |
| + | [AvailabilityCondition](./tables/AvailabilityCondition.md) | optional | 1..1 | AvailabilityCondition | VALIDITY CONDITION stated in terms of DAY TYPES and PROPERTIES OF DAYs. |  |
|  | Description | optional | 0..* | MultilingualString | Description of contents. | Description is optional |
| + | @lang | mandatory | 1..1 | xsd:string | Attribute lang | |
| + | Text | optional | 0..* | MultilingualString | Text content of NOTICe. |  |
| ++ | @lang | mandatory | 1..1 | xsd:string | Attribute lang | |
|  | AssistanceFacilityList | optional | 1..1 | AssistanceFacilityListOfEnumerations | List of ASSISTANCE FACILITies. |  |
|  | AccessibilityToolList | optional | 0..1 | AccessibilityToolListOfEnumerations |  |  |
|  | SanitaryFacilityList | optional | 1..1 | SanitaryFacilityListOfEnumerations | List of SANITARY FACILITies. |  |
|  | TicketingServiceFacilityList | optional | 1..1 | TicketingServiceFacilityListOfEnumerations | List of TICKETING SERVICE FACILITies, e.g. purchase, collection. top up. |  |
|  | EmergencyServiceList | optional | 0..1 | EmergencyServiceListOfEnumerations | Emergency service assistance available. |  |
|  | LuggageLockerFacilityList | optional | 1..1 | LuggageLockerFacilityListOfEnumerations | List of LUGGAGE LOCKER FACILITies. |  |
|  | ParkingFacilityList | optional | 1..1 | ParkingFacilityListOfEnumerations | List of PARKING FACILITies. |  |




*→ [General NeTEx definition](../xcore/netex/elements/SiteFacilitySet.html)*

### Example


```xml
<?xml version="1.0" encoding="UTF-8"?>
<SiteFacilitySet id="generated" version="1">
  <!-- List of SiteFacility. Be careful: not all are supported. Consult profile. Make sure to not generate identical SiteFacilitySets. Reuse them. There might be an overlap to ServiceFacilitySet, but they are used for different purposes. -->
  <validityConditions>
  <AvailabilityCondition id="generated" version="1">
  <FromDate>2026-03-30T12:00:00</FromDate>
  <ToDate>2026-04-01T12:00:00</ToDate>
  <ValidDayBits>01</ValidDayBits>
  </AvailabilityCondition>
  </validityConditions>
  <Description lang="de">SiteFacilitySet Solothurn
  <!-- Description is optional -->
  <Text lang="en">SiteFacilitySet Solothurn</Text>
  </Description>
  <AssistanceFacilityList>personalAssistance information boardingAssistance</AssistanceFacilityList>
  <AccessibilityToolList>audioNavigator</AccessibilityToolList>
  <SanitaryFacilityList>toilet babyChange</SanitaryFacilityList>
  <TicketingServiceFacilityList>all reservations</TicketingServiceFacilityList>
  <EmergencyServiceList>police firstAid</EmergencyServiceList>
  <LuggageLockerFacilityList>lockers</LuggageLockerFacilityList>
  <ParkingFacilityList>parkAndRidePark</ParkingFacilityList>
</SiteFacilitySet>
```



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



Used currently mainly for the relevant accessibility elements that can be expressed currently

*Table: VehicleType*

| Sub | Element | Usage | Card | Type | Description | Note |
|-----|---------|-------|------|------|-------------|------|
|  | @id | mandatory | 1..1 | xsd:string | Attribute id | |
|  | @version | mandatory | 1..1 | xsd:string | Attribute version | |
|  | ShortName | expected | 0..* | MultilingualString | Short Name for service | Will be defined in mapping excel |
|  | LowFloor | optional | 0..1 | xsd:boolean | Whether Vehicle is low floor to facilitate access by the mobility impaired. |  |
|  | HasLiftOrRamp | optional | 0..1 | xsd:boolean | Whether vehicle has lift or ramp to facilitate wheelchair access. |  |
|  | HasHoist | optional | 0..1 | xsd:boolean | Whether vehicle has hoist for wheelchair access. |  |




*→ [General NeTEx definition](../xcore/netex/elements/VehicleType.html)*

### Example


```xml
<?xml version="1.0" encoding="UTF-8"?>
<VehicleType id="ch:1:VehicleType:NF" version="1">
  <!-- Used currently mainly for the relevant accessibility elements that can be expressed currently -->
  <ShortName>NF
  <!-- Will be defined in mapping excel -->
  </ShortName>
  <LowFloor>true</LowFloor>
  <HasLiftOrRamp>false</HasLiftOrRamp>
  <HasHoist>true</HasHoist>
</VehicleType>
```



*→ - [Template](./templates/VehicleType.xml)*

### Usage Notes
* We currently use `VehicleType` but not `VehicleModel`.
* We express accessibility partially through it.
* See more details in the [mapping excel](media/Mappingtabellen_NeTEx_v2.0.xlsx).


