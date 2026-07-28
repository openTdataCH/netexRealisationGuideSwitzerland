# Common Elements and Rules

This chapter has two parts. First, it states important rules to observe (e.g., regarding attributes and date / time formats). Second, it lists the "common" elements that are used by different frames. This in particular includes the `ResourceFrame` and all its elements as it is a container holding data that can be referred to from multiple other frames.

In this chapter:

[Rules to Observe](#rules-to-observe)
- [Attributes](#attributes)
  - [IDs](#ids)
  - [Version](#version)
- [FromDate and ToDate](#fromdate-and-todate)
- [Time formatting and journey after midnight](#time-formatting-and-journey-after-midnight)

[Common Elements and Types](#common-elements-and-types)
- [AlternativeName](#alternativename)
- [AlternativeText](#alternativetext)
- [MultilingualString](#multilingualstring)
- [FrameDefaults](#framedefaults)
- `ResourceFrame` see [here](11_resources.md)


## Rules to Observe

###  Attributes

The following rules apply to common attributes:

| Attribute              | Rule                                                                                                                                                                   |
|------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `id`                   | See description regarding [technical IDs](#ids) below                                                                                                                  |
| `version`              | is always set to `"1"`                                                                                                                                                 |
| `responsibilitySetRef` | We use `responsibilitySetRef` on `ServiceJourney` and `TemplateServiceJourney`.                                                                                        |
| `nameOfRefClass`       | We use `nameOfRefClass` explicitly where a reference target is ambiguous, e.g. on `JourneyPatternRef` (which may resolve to `JourneyPattern` or `ServiceJourneyPattern`). |
| `versionRef`           | is always set to `"1"`. Is used, when the element can't be referenced directly, because it is in a different file. This is in our files true for the INTERCHANGE file. |

*Table: Handling of the most used attributes for elements in NeTEx*

#### IDs
IDs must be globally unique during importation (in the `id`-attribute). 
They may also be partially or completely artificially generated. The persistence of these IDs between exports is then usually not guaranteed. However, for "primary" objects we expect object permanence. This is mentioned in the usage note of each element.
Important business level keys are stored in elements (`KeyList`, `privateCodes/PrivateCode`) in addition to the IDs.

It is important to note that internal or artificially generated IDs should not be used to extract content whenever business keys and attributes are available. 

For readability and easy referencing, we will use the following principles:
-	We use the class of the object to prefix the technical ID like `ch:1:TypeOfNotice:3` for a `TypeOfNotice` element.
-   We use appropriate business values to build technical IDs where available, e.g. `ch:1:TypeOfProductCategory:TER` 
where the value of `ShortName` of the `TypeOfProductCategory` is used to build the ID, or `ch:1:Operator:11`.
-	Where there is a compelling need for global stability, the ID will be a global ID. 


All other defined attributes like `created`, `changed`, `modification` are not used. If we need one, we will inform about it in the table associated with the element.

#### Version
We will use `version="1"` in Switzerland. In some cases we use `versionRef="1"` instead, when the referenced object is not in the same file in references (`XXXRef`-elements). We no longer use `any` and expect to remove that semantic if possible. Also, the version (or versionRef) always must be present.


### FromDate and ToDate
The dates we have are always operating days. Nevertheless, we use
* `2026-01-01T00:00:00`
* `2026-01-01T23:59:59`

to describe a single day.


### Time Formatting and Journey after Midnight

The time format consists only of the hours, minutes (and seconds) of a 24-hour clock, e.g. `23:55:00`. 

Times that pass midnight of the current `OperatingDay` are marked with a `DayOffset` element. 
If a `ServiceJourney` runs over midnight, `DepartureDayOffset` (on `ServiceJourney`) is used for the start of the journey. Since `TimeDemandType` only holds relative durations (`RunTime`/`WaitTime`), there is no separate `DayOffset` element within `TimeDemandType` — any midnight crossing during the journey follows implicitly from cumulating `DepartureTime` with the `RunTime`/`WaitTime` values.

## Common Elements and Types

### AlternativeName

*→ [Glossary definition](A4_annex_glossary.md#alternativetext)*

#### Purpose

`AlternativeName` is used to provide an alternative (alias or translation) of a name, e.g. of 
a `StopPlace` or `Organisation`. 

For all other alternative texts use `MultilingualString`.

#### Table
- [Swiss profile NeTEx definition](../site/tables/AlternativeName.md)

*→ - [General NeTEx definition](../site/netex-html/AlternativeName.html)*
 
#### Example
- [XML Snippet](../site/xml-snippets/AlternativeName.xml)

*→ - [Template](./templates/AlternativeName.xml)*

#### Usage Notes

We only allow the following values for `NameType`: 
- `alias`
- `translation`

### AlternativeText
> `AlternativeText` is not used. We will use `MultilingualString`. This means that there are multiple `<Text>` elements with different `lang`-attributes. 

*→ [Glossary definition](A4_annex_glossary.md#alternativetext)*

#### Purpose
The `AlternativeText` is a generic way to provide an alternative text (translation or alias).  For example, it can be used for the translation of `Notice` texts.



#### Table
- [Swiss profile NeTEx definition](../site/tables/AlternativeText_deprecated.md)

*→ - [General NeTEx definition](../site/netex-html/AlternativeText.html)*
 
#### Example
- [XML Snippet](../site/xml-snippets/AlternativeText_deprecated.xml)

*→ - [Template](./templates/AlternativeText_deprecated.xml)*

#### Usage Notes

The `AlternativeText` is part of a `DataManagedObject` and references the name of the node, for which it provides an alternative. 
It contains the alternative text as an attribute of type `MultilingualString` which indicates the language. 

In addition, the `AlternativeText` element may have a `useForLanguage` attribute to indicate a second language for which it may be used as 
an acceptable presentation, if there is no native language alternative; normally this will be the same as the language 
of the string, but might be different.

Alternative names (translations or aliases) of a `StopPlace` or `Organisation` are modelled with [AlternativeNames](#AlternativeName).

### MultilingualString
*→ [Glossary definition](A4_annex_glossary.md#multilingualstring)*


#### Purpose

NeTEx uses the type `MultilingualString` for descriptive text elements (e.g. `Notice` text, `Name`, `ShortName` etc.).
However, only one language can be set for a given element (e.g. `<MultilingualString lang=”fr”>`). 
Additional languages are introduced through the [AlternativeName](#alternativename) and [AlternativeText](#alternativetext) element.

#### Example

```xml
<Name lang="de">Train Express Regional
  <Text lang="it">Train Express Regional</Text>
  <Text lang="en">Train Express Regional</Text>
  <Text lang="fr">Train Express Regional</Text>
</Name>
```

#### Usage Notes

- For [Organisations](#organisation--operator--authority) e.g. there are all languages present.
- The `StopPlace` names in Switzerland are language-independent.



### FrameDefaults
*→ [Glossary definition](A4_annex_glossary.md#framedefaults)*

#### Purpose
Holds default values for certain basic parameters. 

#### Table
- [Swiss profile NeTEx definition](../site/tables/FrameDefaults.md)

*→ [General NeTEx definition](../site/netex-html/FrameDefaults.html)*

#### Example

- [XML Snippet](../site/xml-snippets/FrameDefaults.xml)

*→ [Template](./templates/FrameDefaults.xml)*

#### Usage Notes
- For values not set in `FrameDefaults` we use the values as indicated in the table and example above.
- We know that the use of the TimezoneOffset are redundant to the TimeZone, but we believe it may make consumption easier and the additional two lines are not really expensive.


