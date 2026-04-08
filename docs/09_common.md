# Common elements

## id/versions and other attributes

* `version` is generelly always set to `"1"`
* We use `responsibilitySetRef` in the following elements xxx
* We use `nameOfClass` in the XXXRef elements.

All other defined attributes like `created`, `changed`, `modification` are not used. If we need one we will inform about it in the table associated with the element.

## MultilingualString
NeTEx uses the type “MultilingualString” for descriptive text elements (e.g. Notice text, Name, ShortName etc.).
However, only one language can be set for a given element (`<MultilingualString lang=”xx”>`). 
Additional languages are introduced through the `AlternativeName` and `AlternativeText` object described in tbd and tbd.

For the organisations e.g. there are all languages present.

The StopPlace names in Switzerland are langugage-independent. 

## IDs
It is important to note that internal or artificially generated IDs should not be used to extract content whenever business keys and attributes are available. For readability and easy refer-encing, we will use the following principles:
-	We will use attributes to build the technical IDs.
-	The class of the object is the beginning of the technical ID in general.
-	Where there is a compelling need for global stability, the ID will be a global ID. This in-formation will be also transmitted separately in a KeyList. 

ID must be globally unique during importation. 
IDs may also be partially or completely artificially generated. The persistence of ID between exports is then usually not guaranteed. Important business level keys are stored in ele-ments not in IDs (PublicKey, PrivateKey, KeyList). They must be communicated as attrib-ute in the elements.

tbd: Must be revisited and updated.

## Time formatting and journey after midnight
The time format consists only of the hour, minutes (and seconds) of a 24 hour clock, e.g. '23:55:00'. Times that pass midnight of the current OperatingDay are marked with a DayOffset element. If a ServiceJourney (in a particular Call) runs over midnight, then DayOffset must be set to '1'.

## FrameDefaults
With the FrameDefaults we set some basic parameters. When they are not set, we still assume the values that we present in the XML snippet.
- [Swiss profile tables](../generated/markdown-examples/FrameDefaults.md)
- [XML Snippet](../generated/xml-snippets/FrameDefaults.xml)
- [Original NeTEx table](tbd)

## AlternativeName
tbd 5.1

- [Swiss profile tables](generated/markdown-examples/AlternativeName.md)
- [XML Snippet](generated/xml-snippets/AlternativeName.xml)

## AlternativeText
tbd 5.2

- [Swiss profile tables](generated/markdown-examples/AlternativeText.md)
- [XML Snippet](generated/xml-snippets/AlternativeText.xml)

# ResourceFrame
The ResourceFrame is first in the standard data.

tbd 6

- [Swiss profile tables](generated/markdown-examples/ResourceFrame.md)
- [XML Snippet](generated/xml-snippets/ResourceFrame.xml)


## ResponsibilitySet
We use this model to  describe the different roles of the participating companies. For the most part, the company code is used to fully identify the services provided. For the PAG company (801), the attribute ResponsibleArea(Ref) must also be taken into account.


For some replacement services, the public transport sector has decided that the different roles of the companies should be represented when defining the services:
- the role of the company holding the concession for the original service
- the role of the company responsible for providing the transport service

These 2 roles are represented in the ResponsibilitySet element. 
- the role of the concession company is represented by the EntityLegalOwnership value of the StakeholderRoleType attribute
- the role of the company responsible for carrying out the transport is represented by the Op-eration value of the StakeholderRoleType attribute.

- [Swiss profile tables](generated/markdown-examples/ResponsibilitySet.md)
- [XML Snippet](generated/xml-snippets/ResponsibilitySet.xml)
tbd 6.5

## TypeOfValue
6.2

### TypeOfNotice
6.2

### TypeOfProductCategory
6.2

### TypeOfService
tbd

## Organisation / Operator / Authority

tbd 6.3., 6.4
- [Swiss profile tables](generated/markdown-examples/Operator.md)
- [XML Snippet](generated/xml-snippets/Operator.xml)
