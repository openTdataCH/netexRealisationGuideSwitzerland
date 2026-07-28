# ServiceJourneyPattern

*Table: ServiceJourneyPattern*

| Sub | Element | Usage | Card | Type | Description | Note |
|-----|---------|-------|------|------|-------------|------|
|  | @id | mandatory | 1..1 | xsd:string | Attribute id | |
|  | @version | mandatory | 1..1 | xsd:string | Attribute version | |
|  | Name | optional | 0..1 | MultilingualString |  |  |
|  | RouteView | mandatory | 1..1 | unknown |  |  |
| + | LineRef | mandatory | 1..1 | LineRefStructure |  |  |
|  | DirectionType | mandatory | 0..1 | RelativeDirectionEnumeration |  |  |
|  | pointsInSequence | mandatory | 0..1 | vehicleMeetingPointsInSequence_RelStructure |  |  |
| + | StopPointInJourneyPattern | mandatory | 0..* | unknown |  |  |
| ++ | ScheduledStopPointRef | mandatory | 0..1 | ScheduledStopPointRefStructure |  |  |
| ++ | ForAlighting | mandatory | 0..1 | xsd:boolean |  |  |
| ++ | ForBoarding | mandatory | 0..1 | xsd:boolean |  |  |
| ++ | DestinationDisplayRef | optional | 1..1 | DestinationDisplayRefStructure |  | Indicates that the destination has changed. Superseeds Line or ServiceJourney |
| ++ | RequestStop | optional | 0..1 | xsd:boolean |  |  |
| ++ | StopUse | optional | 0..1 | StopUseEnumeration |  | All values possible. passthrough is used for Durchfahrt, if such data is delivered. |
| ++ | checkConstraints | optional | 0..1 | checkConstraints_RelStructure |  |  |
| +++ | [CheckConstraint](CheckConstraint.md) | optional | 0..* | unknown | Process associated with a Place, typically giving rise to a delay to the traveller. |  |
| ++ | bookingArrangements | optional | 0..1 | bookingArrangements_RelStructure |  |  |
| +++ | BookingArrangementRef | optional | 0..* | BookingArrangementRefStructure |  | Specially we use bookingArrangementRef here to model the information that a stop is flexible. From the HRDF conversion only a BookingNote can be passed at the moment. With native NeTEx handling we can transfer more information. |
| +++ | BookingArrangement | we expect a BookingArrangementRef. We use this here to show how native NeTEx handling could improve transfering information here | 0..* | unknown |  |  |
| ++++ | BookingMethods | we expect a BookingArrangementRef. We use this here to show how native NeTEx handling could improve transfering information here | 0..1 | BookingMethodListOfEnumerations |  |  |
|  | ServiceJourneyPatternType | expected | 0..1 | ServiceJourneyPatternTypeEnumeration |  |  |
