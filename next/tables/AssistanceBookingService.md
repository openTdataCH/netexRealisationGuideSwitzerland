# AssistanceBookingService

Accessibility. Contact and booking information regarding assistance services.

*Table: AssistanceBookingService*

| Sub | Element | Usage | Card | Type | Description | Note |
|-----|---------|-------|------|------|-------------|------|
|  | WheelchairBookingRequired | optional | 0..1 | boolean | Whether a booking is needed to use a wheelchair. |  |
|  | BookingArrangements | expected | 0..1 | BookingArrangementsStructure | Booking conditions for ASSISTANCE BOOKING SERVICE. DEPRECATED: use bookingArrangements |  |
| + | BookingContact | expected | 0..1 | ContactStructure | Contact for Booking. +v1.1 |  |
| ++ | Email | optional | 0..1 | EmailAddressType | The email address of the contact. |  |
| ++ | Phone | expected | 0..1 | PhoneType | Contact telephone number. |  |
| ++ | Url | optional | 0..1 | anyURI | The web site address of the contact. |  |
| + | LatestBookingTime | expected | 0..1 | time | Latest time in day that booking can be made. |  |
| + | MinimumBookingPeriod | expected | 0..1 | duration | Minimum interval in advance of departure day or time that Service may be ordered. |  |
| + | BookingUrl | optional | 0..1 | InfoLinkStructure | URL for booking. +V1.1 |  |
| + | BookingNote | expected | 0..1 | MultilingualString | Note about booking the FLEXIBLE LINE. |  |
| ++ | Text | expected | 0..1 | MultilingualString |  | Translations |
| +++ | @lang | mandatory | 1..1 | xsd:string | Attribute lang | |
|  | VehicleMode | optional | 0..1 | AllPublicTransportModesEnumeration |  |  |
|  | noticeAssignments | optional | 0..1 | noticeAssignments_RelStructure | NOTICEs for ASSISTANCE BOOKING SERVICE. |  |
| + | [NoticeAssignment](NoticeAssignment.md) | optional | 0..* | NoticeAssignment_VersionStructure | The assignment of a NOTICE showing an exception in a JOURNEY PATTERN, a COMMON SECTION, or a VEHICLE JOURNEY, possibly specifying at which POINT IN JOURNEY PATTERN the validity of the NOTICE starts and ends respectively. | May be used to inform about exceptions. |
