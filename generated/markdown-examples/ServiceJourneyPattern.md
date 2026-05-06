# ServiceJourneyPattern

| Sub | Element | Usage | Card | Type | Description | Note |
|-----|---------|-------|------|------|-------------|------|
|  | ServiceJourneyPattern | mandatory | 1..1 | unknown | The JOURNEY PATTERN for a (passenger carrying) SERVICE JOURNEY. |  |
| + | Name | optional | 0..1 | MultilingualString | Name of Traveller |  |
| + | RouteView | mandatory | 1..1 | unknown | Annotated reference to a ROUTE. |  |
| ++ | LineRef | mandatory | 1..1 | LineRefStructure | Reference to a LINE. |  |
| + | DirectionType | mandatory | 0..1 | RelativeDirectionEnumeration | For fares for DISTANCE MATRIXE LEMENTs, DIRECTION in which price applies. |  |
| + | pointsInSequence | mandatory | 0..1 | vehicleMeetingPointsInSequence_RelStructure |  |  |
| ++ | StopPointInJourneyPattern | mandatory | 1..1 | unknown | The use of a SCHEDULED STOP POINT in a specified order. within a JOURNEY PATTERN or SERVICE PATTERN. |  |
| +++ | ScheduledStopPointRef | mandatory | 0..1 | ScheduledStopPointRefStructure | Specific SCHEDULED STOP POINT at end of CONNECTION. |  |
| +++ | ForAlighting | mandatory | 0..1 | xsd:boolean | Whether alighting is allowed at the stop Default is true. |  |
| +++ | ForBoarding | mandatory | 0..1 | xsd:boolean | Whether boarding is allowed at the stop. Default is true. |  |
| +++ | DestinationDisplayRef | optional | 1..1 | DestinationDisplayRefStructure | Reference to a DESTINATION DISPLAY. | Indicates that the destination has changed. Superseeds Line or ServiceJourney |
| +++ | RequestStop | optional | 0..1 | xsd:boolean | Whether stop is a request stop for this journey. Default is false. |  |
| +++ | StopUse | optional | 0..1 | StopUseEnumeration | Nature of use of stop, e.g. access, interchange only, or pass through. Default is Access. | All values possible |
| +++ | bookingArrangements | optional | 0..1 | bookingArrangements_RelStructure | Set of possible Booking Arrangements for Cancellations. +v2.0 |  |
| ++++ | BookingArrangementRef | optional | 1..1 | BookingArrangementRefStructure | Reference to a BOOKING ARRANGEMENT. | Specially we use bookingArrangementRef here to model the information that a stop is flexible. From the HRDF conversion only a BookingNote can be passed at the moment. With native NeTEx handling we can transfer more information. |
| ++++ | BookingArrangement | we expect a BookingArrangementRef. We use this here to show how native NeTEx handling could improve transfering information here | 1..1 | unknown | Details of the booking arrangements for a given LINE, STOP, SERVICE etc. |  |
| + | ServiceJourneyPatternType | expected | 0..1 | ServiceJourneyPatternTypeEnumeration | Type of SERVICE JOURNEY PATTERN. |  |
