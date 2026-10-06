# AssistanceService

The element allows for more precisely describing the availability of `AssistanceFacility`s and `AccessibilityTools`, e.g., if they need to be booked. It does not add new facilities to the ones already given by the `SiteFacilitySet`.

*Table: AssistanceService*

| Sub | Element | Usage | Card | Type | Description | Note |
|-----|---------|-------|------|------|-------------|------|
|  | AssistanceFacilityList | expected | 0..1 | AssistanceFacilityListOfEnumerations | List of ASSISTANCE FACILITies. | Accessibility. Facilities for which the availability is described below. Allowed values: `boardingAssistance personalAssistance wheelchairAssistance unaccompanied­MinorAssistance conductor information`. |
|  | AssistanceAvailability | expected | 0..1 | AssistanceAvailabilityEnumeration | Availability of assistance service. | Accessibility. Facilities for which the availability is described below. Allowed values: `available availableIfBooked availableAtCertainTimes availableDependentOnJourney unknown`. |
|  | AccessibilityToolList | optional | 0..1 | AccessibilityToolListOfEnumerations | List of TYPEs of ACCESSIBILITY TOOLs. | Accessibility. If the availabilty of wheelchairs for passenger use is restricted: `wheelchair`. |
