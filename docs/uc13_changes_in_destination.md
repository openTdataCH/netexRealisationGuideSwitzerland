# Handling of changes in the destination

The destination to display may change during a trip:
- in some cases multiple `ServiceJourney` are chained together. And the final stop should be shown, some intermediate stop should be shown on some part and then the final one.
- Also, during one `ServiceJourney` the destination could change.
- Also, in some cases the service journey is shortened. This results in a new destination to be shown for all or part of the service journey.

We will adhere to the following rules:
- if the ServiceJourney has a `DestinationDisplayRef` it is the general destination to use unless
- if the `ServiceJourneyPattern` has for a `PointInJourneyPattern` a `DestinationDisplayRef` this is shown. 
 
We could have a sort of progression rule, e.g. when at the third stop the destination display changes, keep it to the end. We want however, that from then on the `DestinationDisplayRef` is set. Otherwise it reverses to the one on the `ServiceJourneyPattern`

Conclusion:
* The `DestinationDisplay` are stored in `ServiceFrame`.
* The references for the whole `ServiceJourney` are stored in `ServiceJourney/Destination/DestinationDisplayRef`.
* If the destination changes on a given stop, it is mentionend in `ServiceJourneyPattern/pointsInJourneyPattern/StopPointInJourneyPattern/DestinationDisplayRef`.

All this is shown in one of the [examples](../examples/NeTEx_CH_BLS_Bern_Luzern_DestinationChange.xml).

