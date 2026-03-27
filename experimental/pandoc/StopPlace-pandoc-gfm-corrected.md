
## StopPlace

(NeTEx-1, 8.5.4.5.1, NeTEx-8.5.3.3.1)

*The STOP PLACE model describes different aspects of a physical point of
access to transport, such as a stop or station.*

*A STOP PLACE represents physical stop or station; that is an
interchange, a pair of stops or a cluster of stops on a LINE. A STOP
PLACE is a type of SITE. Note that a STOP PLACE is a distinct concept
from the representation of the stop in a timetable – the SCHEDULED STOP
POINT. The two can be connected using a STOP ASSIGNMENT.*

*The various spaces of which a STOP PLACE is comprised are described as
different types of SITE COMPONENT specific to a STOP PLACE, such as
platforms (QUAYs).*

### Business Requirements 

In Switzerland all these `StopPlace` codes are defined in Didok by order
of the Department of Transport (BAV). If the BAV will regulate also
“Haltepunkte” and “Haltekante” then also the Quays will be regulated.
Foreign `StopPlaces` may be mapped to Swiss Didok codes.

It is important to notice that the main connection between Didok codes
and the NeTEx export are the `ScheduledStopPoints`. Those will have the
same Id (besides the different \<Element Name\> as the StopPlace in many
cases. Exceptions are meta stations and local public transport that
already uses assignment to “Haltekanten”. In that case the
`ScheduledStopPoint` is more refined than the DiDok UIC like codes.

There will be meta-stations added with their own code. In some cases
these are added for operational or searching reasons.

### Structure of `StopPlace`

| Element            | Usage | Type                                     | Description                                                                                                                                                                                                                                                                                                                                                                 |
|--------------------|-------|------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ValidBetween       | 0..*  |                                          | See [Substructure](#stopplace.substructure). Validity from the StopPlace                                                                                                                                                                                                                                                                                                    |
| alternativeTexts   | 0:*   | `AlternativText`                         | Abbreviation of the STOP PLACE.                                                                                                                                                                                                                                                                                                                                             |
| keyList            | 0:*   | [KeyValue](#keyvalue)                    | KEY LIST with the KEY VALUEs related to the STOP PLACE.<br>SKI use KeyValues:<br>one for the Didok number one for the SLOID For delivery to SKI only one Value is necessary.                                                                                                                                                                                                |
| Extensions         | 0:1   | ExtensionStructure                       | See [Substructure](#stopplace.substructure)                                                                                                                                                                                                                                                                                                                                 |  Extensions of the STOP PLACE |
| HafasPriority      |       | `HafasKMInfo`                            
| Name		             |       | `MultiLingualString`	                    | Name of TYPE OF VALUE.                                                                                                                                                                                                                                                                                                                                                      
| ShortName          |       | `MultiLingualString`                     | Description of TYPE OF VALUE. Is used to transmit the abbreviation of the `StopPlace`.<br/> There is not one abbreviation for all StopPlaces                                                                                                                                                                                                                                
| PrivateCode        | 1:1   | `PrivateCodeType`                        | 	Private Code of STOP PLACE. Field must be filled. In Switzerland it is the DiDok number.                                                                                                                                                                                                                                                                                   
| Centroid           | 	0:1  | [Location](#stopplace.substructure)      |Global or national location of STOP PLACE.                                                                                                                                                                                                                                                                                     
| alternativeNames   | 0:*   | [AlternativeName](#stopplace.substructure) | Alternative names for SITE ELEMENT. We will also use these for synonyms. From INFO+ the synonyms are used on the StopPlace.                                                                                                                                                                                                 
| TopographicPlaceRef	 | 0:1   | xsd:string                               |	Reference to `TopographicPlace`. Link to TopographicPlace of type county or country 
| Weighting	         | 0:1   | `InterchangeUseEnum`	                    | Default relative weighting to be used for stop place. The STOP PLACE element WEIGHTING basically accomplishes this feature but only allows the following values: noInterchange interchangeAllowed recommendedInterchange preferredInterchange. To incorporate the desired value range, we will add an EXTENSION element “HafasPriority” that contains the full information. 
| quays 	            | 0:* | [Quay](#quay)                            | See 7.4 Quay. The QUAYs contained in the STOP PLACE, that is platforms, jetties, bays, taxi ranks, and other points of physical access to VEHICLEs.                                                                                                                                                                                                                                                                                                                                                                


#### Elements of 'StopPlace'

Using definition lists...

keyList
: KEY LIST with the KEY VALUEs related to the STOP PLACE.
: SKI use KeyValues:<br>one for the Didok number, one for the SLOID. For delivery to SKI only one Value is necessary.

ShortName
: Description of TYPE OF VALUE. Is used to transmit the abbreviation of the `StopPlace`.<br/> There is not one abbreviation for all StopPlaces.

PrivateCode
: Private Code of STOP PLACE.
: Field must be filled. 
: In Switzerland it is the DiDok number.


#### ASCII hierarchy
Alternative way to show structure (could be generated):
``` text
StopPlace:
├─ @id [required]
├─ @version [required]
├─ ValidBetween [0:*]
├─ alternativeTexts: [0:*] (AlternativText)
├─ keyList [0:*] (KeyList)
├─ Extensions [0:*] (ExtensionStructure)
├─ HafasPriority [0:*] (HafasKMInfo)
├─ Name [0:*] (MultiLingualString)
├─ ShortName [0:*]
├─ PrivateCode [0:*]
├─ Centroid [0:*]
├─ alternativeNames [0:*] (AlternativeName)
├─ TopographicPlaceRef [0:1]
     ├─  @ref [required]
     └─  @version [required]
├─ Weighting [0:1]: InterchangeUseEnum
└─ quays:Quay [0:*]
```
StopPlace:
- @id (ID) [required]
- @version [required]
- ValidBetween [0:*]
- alternativeTexts: [0:*] AlternativText
- keyList [0:*] KeyList
- Extensions [0:*] ExtensionStructure
- HafasPriority [0:*] HafasKMInfo
- Name [0:*] MultiLingualString
- ShortName [0:*]
- PrivateCode [0:*]
- Centroid [0:*]
- alternativeNames [0:*]  [AlternativeName](#stopplace.substructure)
- TopographicPlaceRef [0:1]
- Weighting [0:1]: InterchangeUseEnum
- quays [0:*] Quay 

#### XML Schema of StopPlace
``` xml
<?xml version="1.0" encoding="UTF-8"?>
<xsd:schema xmlns:xsd="http://www.w3.org/2001/XMLSchema"
            elementFormDefault="unqualified"
            attributeFormDefault="unqualified">

  <!-- Reusable localized string with optional 'lang' attribute -->
  <xsd:complexType name="LocalisedStringType">
    <xsd:simpleContent>
      <xsd:extension base="xsd:string">
        <xsd:attribute name="lang" type="xsd:language" use="optional"/>
      </xsd:extension>
    </xsd:simpleContent>
  </xsd:complexType>

  <!-- Validity period -->
  <xsd:complexType name="ValidBetweenType">
    <xsd:sequence>
      <xsd:element name="FromDate" type="xsd:dateTime"/>
      <xsd:element name="ToDate" type="xsd:dateTime"/>
    </xsd:sequence>
  </xsd:complexType>

  <!-- Alternative text entry -->
  <xsd:complexType name="AlternativeTextType">
    <xsd:sequence>
      <xsd:element name="Text" type="LocalisedStringType"/>
    </xsd:sequence>
    <xsd:attribute name="attributeName" type="xsd:string" use="required"/>
  </xsd:complexType>

  <!-- Key/value list -->
  <xsd:complexType name="KeyValueType">
    <xsd:sequence>
      <xsd:element name="Key" type="xsd:string"/>
      <xsd:element name="Value" type="xsd:string"/>
    </xsd:sequence>
  </xsd:complexType>

  <xsd:complexType name="KeyListType">
    <xsd:sequence>
      <xsd:element name="KeyValue" type="KeyValueType" minOccurs="1" maxOccurs="unbounded"/>
    </xsd:sequence>
  </xsd:complexType>

  <!-- Extensions -->
  <xsd:complexType name="ExtensionsType">
    <xsd:sequence>
      <xsd:element name="HafasPriority" minOccurs="0">
        <xsd:complexType>
          <xsd:sequence>
            <xsd:element name="Value" type="xsd:int"/>
          </xsd:sequence>
        </xsd:complexType>
      </xsd:element>
      <xsd:element name="HafasKMInfo" minOccurs="0">
        <xsd:complexType>
          <xsd:sequence>
            <xsd:element name="Value" type="xsd:decimal"/>
          </xsd:sequence>
        </xsd:complexType>
      </xsd:element>
    </xsd:sequence>
  </xsd:complexType>

  <!-- Centroid/location -->
  <xsd:complexType name="CentroidType">
    <xsd:sequence>
      <xsd:element name="Location">
        <xsd:complexType>
          <xsd:sequence>
            <xsd:element name="Longitude" type="xsd:decimal"/>
            <xsd:element name="Latitude" type="xsd:decimal"/>
          </xsd:sequence>
        </xsd:complexType>
      </xsd:element>
    </xsd:sequence>
  </xsd:complexType>

  <!-- Alternative names -->
  <xsd:complexType name="AlternativeNameType">
    <xsd:sequence>
      <xsd:element name="NameType" type="xsd:string"/>
      <xsd:element name="TypeOfName" type="xsd:string"/>
      <xsd:element name="Name" type="LocalisedStringType"/>
    </xsd:sequence>
    <xsd:attribute name="id" type="xsd:string" use="required"/>
    <xsd:attribute name="version" type="xsd:string" use="required"/>
  </xsd:complexType>

  <!-- Reference to topographic place -->
  <xsd:complexType name="TopographicPlaceRefType">
    <xsd:attribute name="ref" type="xsd:string" use="required"/>
    <xsd:attribute name="version" type="xsd:string" use="optional"/>
  </xsd:complexType>

  <!-- Quay -->
  <xsd:complexType name="QuayType">
    <xsd:sequence>
      <xsd:element name="PublicCode" type="xsd:string"/>
      <xsd:element name="keyList" type="KeyListType" minOccurs="0"/>
    </xsd:sequence>
    <xsd:attribute name="id" type="xsd:string" use="required"/>
    <xsd:attribute name="version" type="xsd:string" use="required"/>
  </xsd:complexType>

  <!-- StopPlace -->
  <xsd:complexType name="StopPlaceType">
    <xsd:sequence>
      <xsd:element name="ValidBetween" type="ValidBetweenType"/>
      <xsd:element name="alternativeTexts" minOccurs="0">
        <xsd:complexType>
          <xsd:sequence>
            <xsd:element name="AlternativeText" type="AlternativeTextType" minOccurs="0" maxOccurs="unbounded"/>
          </xsd:sequence>
        </xsd:complexType>
      </xsd:element>
      <xsd:element name="keyList" type="KeyListType" minOccurs="0"/>
      <xsd:element name="Extensions" type="ExtensionsType" minOccurs="0"/>
      <xsd:element name="Name" type="xsd:string"/>
      <xsd:element name="ShortName" type="LocalisedStringType" minOccurs="0"/>
      <xsd:element name="PrivateCode" type="xsd:string" minOccurs="0"/>
      <xsd:element name="Centroid" type="CentroidType" minOccurs="0"/>
      <xsd:element name="alternativeNames" minOccurs="0">
        <xsd:complexType>
          <xsd:sequence>
            <xsd:element name="AlternativeName" type="AlternativeNameType" minOccurs="0" maxOccurs="unbounded"/>
          </xsd:sequence>
        </xsd:complexType>
      </xsd:element>
      <xsd:element name="TopographicPlaceRef" type="TopographicPlaceRefType" minOccurs="0"/>
      <xsd:element name="Weighting" type="xsd:string" minOccurs="0"/>
      <xsd:element name="quays" minOccurs="0">
        <xsd:complexType>
          <xsd:sequence>
            <xsd:element name="Quay" type="QuayType" minOccurs="0" maxOccurs="unbounded"/>
          </xsd:sequence>
        </xsd:complexType>
      </xsd:element>
    </xsd:sequence>
    <xsd:attribute name="id" type="xsd:string" use="required"/>
    <xsd:attribute name="version" type="xsd:string" use="required"/>
  </xsd:complexType>

  <xsd:element name="StopPlace" type="StopPlaceType"/>

</xsd:schema>

```

<a id="stopplace.substructure"></a>
### Substructure

**ValidBetween**

**KeyList**



**KeyValue**

| **Element** | **Usage** | **Structure**        | **Description** |
|:------------|:----------|:---------------------|:----------------|
| Key         | 1:1       | xsd.normalizedString | Key             |
| Value       | 1:1       | xsd.normalizedString | Value           |

**Extensions**


**HafasPriority**

| **Element** | **Usage** | **Structure** | **Description** |
|:---|:---|:---|:---|
| Value | 1:1 | integer | Interchange Priority wenn several alternative interchange possibilities exist |

**HafasKMInfo**

| **Element** | **Usage** | **Structure** | **Description**              |
|:------------|:----------|:--------------|:-----------------------------|
| Value       | 1:1       | integer       | Value for Interchange points |

**Centroid**

Comment to Centroid

The “Centroid” always contains a location.

- The main coordinates are given as WSG84.
- The Swiss coordinates are added as well, when available (see below)
- INFO+ will not use the data from the import. Always the DIDOK master
  data will be used for all Swiss coordinates. INFO+ will use the data
  of foreign places.

### Example

``` xml
<StopPlace id="ch:1:StopPlace:8503000" version="any">
    <ValidBetween>
        <FromDate>1978-10-01T00:00:00</FromDate>
        <ToDate>2500-12-31T00:00:00</ToDate>
    </ValidBetween>
    <alternativeTexts>
        <AlternativeText attributeName="Text">
            <Text lang="de">ZUE</Text>
        </AlternativeText>
    </alternativeTexts>
    <keyList>
        <KeyValue>
            <Key>DIDOK</Key>
            <Value>8503000</Value>
        </KeyValue>
        <KeyValue>
            <Key>SLOID</Key>
            <Value>ch:1:sloid:03000</Value>
        </KeyValue>
    </keyList>
    <Extensions>
        <HafasPriority>
            <Value>4</Value>
        </HafasPriority>
        <HafasKMInfo>
            <Value>1000</Value>
        </HafasKMInfo>
    </Extensions>
    <Name>Zürich HB</Name>
    <ShortName lang="de">8503000</ShortName>
    <PrivateCode>8503000</PrivateCode>
    <Centroid>
        <Location>
            <Longitude>8.540212</Longitude>
            <Latitude>47.378177</Latitude>
        </Location>
    </Centroid>
    <alternativeNames>
        <AlternativeName id="ch:1:AlternativeName:StopPlace:8503000_8" version="any">
            <NameType>alias</NameType>
            <TypeOfName>offical</TypeOfName>
            <Name lang="de">ZH</Name>
        </AlternativeName>
        <AlternativeName id="ch:1:AlternativeName:StopPlace:8503000_10" version="any">
            <NameType>alias</NameType>
            <TypeOfName>offical</TypeOfName>
            <Name lang="de">Zurigo</Name>
        </AlternativeName>
        <AlternativeName id="ch:1:AlternativeName:StopPlace:8503000_11" version="any">
            <NameType>alias</NameType>
            <TypeOfName>offical</TypeOfName>
            <Name lang="de">Züri</Name>
        </AlternativeName>
    </alternativeNames>
    <TopographicPlaceRef ref="ch:1:TopographicPlace:CH-ZH" version="any" />
    <Weighting>preferredInterchange</Weighting>
    <quays>
        <Quay id="ch:1:Quay:8503000-10" version="any">
            <PublicCode>10</PublicCode>
            <keyList>
                <KeyValue>
                    <Key>SLOID</Key>
                    <Value>ch:1:sloid:03000:0:10</Value>
                </KeyValue>
             </keyList>
        </Quay>
        <Quay id="ch:1:Quay:8503000-11" version="any">
            <PublicCode>11</PublicCode>
            <keyList>
                <KeyValue>
                    <Key>SLOID</Key>
                    <Value>ch:1:sloid:03000:0:11</Value>
                </KeyValue>
             </keyList>
        </Quay>
        ...
    </quays>
</StopPlace>

```

