# SiteFacilitySet_withAccessibility

*Table: SiteFacilitySet*

| Sub | Element | Usage | Card | Type | Description | Note |
|-----|---------|-------|------|------|-------------|------|
|  | AssistanceFacilityList | expected | 0..1 | AssistanceFacilityListOfEnumerations | List of ASSISTANCE FACILITies. | Accessibility. Presence or absence of the following facilities should be signalled: `boardingAssistance personalAssistance wheelchairAssistance unaccompanied­MinorAssistance conductor information`. |
|  | AccessibilityToolList | optional | 0..1 | AccessibilityToolListOfEnumerations | List of TYPEs of ACCESSIBILITY TOOLs. | Accessibility. Presence or absence of the following facility may be signalled; absence of the item means absence of the facility (if the element is present): `wheelchair` - wheelchairs available for passenger use. |
|  | SanitaryFacilityList | expected | 0..1 | SanitaryFacilityListOfEnumerations | List of SANITARY FACILITies. | Accessibility. Presence or absence of the following facilities should be signalled: `wheelchairAccessToilet wheelchairBabyChange toilet babyChange shower`. |
|  | TicketingServiceFacilityList | optional | 0..1 | TicketingServiceFacilityListOfEnumerations | List of TICKETING SERVICE FACILITies, e.g. purchase, collection. top up. |  |
|  | EmergencyServiceList | expected | 0..1 | EmergencyServiceListOfEnumerations | List of EMERGENCY SERVICE FACILITies. | Accessibility. Presence or absence of the following facilities should be signalled: `sosPoint firstAid`. Optional: `police fire`. |
|  | ParkingFacilityList | expected | 0..1 | ParkingFacilityListOfEnumerations | List of PARKING FACILITies. | Accessibility. Presence or absence of the following facilities should be signalled: `carPark parkAndRidePark motorcyclePark cyclePark`. Others are optional: `cachPark rentalCarPark`. |
