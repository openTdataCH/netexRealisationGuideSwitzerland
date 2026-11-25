# FlexibleStopAssignment

Links the ScheduledStopPoint of a service area to its FlexibleStopPlace and FlexibleArea in SITE_OFFER. Same role as PassengerStopAssignment for regular stops. See uc16_drt.

*Table: FlexibleStopAssignment*

| Sub | Element | Usage | Card | Type | Description | Note |
|-----|---------|-------|------|------|-------------|------|
|  | @id | mandatory | 1..1 | xsd:string | Attribute id | |
|  | @version | mandatory | 1..1 | xsd:string | Attribute version | |
|  | ScheduledStopPointRef | mandatory | 0..1 | ScheduledStopPointRefStructure |  | ScheduledStopPoint that stands for the whole area in the ServiceJourneyPattern. |
|  | FlexibleStopPlaceRef | mandatory | 1..1 | FlexibleStopPlaceRefStructure |  |  |
|  | FlexibleAreaRef | expected | 1..1 | FlexibleAreaRefStructure |  | FlexibleArea of the FlexibleStopPlace. |
