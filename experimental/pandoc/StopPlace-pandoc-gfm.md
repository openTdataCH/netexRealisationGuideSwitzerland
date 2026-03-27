
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

In Switzerland all these StopPlace codes are defined in Didok by order
of the Department of Transport (BAV). If the BAV will regulate also
“Haltepunkte” and “Haltekante” then also the Quays will be regulated.
Foreign StopPlaces may be mapped to Swiss Didok codes.

It is important to notice that the main connection between Didok codes
and the NeTEx export are the ScheduledStopPoints. Those will have the
same Id (besides the different \<Element Name\> as the StopPlace in many
cases. Exceptions are meta stations and local public transport that
already uses assignment to “Haltekanten”. In that case the
ScheduledStopPoint is more refined than the DiDok UIC like codes.

There will be meta-stations added with their own code. In some cases
these are added for operational or searching reasons.

### Structure

<table>
<colgroup>
<col style="width: 27%" />
<col style="width: 11%" />
<col style="width: 24%" />
<col style="width: 35%" />
</colgroup>
<thead>
<tr>
<th><strong>Element</strong></th>
<th><strong>Usage</strong></th>
<th><strong>Structure</strong></th>
<th><strong>Description</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="4"><p>Attributes:</p>
<ul>
<li><p>Id</p></li>
<li><p>version</p></li>
</ul></td>
</tr>
<tr>
<td style="text-align: left;">ValidBetween</td>
<td style="text-align: left;">0..*</td>
<td style="text-align: left;">See <em><a
href="#substructure-3">7.3.3</a> <a
href="#substructure-3">Substructure</a></em></td>
<td style="text-align: left;">Validity from the StopPlace</td>
</tr>
<tr>
<td style="text-align: left;">alternativeTexts</td>
<td style="text-align: left;">0:*</td>
<td style="text-align: left;"><p>AlternativeText</p>
<p>See <em><a href="#alternativetext">5.2</a> <a
href="#alternativetext">AlternativeText</a></em></p></td>
<td>Abbreviation of the STOP PLACE.</td>
</tr>
<tr>
<td>keyList</td>
<td style="text-align: left;">0:*</td>
<td style="text-align: left;"><p>KeyValue</p>
<p>See <em><a href="#substructure-3">7.3.3</a> <a
href="#substructure-3">Substructure</a></em></p></td>
<td style="text-align: left;"><p>KEY LIST with the KEY VALUEs related to
the STOP PLACE.</p>
<p>SKI use KeyValues:</p>
<p>one for the Didok number</p>
<p>one for the SLOID</p>
<p>For delivery to SKI only one Value is necessary.</p></td>
</tr>
<tr>
<td>Extensions</td>
<td style="text-align: left;">0:1</td>
<td style="text-align: left;"><p>ExtensionStructure</p>
<p>See <em><a href="#substructure-3">7.3.3</a> <a
href="#substructure-3">Substructure</a></em></p></td>
<td style="text-align: left;"><p>Extensions of the STOP PLACE.</p>
<ul>
<li><p>HafasPriority</p></li>
<li><p>HafasKMInfo</p></li>
</ul></td>
</tr>
<tr>
<td>Name</td>
<td></td>
<td>MultiLingualString</td>
<td>Name of TYPE OF VALUE.</td>
</tr>
<tr>
<td><p>ShortName</p>
<p>Attributes:</p>
<ul>
<li><p>lang</p></li>
</ul></td>
<td></td>
<td>MultiLingualString</td>
<td><p>Description of TYPE OF VALUE.</p>
<p>Is used to transmit the abbreviation of the StopPlace. There is not
one abbreviation for all StopPlaces</p></td>
</tr>
<tr>
<td>PrivateCode</td>
<td>1:1</td>
<td>PrivateCodeType</td>
<td>Private Code of STOP PLACE.<br />
Field <strong>must be filled</strong>. In Switzerland it is the
<strong>DiDok</strong> number.</td>
</tr>
<tr>
<td>Centroid</td>
<td>0:1</td>
<td><p>Location</p>
<p>See <em><a href="#substructure-3">7.3.3</a> <a
href="#substructure-3">Substructure</a></em></p></td>
<td>Global or national location of STOP PLACE.</td>
</tr>
<tr>
<td style="text-align: left;">alternativeNames</td>
<td style="text-align: left;">0:*</td>
<td style="text-align: left;"><p>AlternativeName</p>
<p>See <em><a href="#alternativename">5.1</a> <a
href="#alternativename">AlternativeName</a></em></p></td>
<td><p>Alternative names for SITE ELEMENT.</p>
<p>We will also use these for synonyms. From INFO+ the synonyms are used
on the StopPlace.</p></td>
</tr>
<tr>
<td>TopographicPlaceRef</td>
<td>0:1</td>
<td>Reference to TopographicPlace</td>
<td>Link to TopographicPlace of type county or country</td>
</tr>
<tr>
<td style="text-align: left;">Weighting</td>
<td style="text-align: left;">0:1</td>
<td style="text-align: left;">InterchangeUseEnum</td>
<td style="text-align: left;"><p>Default relative weighting to be used
for stop place.</p>
<p>The STOP PLACE element WEIGHTING basically accomplishes this feature
but only allows the following values:</p>
<ul>
<li><p>noInterchange</p></li>
<li><p>interchangeAllowed</p></li>
<li><p>recommendedInterchange</p></li>
<li><p>preferredInterchange</p></li>
</ul>
<p>To incorporate the desired value range, we will add an EXTENSION
element “HafasPriority” that contains the full information.</p></td>
</tr>
<tr>
<td style="text-align: left;">quays</td>
<td style="text-align: left;">0:*</td>
<td style="text-align: left;"><p>Quay</p>
<p>See <em><a href="#quay">7.4</a> <a
href="#quay">Quay</a></em></p></td>
<td style="text-align: left;">The QUAYs contained in the STOP PLACE,
that is platforms, jetties, bays, taxi ranks, and other points of
physical access to VEHICLEs.</td>
</tr>
</tbody>
</table>

### Substructure

**ValidBetween**

<table>
<colgroup>
<col style="width: 24%" />
<col style="width: 14%" />
<col style="width: 24%" />
<col style="width: 35%" />
</colgroup>
<thead>
<tr>
<th><strong>Element</strong></th>
<th><strong>Usage</strong></th>
<th><strong>Structure</strong></th>
<th><strong>Description</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="4">Validity from the StopPoint</td>
</tr>
<tr>
<td style="text-align: left;">FromDate</td>
<td style="text-align: left;">0:1</td>
<td style="text-align: left;"><p>date</p>
<p>YYYY-MM-DDTHH:MM:SS</p></td>
<td style="text-align: left;">First day of validity</td>
</tr>
<tr>
<td style="text-align: left;">ToDate</td>
<td style="text-align: left;">0:1</td>
<td style="text-align: left;"><p>date</p>
<p>YYYY-MM-DDTHH:MM:SS</p></td>
<td>Last day of validity</td>
</tr>
</tbody>
</table>

**KeyList**

<table>
<colgroup>
<col style="width: 25%" />
<col style="width: 14%" />
<col style="width: 25%" />
<col style="width: 35%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;"><strong>Element</strong></th>
<th style="text-align: left;"><strong>Usage</strong></th>
<th style="text-align: left;"><strong>Structure</strong></th>
<th style="text-align: left;"><strong>Description</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="4" style="text-align: left;">KEY LIST with the KEY VALUEs
related to the STOP PLACE.</td>
</tr>
<tr>
<td style="text-align: left;">KeyValue</td>
<td style="text-align: left;">0:*</td>
<td style="text-align: left;">KeyValue</td>
<td style="text-align: left;"></td>
</tr>
</tbody>
</table>

**KeyValue**

| **Element** | **Usage** | **Structure**        | **Description** |
|:------------|:----------|:---------------------|:----------------|
| Key         | 1:1       | xsd.normalizedString | Key             |
| Value       | 1:1       | xsd.normalizedString | Value           |

**Extensions**

<table>
<colgroup>
<col style="width: 24%" />
<col style="width: 14%" />
<col style="width: 24%" />
<col style="width: 35%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;"><strong>Element</strong></th>
<th style="text-align: left;"><strong>Usage</strong></th>
<th style="text-align: left;"><strong>Structure</strong></th>
<th style="text-align: left;"><strong>Description</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="4" style="text-align: left;">KEY LIST with the KEY VALUEs
related to the STOP PLACE.</td>
</tr>
<tr>
<td style="text-align: left;">HafasPriority</td>
<td style="text-align: left;">0:1</td>
<td style="text-align: left;">HafasPriority</td>
<td style="text-align: left;">Interchange Priority wenn several
alternative interchange possibilities exist</td>
</tr>
<tr>
<td style="text-align: left;">HafasKMInfo</td>
<td style="text-align: left;">0:1</td>
<td style="text-align: left;">HafasKMInfo</td>
<td style="text-align: left;">Value for Interchange points</td>
</tr>
</tbody>
</table>

**HafasPriority**

| **Element** | **Usage** | **Structure** | **Description** |
|:---|:---|:---|:---|
| Value | 1:1 | integer | Interchange Priority wenn several alternative interchange possibilities exist |

**HafasKMInfo**

| **Element** | **Usage** | **Structure** | **Description**              |
|:------------|:----------|:--------------|:-----------------------------|
| Value       | 1:1       | integer       | Value for Interchange points |

**Centroid**

<table>
<colgroup>
<col style="width: 24%" />
<col style="width: 14%" />
<col style="width: 24%" />
<col style="width: 35%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;"><strong>Element</strong></th>
<th style="text-align: left;"><strong>Usage</strong></th>
<th style="text-align: left;"><strong>Structure</strong></th>
<th style="text-align: left;"><strong>Description</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p>srsName</p>
<p>(P) Location</p></td>
<td style="text-align: left;">0:1</td>
<td style="text-align: left;">LocatingSystemNameType</td>
<td style="text-align: left;">GML id of Type of LOCATING SYSTEM
used.</td>
</tr>
<tr>
<td style="text-align: left;">Longitude</td>
<td style="text-align: left;">1:1</td>
<td style="text-align: left;">LongitudeType</td>
<td style="text-align: left;">Longitude of Location.</td>
</tr>
<tr>
<td style="text-align: left;">Latitude</td>
<td style="text-align: left;">1:1</td>
<td style="text-align: left;">LatitudeType</td>
<td style="text-align: left;">Latitude of Location.</td>
</tr>
<tr>
<td style="text-align: left;">Altitude</td>
<td style="text-align: left;">0:</td>
<td style="text-align: left;">AltitudeType</td>
<td style="text-align: left;">Altitude of Location.</td>
</tr>
<tr>
<td style="text-align: left;"><p>Coordinates</p>
<p>(P) Location</p></td>
<td style="text-align: left;">0:1</td>
<td style="text-align: left;">CoordinateString gml:pos</td>
<td style="text-align: left;"><p>GML coordinates providing location in a
specified Location system.</p>
<p>We use this element for Swiss coordinates in our data (swisstopo
link).</p>
<p>This String is only provided during export by SKI.</p></td>
</tr>
</tbody>
</table>

Comment to Centroid

The “Centroid” always contains a location.

- The main coordinates are given as WSG84.

- The Swiss coordinates are added as well, when available (see below)

- INFO+ will not use the data from the import. Always the DIDOK master
  data will be used for all Swiss coordinates. INFO+ will use the data
  of foreign places.

### Example

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr>
<th><p>&lt;StopPlace id=<strong>"ch:1:StopPlace:8503000"</strong>
version=<strong>"any"</strong>&gt;</p>
<p>&lt;ValidBetween&gt;</p>
<p>&lt;FromDate&gt;<strong>1978-10-01T00:00:00</strong>&lt;/FromDate&gt;</p>
<p>&lt;ToDate&gt;<strong>2500-12-31T00:00:00</strong>&lt;/ToDate&gt;</p>
<p>&lt;/ValidBetween&gt;</p>
<p>&lt;alternativeTexts&gt;</p>
<p>&lt;AlternativeText attributeName=<strong>"Text"</strong>&gt;</p>
<p>&lt;Text
lang=<strong>"de"</strong>&gt;<strong>ZUE</strong>&lt;/Text&gt;</p>
<p>&lt;/AlternativeText&gt;</p>
<p>&lt;/alternativeTexts&gt;</p>
<p>&lt;keyList&gt;</p>
<p>&lt;KeyValue&gt;</p>
<p>&lt;Key&gt;<strong>DIDOK</strong>&lt;/Key&gt;</p>
<p>&lt;Value&gt;<strong>8503000</strong>&lt;/Value&gt;</p>
<p>&lt;/KeyValue&gt;</p>
<p>&lt;KeyValue&gt;</p>
<p>&lt;Key&gt;<strong>SLOID</strong>&lt;/Key&gt;</p>
<p>&lt;Value&gt;<strong>ch:1:sloid:03000</strong>&lt;/Value&gt;</p>
<p>&lt;/KeyValue&gt;</p>
<p>&lt;/keyList&gt;</p>
<p>&lt;Extensions&gt;</p>
<p>&lt;HafasPriority&gt;</p>
<p>&lt;Value&gt;<strong>4</strong>&lt;/Value&gt;</p>
<p>&lt;/HafasPriority&gt;</p>
<p>&lt;HafasKMInfo&gt;</p>
<p>&lt;Value&gt;<strong>1000</strong>&lt;/Value&gt;</p>
<p>&lt;/HafasKMInfo&gt;</p>
<p>&lt;/Extensions&gt;</p>
<p>&lt;Name&gt;<strong>Zürich HB</strong>&lt;/Name&gt;</p>
<p>&lt;ShortName
lang=<strong>"de"</strong>&gt;<strong>8503000</strong>&lt;/ShortName&gt;</p>
<p>&lt;PrivateCode&gt;<strong>8503000</strong>&lt;/PrivateCode&gt;</p>
<p>&lt;Centroid&gt;</p>
<p>&lt;Location&gt;</p>
<p>&lt;Longitude&gt;<strong>8.540212</strong>&lt;/Longitude&gt;</p>
<p>&lt;Latitude&gt;<strong>47.378177</strong>&lt;/Latitude&gt;</p>
<p>&lt;/Location&gt;</p>
<p>&lt;/Centroid&gt;</p>
<p>&lt;alternativeNames&gt;</p>
<p>&lt;AlternativeName
id=<strong>"ch:1:AlternativeName:StopPlace:8503000_8"</strong>
version=<strong>"any"</strong>&gt;</p>
<p>&lt;NameType&gt;<strong>alias</strong>&lt;/NameType&gt;</p>
<p>&lt;TypeOfName&gt;<strong>offical</strong>&lt;/TypeOfName&gt;</p>
<p>&lt;Name
lang=<strong>"de"</strong>&gt;<strong>ZH</strong>&lt;/Name&gt;</p>
<p>&lt;/AlternativeName&gt;</p>
<p>&lt;AlternativeName
id=<strong>"ch:1:AlternativeName:StopPlace:8503000_10"</strong>
version=<strong>"any"</strong>&gt;</p>
<p>&lt;NameType&gt;<strong>alias</strong>&lt;/NameType&gt;</p>
<p>&lt;TypeOfName&gt;<strong>offical</strong>&lt;/TypeOfName&gt;</p>
<p>&lt;Name
lang=<strong>"de"</strong>&gt;<strong>Zurigo</strong>&lt;/Name&gt;</p>
<p>&lt;/AlternativeName&gt;</p>
<p>&lt;AlternativeName
id=<strong>"ch:1:AlternativeName:StopPlace:8503000_11"</strong>
version=<strong>"any"</strong>&gt;</p>
<p>&lt;NameType&gt;<strong>alias</strong>&lt;/NameType&gt;</p>
<p>&lt;TypeOfName&gt;<strong>offical</strong>&lt;/TypeOfName&gt;</p>
<p>&lt;Name
lang=<strong>"de"</strong>&gt;<strong>Züri</strong>&lt;/Name&gt;</p>
<p>&lt;/AlternativeName&gt;</p>
<p>&lt;/alternativeNames&gt;</p>
<p>&lt;TopographicPlaceRef
ref=<strong>"ch:1:TopographicPlace:CH-ZH"</strong>
version=<strong>"any"</strong> /&gt;</p>
<p>&lt;Weighting&gt;<strong>preferredInterchange</strong>&lt;/Weighting&gt;</p>
<p>&lt;quays&gt;</p>
<p>&lt;Quay id=<strong>"ch:1:Quay:8503000-10"</strong>
version=<strong>"any"</strong>&gt;</p>
<p>&lt;PublicCode&gt;<strong>10</strong>&lt;/PublicCode&gt;</p>
<p>&lt;keyList&gt;</p>
<p>&lt;KeyValue&gt;</p>
<p>&lt;Key&gt;<strong>SLOID</strong>&lt;/Key&gt;</p>
<p>&lt;Value&gt;<strong>ch:1:sloid:03000:0:10</strong>&lt;/Value&gt;</p>
<p>&lt;/KeyValue&gt;</p>
<p>&lt;/keyList&gt;</p>
<p>&lt;/Quay&gt;</p>
<p>&lt;Quay id=<strong>"ch:1:Quay:8503000-11"</strong>
version=<strong>"any"</strong>&gt;</p>
<p>&lt;PublicCode&gt;<strong>11</strong>&lt;/PublicCode&gt;</p>
<p>&lt;keyList&gt;</p>
<p>&lt;KeyValue&gt;</p>
<p>&lt;Key&gt;<strong>SLOID</strong>&lt;/Key&gt;</p>
<p>&lt;Value&gt;<strong>ch:1:sloid:03000:0:11</strong>&lt;/Value&gt;</p>
<p>&lt;/KeyValue&gt;</p>
<p>&lt;/keyList&gt;</p>
<p>&lt;/Quay&gt;</p>
<p><strong>...</strong></p>
<p>&lt;/quays&gt;</p>
<p>&lt;/StopPlace&gt;</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>
