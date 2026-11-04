# AssistanceService

Presence of`AssistanceFacility`s and their availability , e.g., if they need to be booked.

*Table: AssistanceService*

| Sub | Element | Usage | Card | Type | Description | Note |
|-----|---------|-------|------|------|-------------|------|
|  | Note | expected | 0..1 | MultilingualString |  |  |
|  | AssistanceFacilityList | expected | 0..1 | AssistanceFacilityListOfEnumerations |  | Accessibility. Facilities for which the availability is described below. Allowed values: `boardingAssistance personalAssistance wheelchairAssistance unaccompanied­MinorAssistance conductor information`. |
|  | AssistanceAvailability | expected | 0..1 | AssistanceAvailabilityEnumeration | Availability of assistance service. | Accessibility. Allowed values: `available availableIfBooked availableAtCertainTimes availableDependentOnJourney unknown`. |
