# StopPlace_withAccessibility

*Table: StopPlace*

| Sub | Element | Usage | Card | Type | Description | Note |
|-----|---------|-------|------|------|-------------|------|
|  | [AccessibilityAssessment](AccessibilityAssessment.md) | mandatory | 0..1 | AccessibilityAssessment_VersionedChildStructure | Assessment of the accessibility of a SITE. | Accessibility. Whether the StopPlace and the Quays are accessible for passengers with different mobility or sensory impairments. |
|  | Covered | optional | 0..1 | CoveredEnumeration | Whether the component is Indoors or outdoors. Default is Indoors. | Accessibility. Allowed values: `indoors outdoors covered unknown`. Railway stations are usually covered, many bus stops are outdoors. **TODO** Do we want that element? Not required by TRM PSI. |
|  | AllAreasWheelchairAccessible | expected | 0..1 | xsd:boolean | Whether all areas of the component are wheelchair accessible. | Accessibility. True or false if data available, otherwise drop the element. |
|  | facilities | expected | 0..1 | serviceFacilitySets_RelStructure | FACILITies available associated with LINE. It is always recommended to also model accessibility relevant things as equipment on the VEHICLE and physical elements, if real-time information is needed. | Accessibility. Facilites available at the StopPlace. For some of the facilities it is possible to more precisely describe their availabilty using `AssistanceService` further below. |
| + | [SiteFacilitySet](SiteFacilitySet.md) | expected | 1..* | SiteFacilitySetStructure | Set of enumerated FACILITY values that are relevant to a SITE (names based on TPEG classifications, augmented with UIC etc.). | Accessibility. EPIAP wants the SiteFacilitySets being defined here. |
| + | SiteFacilitySetRef | optional | 0..* | SiteFacilitySetRefStructure | Reference to a SITE FACILITY SET. | Accessibility. **TODO**: Shall we allow the use of references here, e.g., for standard configurations? |
|  | levels | expected | 0..1 | levels_RelStructure | LEVELs found within SITe. | Accessibility. Mandatory if the StopPlace has more than one level. |
| + | [Level](Level.md) | expected | 0..* | Level_VersionStructure | Level of a Building or SITE. | Accessibility. Mandatory if the StopPlace has more than one level. |
|  | entrances | expected | 0..1 | pointOfInterestEntrances_RelStructure | ENTRANCEs to and within SITE. | Accessibility. Entrances to the StopPlace. At least one entrance that can be used by passengers with mobility or sensory impairments. Additional entrances are optional. |
| + | [StopPlaceEntrance](StopPlaceEntrance.md) | expected | 0..* | StopPlaceEntrance_VersionStructure | Passenger Entrance to a STOP PLACE. | Accessibility. |
|  | equipmentPlaces | optional | 0..1 | equipmentPlaces_RelStructure | EQUIPMENT PLACEs within SITE COMPONENT. | Accessibility. **TODO** Only needed if we model LiftEquipment, TicketOfficeEquipment, etc. |
| + | EquipmentPlaceRef | optional | 0..* | EquipmentPlaceRefStructure | Reference to an EQUIPMENT PLACE. |  |
|  | placeEquipments | optional | 0..1 | placeEquipments_RelStructure | Items of fixed EQUIPMENT that may be located in places within the SITE ELEMENT. | Accessibility. **TODO** Only needed if we model equipments. |
| + | LiftEquipmentRef | optional | 0..* | AccessEquipmentRefStructure | Identifier of an LIFT EQUIPMENT. | Accessibility. Lift as an example. |
|  | localServices | optional | 0..1 | localServices_RelStructure | LOCAL SERVICEs that may be located in PLACEs within the SITE ELEMENT. |  |
| + | [AssistanceService](AssistanceService.md) | optional | 0..* | AssistanceService_VersionStructure | Specialisation of LOCAL SERVICE for ASSISTANCE providing information like language, accessibility trained staff, etc. | Accessibility. The element allows for more precisely describing the availability of `AssistanceFacility`s and `AccessibilityTools`, e.g., if they need to be booked. It does not add, however, new facilities to the ones already given by the `SiteFacilitySet` (see above). |
| + | [AssistanceBookingService](AssistanceBookingService.md) | optional | 0..* | AssistanceBookingService_VersionStructure | Information about how to book assistance for wheelchair and disabled users. | Accessibility. Contact and booking information regarding assistance services. |
| + | MeetingPointService | expected | 0..* | MeetingPointService_VersionStructure | Specialisation of CUSTOMER SERVICE for meeting points (provides characteristics like description, label, etc.). | Accessibility. Indicates the presence or absence of a meeting point. |
| ++ | MeetingPointServiceType | mandatory | 1..1 | MeetingPointEnumeration | Type of MEETING POINT. | Only a single value allowed from: `meetingPoint groupMeetingPoint`. |
| ++ | Label | expected | 0..1 | MultilingualString | Label on step. |  |
|  | accessSpaces | expected | 0..1 | accessSpaces_RelStructure | ACCESS SPACEs within the STOP PLACE. | Accessibility. **TODO** Needed if we model equipments - EquipmentPlaces may require an AccessSpace as parent. |
| + | [AccessSpace](AccessSpace.md) | expected | 0..* | AccessSpace_VersionStructure | An area within a STOP PLACE that does not give direct access to transport vehicles. May be connected to QUAYS by PATH LINKs. | Accessibility. |
