# StopPlace_accessibility

*Table: StopPlace*

| Sub | Element | Usage | Card | Type | Description | Note |
|-----|---------|-------|------|------|-------------|------|
|  | [AccessibilityAssessment](AccessibilityAssessment.md) | expected | 0..1 | AccessibilityAssessment_VersionedChildStructure | Accessibility values associated with LEVEL. | Accessibility. Whether the StopPlace and the Quays are accessible for passengers with different mobility or sensory impairments. |
|  | facilities | expected | 0..1 | siteFacilitySets_RelStructure | Facilities available at SITe. | Facilities available at the stop. |
| + | [SiteFacilitySet](SiteFacilitySet.md) | expected | 0..* | SiteFacilitySetStructure | Set of enumerated FACILITY values that are relevant to a SITE (names based on TPEG classifications, augmented with UIC etc.). | In particular for accessibility information. |
|  | levels | expected | 0..1 | levels_RelStructure | LEVELs found within SITe. | Mandatory if the StopPlace has more than one level. |
| + | Level | expected | 0..* | Level_VersionStructure | Level of a Building or SITE. | Mandatory if the StopPlace has more than one level. |
|  | entrances | optional | 0..1 | siteEntrances_RelStructure | ENTRANCEs to SPACE. | Reference points that will be exported from ATLAS for ERA TSI PRM. |
| + | [StopPlaceEntrance](StopPlaceEntrance.md) | mandatory | 0..* | StopPlaceEntrance_VersionStructure | Passenger Entrance to a STOP PLACE. | Currently only the sloid is known, coordinates planned for 2027. From this point all references to accessibility are made in Switzerland. |
|  | placeEquipments | optional | 0..1 | equipments_RelStructure | Items of EQUIPMENT that may be located in an EQUIPMENT PLACE. | Used in exports for all TSI PRM relevant equipments. Especially in the data transmissions for rail to ERA. We only have Equipments and no EquipmentPlaces. |
| + | TicketingEquipment | optional | 0..* | unknown |  | Ticketing equipment. |
| ++ | TicketMachines | expected | 0..1 | boolean | Whether there are ticket machines. | Will be exported from ATLAS for ERA TSI PRM (Billettautomat - "Billettautomat vorhanden"). Mirrored in SiteFacilitySet - ticketMachines. |
| ++ | TicketOffice | expected | 0..1 | boolean | Whether there is a distinct ticket office. | Will be exported from ATLAS for ERA TSI PRM (Schalter present). Mirrored in SiteFacilitySet - ticketOffice. |
| ++ | TicketCounter | optional | 0..1 | boolean | Whether there is a ticket counter. | Will be exported from ATLAS for ERA TSI PRM (Schalter present). We don't distinguish between TicketOffice and TicketCounter. |
| ++ | LowCounterAccess | optional | 0..1 | boolean | Whether there is a low counter for accessibility. | Will be exported from ATLAS for ERA TSI PRM (Schalter - "Rollstuhlzugänglichkeit" or Billettautomat - "Barrierefrei"). Applicable for TicketMachine, TicketOffice, TicketCounter. |
| ++ | InductionLoops | optional | 0..1 | boolean | Whether there are induction loops. | Will be exported from ATLAS for ERA TSI PRM (Schalter - "Induktionsverstärker"). Only applicable for TicketOffice, TicketCounter. |
| ++ | TactileInterfaceAvailable | optional | 0..1 | boolean | Indicates whether there is a tactile interface +v1.1. | Will be exported from ATLAS for ERA TSI PRM (Billettautomat - "Akustische und taktile Ausrüstung"). Only applicable for TicketMachine. |
| ++ | AudioInterfaceAvailable | optional | 0..1 | boolean | Indicates whether there is an accessible audio interface (allowing a use closed eyes). +v1.1 | Will be exported from ATLAS for ERA TSI PRM (Billettautomat - "Akustische und taktile Ausrüstung"). Only applicable for TicketMachine. |
| ++ | WheelchairSuitable | expected | 0..1 | boolean | Indicates whether equipment may be used while seated in a wheelchair. +v1.1 | Will be exported from ATLAS for ERA TSI PRM (Schalter - "Rollstuhlzugänglichkeit" or Billettautomat - "Barrierefrei"). Applicable for TicketMachine, TicketOffice, TicketCounter. |
| + | AccessVehicleEquipment | optional | 0..* | AccessVehicleEquipment_VersionStructure | Specialisation of VEHICLE EQUIPMENT for ACCESS providing information such as low floor, ramp, access area dimensions, etc. | Method to get on the vehicle |
| ++ | Hoist | expected | 0..1 | boolean | VEHICLE has a hoist or lift for wheelchairs. | Will be exported from ATLAS for ERA TSI PRM (Haltekante - "Hilfsmittel für Rollstuhl"). May not be set to true for the StopPlace if there is a Quay unaccessible by wheelchair. |
| ++ | Ramp | expected | 0..1 | boolean | Whether a ramp may be used to access VEHICLE. | Will be exported from ATLAS for ERA TSI PRM (Haltekante - "Hilfsmittel für Rollstuhl"). May not be set to true for the StopPlace if there is a Quay unaccessible by wheelchair. |
| + | SanitaryEquipment | optional | 0..* | unknown |  |  |
| ++ | Name | optional | 0..1 | MultilingualString | Name of EQUIPMENT. |  |
| ++ | [AccessibilityAssessment](AccessibilityAssessment.md) | optional | 0..1 | AccessibilityAssessment_VersionedChildStructure |  |  |
| ++ | SanitaryFacilityList | mandatory | 0..1 | SanitaryFacilityListOfEnumerations |  | Will be exported from ATLAS for ERA TSI PRM (Toiletten - "Rollstuhlgängige Toilette). Presence or absence of `wheelchairAccessToilet toilet`. Mirrored in SiteFacilitySet - SanitaryFacilityList. |
| ++ | ToiletsType | optional | 0..1 | ToiletsTypeEnumeration | Indicates the position of using the toilet. | Allowed values: `seated urinal seatedAndUrinal squat`. |
|  | localServices | optional | 0..1 | localServices_RelStructure |  | Will be exported from ATLAS for ERA TSI PRM. |
| + | [AssistanceService](AssistanceService.md) | mandatory | 0..* | AssistanceService_VersionStructure | Specialisation of LOCAL SERVICE for ASSISTANCE providing information like language, accessibility trained staff, etc. | Presence of`AssistanceFacility`s and their availability , e.g., if they need to be booked. |
| + | [AssistanceBookingService](AssistanceBookingService.md) | optional | 0..* | AssistanceBookingService_VersionStructure | Information about how to book assistance for wheelchair and disabled users. | Accessibility. Contact and booking information regarding assistance services. |
