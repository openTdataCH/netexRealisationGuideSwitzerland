# The following changes from the NeTEx schema can occur in the profile.
Several points can be combined.

We will then check, how we can use those to validate.
We can also use this for a more formal description and perhaps generate part of the documentation as well.

## Add description
We want to add some more details to the xsd:documentation.

This is not really relevant for  the validation. It helps understanding.

## Change cardinality
Usually optional ->  mandatory.

E.g. `OperatorRef is now mandatory.

Needed parameters:
- XPath
- mandatory or new `minOccurs`, `maxOccurs`

## Restricted choice
In some cases only a subset of choices is allowed.

e.g. `passingtimes` or `calls`

Needed parameters:
- xpath
- list of allowed choices

## Disallow element / attribute
e.g. attribute `ShortName`not allowed for `Operator`.

Needed parameters:
- xpath

## Mark an element / attribute as to be ignored during importation.
We won't do this currently.

Needed parameters:
- xpath

## Restrict an enumeration in a given element
Only a subset of values is allowed. 

e.g. `railSubmode` `metro`not allowed

Note: This may only happen in certain places.

Needed parameters:
- xpath
- list of allowed values

## Restrict strings, integers etc
We won't do this currently.

e.g. only values between-5 and 5.

## Restrict the allowed types in a container

e.g. no `QuayRef` in quays only `Quay`

Needed parameters:
- xpath
- allowed values

## Extension in extension point
This may also be a full substructure

We will check for mandatory elements, if necessary

## Restrict to a subset of substitionGroup
Check, if we need th
Needed parameters:
- xpath
is. The French profile used it.
