# ServiceJourneyPattern

*Table: ServiceJourneyPattern*

| Sub | Element | Usage | Card | Type | Description | Note |
|-----|---------|-------|------|------|-------------|------|
|  | @id | mandatory | 1..1 | xsd:string | Attribute id | |
|  | @version | mandatory | 1..1 | xsd:string | Attribute version | |
|  | Name | optional | 0..1 | MultilingualString | Name of VALIDITY CONDITION. |  |
|  | RouteView | mandatory | 1..1 | Route_DerivedViewStructure | Annotated reference to a ROUTE. |  |
| + | LineRef | mandatory | 1..* | LineRefStructure | Reference to a LINE. |  |
|  | DirectionType | mandatory | 0..1 | RelativeDirectionEnumeration | A Direction of a ROUTE. One of a restricted set of values. Default is "Outbound" |  |
|  | pointsInSequence | mandatory | 0..1 | vehicleMeetingPointsInSequence_RelStructure | Ordered List of points used in TIMING PATTERN. specific to TIMING PATTERN. |  |
| + | StopPointInJourneyPattern | mandatory | 0..* | unknown |  |  |
| ++ | ScheduledStopPointRef | mandatory | 0..1 | ScheduledStopPointRefStructure | Reference to a SCHEDULED STOP POINT. |  |
| ++ | ForAlighting | mandatory | 0..1 | xsd:boolean | Default for whether SCHEDULED STOP POINT may be used for alighting. May be overridden on specific services. |  |
| ++ | ForBoarding | mandatory | 0..1 | xsd:boolean | Default for whether SCHEDULED STOP POINT may be used for boarding. May be overridden on specific services. |  |
| ++ | DestinationDisplayRef | optional | 1..* | DestinationDisplayRefStructure | Reference to a DESTINATION DISPLAY. | Indicates that the destination has changed. Superseeds Line or ServiceJourney |
| ++ | RequestStop | optional | 0..1 | xsd:boolean | Whether stop is by default a request stop in the timetable. May be overridden in specific SERVICE PATTERNs. |  |
| ++ | StopUse | optional | 0..1 | StopUseEnumeration | Nature of use of stop, e.g. access, interchange only, or pass through. Default is Access. | All values possible. passthrough is used for Durchfahrt, if such data is delivered. See mapping excel. |
| ++ | checkConstraints | optional | 0..1 | checkConstraints_RelStructure | CHECK CONSTRAINTs in frame. |  |
| +++ | [CheckConstraint](CheckConstraint.md) | optional | 1..* | CheckConstraint_VersionStructure | Characteristics of a SITE COMPONENT representing a process, such as check-in, security screening, ticket control or immigration, that may potentially incur a time penalty that should be allowed for when journey planning. Used to mark PATH LINKs to determine transit routes through interchanges. |  |
| ++ | bookingArrangements | optional | 0..1 | bookingArrangements_RelStructure | BOOKING ARRANGEMENTs in frame +v2.0. |  |
| +++ | BookingArrangementRef | optional | 0..* | BookingArrangementRefStructure | Reference to a BOOKING ARRANGEMENT. | Specially we use bookingArrangementRef here to model the information that a stop is flexible. From the HRDF conversion only a BookingNote can be passed at the moment. With native NeTEx handling we can transfer more information. |
| +++ | BookingArrangement | we expect a BookingArrangementRef. We use this here to show how native NeTEx handling could improve transfering information here | 1..* | BookingArrangement_VersionStructure | Details of the booking arrangements for a given LINE, STOP, SERVICE etc. |  |
| ++++ | BookingMethods | we expect a BookingArrangementRef. We use this here to show how native NeTEx handling could improve transfering information here | 0..1 | BookingMethodListOfEnumerations | Allowed Ways of Making a BOOKING. |  |
|  | ServiceJourneyPatternType | expected | 0..1 | ServiceJourneyPatternTypeEnumeration | Type of SERVICE JOURNEY PATTERN. | We currently only allow passenger |
