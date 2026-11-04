# AssistanceBookingService

Accessibility. Contact and booking information regarding assistance services.

*Table: AssistanceBookingService*

| Sub | Element | Usage | Card | Type | Description | Note |
|-----|---------|-------|------|------|-------------|------|
|  | WheelchairBookingRequired | optional | 0..1 | boolean | Whether a booking is needed to use a wheelchair. |  |
|  | BookingContact | expected | 0..1 | ContactStructure | Contact details for ASSISTANCE BOOKING SERVICE. |  |
|  | VehicleMode | optional | 0..1 | AllPublicTransportModesEnumeration |  |  |
|  | noticeAssignments | optional | 0..1 | noticeAssignments_RelStructure | NOTICEs for ASSISTANCE BOOKING SERVICE. |  |
| + | [NoticeAssignment](NoticeAssignment.md) | expected | 0..* | NoticeAssignment_VersionStructure | The assignment of a NOTICE showing an exception in a JOURNEY PATTERN, a COMMON SECTION, or a VEHICLE JOURNEY, possibly specifying at which POINT IN JOURNEY PATTERN the validity of the NOTICE starts and ends respectively. |  |
