# CheckConstraints

Check constraints are very broad elements within NeTEx. A lot of things can be expressed with it.
In Switzerland, we use the following use cases:
- Special delays in alighting or boarding.
- Doors closed already before departure (e.g. for TGV).
- Waiting times (e.g. for carTransportRail and touristic offers)

CheckConstraints can apply while boarding or alighting.

We can have `CheckConstraint`s on [`ServiceJourney`](09_timetable.md#servicejourney) and [`ServiceJourneyPattern`](07_service.md#servicejourneypattern).

We don't reference `CheckConstriants` but they are always instantiated in the `ServiceJourney` or `ServiceJourneyPattern`.



## CheckConstraint
*→ [Glossary definition](A4_annex_glossary.md#checkconstraint)*

### Purpose
`CheckConstraint`s can be used for a lot of different obstacles and delays in alighting/boarding or within sites.

### Table
- [Swiss profile NeTEx definition](../site/tables/CheckConstraint.md)

*-> [General NeTEx definition](../xcore/netex/elements/CheckConstraint.html)*

### Example

- [Example snippet](../site/xml-snippets/CheckConstraint.xml)

*->[Template](./templates/CheckConstraint.xml)*

### Usage Notes
- We prefer the `CheckConstraint` on the `ServiceJourneyPattern`.
- A main usage is the waiting time at carTransportRail.
- It is important to mention if a CheckConstraint applies to alighting or boarding.
- `CheckConstraint` can also cover congestion, which we don't do for the moment.
- The CI / CO times from HRDF can be conveyed as a `CheckConstraint` each.
- `CheckConstraint` can also be associated with equipment, we don't do this either.
- id-attribute can be generated.