# ServiceJourneyPattern

*Table: ServiceJourneyPattern*

| Sub | Element | Usage | Card | Type | Description | Note |
|-----|---------|-------|------|------|-------------|------|
|  | @id | mandatory | 1..1 | xsd:string | Attribute id | |
|  | @version | mandatory | 1..1 | xsd:string | Attribute version | |
|  | Name | optional | 0..1 | MultilingualString | A coherent set of Service data to which the same frame VALIDITY CONDITIONs have been assigned. |  |
|  | RouteView | mandatory | 1..1 | unknown | A coherent set of Service data to which the same frame VALIDITY CONDITIONs have been assigned. |  |
| + | LineRef | mandatory | 1..1 | LineRefStructure | A coherent set of Service data to which the same frame VALIDITY CONDITIONs have been assigned. |  |
|  | DirectionType | mandatory | 0..1 | RelativeDirectionEnumeration | A coherent set of Service data to which the same frame VALIDITY CONDITIONs have been assigned. |  |
|  | pointsInSequence | mandatory | 0..1 | vehicleMeetingPointsInSequence_RelStructure | A coherent set of Service data to which the same frame VALIDITY CONDITIONs have been assigned. |  |
| + | StopPointInJourneyPattern | mandatory | 0..* | unknown | A coherent set of Service data to which the same frame VALIDITY CONDITIONs have been assigned. |  |
| ++ | ScheduledStopPointRef | mandatory | 0..1 | ScheduledStopPointRefStructure | A coherent set of Service data to which the same frame VALIDITY CONDITIONs have been assigned. |  |
| ++ | ForAlighting | mandatory | 0..1 | xsd:boolean | A coherent set of Service data to which the same frame VALIDITY CONDITIONs have been assigned. |  |
| ++ | ForBoarding | mandatory | 0..1 | xsd:boolean | A coherent set of Service data to which the same frame VALIDITY CONDITIONs have been assigned. |  |
| ++ | DestinationDisplayRef | optional | 1..1 | DestinationDisplayRefStructure | A coherent set of Service data to which the same frame VALIDITY CONDITIONs have been assigned. | Indicates that the destination has changed. Superseeds Line or ServiceJourney |
| ++ | RequestStop | optional | 0..1 | xsd:boolean | A coherent set of Service data to which the same frame VALIDITY CONDITIONs have been assigned. |  |
| ++ | StopUse | optional | 0..1 | StopUseEnumeration | A coherent set of Service data to which the same frame VALIDITY CONDITIONs have been assigned. | All values possible. passthrough is used for Durchfahrt, if such data is delivered. |
| ++ | checkConstraints | optional | 0..1 | checkConstraints_RelStructure | A coherent set of Service data to which the same frame VALIDITY CONDITIONs have been assigned. |  |
| +++ | [CheckConstraint](CheckConstraint.md) | optional | 0..* | unknown | A coherent set of Service data to which the same frame VALIDITY CONDITIONs have been assigned. |  |
| ++ | bookingArrangements | optional | 0..1 | bookingArrangements_RelStructure | A coherent set of Service data to which the same frame VALIDITY CONDITIONs have been assigned. |  |
| +++ | BookingArrangementRef | optional | 0..* | BookingArrangementRefStructure | A coherent set of Service data to which the same frame VALIDITY CONDITIONs have been assigned. | Specially we use bookingArrangementRef here to model the information that a stop is flexible. From the HRDF conversion only a BookingNote can be passed at the moment. With native NeTEx handling we can transfer more information. |
| +++ | BookingArrangement | we expect a BookingArrangementRef. We use this here to show how native NeTEx handling could improve transfering information here | 0..* | unknown | A coherent set of Service data to which the same frame VALIDITY CONDITIONs have been assigned. |  |
| ++++ | BookingMethods | we expect a BookingArrangementRef. We use this here to show how native NeTEx handling could improve transfering information here | 0..1 | BookingMethodListOfEnumerations | A coherent set of Service data to which the same frame VALIDITY CONDITIONs have been assigned. |  |
|  | ServiceJourneyPatternType | expected | 0..1 | ServiceJourneyPatternTypeEnumeration | A coherent set of Service data to which the same frame VALIDITY CONDITIONs have been assigned. |  |
