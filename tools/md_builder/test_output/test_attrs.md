# test_attrs

| Sub | Element | Usage | Card | Type | Description | Note |
|-----|---------|-------|------|------|-------------|------|
|  | TestElement | ignored | 1..1 | unknown |  |  |
| > | DeprecatedElement | forbidden | 1..1 | unknown | This element is no longer used NOTE: DEPRECATED | This element is no longer used NOTE: DEPRECATED |
| > | ElementWithAttrs | mandatory | 1..1 | unknown | Element that has required attributes | Element that has required attributes |
| > | @id | mandatory | 1..1 | xsd:string | Attribute id | |
| > | @version | mandatory | 1..1 | xsd:string | Attribute version | |
| > | @name | mandatory | 1..1 | xsd:string | Attribute name | |
| >> | ChildElement | optional | 1..1 | unknown |  |  |
