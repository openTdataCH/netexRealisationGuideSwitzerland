# ServiceJourneyPattern

*Table: ServiceJourneyPattern*

| Sub | Element | Usage | Card | Type | Description | Note |
|-----|---------|-------|------|------|-------------|------|
|  | @id | mandatory | 1..1 | xsd:string | Attribute id | |
|  | @version | mandatory | 1..1 | xsd:string | Attribute version | |
|  | Name | optional | 0..1 | MultilingualString | Name of SERVIC CALENDAR. |  |
|  | RouteView | mandatory | 1..1 | unknown |  |  |
| + | LineRef | mandatory | 0..1 | LineRefStructure |  |  |
|  | DirectionType | mandatory | 0..1 | RelativeDirectionEnumeration | DIRECTION of JOURNEY PATTERN. Should be same as for ROUTE on which PATTERN is based. |  |
|  | pointsInSequence | mandatory | 0..1 | pointsInJourneyPattern_RelStructure | Sequence of points in JOURNEY PATTERN Points may be SCHEDULED STOP POINTs or TIMING POINTs. |  |
| + | StopPointInJourneyPattern | mandatory | 0..* | unknown |  |  |
| ++ | ScheduledStopPointRef | mandatory | 0..1 | ScheduledStopPointRefStructure | Reference to a SCHEDULED STOP POINT. |  |
| ++ | ForAlighting | mandatory | 0..1 | boolean | Whether alighting is allowed at the stop. Default is true. |  |
| ++ | ForBoarding | mandatory | 0..1 | boolean | Whether boarding is allowed at the stop. Default is true. |  |
| ++ | DestinationDisplayRef | optional | 1..1 | DestinationDisplayRefStructure |  | Indicates that the destination has changed. Superseeds Line or ServiceJourney |
| ++ | RequestStop | optional | 0..1 | boolean | Whether stop is a request stop for this journey. Default is false. |  |
| ++ | StopUse | optional | 0..1 | StopUseEnumeration | Nature of use of stop, e.g. access, interchange only, or pass through. Default is Access. | All values possible. passthrough is used for Durchfahrt, if such data is delivered. See mapping excel. |
| ++ | checkConstraints | optional | 0..1 | checkConstraints_RelStructure | Implements the navigation from processes or barriers that the travellers will be facing (e.g., security check, check-in, etc.). +v2.1 |  |
| +++ | [CheckConstraint](CheckConstraint.md) | optional | 0..* | CheckConstraint_VersionStructure | Process associated with a Place, typically giving rise to a delay to the traveller. |  |
| ++ | bookingArrangements | optional | 0..1 | bookingArrangements_RelStructure | Set of possible Booking Arrangements for stop if different from those for SERVICE JOURNEY. +v2.0 |  |
| +++ | BookingArrangementRef | optional | 0..* | BookingArrangementRefStructure |  | Specially we use bookingArrangementRef here to model the information that a stop is flexible. From the HRDF conversion only a BookingNote can be passed at the moment. With native NeTEx handling we can transfer more information. |
| +++ | BookingArrangement | we expect a BookingArrangementRef. We use this here to show how native NeTEx handling could improve transfering information here | 0..* | BookingArrangement_VersionStructure | Details of the booking arrangements for a given LINE, STOP, SERVICE etc. |  |
| ++++ | BookingMethods | we expect a BookingArrangementRef. We use this here to show how native NeTEx handling could improve transfering information here | 0..1 | BookingMethodListOfEnumerations | Allowed Ways of Making a BOOKING. |  |
|  | ServiceJourneyPatternType | expected | 0..1 | ServiceJourneyPatternTypeEnumeration | Type of SERVICE JOURNEY PATTERN. | We currently only allow passenger |
