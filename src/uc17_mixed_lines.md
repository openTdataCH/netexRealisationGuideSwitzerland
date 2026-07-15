---
mermaid: true
---

# Use Case: Mixed Lines

The migration document for the SLNID shows what different partial lines exist. There is an [example](examples/NeTEx_CH_Linie_722_Mischbetrieb.xml) that we have modeled also.

The main line types shown there are:
- "Ordentliche Linie"
- "Dispositionslinie"
- "Temporäre Linie"
Those are model as Line in NeTEx.
- "Betriebliche Linie" is not modeled.


All these lines can have partial lines.  

Possible motivations:
- joint operations by different transport operators (multiple owners or owner/subcontractor). Having multiple owners was not a good idea, as this was never modeled in the passenger information systems.
- operational / technical reasons.

Each partial line is modeled as a `Line`. The main line is also modeled as a `Line`. In addition a `GroupOfLines` is added as well. We suggest to use the slnid of the main line for the `id`-attribute.
The basic information is replicated (e.g. `PublicCode`, `TransportMode`).
The `Name` might be different to express something.
All `ServiceJourneyPattern` and `ServiceJourney`are only added to the partial lines.

## The problem with two concessionaries
NeTEx does not really assume this. Also, the way we build `responsibilitySet` does not cover it originally.
We also have only one `OperatorRef` in the main Line, and we want to have this in a mandatory fashion.

We could have said that the information in the main line can be overwritten from the partial lines. This works for the `EntityLegalOwner` in `responsibilitySet`, but not for the `OperatorRef`.
However, this is such a special case, that outside the Swiss ecosystem this is not understood, and also it is not manageable in GTFS and other formats. Atlas does not support it either.

So we do it as follows:
> NB: If partial lines have different `EntityLegalOwner` in the partial lines, then those are co-owners. This is NOT reflected in the main line, where only one can (and must be mentioned). The owners must agree on which one there is in Atlas and that's the one that gets written into the main line.

>**LATER**: We have to define how we obtain the information (currently through HRDF) to do this correctly.

## Delivery of partial lines
* It is currently NOT allowed to send anything but the full timetable year. A change here would need detailed discussions in AG Solldaten.
* Delivery of partial lines is allowed. Who is responsible for the delivery of which line or partial lines must be agreed upon with Fachbus INFO+ when the deliveries are set up.
* The concessionaries are responsible to make sure that all partial lines are delivered in a timely fashion and that no additional work is created for the Fachbus INFO+.


