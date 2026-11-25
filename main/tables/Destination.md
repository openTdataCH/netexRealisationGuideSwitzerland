# Destination

We don't use the full Destination element, but only the DestinationDisplayRef within. The Destination can also be defined by having a DestinationDisplayRef on stops within ServiceJourneyPattern. If there is one on the first stop, then this element is basically obsolete. Because we use propagation of the destination on the StopPointInJourneyPattern.

*Table: Destination*

| Sub | Element | Usage | Card | Type | Description | Note |
|-----|---------|-------|------|------|-------------|------|
|  | DestinationDisplayRef | expected | 1..* | DestinationDisplayRefStructure | Reference to a DESTINATION DISPLAY. | We use a DestinationDiplayRef in such cases and nothing else. |
