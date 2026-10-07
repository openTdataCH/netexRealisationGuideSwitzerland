# AssistanceBookingService

Accessibility. Contact and booking information regarding assistance services.

*Table: AssistanceBookingService*

| Sub | Element | Usage | Card | Type | Description | Note |
|-----|---------|-------|------|------|-------------|------|
|  | WheelchairBookingRequired | optional | 0..1 | xsd:boolean | Whether a booking is needed to use a wheelchair. |  |
|  | BookingContact | expected | 0..1 | ContactStructure | Contact for Booking. +v1.1 |  |
|  | VehicleMode | optional | 0..1 | AllPublicTransportModesEnumeration | PUBLIC TRANSPORT MODE: a characterisation of the operation according to the means of transport (bus, tram, metro, train, ferry, ship). |  |
|  | noticeAssignments | optional | 0..1 | noticeAssignments_RelStructure | NOTICE ASSIGNMENTs in frame. |  |
| + | [NoticeAssignment](NoticeAssignment.md) | expected | 0..* | NoticeAssignment_VersionStructure | The assignment of a NOTICE showing an exception in a JOURNEY PATTERN, a COMMON SECTION, or a VEHICLE JOURNEY, possibly specifying at which POINT IN JOURNEY PATTERN the validity of the NOTICE starts and ends respectively. |  |
