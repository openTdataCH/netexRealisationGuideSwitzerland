
## StopPlace {#stopplace}

(NeTEx-1, 8.5.4.5.1, NeTEx-8.5.3.3.1)

*The STOP PLACE model describes different aspects of a physical point of access to transport, such as a stop or station.*

*A STOP PLACE represents physical stop or station; that is an interchange, a pair of stops or a cluster of stops on a LINE. A STOP PLACE is a type of SITE. Note that a STOP PLACE is a distinct concept from the representation of the stop in a timetable -- the SCHEDULED STOP POINT. The two can be connected using a STOP ASSIGNMENT.*

*The various spaces of which a STOP PLACE is comprised are described as different types of SITE COMPONENT specific to a STOP PLACE, such as platforms (QUAYs).*

### Business Requirements  {#business-requirements-11}

In Switzerland all these StopPlace codes are defined in Didok by order of the Department of Transport (BAV). If the BAV will regulate also "Haltepunkte" and "Haltekante" then also the Quays will be regulated. Foreign StopPlaces may be mapped to Swiss Didok codes.

It is important to notice that the main connection between Didok codes and the NeTEx export are the ScheduledStopPoints. Those will have the same Id (besides the different \<Element Name\> as the StopPlace in many cases. Exceptions are meta stations and local public transport that already uses assignment to "Haltekanten". In that case the ScheduledStopPoint is more refined than the DiDok UIC like codes.

There will be meta-stations added with their own code. In some cases these are added for operational or searching reasons.

### Structure {#structure-11}

+---------------------+--------------------+---------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------+
| **Element**         | **Usage**          | **Structure**                         | **Description**                                                                                                                       |
+=====================+====================+=======================================+=======================================================================================================================================+
| Attributes:                                                                                                                                                                                                              |
|                                                                                                                                                                                                                          |
| - Id                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                          |
| - version                                                                                                                                                                                                                |
+---------------------+--------------------+---------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------+
| ValidBetween        | 0..\*              | See *[7.3.3][] [Substructure][7.3.3]* | Validity from the StopPlace                                                                                                           |
+---------------------+--------------------+---------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------+
| alternativeTexts    | 0:\*               | AlternativeText                       | Abbreviation of the STOP PLACE.                                                                                                       |
|                     |                    |                                       |                                                                                                                                       |
|                     |                    | See *[5.2][20] [AlternativeText][20]* |                                                                                                                                       |
+---------------------+--------------------+---------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------+
| keyList             | 0:\*               | KeyValue                              | KEY LIST with the KEY VALUEs related to the STOP PLACE.                                                                               |
|                     |                    |                                       |                                                                                                                                       |
|                     |                    | See *[7.3.3][] [Substructure][7.3.3]* | SKI use KeyValues:                                                                                                                    |
|                     |                    |                                       |                                                                                                                                       |
|                     |                    |                                       | one for the Didok number                                                                                                              |
|                     |                    |                                       |                                                                                                                                       |
|                     |                    |                                       | one for the SLOID                                                                                                                     |
|                     |                    |                                       |                                                                                                                                       |
|                     |                    |                                       | For delivery to SKI only one Value is necessary.                                                                                      |
+---------------------+--------------------+---------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------+
| Extensions          | 0:1                | ExtensionStructure                    | Extensions of the STOP PLACE.                                                                                                         |
|                     |                    |                                       |                                                                                                                                       |
|                     |                    | See *[7.3.3][] [Substructure][7.3.3]* | - HafasPriority                                                                                                                       |
|                     |                    |                                       |                                                                                                                                       |
|                     |                    |                                       | - HafasKMInfo                                                                                                                         |
+---------------------+--------------------+---------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------+
| Name                |                    | MultiLingualString                    | Name of TYPE OF VALUE.                                                                                                                |
+---------------------+--------------------+---------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------+
| ShortName           |                    | MultiLingualString                    | Description of TYPE OF VALUE.                                                                                                         |
|                     |                    |                                       |                                                                                                                                       |
| Attributes:         |                    |                                       | Is used to transmit the abbreviation of the StopPlace. There is not one abbreviation for all StopPlaces                               |
|                     |                    |                                       |                                                                                                                                       |
| - lang              |                    |                                       |                                                                                                                                       |
+---------------------+--------------------+---------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------+
| PrivateCode         | 1:1                | PrivateCodeType                       | Private Code of STOP PLACE.\                                                                                                          |
|                     |                    |                                       | Field **must be filled**. In Switzerland it is the **DiDok** number.                                                                  |
+---------------------+--------------------+---------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------+
| Centroid            | 0:1                | Location                              | Global or national location of STOP PLACE.                                                                                            |
|                     |                    |                                       |                                                                                                                                       |
|                     |                    | See *[7.3.3][] [Substructure][7.3.3]* |                                                                                                                                       |
+---------------------+--------------------+---------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------+
| alternativeNames    | 0:\*               | AlternativeName                       | Alternative names for SITE ELEMENT.                                                                                                   |
|                     |                    |                                       |                                                                                                                                       |
|                     |                    | See *[5.1][18] [AlternativeName][18]* | We will also use these for synonyms. From INFO+ the synonyms are used on the StopPlace.                                               |
+---------------------+--------------------+---------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------+
| TopographicPlaceRef | 0:1                | Reference to TopographicPlace         | Link to TopographicPlace of type county or country                                                                                    |
+---------------------+--------------------+---------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------+
| Weighting           | 0:1                | InterchangeUseEnum                    | Default relative weighting to be used for stop place.                                                                                 |
|                     |                    |                                       |                                                                                                                                       |
|                     |                    |                                       | The STOP PLACE element WEIGHTING basically accomplishes this feature but only allows the following values:                            |
|                     |                    |                                       |                                                                                                                                       |
|                     |                    |                                       | - noInterchange                                                                                                                       |
|                     |                    |                                       |                                                                                                                                       |
|                     |                    |                                       | - interchangeAllowed                                                                                                                  |
|                     |                    |                                       |                                                                                                                                       |
|                     |                    |                                       | - recommendedInterchange                                                                                                              |
|                     |                    |                                       |                                                                                                                                       |
|                     |                    |                                       | - preferredInterchange                                                                                                                |
|                     |                    |                                       |                                                                                                                                       |
|                     |                    |                                       | To incorporate the desired value range, we will add an EXTENSION element "HafasPriority" that contains the full information.          |
+---------------------+--------------------+---------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------+
| quays               | 0:\*               | Quay                                  | The QUAYs contained in the STOP PLACE, that is platforms, jetties, bays, taxi ranks, and other points of physical access to VEHICLEs. |
|                     |                    |                                       |                                                                                                                                       |
|                     |                    | See *[7.4][41] [Quay][41]*            |                                                                                                                                       |
+---------------------+--------------------+---------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------+

### Substructure {#substructure-3}

**ValidBetween**

+--------------------+--------------------+---------------------+------------------------+
| **Element**        | **Usage**          | **Structure**       | **Description**        |
+====================+====================+=====================+========================+
| Validity from the StopPoint                                                            |
+--------------------+--------------------+---------------------+------------------------+
| FromDate           | 0:1                | date                | First day of validity  |
|                    |                    |                     |                        |
|                    |                    | YYYY-MM-DDTHH:MM:SS |                        |
+--------------------+--------------------+---------------------+------------------------+
| ToDate             | 0:1                | date                | Last day of validity   |
|                    |                    |                     |                        |
|                    |                    | YYYY-MM-DDTHH:MM:SS |                        |
+--------------------+--------------------+---------------------+------------------------+

**KeyList**

+--------------------+--------------------+--------------------+------------------------+
| **Element**        | **Usage**          | **Structure**      | **Description**        |
+:===================+:===================+:===================+:=======================+
| KEY LIST with the KEY VALUEs related to the STOP PLACE.                               |
+--------------------+--------------------+--------------------+------------------------+
| KeyValue           | 0:\*               | KeyValue           |                        |
+--------------------+--------------------+--------------------+------------------------+

**KeyValue**

  ------------------------------------------------------------------------------
  **Element**       **Usage**   **Structure**          **Description**
  ----------------- ----------- ---------------------- -------------------------
  Key               1:1         xsd.normalizedString   Key

  Value             1:1         xsd.normalizedString   Value
  ------------------------------------------------------------------------------

**Extensions**

+--------------------+--------------------+--------------------+-------------------------------------------------------------------------------+
| **Element**        | **Usage**          | **Structure**      | **Description**                                                               |
+:===================+:===================+:===================+:==============================================================================+
| KEY LIST with the KEY VALUEs related to the STOP PLACE.                                                                                      |
+--------------------+--------------------+--------------------+-------------------------------------------------------------------------------+
| HafasPriority      | 0:1                | HafasPriority      | Interchange Priority wenn several alternative interchange possibilities exist |
+--------------------+--------------------+--------------------+-------------------------------------------------------------------------------+
| HafasKMInfo        | 0:1                | HafasKMInfo        | Value for Interchange points                                                  |
+--------------------+--------------------+--------------------+-------------------------------------------------------------------------------+

**HafasPriority**

  -------------------------------------------------------------------------------------------------------------------------------
  **Element**       **Usage**   **Structure**     **Description**
  ----------------- ----------- ----------------- -------------------------------------------------------------------------------
  Value             1:1         integer           Interchange Priority wenn several alternative interchange possibilities exist

  -------------------------------------------------------------------------------------------------------------------------------

**HafasKMInfo**

  ------------------------------------------------------------------------------
  **Element**       **Usage**   **Structure**     **Description**
  ----------------- ----------- ----------------- ------------------------------
  Value             1:1         integer           Value for Interchange points

  ------------------------------------------------------------------------------

**Centroid**

+----------------+-----------+--------------------------+-------------------------------------------------------------------------+
| **Element**    | **Usage** | **Structure**            | **Description**                                                         |
+:===============+:==========+:=========================+:========================================================================+
| srsName        | 0:1       | LocatingSystemNameType   | GML id of Type of LOCATING SYSTEM used.                                 |
|                |           |                          |                                                                         |
| \(P\) Location |           |                          |                                                                         |
+----------------+-----------+--------------------------+-------------------------------------------------------------------------+
| Longitude      | 1:1       | LongitudeType            | Longitude of Location.                                                  |
+----------------+-----------+--------------------------+-------------------------------------------------------------------------+
| Latitude       | 1:1       | LatitudeType             | Latitude of Location.                                                   |
+----------------+-----------+--------------------------+-------------------------------------------------------------------------+
| Altitude       | 0:        | AltitudeType             | Altitude of Location.                                                   |
+----------------+-----------+--------------------------+-------------------------------------------------------------------------+
| Coordinates    | 0:1       | CoordinateString gml:pos | GML coordinates providing location in a specified Location system.      |
|                |           |                          |                                                                         |
| \(P\) Location |           |                          | We use this element for Swiss coordinates in our data (swisstopo link). |
|                |           |                          |                                                                         |
|                |           |                          | This String is only provided during export by SKI.                      |
+----------------+-----------+--------------------------+-------------------------------------------------------------------------+

Comment to Centroid

The "Centroid" always contains a location.

- The main coordinates are given as WSG84.

- The Swiss coordinates are added as well, when available (see below)

- INFO+ will not use the data from the import. Always the DIDOK master data will be used for all Swiss coordinates. INFO+ will use the data of foreign places.

### Example {#example-7}

+----------------------------------------------------------------------------------------------+
| \<StopPlace id=**\"ch:1:StopPlace:8503000\"** version=**\"any\"**\>                          |
|                                                                                              |
| \<ValidBetween\>                                                                             |
|                                                                                              |
| \<FromDate\>**1978-10-01T00:00:00**\</FromDate\>                                             |
|                                                                                              |
| \<ToDate\>**2500-12-31T00:00:00**\</ToDate\>                                                 |
|                                                                                              |
| \</ValidBetween\>                                                                            |
|                                                                                              |
| \<alternativeTexts\>                                                                         |
|                                                                                              |
| \<AlternativeText attributeName=**\"Text\"**\>                                               |
|                                                                                              |
| \<Text lang=**\"de\"**\>**ZUE**\</Text\>                                                     |
|                                                                                              |
| \</AlternativeText\>                                                                         |
|                                                                                              |
| \</alternativeTexts\>                                                                        |
|                                                                                              |
| \<keyList\>                                                                                  |
|                                                                                              |
| \<KeyValue\>                                                                                 |
|                                                                                              |
| \<Key\>**DIDOK**\</Key\>                                                                     |
|                                                                                              |
| \<Value\>**8503000**\</Value\>                                                               |
|                                                                                              |
| \</KeyValue\>                                                                                |
|                                                                                              |
| \<KeyValue\>                                                                                 |
|                                                                                              |
| \<Key\>**SLOID**\</Key\>                                                                     |
|                                                                                              |
| \<Value\>**ch:1:sloid:03000**\</Value\>                                                      |
|                                                                                              |
| \</KeyValue\>                                                                                |
|                                                                                              |
| \</keyList\>                                                                                 |
|                                                                                              |
| \<Extensions\>                                                                               |
|                                                                                              |
| \<HafasPriority\>                                                                            |
|                                                                                              |
| \<Value\>**4**\</Value\>                                                                     |
|                                                                                              |
| \</HafasPriority\>                                                                           |
|                                                                                              |
| \<HafasKMInfo\>                                                                              |
|                                                                                              |
| \<Value\>**1000**\</Value\>                                                                  |
|                                                                                              |
| \</HafasKMInfo\>                                                                             |
|                                                                                              |
| \</Extensions\>                                                                              |
|                                                                                              |
| \<Name\>**Zürich HB**\</Name\>                                                               |
|                                                                                              |
| \<ShortName lang=**\"de\"**\>**8503000**\</ShortName\>                                       |
|                                                                                              |
| \<PrivateCode\>**8503000**\</PrivateCode\>                                                   |
|                                                                                              |
| \<Centroid\>                                                                                 |
|                                                                                              |
| \<Location\>                                                                                 |
|                                                                                              |
| \<Longitude\>**8.540212**\</Longitude\>                                                      |
|                                                                                              |
| \<Latitude\>**47.378177**\</Latitude\>                                                       |
|                                                                                              |
| \</Location\>                                                                                |
|                                                                                              |
| \</Centroid\>                                                                                |
|                                                                                              |
| \<alternativeNames\>                                                                         |
|                                                                                              |
| \<AlternativeName id=**\"ch:1:AlternativeName:StopPlace:8503000_8\"** version=**\"any\"**\>  |
|                                                                                              |
| \<NameType\>**alias**\</NameType\>                                                           |
|                                                                                              |
| \<TypeOfName\>**offical**\</TypeOfName\>                                                     |
|                                                                                              |
| \<Name lang=**\"de\"**\>**ZH**\</Name\>                                                      |
|                                                                                              |
| \</AlternativeName\>                                                                         |
|                                                                                              |
| \<AlternativeName id=**\"ch:1:AlternativeName:StopPlace:8503000_10\"** version=**\"any\"**\> |
|                                                                                              |
| \<NameType\>**alias**\</NameType\>                                                           |
|                                                                                              |
| \<TypeOfName\>**offical**\</TypeOfName\>                                                     |
|                                                                                              |
| \<Name lang=**\"de\"**\>**Zurigo**\</Name\>                                                  |
|                                                                                              |
| \</AlternativeName\>                                                                         |
|                                                                                              |
| \<AlternativeName id=**\"ch:1:AlternativeName:StopPlace:8503000_11\"** version=**\"any\"**\> |
|                                                                                              |
| \<NameType\>**alias**\</NameType\>                                                           |
|                                                                                              |
| \<TypeOfName\>**offical**\</TypeOfName\>                                                     |
|                                                                                              |
| \<Name lang=**\"de\"**\>**Züri**\</Name\>                                                    |
|                                                                                              |
| \</AlternativeName\>                                                                         |
|                                                                                              |
| \</alternativeNames\>                                                                        |
|                                                                                              |
| \<TopographicPlaceRef ref=**\"ch:1:TopographicPlace:CH-ZH\"** version=**\"any\"** /\>        |
|                                                                                              |
| \<Weighting\>**preferredInterchange**\</Weighting\>                                          |
|                                                                                              |
| \<quays\>                                                                                    |
|                                                                                              |
| \<Quay id=**\"ch:1:Quay:8503000-10\"** version=**\"any\"**\>                                 |
|                                                                                              |
| \<PublicCode\>**10**\</PublicCode\>                                                          |
|                                                                                              |
| \<keyList\>                                                                                  |
|                                                                                              |
| \<KeyValue\>                                                                                 |
|                                                                                              |
| \<Key\>**SLOID**\</Key\>                                                                     |
|                                                                                              |
| \<Value\>**ch:1:sloid:03000:0:10**\</Value\>                                                 |
|                                                                                              |
| \</KeyValue\>                                                                                |
|                                                                                              |
| \</keyList\>                                                                                 |
|                                                                                              |
| \</Quay\>                                                                                    |
|                                                                                              |
| \<Quay id=**\"ch:1:Quay:8503000-11\"** version=**\"any\"**\>                                 |
|                                                                                              |
| \<PublicCode\>**11**\</PublicCode\>                                                          |
|                                                                                              |
| \<keyList\>                                                                                  |
|                                                                                              |
| \<KeyValue\>                                                                                 |
|                                                                                              |
| \<Key\>**SLOID**\</Key\>                                                                     |
|                                                                                              |
| \<Value\>**ch:1:sloid:03000:0:11**\</Value\>                                                 |
|                                                                                              |
| \</KeyValue\>                                                                                |
|                                                                                              |
| \</keyList\>                                                                                 |
|                                                                                              |
| \</Quay\>                                                                                    |
|                                                                                              |
| **\...**                                                                                     |
|                                                                                              |
| \</quays\>                                                                                   |
|                                                                                              |
| \</StopPlace\>                                                                               |
+==============================================================================================+

