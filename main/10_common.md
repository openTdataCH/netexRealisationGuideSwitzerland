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
| `nameOfRefClass`       | We use `nameOfRefClass` explicitly where a reference target is ambiguous, e.g. on `PointRef` (which may resolve to `ScheduledStopPoint` mostly for us).                |
| `versionRef`           | is always set to `"1"`. Is used, when the element can't be referenced directly, because it is in a different file. This is in our files true for the INTERCHANGE file. |

*Table: Handling of the most used attributes for elements in NeTEx*

#### IDs
IDs must be globally unique during importation (in the `@id` of the element). By globally unique we mean:
- They are unique by object type.
- Also they are unique within one delivery (may be multiple files). If two elements have the same `@id` then they must be the same element.
- Between delivery they may change, when they are declared as stable.
- 
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

`AlternativeName` is used to provide an alternative (alias) of a name, e.g. of 
a `StopPlace` or `Organisation`. 

For all translations and other alternative texts use `MultilingualString`.

#### Table



In some cases we need translations or alias of the Name element. This is done with AlternativeName.

*Table: AlternativeName*

| Sub | Element | Usage | Card | Type | Description | Note |
|-----|---------|-------|------|------|-------------|------|
|  | NameType | mandatory | 0..1 | NameTypeEnumeration | Type of Name - fixed value. Default is alias. | In some cases we need translations or alias of the Name element. This is done with AlternativeName. alias allowed for StopPlace. |
|  | TypeOfName | optional | 0..1 | xsd:normalizedString | Type of Name - open value. | For StopPlace official is used for the official name |
|  | Name | mandatory | 0..* | MultilingualString | Name of Traveller |  |
| + | @lang | mandatory | 1..1 | xsd:string | Attribute lang | |




*→ - [General NeTEx definition](../site/netex-html/AlternativeName.html)*
 
#### Example


```xml
<?xml version="1.0" encoding="UTF-8"?>
<AlternativeName>
  <!-- In some cases we need translations or alias of the Name element. This is done with AlternativeName. -->
  <NameType>alias
  <!-- alias allowed for StopPlace. -->
  </NameType>
  <TypeOfName>offical
  <!-- For StopPlace official is used for the official name -->
  </TypeOfName>
  <Name lang="de">Die Übersetzung des Namens.</Name>
</AlternativeName>
```



*→ - [Template](./templates/AlternativeName.xml)*

#### Usage Notes

We only allow the following values for `NameType`: 
- `alias`


### AlternativeText
> `AlternativeText` is not used. We will use `MultilingualString`. This means that there are multiple `<Text>` elements with different `lang`-attributes. 

*→ [Glossary definition](A4_annex_glossary.md#alternativetext)*

### MultilingualString
*→ [Glossary definition](A4_annex_glossary.md#multilingualstring)*


#### Purpose

NeTEx uses the type `MultilingualString` for descriptive text elements (e.g. `Notice` text, `Name`, `ShortName` etc.).
However, only one language can be set for a given element (e.g. `<MultilingualString lang=”fr”>`). 
Additional languages are introduced through the [AlternativeName](#alternativename) and [AlternativeText](#alternativetext) element.

#### Example

```xml
<Text lang="de">Reservation erforderlich
  <Text lang="it">Prenotazione obbligatoria</Text>
  <Text lang="en">Reservation required</Text>
  <Text lang="fr">Réservation obligatoire</Text>
</Text>
```

#### Usage Notes

- For [Organisations](#organisation--operator--authority) e.g. there are all languages present.
- The `StopPlace` names in Switzerland are language-independent.
- Sometimes the parent element is `Text` as well. So we have `Text/Text`.


### FrameDefaults
*→ [Glossary definition](A4_annex_glossary.md#framedefaults)*

#### Purpose
Holds default values for certain basic parameters. 

#### Table



*Table: FrameDefaults*

| Sub | Element | Usage | Card | Type | Description | Note |
|-----|---------|-------|------|------|-------------|------|
|  | DefaultLocale | mandatory | 0..1 | LocaleStructure | Default LOCAL for frame elements. Assume this value for timezone and language of elements if not specified on individual elements. | The default locale is German (de) for Swiss public transport. |
| + | TimeZoneOffset | mandatory | 0..1 | TimeZoneOffsetType | Timezone offset from Greenwich at LOCALE. | We prefer times without the suf-fix "+hh:mm". Instead we specify a default TimeZoneOffset (+1) and SummerTimeZoneOffset (+2) |
| + | TimeZone | mandatory | 0..1 | xsd:normalizedString | Timezone name at LOCALE. |  |
| + | SummerTimeZoneOffset | mandatory | 0..1 | TimeZoneOffsetType | Summer timezone offset if different from Time zone offset. | We prefer times without the suf-fix "+hh:mm". Instead we specify a default TimeZoneOffset (+1) and SummerTimeZoneOffset (+2) |
| + | DefaultLanguage | mandatory | 0..1 | xsd:language | Default Language for LOCALE. Assume language use is "normally used" | Is always set to “de” for Swiss public transport. |
|  | DefaultLocationSystem | mandatory | 0..1 | xsd:normalizedString | Default spatial coordinate system (srsName). E.g. WGS84 Value to use for location elements using coordinates if not specified on individual elements. |  |




*→ [General NeTEx definition](../site/netex-html/FrameDefaults.html)*

#### Example



```xml
<?xml version="1.0" encoding="UTF-8"?>
<FrameDefaults>
  <DefaultLocale>
  <!-- The default locale is German (de) for Swiss public transport. -->
  <TimeZoneOffset>1
  <!-- We prefer times without the suf-fix "+hh:mm". Instead we specify a default TimeZoneOffset (+1) and SummerTimeZoneOffset (+2) -->
  </TimeZoneOffset>
  <TimeZone>Europe/Zurich</TimeZone>
  <SummerTimeZoneOffset>2
  <!-- We prefer times without the suf-fix "+hh:mm". Instead we specify a default TimeZoneOffset (+1) and SummerTimeZoneOffset (+2) -->
  </SummerTimeZoneOffset>
  <DefaultLanguage>de
  <!-- Is always set to “de” for Swiss public transport. -->
  </DefaultLanguage>
  </DefaultLocale>
  <DefaultLocationSystem>urn:ogc:def:crs:EPSG::4326</DefaultLocationSystem>
</FrameDefaults>
```



*→ [Template](./templates/FrameDefaults.xml)*

#### Usage Notes
- For values not set in `FrameDefaults` we use the values as indicated in the table and example above.
- We know that the use of the TimezoneOffset are redundant to the TimeZone, but we believe it may make consumption easier and the additional two lines are not really expensive.


