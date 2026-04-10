# Schematron based Profile Schema Generator 

Idea: generate a profile schema from mapping rules (schema changes) described in a Schematron document.

## schema-generator.py

A Python script is used to generate a profile schema from a Schematron document.

### How to use schema-generator.py

```
python schema-generator.py --base ../StopPlace.xsd --sch StopPlaceSchematron.xml --out StopPlaceGenerated.xsd
```

## How could we express schema changes in Schematron?

See also: [Changes_in_profile.md](../../mgmt/Changes_in_profile.md).

| Schema Change                               | Schematron Test Assertion      | Comment                                                                                            |
|---------------------------------------------|--------------------------------|----------------------------------------------------------------------------------------------------|
| Add Profile Note (xsd:description element)  | `count(xpath-to-element) <= 1` | Same as extension. Define description in text content of `sch:assert` element.                     |
| Change Cardinality: Exactly one             | `count(xpath-to-element) = 1`  | 
| Change Cardinality: At least one            | `count(xpath-to-element) >= 1` |
| Change Cardinality: At most N               | `count(xpath-to-element) <= N` |
| Restricted Choice                           |                                | ?                                                                                                  |
| Disallow Element                            | `not(xpath-to-element)`        |
| Disallow Attribute                          | `not(xpath-to-attribute)`      |
| Mark Element as to be ignored during Import |                                | ? KI: Use `sch:report` with test="xpath-to-element" so presence is reported/annotated, not failed. | 
| Restrict enumeration                        |                                |                                                                                            
| Restrict strings, integers etc.             |                                |
| Extension in extension point                | `count(xpath-to-element) <= 1` |
| Restrict to a subset of substitutionGroup   |                                |

