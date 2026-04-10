### Elements
| Element | Usage | Type | Description |
|---|---|---|---|
| ValidBetween | 1..1 | ValidBetweenType | Validity of the StopPlace |
| alternativeTexts | 0..1 | AlternativeTextType[] | Alternative texts for the StopPlace |
| keyList | 0..1 | KeyListType | KEY LIST with the KEY VALUEs related to the STOP PLACE. SKI use KeyValues: one for the Didok number one for the SLOID For delivery to SKI only one Value is necessary. |
| Extensions | 0..1 | ExtensionsType | See description of extensions |
| Name | 1..1 | string | The name of the StopPlace |
| ShortName | 0..1 | LocalisedStringType | Description of TYPE OF VALUE. Is used to transmit the abbreviation of the StopPlace. There is not one abbreviation for all StopPlaces |
| PrivateCode | 0..1 | string | Private Code of STOP PLACE. Field must be filled. In Switzerland it is the DiDok number. |
| Centroid | 0..1 | CentroidType | Global or national location of STOP PLACE. |
| alternativeNames | 0..1 | AlternativeNameType[] | Alternative names for SITE ELEMENT. We will also use these for synonyms. From INFO+ the synonyms are used on the StopPlace. |
| TopographicPlaceRef | 0..1 | TopographicPlaceRefType | Reference to TopographicPlace. Link to TopographicPlace of type county or country |
| Weighting | 0..1 | string | Default relative weighting to be used for stop place. The STOP PLACE element WEIGHTING basically accomplishes this feature but only allows the following values: noInterchange interchangeAllowed recommendedInterchange preferredInterchange. To incorporate the desired value range, we will add an EXTENSION element “HafasPriority” that contains the full information. |
| quays | 0..1 | QuayType[] | The QUAYs contained in the STOP PLACE, that is platforms, jetties, bays, taxi ranks, and other points of physical access to VEHICLEs. |
### Substructure
...
