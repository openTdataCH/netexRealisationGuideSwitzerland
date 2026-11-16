# SiteFacilitySet

List of SiteFacility. Be careful: not all are supported. Consult profile. Make sure to not generate identical SiteFacilitySets. Reuse them. There might be an overlap to ServiceFacilitySet, but they are used for different purposes.

*Table: SiteFacilitySet*

| Sub | Element | Usage | Card | Type | Description | Note |
|-----|---------|-------|------|------|-------------|------|
|  | @id | mandatory | 1..1 | xsd:string | Attribute id | |
|  | @version | mandatory | 1..1 | xsd:string | Attribute version | |
|  | validityConditions | optional | 1..1 | validityConditions_RelStructure |  |  |
| + | [AvailabilityCondition](AvailabilityCondition.md) | optional | 0..* | AvailabilityCondition_VersionStructure | VALIDITY CONDITION stated in terms of DAY TYPES and PROPERTIES OF DAYs. |  |
|  | Description | optional | 0..1 | MultilingualString |  | Description is optional. |
| + | @lang | mandatory | 1..1 | xsd:string | Attribute lang | |
| + | Text | optional | 0..* | MultilingualString |  | All necessary languages are modeled as a Text element |
| ++ | @lang | mandatory | 1..1 | xsd:string | Attribute lang | |
|  | AccessibilityInfoFacilityList | expected | 0..1 | AccessibilityInfoFacilityListOfEnumerations | List of ACCESSIBILITY INFORMATION FACILITies. | Will be exported from ATLAS for ERA TSI PRM (`visualDisplays`: Kundeninformation Haltestelle - "Statisch/optisch; `audioInformation`: Kundeninformation - "Akustisch"). Note that AccessibilityAssessment features `AudibleSignalsAvailable` and `VisualSignsAvailable`, the latter implying dynamic visual information (Kundeninformation Haltestelle - "Dynamisch/optisch"). |
|  | AssistanceFacilityList | expected | 0..1 | AssistanceFacilityListOfEnumerations | List of ASSISTANCE FACILITies. | Will be exported from ATLAS for ERA TSI PRM (Autonome Benutzbarkeit - "Hilfestellung durch Personal" sets `boardingAssistance personalAssistance wheelchairAssistance`). |
|  | MobilityFacilityList | expected | 0..1 | MobilityFacilityListOfEnumerations | List of MOBILITY FACILITies. | Will be exported from ATLAS for ERA TSI PRM (`suitableForWheelchair`: Autonome Benutzbarkeit - "Voraussetzungen erfüllt"; `boardingAssistance`: AutonomeBenutzbarkeit - "Hilfestellung durch Personal"; `stepFreeAccess`: Haltekante - "Niveaugleicher Einstieg";`tactilePlatformEdges`: Haltekante - "Taktil-visuelle Markierung Perronfläche"). Additional allowed value if no data in ATLAS: `unknown`. |
|  | SanitaryFacilityList | expected | 0..1 | SanitaryFacilityListOfEnumerations | List of SANITARY FACILITies. | Will be exported from ATLAS for ERA TSI PRM (Toiletten - "Rollstuhlgängige Toilette). Presence or absence of `wheelchairAccessToilet toilet`. |
|  | TicketingFacilityList | expected | 0..1 | TicketingFacilityListOfEnumerations | List of TICKETING FACILITies. | Will be exported from ATLAS for ERA TSI PRM (Billettautomat - "Billettautomat vorhanden", and Schalter present, respectively). Presence or absence of the following facilities should be signalled: `unknown ticketMachines ticketOffice`. |
|  | ParkingFacilityList | expected | 0..1 | ParkingFacilityListOfEnumerations | List of PARKING FACILITies. | Will be exported from ATLAS for ERA TSI PRM (Parkplatz - Parkplätze). The following should be signalled: `carPark unknown`. |
