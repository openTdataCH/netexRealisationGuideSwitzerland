
# Specifying the profile using XML examples/templates
First thoughts based on the idea that XML examples could be used as a scaffold for a documentation of the profile.

**Principle:** An XML example/template is annotated with comments that contain all necessary information allowing (a) to derive the Swiss profile from the NeTEx schema, and (b) to provide useful profile-specific documentation. 

**Machinery:** Software by Hans-Jürgen Rennau is likely capable of generating documentation tables for each XML example/template, as well a a complete xsd for the Swiss profile. 


**Advantages:**
- Profile specification attached to XML example/template is quite easily readable and maintainable.
- Minimal effort when NeTEx changes
- XML examples/templates can be copy-pasted by users and the comments help understanding and adhering to the profile.

**Example:** 
- XML example/template for StopPlace - https://github.com/openTdataCH/netexRealisationGuideSwitzerland/tree/main/experimental/specifying_profile_in_xml_example/StopPlace.xml
- The corresponding documentation table is shown below

### StopPlace

| Sub   | Element             | Usage     | Card  | Type                     | Description                                                                                                                           | Note                                                                                                                                                                                                                                                                                                                                                                        |
| ----- | ------------------- | --------- | ----- | ------------------------ | ------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| <<    | ValidBetween        | mandatory | 1..1  | ValidBetweenType         | Validity of the StopPlace                                                                                                             |                                                                                                                                                                                                                                                                                                                                                                             |
|       | alternativeTexts    | mandatory | 1..1  | AlternativeTextType[]    | Alternative texts for the StopPlace                                                                                                   | Abbreviation of the STOP PLACE.                                                                                                                                                                                                                                                                                                                                             |
| >>    | AlternativeText     | mandatory | 1:..* | AlternativeTextType      | ALTERNATIVE TEXTs associated with ENTITY.                                                                                             | Variant for de is always required. Further languages fr, it, en only necessary if different from de.                                                                                                                                                                                                                                                                        |
| >>>>  | Text                | mandatory | 1..1  | MultilingualString       | Variant of the text in the specified language.                                                                                        | Name of the StopPlace in a defined language                                                                                                                                                                                                                                                                                                                                 |
| <<    | keyList             | mandatory | 0..1  | KeyListType              |                                                                                                                                       | KEY LIST with the KEY VALUEs related to the STOP PLACE. SKI use KeyValues: one for the Didok number one for the SLOID For delivery to SKI only one Value is necessary.                                                                                                                                                                                                      |
|       | Extensions          | mandatory | 1..1  | ExtensionsType           | See description of extensions                                                                                                         |                                                                                                                                                                                                                                                                                                                                                                             |
| >>    | HafasPriority       | mandatory | 1..1  | ValueType                |                                                                                                                                       |                                                                                                                                                                                                                                                                                                                                                                             |
| >>>>  | Value               | mandatory | 1..1  | xsd:nonNegativeInteger   |                                                                                                                                       |                                                                                                                                                                                                                                                                                                                                                                             |
| >>    | HafasKMInfo         | expected  | 0..1  | ValueType                |                                                                                                                                       |                                                                                                                                                                                                                                                                                                                                                                             |
| >>>>  | Value               | mandatory | 1..1  | xsd:nonNegativeInteger   |                                                                                                                                       |                                                                                                                                                                                                                                                                                                                                                                             |
|       | Name                | mandatory | 1..1  | MultilingualString       | The name of the StopPlace                                                                                                             |                                                                                                                                                                                                                                                                                                                                                                             |
|       | ShortName           | expected  | 0..1  | MultilingualString       | Description of TYPE OF VALUE.                                                                                                         | Is used to transmit the abbreviation of the StopPlace. There is not one abbreviation for all StopPlaces                                                                                                                                                                                                                                                                     |
|       | PrivateCode         | mandatory | 1..1  | xsd:string               | Private Code of STOP PLACE.                                                                                                           | Field **must be filled**. In Switzerland it is the **DiDok** number.                                                                                                                                                                                                                                                                                                        |
| <<    | Centroid            | expected  | 0..1  | CentroidType             | Global or national location of STOP PLACE.                                                                                            |                                                                                                                                                                                                                                                                                                                                                                             |
|       | alternativeNames    | expected  | 0..1  | AlternativeNameType[]    | Alternative names for SITE ELEMENT.                                                                                                   | We will also use these for synonyms. From INFO+ the synonyms are used on the StopPlace.                                                                                                                                                                                                                                                                                     |
| >> << | AlternativeName     | expected  | 0..*  | AlternativNameType       |                                                                                                                                       | **Use NameType alias, TypeOfName official.**                                                                                                                                                                                                                                                                                                                                |
|       | TopographicPlaceRef | expected  | 0..1  | TopographicPlaceRefType  | Reference to TopographicPlace. Link to TopographicPlace of type county or country                                                     |                                                                                                                                                                                                                                                                                                                                                                             |
|       | Weighting           | optional  | 0..1  | InterchangeWeightingEnum | STOP PLACEs can be classified for their relative desirability (weighting) as an interchange.                                          | Default relative weighting to be used for stop place. The STOP PLACE element WEIGHTING basically accomplishes this feature but only allows the following values: noInterchange interchangeAllowed recommendedInterchange preferredInterchange. To incorporate the desired value range, we will add an EXTENSION element “HafasPriority” that contains the full information. |
|       | quays               | expected  | 0..1  | QuayType[]               | The QUAYs contained in the STOP PLACE, that is platforms, jetties, bays, taxi ranks, and other points of physical access to VEHICLEs. |                                                                                                                                                                                                                                                                                                                                                                             |
| >> << | Quay                | expected  | 0..*  | QuayType                 |                                                                                                                                       |                                                                                                                                                                                                                                                                                                                                                                             |


## Comments

Note the keywords in the XML example/template: *TEMPLATE:, Note:, Usage:* 

- In the table, the columns ***Element, Type, Description*** would be copies from the NeTEx xsd.
- **Column *Sub***: *<<* indicates that the element is described in a table of its own; *>>* indicates that the element is contained in the element from the previous row.
- **Column *Usage***: *mandatory, expected, optional* - perhaps more... (see below)?
- **Column *Note***: profile-specific text complementing ***Description*** 
- **Column *Card***: Cardinality from NeTEx xsd updated by value in ***Usage***


## What kind of changes can be specified?

The document https://github.com/openTdataCH/netexRealisationGuideSwitzerland/blob/main/mgmt/Changes_in_profile.md describes the changes we might want to apply to the standard NeTEx schema in order to obtain the profile. 

Here the thoughts how and to what extent this might be achieved for each type of change. I just treated elements so far, not attributes.

### Add description

`<!-- Note: -->`

### Change cardinality

`<!-- Usage: -->`
- mandatory
- optional

Perhaps additional categories? 
- expected
- deprecated
- ignored - this could be taken as the default if the element doesn't show up in the documentation; the xsd for the profile would contain the element
- forbidden - would we want to show that in the documentation? The xsd would not contain the element.


### Restricted choice

In some cases only a subset of choices is allowed.

If only one choice is allowed - simple: the template XML shows only the allowed variant. 

If multiple choices are allowed - the template XML could be extended with additonal variants (thereby violating the xsd) and marking all elements affected by the choices.

```
<!-- CHOICE: a -->
<!-- CHOICE: a -->
<!-- CHOICE: b -->
<!-- CHOICE: b -->
```


### Disallow element / attribute

```<!-- Note: Data containing the element will be rejected. -->
<!-- Usage: forbidden -->
```

See section **Cardinality** above.

### Mark an element / attribute as to be ignored during importation.

```<!-- Note: Importer will ignore the element. -->
<!-- Usage: ignored -->
```

See section **Cardinality** above. Or slightly different treatment?

### Restrict an enumeration in a given element

Either in `<!-- Note: -->` or `<!-- AllowedEnums: -->`

In any case, the list of enums should appear in *Note* column of the documentation table. 

Also possible to restrict the xsd if the enum is documented in its own separate table.


### Restrict strings, integers etc

We won't do this currently.

e.g. only values between-5 and 5.

### Restrict the allowed types in a container

e.g. no `QuayRef` in quays only `Quay`

- Either just as a `<!-- Note: -->`
- Or, theoretically, one could also have  `<!-- AllowedElements: Quay -->`  and some additional logic. 


### Extension in extension point

Extensions are explicit in the template XML, can be marked as mandatory by `<!-- Usage: mandatory -->`.

This may also be a full substructure


### Restrict to a subset of substitutionGroup

Restrictions on elements that are inherited or part of a subgroup is straightforward since they appear explicitely in the template XML and can be marked as necessary. 

`<!-- Usage: -->`, see section ***ChangeCardinality***

