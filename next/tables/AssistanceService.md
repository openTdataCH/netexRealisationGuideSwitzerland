# AssistanceService

Presence of`AssistanceFacility`s and their availability , e.g., if they need to be booked.

*Table: AssistanceService*

| Sub | Element | Usage | Card | Type | Description | Note |
|-----|---------|-------|------|------|-------------|------|
|  | Note | expected | 0..1 | MultilingualString |  |  |
|  | AssistanceFacilityList | expected | 0..1 | AssistanceFacilityListOfEnumerations |  | Will be exported from ATLAS for ERA TSI PRM (Autonome Benutzbarkeit - "Hilfestellung durch Personal" sets `boardingAssistance personalAssistance wheelchairAssistance`). Mirrored in SiteFacilitySet - AssistanceFacilityList. Availability of the facilities may be described below. |
|  | AssistanceAvailability | expected | 0..1 | AssistanceAvailabilityEnumeration | Availability of assistance service. | Will be exported from ATLAS for ERA TSI PRM (may be a standard availability or derived Autonome Benutzbarkeit - "Hinweise zur Hilfestellung". Allowed values: `available availableIfBooked availableAtCertainTimes availableDependentOnJourney unknown`. |
