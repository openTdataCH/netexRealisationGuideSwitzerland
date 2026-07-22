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



CheckConstraints are used for different use cases

*Table: CheckConstraint*

| Sub | Element | Usage | Card | Type | Description | Note |
|-----|---------|-------|------|------|-------------|------|
|  | CheckDirection | optional | 0..1 | CheckDirectionEnumeration | For CHECK CONSTRAINTs associated with PATH LINKs, the direction in which the check applies. Forwards = from/to, backwards = to/from. For Check constraints associated with an external ENTRANCE, forwards is into the SITE, backwards is out of the SITE. | We usually only use one direction. |
|  | CheckProcess | optional | 0..1 | CheckProcessTypeEnumeration | Type of process that may occur at CHECK CONSTRAINT. | Only a given subset is allowed |
|  | Congestion | optional | 0..1 | CongestionEnumeration | Type of crowding that may slow use of CHECK CONSTRAINT. |  |
|  | delays | expected | 0..1 | delays | Delays for CHECK CONSTRAINT .process. |  |
| + | CheckConstraintDelay | expected | 1..1 | CheckConstraintDelay | Time penalty associated with a CHECK CONSTRAINT. | We currently only model delays |
| ++ | AverageDelay | expected | 0..1 | xsd:duration | Average duration expected to pass through Check. |  |
| ++ | MaximumLikelyDelay | optional | 0..1 | xsd:duration | Maximum duration expected to pass through CHECK CONSTRAINT. |  |




*-> [General NeTEx definition](../generated/netex-html/CheckConstraint.html)*

### Example



```xml
<?xml version="1.0" encoding="UTF-8"?>
<CheckConstraint  id="" version="1">
  <!-- CheckConstraints are used for different use cases -->
  <CheckDirection>forwards</CheckDirection>
  <!-- We usually only use one direction. -->
  <CheckProcess>alighting</CheckProcess>
  <!-- Only a given subset is allowed -->
  <Congestion>queue</Congestion>
  <delays>
    <CheckConstraintDelay id="generated" version="1">
      <!-- We currently only model delays -->
      <AverageDelay>PT4M</AverageDelay>
      <MaximumLikelyDelay>PT8M</MaximumLikelyDelay>
    </CheckConstraintDelay>
  </delays>
</CheckConstraint>

```



*->[Template](./templates/CheckConstraint.xml)*

### Usage Notes
- We prefer the `CheckConstraint` on the `ServiceJourneyPattern`.
- A main usage is the waiting time at carTransportRail.
- It is important to mention if a CheckConstraint applies to alighting or boarding.
- `CheckConstraint` can also cover congestion, which we don't do for the moment.
- The CI / CO times from HRDF can be conveyed as a `CheckConstraint` each.
- `CheckConstraint` can also be associated with equipment, we don't do this either.
- id-attribute can be generated.