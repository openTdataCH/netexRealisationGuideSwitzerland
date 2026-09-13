# Annex: Relevant differences between EPIP, EPIAP and the Swiss realisation guide 2.0

Note: The following list is not necessarily comprehensive.
>**LATER** https://github.com/openTdataCH/netexRealisationGuideSwitzerland/blob/main/docs/A2_annex_comparison_EPIP_EPIAP.md

## Main differences

The following lists aim to give an overviiew of all elements related to accessibility information. Most of them are described in EPIAP, while a few are documented in greater detail in Part 1 of NeTEx (in particular, various Services and enumerations). 

The elements in ***italics*** are the ones that are (tentatively) elected for being included in the Swiss profile. Note that, in contrast, the French profile includes practically the totality of EPIAP. 

### AccessibilityAssessment

***AccessibilityAssessment*** for:
- ***StopPlace***
- ***Quay.***
- ***Entrance***
- Line - ?
- NavigationPath
- ***PathLink***
- ***SanitaryEquipment***
- any SiteElement

### Basic Orientation

***Level*** (NO, not FR, but EPIAP says mandatory if > 1)
- AccessibilityAssessment
- ***Description***
- ***Name***
- PublicUse

***Entrance*** 
- **EntranceType**
-  Height 
- ***IsEntry*** 
- ***IsExit*** 
- IsExternal 
-  ***Width*** 
- ***checkConstraints*** 
- ***placeEquipments***

***AccessSpace***


### Private Mobility

***Parking***
- ***ParkingType***
- ***ParkingVehicleType***
- RechargingAvailable
- Principal***Capacity***
- TotalCapacity
- etc.

***VehicleMeetingPoint***

Crossing 
- AcousticCrossingAids 
- AcousticDeviceSensors 
- BumpCrossing 
- CrossingType 
- MarkingStatus 
-  PedestrianLights 
-  TactileGuidanceStrips 
-  TactileWarningStrip 
-  VibratingCrossingAids 
- VisualObstacle
-  ZebraCrossing 


**Path Navigation**

***SitePathLink***
- ***AccessFeatureType*** 
- ***AccessibilityAssessment*** 
- ***AllAreasWheelchair*** 
- ***AllowedUse*** 
- Back 
- ***Covered*** 
- ***Description*** 
- ***Distance*** 
- FlooringType 
- ***From*** 
- ***Gated*** 
- Gradient
- LeftSideBorder
- Lighting 
- ***MinimumWidth*** 
- ***NumberOfSteps*** 
- PassageType 
- PublicUse 
- RightSideBorder
- TactileGuidingStrip 
- TactileWarningStrip 
- TiltAngle 
- TiltType 
- Towards 
- ***TransferDuration***
- ***Transition***
- checks
- placeEquipments

***PathLinkEnd***
- ***EntranceRef***
- ***LevelRef***
- ***PlaceRef***

PathLinkSequence
- Instruction
- Label
- PathLinkRef
- Reverse

***PathJunction***
- AllAreasWheelchair
- Covered
- Gated
- Label
- Lighting
- PublicUse
- ***SiteComponentRef***

ConnectionEnd
- MobilityRestrictedTravellerDuration


NavigationPath
- AccessibilityAssessment
- Covered
- From
- To
- Gated
- Lighting
- NavigationType
- TransferDuration
- pathLinksInSequence

***WalkTransferduration*** (in SiteConnection, DefaultConnection)
- ***MobilityRestrictedTravellerDuration***




### Facilities & Equipments


***EquipmentPlace*** (in Quay, Entrance, StopPlace (indirecty via `AccessSpace`))


any Site
- ***entrances***
- ***equipmentPlaces***
- ***levels***
- ***localServices***
- ***placeEquipments***


any SiteElement
- AccessibilityAssessment
- Covered
- Gated
- Lighting
- facilities
- etc.


any Equipment
- ***Description***
- ***Image***
- ***Name***
- ***Note***
- ***OutOfService***
- ***TypeOfEquipmentRef***


EquipmentPosition
- Description
- Location
- ReferencePointRef
- XOffset
- YOffset


***EntranceEquipment***
- AcousticSensor 
- AudioOrVideolntercom 
- AudioPassthroughindicator 
- ***AutomaticDoor***
- ***Barrier***
- ***GlassDoor***
- ***Door*** 
- DoorstepMark 
* ***DropKerbOutside*** 
- EntranceAttention 
- EntranceRequiresStaffing 
-  ***EntranceRequiresTicket***
- ***KeptOpen*** 
- NecessaryForceToOpen 
- ***NumberOfGates*** 
- RampDoorbell optional 0:1
- ***RevolvingDoor*** 
- TurningSpacePosition 
- ***WheelchairPassable*** 
- WheelchairTurningCircle
- etc.



***EscalatorEquipment***
- ***DogsMustBeCarried***
- TactileActuators
- etc.


***LiftEquipment***
- ***AudioAnnouncements*** 
- ***Automatic***
- ***BrailleButtons***
- ButtonsHeight 
- CallButtonHeight
- ***Depth*** 
- DirectionButtonHeight 
- ExternalFloorSelection 
- GroundMarkalignedWithButton 
- HandrailHeight 
- HandrailType 
- ***InternalWidth*** 
- LowerHandrailHeight 
- MagneticinductionLoop 
- MaximumLoad 
- MirrorOnOppositeSide 
- RaisedButtons 
- ReachedFloorAnnouncement 
- SignageToLift 
- ***TactileActuators*** 
- ***TactileGroundFloorButton*** 
- WheelchairTurningCircle 
- etc.



***RampEquipment***
- ***Gradient***
- ***GradientType***
- HandrailHeight
- HandrailType
- Length
- Pedestal
- RestStopDistance
- SafetyEdge



***TravelatorEquipment***
- Gradient
- TactileActuators
- ***SafeForGuideDog***
- etc.

Staircase
- BottomEnd 
- ContinuousHandrail 
- Depth 
- HandrailHeight 
- LowerHandrailHeight 
- NumberOfFlights 
- NumberOfSteps
- SpiralStair 
- StepColourContrast 
- StepCondition 
- StepHeight 
- StepLength 
- etc.



***LuggageLockerEquipment***
- ***BlindAccessible***
- ***WheelchairAccepted***
- ***NumberOfLockers***
- etc.


***TrolleyStandEquipment***
- ***FreeToUse***


PassengerEquipment
- Fixed

***PassengerSafetyEquipment***
- ***AcousticAnnouncements***
- ***AcousticAnnouncementsTrigger***
- ***AnnouncementTriggeringMethod***
- ***HeightOfSosPanel***
- ***Lighting***
- ***PanicButton***
- ***SosPanel***



***SanitaryEquipment***
- ***AccessibilityAssessment***
- ***CallButtonAvailable***
- DrinkingWater 
- ***Gender*** 
- HandWashing
- KeyScheme - ?
- LockedAccess - ?
- SharpsDisposal 
- Staffing 
- SupportBarHeigth 
- ***ToiletsType*** 
- WheelchairTurningCircle 

***TicketingEquipment*** 
- DisabledPriority 
- HeightOfLowCounter 
- HeightOfMachinelnterface 
- ***InductionLoops*** 
- LowCounterAccess 
- ***NumberOfMachines*** 
- ***TactilelnterfaceAvailable*** 
- ***TicketCounter*** 
- ***TicketMachines*** 
- ***WheelchairSuitable*** 


QueingEquipment - ?
- DisabledPriority
- QueingSeatedPossible
- RailedQueue
- TicketedQueue


RubbishDisposalEquipment


***TicketValidatorEquipment***
- AudioValidationFeedback
- TactileValidationFeedback
- ValidationGuidance
- VisualValidationFeedback


ShelterEquipment - ?
- DistanceFromNearestKerb
- Enclosed


***WaitingEquipment***
- AirConditioned
- ***Heated***
- ***Seats***
- ***SmokingAllowed***
- ***StepFree***
- ***WheelchairAreaLength***
- ***WheelchairAreaWidth***
- etc.


***WaitingRoomEquipment***
- ***Facilities***
- ***TypeOfFareClass***


***SignEquipment*** - ?
- ***AsBraille***
- ***AudioTriggerMethod***
- Contrast
- ***FontSize***
- etc.


Accommodation
- AcommodationFacility
- PassengercommsFacilityList
- ToiletFacility


localServices in StopPlace

***AssistanceService***
- ***AccessibilityTrainedStaff***
- ***AssistanceAvailability***
- ***SafetyFacilityList***
- ***etc.***

***AssistanceBookingService***

***LostPropertyService***

***LuggageService***
- LuggageMaximalWeigth
- ***LuggageTrolleys***
- WheelchairLuggageTrolleys
- etc.

***MeetingPointService***
- ***Label***
- ***MeetingPointType***

***TicketingService***
- ***MobileDeviceTickets***
- ***OnboardPurchase***
- ***TicketCounterService***



***SiteFrame***
- ***siteFacilitySets***

***SiteFacilitySet for***
- ***StopPlace***
- ***Quay***


***SiteFacilitySet***
- ***AccessFacilityList***
- ***AccessibilityInfoFacilityList***
- ***AccessibilityToolList*** 
- ***AssistanceFacilityList***
- ***Description*** 
- ***LuggageLockerFacilityList*** 
- ***LuggageServiceFacilityList*** 
- ***MobilityFacilityList***
- ***SafeteyFacilityList***
- ***ParkingFacilityList*** 
- ***Staffing***
- ***SanitaryFacilityList***
- ***TicketingServiceFacilityList*** 
- etc.


***ServiceFacilitySet***
- ***VehicleAccessFacilityList***
- ***AccommodationFacilityLis***t - pushchair, wheelchair
- ***LuggageCarriageFacilityList*** - pushchairsAllowed, cyclesAllowed, etc.
- accommodations
- onboardStays



PlaceLighting
- AlwaysLit
- Lighting
- LightingMethod

RoughSurface
- SurfaceType


***Operator***
- ***ContactDetails***

***CustomerService***
- ***Email***
- ***InfoLink***
- ***Phone***



### Vehicles & Vehicle Stop Interaction

***VehicleType (later)***
- ***Description*** 
- ***HasHoist*** 
- ***HasLiftOrRamp*** 
- Height 
- Length
- ***LowFloor*** 
- ***equipments***
- ***facilities***
- ***equipmentProfiles - VehicleEquipmentProfile - WheelchairVehicleEquipment***
- ***PassengerCapacity***
	- ***WheelchairPlaceCapacity***
- etc.

PlatformHeight, GapToPlatform

***BoardingPosition*** (NO, not FR)
- ***BoardingPositionType***
- ***Label***

***TrainStopAssignment***
- ***BoardingPositionRef***
- ***EntranceToVehicle***
- PassengerStopAssignmentRef
- TrainRef
- TrainComponentRef




## Other noteworthy differences
* DELFI, PRM TSI ...
* Accessibility in the French profile ...
* EPIAP requires AlternativeText, Swiss profile excludes it
* bla

## Things that should be included/changed for the new European profile for 2028
* bla
* bla
* bla


# EPIAP in Switzerland - WORK IN PROGRESS

Definition of the Swiss Accessibility Profile.

## AccessibilityAssessment
*→ [Glossary definition](A4_annex_glossary.md#accessibilityassessment)* TODO

### Purpose

An assessment of the usability by passengers with specific needs, for example, those needing wheelchair access, step-free access or for the visually or the auditorily impaired.


### Table



*Table: AccessibilityAssessment*

| Sub | Element | Usage | Card | Type | Description | Note |
|-----|---------|-------|------|------|-------------|------|
|  | MobilityImpairedAccess | mandatory | 1..1 | LimitationStatusEnumeration | Summary indication as to whether the component is considered to be accessible or not. | Accessibility. Overall assessment for mobility and sensory impaired users. partial means that there must exist AccessibiltyAssessment at lower levels like Quays or other elements. Some Quays may not be accessible if partial is used on the StoPlace. |
|  | limitations | expected | 0..1 | usageParameters_RelStructure | The ACCESSIBILITY LIMITATION that apply to component. | Accessibility. Limitations can be omitted if MobilityImpairedaccess is set to true and no additional information needs to be conveyed. |
| + | AccessibilityLimitation | mandatory | 0..* | AccessibilityLimitation_VersionedChildStructure | Assessment of the accessibility of a SITE. | Accessibility. |
| ++ | WheelchairAccess | mandatory | 1..1 | LimitationStatusEnumeration | Whether a PLACE is wheelchair accessible. | Accessibility. |
| ++ | StepFreeAccess | expected | 0..1 | LimitationStatusEnumeration | Whether a PLACE has step free access. | Accessibility. If absent the value `unknown` is assumed. Allowed values: true, false, partial, unknown. |
| ++ | StairFreeAccess | expected | 0..1 | LimitationStatusEnumeration | Whether a PLACE has stair free access, in comparison with step free access one single step in the route is allowed. +v2.0 | Accessibility. Not mandatory in EPIAP, but very useful for perambulators, assisted wheelchairs, bicycles, heavy luggage. Allowed values: true, false, partial, unknown. |
| ++ | RampFreeAccess | expected | 0..1 | LimitationStatusEnumeration | Whether a PLACE has ramp free access. Ramp free isn't necessary absolute. If a ramp is not steep, then a PLACE can still be considered ramp free. | Accessibility. Reachable without steep ramps, stairs, or steps. Allowed values: true, false, partial, unknown. |
| ++ | GuideDogAccess | expected | 0..1 | LimitationStatusEnumeration | Whether a PLACE allows guide dog access. | Accessibility. If absent the value `unknown` is assumed. Allowed values: true, false, partial, unknown. |
| ++ | TactileGuidanceAvailable | expected | 0..1 | LimitationStatusEnumeration | Whether a PLACE has tactile guidance. | Accessibility. Whether the object has tactileGuidance (for the visually impaired). If absent the value `unknown` is assumed. Allowed values: true, false, partial, unknown. |
| ++ | VisualSignsAvailable | expected | 0..1 | LimitationStatusEnumeration | Whether a PLACE has visual signals for the hearing impaired. | Accessibility. If absent the value `unknown` is assumed. Allowed values: true, false, partial, unknown. |
| ++ | LevelAccessIntoVehicle | expected | 0..1 | LimitationStatusEnumeration | Whether the platform is high enough and gap is small enough for level access into vehicle. At least at a designated wheelchair door position the gap between platform and vehicle floor (of level access vehicle) does not exceed 75 mm measured horizontally and 50 mm measured vertically including sliding step (according to PRM TSI). | Accessibility. Whether the platform is high enough and gap is small enough for level access to vehicle. If absent the value `unknown` is assumed. Allowed values: true, false, partial, unknown. |




*→ [General NeTEx definition ](../xcore/netex/elements/AccessibilityAssessment.html)*

### Example


```xml
<?xml version="1.0" encoding="UTF-8"?>
<AccessibilityAssessment id="generated" version="1">
  <MobilityImpairedAccess>true
    <!-- Accessibility. Overall assessment for mobility and sensory impaired users. partial means that there must exist AccessibiltyAssessment at lower levels like Quays or other elements. Some Quays may not be accessible if partial is used on the StoPlace. -->
  </MobilityImpairedAccess>
  <limitations>
    <!-- Accessibility. Limitations can be omitted if MobilityImpairedaccess is set to true and no additional information needs to be conveyed. -->
    <AccessibilityLimitation>
      <!-- Accessibility. -->
      <WheelchairAccess>true
        <!-- Accessibility. -->
      </WheelchairAccess>
      <StepFreeAccess>true
        <!-- Accessibility. If absent the value `unknown` is assumed. Allowed values: true, false, partial, unknown. -->
      </StepFreeAccess>
      <StairFreeAccess>true
        <!-- Accessibility. Not mandatory in EPIAP, but very useful for perambulators, assisted wheelchairs, bicycles, heavy luggage. Allowed values: true, false, partial, unknown. -->
      </StairFreeAccess>
      <RampFreeAccess>true
        <!-- Accessibility. Reachable without steep ramps, stairs, or steps. Allowed values: true, false, partial, unknown. -->
      </RampFreeAccess>
      <GuideDogAccess>true
        <!-- Accessibility. If absent the value `unknown` is assumed. Allowed values: true, false, partial, unknown. -->
      </GuideDogAccess>
      <TactileGuidanceAvailable>true
        <!-- Accessibility. Whether the object has tactileGuidance (for the visually impaired). If absent the value `unknown` is assumed. Allowed values: true, false, partial, unknown. -->
      </TactileGuidanceAvailable>
      <VisualSignsAvailable>true
        <!-- Accessibility. If absent the value `unknown` is assumed. Allowed values: true, false, partial, unknown. -->
      </VisualSignsAvailable>
      <LevelAccessIntoVehicle>true
        <!-- Accessibility. Whether the platform is high enough and gap is small enough for level access to vehicle. If absent the value `unknown` is assumed. Allowed values: true, false, partial, unknown. -->
      </LevelAccessIntoVehicle>
    </AccessibilityLimitation>
  </limitations>
</AccessibilityAssessment>
```



*→ [Template](./templates/AccessibilityAssessment.xml)*


### Usage Notes

In case of `StopPlace` or `Quay`, EPIAP uses the following interpretation: 
`MobilityImpairedAccess` set to `true` means:
* `WheelchairAccess` `true`
* `StepFreeAccess` `true`
* `VisualSignsAvailable` `true` (only for railway stations)
* `TactileGuidanceAvailable` `true`

Interpretation of `AccessibilityLimitation`:

|   |   |
|---|---|
|`WheelchairAccess`|1.    `StepFreeAccess` from an accessible entrance (see next row).<br>2.    The stop/platform is sufficiently wide to make a turn with a wheelchair when entering/leaving the vehicles that usually stops at this stop/platform (depending on the available/needed tools for entering/leaving the vehicle).<br>3.    If boarding trains requires boarding assistance, onsite assistance is available.|
|`StepFreeAccess`|1.    A step-free route is an obstacle-free/barrier free route that meets the needs of mobility impaired persons. Changes in level are avoided or, when they cannot be avoided, they are bridged via ramps or lifts (compliant with PRM TSI).<br>2.    The platform or Stop is accessible without steps from the surrounding area (footpaths).<br>A platform which has `StepFreeAccess` without `WheelchairAccess` (= `false`) may be not sufficiently wide to make a turn with a wheelchair.|
|`StairFreeAccess`|A stair-free route. Single steps allowed.|
|`LevelAccessIntoVehicle`|Whether the platform is high enough and gap is small enough for level access into vehicle.<br><br>At least at a designated wheelchair door position the gap between platform and vehicle floor (of level access vehicle) does not exceed 75 mm measured horizontally and 50 mm measured vertically including sliding step (according to PRM TSI).|
|`EscalatorFreeAccess` (not included in profile)|Reachable without using an escalator.|
|`LiftFreeAccess` (not included in profile)|Reachable without using an elevator.|
|`RampFreeAccess`|Reachable without using a ramp that doesn't fit the UN Design [Considerations](https://euc-word-edit.officeapps.live.com/we/wordeditorframe.aspx?ui=nl-nl&rs=nl-nl&wopisrc=https%3A%2F%2Fitxptorg.sharepoint.com%2Fsites%2FEU.DATA4PT.NETEX%2F_vti_bin%2Fwopi.ashx%2Ffiles%2Fc2c9167177c34bc1bb50e4880ff7b6ac&wdenableroaming=1&mscc=1&hid=12869e13-00bf-76bc-9351-10ac590e57c1-730&uiembed=1&uih=teams&uihit=files&hhdr=1&dchat=1&sc=%7B%22pmo%22%3A%22https%3A%2F%2Fteams.microsoft.com%22%2C%22pmshare%22%3Atrue%2C%22surl%22%3A%22%22%2C%22curl%22%3A%22%22%2C%22vurl%22%3A%22%22%2C%22eurl%22%3A%22https%3A%2F%2Fteams.microsoft.com%2Ffiles%2Fapps%2Fcom.microsoft.teams.files%2Ffiles%2F2441637157%2Fopen%3Fagent%3Dpostmessage%26objectUrl%3Dhttps%253A%252F%252Fitxptorg.sharepoint.com%252Fsites%252FEU.DATA4PT.NETEX%252FShared%2520Documents%252FGeneral%252FCEN_Accessibility_Profile%252F20210326%2520PrTS%252016614-6.docx%26fileId%3Dc2c91671-77c3-4bc1-bb50-e4880ff7b6ac%26fileType%3Ddocx%26ctx%3Daggregate%26scenarioId%3D730%26locale%3Dnl-nl%26theme%3Ddefault%26version%3D21100501100%26setting%3Dring.id%3Ageneral%26setting%3DcreatedTime%3A1639152919292%22%7D&wdorigin=TEAMS-ELECTRON.aggregatefiles.aggregate&jsapi=1&jsapiver=v1&newsession=1&corrid=ce9d3917-7c65-4632-a7d4-9644eb2f8575&usid=ce9d3917-7c65-4632-a7d4-9644eb2f8575&sftc=1&sams=1&accloop=1&sdr=6&scnd=1&sat=1&hbcv=1&htv=1&hodflp=1&instantedit=1&wopicomplete=1&wdredirectionreason=Unified_SingleFlush&rct=Medium&ctp=LeastProtected#_ftn1) (for instance, because they are too steep or a landing is missing in case of a ramp of more than 10 m). [[1]](https://euc-word-edit.officeapps.live.com/we/wordeditorframe.aspx?ui=nl-nl&rs=nl-nl&wopisrc=https%3A%2F%2Fitxptorg.sharepoint.com%2Fsites%2FEU.DATA4PT.NETEX%2F_vti_bin%2Fwopi.ashx%2Ffiles%2Fc2c9167177c34bc1bb50e4880ff7b6ac&wdenableroaming=1&mscc=1&hid=12869e13-00bf-76bc-9351-10ac590e57c1-730&uiembed=1&uih=teams&uihit=files&hhdr=1&dchat=1&sc=%7B%22pmo%22%3A%22https%3A%2F%2Fteams.microsoft.com%22%2C%22pmshare%22%3Atrue%2C%22surl%22%3A%22%22%2C%22curl%22%3A%22%22%2C%22vurl%22%3A%22%22%2C%22eurl%22%3A%22https%3A%2F%2Fteams.microsoft.com%2Ffiles%2Fapps%2Fcom.microsoft.teams.files%2Ffiles%2F2441637157%2Fopen%3Fagent%3Dpostmessage%26objectUrl%3Dhttps%253A%252F%252Fitxptorg.sharepoint.com%252Fsites%252FEU.DATA4PT.NETEX%252FShared%2520Documents%252FGeneral%252FCEN_Accessibility_Profile%252F20210326%2520PrTS%252016614-6.docx%26fileId%3Dc2c91671-77c3-4bc1-bb50-e4880ff7b6ac%26fileType%3Ddocx%26ctx%3Daggregate%26scenarioId%3D730%26locale%3Dnl-nl%26theme%3Ddefault%26version%3D21100501100%26setting%3Dring.id%3Ageneral%26setting%3DcreatedTime%3A1639152919292%22%7D&wdorigin=TEAMS-ELECTRON.aggregatefiles.aggregate&jsapi=1&jsapiver=v1&newsession=1&corrid=ce9d3917-7c65-4632-a7d4-9644eb2f8575&usid=ce9d3917-7c65-4632-a7d4-9644eb2f8575&sftc=1&sams=1&accloop=1&sdr=6&scnd=1&sat=1&hbcv=1&htv=1&hodflp=1&instantedit=1&wopicomplete=1&wdredirectionreason=Unified_SingleFlush&rct=Medium&ctp=LeastProtected#_ftnref1) [https://www.un.org/esa/socdev/enable/designm/AD2-01.htm](https://www.un.org/esa/socdev/enable/designm/AD2-01.htm)|
|`AudibleSignalsAvailable`|Whether audible signals for the visually impaired are present.|
|`VisualSignsAvailable`|PRM TSI: visual information as signposting, pictograms and dynamic information.|
|`TactileGuidanceAvailable`|Whether the object has tactile guidance (for the visually impaired). If absent assume `unknown`.<br>PRM TSI: obstacle-free route to each Quay for the visually impaired passengers equipped with tactile information.  <br>For bus- and tram stops:  <br>1.  Groundsurfaceindicator (at location first door) and/or full-length guideline (for boarding at all entrances)<br>2.   Tactile guideline or boarding position connected to (natural) guideline in environment|

#### Remarks `RampFreeAccess`

* Note that `RampFreeAccess` may very well include ramps - provided their slopes are only moderate.
* It seems obvious that `RampFreeAccess`should also include `StairFreeAccess` and `StepFreeAccess` - this isn't explicitely stated in EPIAP, however. 
* `RampFreeAccess`is thus a stronger form of `WheelchairAccess` excluding steeper slopes.


#### Limitiations of AccessibilityAssessment

* If, e.g., `WheelchairAccess` or `StairFreeAccess` requires using a lift, the `AccessibilityAssessment` does not convey this information. 

* According to EPIAP definitions, a quay with, e.g., `WheelchairAccess` means that there is at least one entrance from which it is reachable. It may be that `WheelchairAccess` only works from a secondary entrance, not from the main entrance. 

Such information can be encoded using `PathLink`s and `PathJunction`s that describe a routing network including accessibility and location data.


## StopPlace - the Additional Elements



### Table



*Table: StopPlace*

| Sub | Element | Usage | Card | Type | Description | Note |
|-----|---------|-------|------|------|-------------|------|
|  | [AccessibilityAssessment](./tables/AccessibilityAssessment.md) | mandatory | 0..1 | AccessibilityAssessment_VersionedChildStructure | Assessment of the accessibility of a SITE. | Accessibility. |
|  | Covered | expected | 0..1 | CoveredEnumeration | Whether the component is Indoors or outdoors. Default is Indoors. | Accessibility. |
|  | AllAreasWheelchairAccessible | mandatory | 0..1 | xsd:boolean | Whether all areas of the component are wheelchair accessible. | Accessibility. |
|  | facilities | expected | 0..1 | serviceFacilitySets_RelStructure | FACILITies available associated with LINE. It is always recommended to also model accessibility relevant things as equipment on the VEHICLE and physical elements, if real-time information is needed. | Accessibility. |
| + | SiteFacilitySet | optional | 1..* | SiteFacilitySetStructure | Set of enumerated FACILITY values that are relevant to a SITE (names based on TPEG classifications, augmented with UIC etc.). | Accessibility. |
| + | SiteFacilitySetRef | optional | 0..* | SiteFacilitySetRefStructure | Reference to a SITE FACILITY SET. | Accessibility. TODO: EPIAP wants the SiteFacilitySets being defined here, referernces may be wrong. |
|  | levels | expected | 0..1 | levels_RelStructure | LEVELs found within SITe. | Accessibility. Mandatory if the StopPlace has more than one level. |
| + | [Level](./tables/Level.md) | expected | 0..* | Level_VersionStructure | Level of a Building or SITE. | Accessibility. Mandatory if the StopPlace has more than one level. |
| + | [Level](./tables/Level.md) | expected | 0..* | Level_VersionStructure | Level of a Building or SITE. | Accessibility. Mandatory if the StopPlace has more than one level. |
|  | entrances | expected | 0..1 | pointOfInterestEntrances_RelStructure | ENTRANCEs to and within SITE. | Accessibility. |
| + | [Entrance](./tables/Entrance.md) | expected | 0..* | SiteEntrance_VersionStructure | Entrance to a SITE. | Accessibility. |
|  | equipmentPlaces | optional | 0..1 | equipmentPlaces_RelStructure | EQUIPMENT PLACEs within SITE COMPONENT. | Accessibility. TODO |
|  | placeEquipments | optional | 0..1 | placeEquipments_RelStructure | Items of fixed EQUIPMENT that may be located in places within the SITE ELEMENT. | Accessibility. TODO |
|  | localServices | expected | 0..1 | localServices_RelStructure | LOCAL SERVICEs that may be located in PLACEs within the SITE ELEMENT. | Accessibility. |
| + | AssistanceServiceRef | optional | 0..* | AssistanceServiceRefStructure | Identifier of an ASSISTANCE SERVICE. | Accessibility. |
|  | accessSpaces | expected | 0..1 | accessSpaces_RelStructure | ACCESS SPACEs within the STOP PLACE. | Accessibility. |
| + | [AccessSpace](./tables/AccessSpace.md) | expected | 0..* | AccessSpace_VersionStructure | An area within a STOP PLACE that does not give direct access to transport vehicles. May be connected to QUAYS by PATH LINKs. | Accessibility. |





### Example


```xml
<?xml version="1.0" encoding="UTF-8"?>
<StopPlace id="ch:1:sloid:7000" version="1">
  <ValidBetween>
    <FromDate>2025-12-14T00:00:00</FromDate>
    <ToDate>2026-12-12T23:59:59</ToDate>
  </ValidBetween>
  <keyList>
    <KeyValue>
      <Key>HafasPriority</Key>
      <Value>4</Value>
    </KeyValue>
    <KeyValue>
      <Key>HafasKMInfo</Key>
      <Value>1000</Value>
    </KeyValue>
  </keyList>
  <privateCodes>
    <PrivateCode type="didok">7000</PrivateCode>
    <PrivateCode type="sloid">ch:1:sloid:7000</PrivateCode>
  </privateCodes>
  <Name>Bern</Name>
  <ShortName/>
  <PrivateCode/>
  <Centroid>
    <Name/>
    <Location>
      <Longitude>7.43913088992</Longitude>
      <Latitude>46.94883228914</Latitude>
      <Altitude>540.2</Altitude>
    </Location>
  </Centroid>
  <AccessibilityAssessment id="generated" version="1">
    <!-- Accessibility. -->
    <MobilityImpairedAccess>true
      <!-- Accessibility. -->
    </MobilityImpairedAccess>
  </AccessibilityAssessment>
  <alternativeNames>
    <AlternativeName id="ch:1:sloid:7000:it" version="1">
      <NameType>alias</NameType>
      <Name lang="it">Berna</Name>
    </AlternativeName>
  </alternativeNames>
  <Covered>covered
    <!-- Accessibility. -->
  </Covered>
  <AllAreasWheelchairAccessible>true
    <!-- Accessibility. -->
  </AllAreasWheelchairAccessible>
  <facilities>
    <!-- Accessibility. -->
    <SiteFacilitySet id="ch:1:sitefacilityset:7000:1" version="1">
      <!-- Accessibility. -->
    </SiteFacilitySet>
    <SiteFacilitySetRef ref="generated" version="1">
      <!-- Accessibility. TODO: EPIAP wants the SiteFacilitySets being defined here, referernces may be wrong. -->
    </SiteFacilitySetRef>
  </facilities>
  <TopographicPlaceRef ref="BE-bern" version="1"/>
  <Locale>
    <TimeZone>Europe/Zurich</TimeZone>
  </Locale>
  <levels>
    <!-- Accessibility. Mandatory if the StopPlace has more than one level. -->
    <Level id="ch:1:level:7000:0" version="1">
      <!-- Accessibility. Mandatory if the StopPlace has more than one level. -->
    </Level>
    <Level id="ch:1:level:7000:-1" version="1">
      <!-- Accessibility. Mandatory if the StopPlace has more than one level. -->
    </Level>
  </levels>
  <entrances>
    <!-- Accessibility. -->
    <Entrance id="ch:1:entrance:7000:1" version="1">
      <!-- Accessibility. -->
    </Entrance>
  </entrances>
  <equipmentPlaces>
    <!-- Accessibility. TODO -->
  </equipmentPlaces>
  <placeEquipments>
    <!-- Accessibility. TODO -->
  </placeEquipments>
  <localServices>
    <!-- Accessibility. -->
    <AssistanceServiceRef ref="generated" version="1">
      <!-- Accessibility. -->
    </AssistanceServiceRef>
  </localServices>
  <StopPlaceType>railStation</StopPlaceType>
  <LimitedUse>interchangeOnly</LimitedUse>
  <Weighting>preferredInterchange</Weighting>
  <quays>
    <Quay id="ch:1:sloid:7000:5:9" version="1"/>
  </quays>
  <accessSpaces>
    <!-- Accessibility. -->
    <AccessSpace id="ch:1:accessspace:7000:1" version="1">
      <!-- Accessibility. -->
    </AccessSpace>
  </accessSpaces>
</StopPlace>
```



*→ [Template](./templates/StopPlace_withAccessibility.xml)*


---
---


**TEMPLATES FOR THIS DOCUMENT**


## NewElementX
*→ [Glossary definition](A4_annex_glossary.md#accessibilityassessment)* TODO

### Purpose
...


### Table



*Table: AccessibilityAssessment*

| Sub | Element | Usage | Card | Type | Description | Note |
|-----|---------|-------|------|------|-------------|------|
|  | MobilityImpairedAccess | mandatory | 1..1 | LimitationStatusEnumeration | Summary indication as to whether the component is considered to be accessible or not. | Accessibility. Overall assessment for mobility and sensory impaired users. partial means that there must exist AccessibiltyAssessment at lower levels like Quays or other elements. Some Quays may not be accessible if partial is used on the StoPlace. |
|  | limitations | expected | 0..1 | usageParameters_RelStructure | The ACCESSIBILITY LIMITATION that apply to component. | Accessibility. Limitations can be omitted if MobilityImpairedaccess is set to true and no additional information needs to be conveyed. |
| + | AccessibilityLimitation | mandatory | 0..* | AccessibilityLimitation_VersionedChildStructure | Assessment of the accessibility of a SITE. | Accessibility. |
| ++ | WheelchairAccess | mandatory | 1..1 | LimitationStatusEnumeration | Whether a PLACE is wheelchair accessible. | Accessibility. |
| ++ | StepFreeAccess | expected | 0..1 | LimitationStatusEnumeration | Whether a PLACE has step free access. | Accessibility. If absent the value `unknown` is assumed. Allowed values: true, false, partial, unknown. |
| ++ | StairFreeAccess | expected | 0..1 | LimitationStatusEnumeration | Whether a PLACE has stair free access, in comparison with step free access one single step in the route is allowed. +v2.0 | Accessibility. Not mandatory in EPIAP, but very useful for perambulators, assisted wheelchairs, bicycles, heavy luggage. Allowed values: true, false, partial, unknown. |
| ++ | RampFreeAccess | expected | 0..1 | LimitationStatusEnumeration | Whether a PLACE has ramp free access. Ramp free isn't necessary absolute. If a ramp is not steep, then a PLACE can still be considered ramp free. | Accessibility. Reachable without steep ramps, stairs, or steps. Allowed values: true, false, partial, unknown. |
| ++ | GuideDogAccess | expected | 0..1 | LimitationStatusEnumeration | Whether a PLACE allows guide dog access. | Accessibility. If absent the value `unknown` is assumed. Allowed values: true, false, partial, unknown. |
| ++ | TactileGuidanceAvailable | expected | 0..1 | LimitationStatusEnumeration | Whether a PLACE has tactile guidance. | Accessibility. Whether the object has tactileGuidance (for the visually impaired). If absent the value `unknown` is assumed. Allowed values: true, false, partial, unknown. |
| ++ | VisualSignsAvailable | expected | 0..1 | LimitationStatusEnumeration | Whether a PLACE has visual signals for the hearing impaired. | Accessibility. If absent the value `unknown` is assumed. Allowed values: true, false, partial, unknown. |
| ++ | LevelAccessIntoVehicle | expected | 0..1 | LimitationStatusEnumeration | Whether the platform is high enough and gap is small enough for level access into vehicle. At least at a designated wheelchair door position the gap between platform and vehicle floor (of level access vehicle) does not exceed 75 mm measured horizontally and 50 mm measured vertically including sliding step (according to PRM TSI). | Accessibility. Whether the platform is high enough and gap is small enough for level access to vehicle. If absent the value `unknown` is assumed. Allowed values: true, false, partial, unknown. |




*→ [General NeTEx definition ](../xcore/netex/elements/AccessibilityAssessment.html)*

### Example


```xml
<?xml version="1.0" encoding="UTF-8"?>
<AccessibilityAssessment id="generated" version="1">
  <MobilityImpairedAccess>true
    <!-- Accessibility. Overall assessment for mobility and sensory impaired users. partial means that there must exist AccessibiltyAssessment at lower levels like Quays or other elements. Some Quays may not be accessible if partial is used on the StoPlace. -->
  </MobilityImpairedAccess>
  <limitations>
    <!-- Accessibility. Limitations can be omitted if MobilityImpairedaccess is set to true and no additional information needs to be conveyed. -->
    <AccessibilityLimitation>
      <!-- Accessibility. -->
      <WheelchairAccess>true
        <!-- Accessibility. -->
      </WheelchairAccess>
      <StepFreeAccess>true
        <!-- Accessibility. If absent the value `unknown` is assumed. Allowed values: true, false, partial, unknown. -->
      </StepFreeAccess>
      <StairFreeAccess>true
        <!-- Accessibility. Not mandatory in EPIAP, but very useful for perambulators, assisted wheelchairs, bicycles, heavy luggage. Allowed values: true, false, partial, unknown. -->
      </StairFreeAccess>
      <RampFreeAccess>true
        <!-- Accessibility. Reachable without steep ramps, stairs, or steps. Allowed values: true, false, partial, unknown. -->
      </RampFreeAccess>
      <GuideDogAccess>true
        <!-- Accessibility. If absent the value `unknown` is assumed. Allowed values: true, false, partial, unknown. -->
      </GuideDogAccess>
      <TactileGuidanceAvailable>true
        <!-- Accessibility. Whether the object has tactileGuidance (for the visually impaired). If absent the value `unknown` is assumed. Allowed values: true, false, partial, unknown. -->
      </TactileGuidanceAvailable>
      <VisualSignsAvailable>true
        <!-- Accessibility. If absent the value `unknown` is assumed. Allowed values: true, false, partial, unknown. -->
      </VisualSignsAvailable>
      <LevelAccessIntoVehicle>true
        <!-- Accessibility. Whether the platform is high enough and gap is small enough for level access to vehicle. If absent the value `unknown` is assumed. Allowed values: true, false, partial, unknown. -->
      </LevelAccessIntoVehicle>
    </AccessibilityLimitation>
  </limitations>
</AccessibilityAssessment>
```



*→ [Template](./templates/AccessibilityAssessment.xml)*


## ExistingElementY - the Additional Elements



### Table



*Table: StopPlace*

| Sub | Element | Usage | Card | Type | Description | Note |
|-----|---------|-------|------|------|-------------|------|
|  | [AccessibilityAssessment](./tables/AccessibilityAssessment.md) | mandatory | 0..1 | AccessibilityAssessment_VersionedChildStructure | Assessment of the accessibility of a SITE. | Accessibility. |
|  | Covered | expected | 0..1 | CoveredEnumeration | Whether the component is Indoors or outdoors. Default is Indoors. | Accessibility. |
|  | AllAreasWheelchairAccessible | mandatory | 0..1 | xsd:boolean | Whether all areas of the component are wheelchair accessible. | Accessibility. |
|  | facilities | expected | 0..1 | serviceFacilitySets_RelStructure | FACILITies available associated with LINE. It is always recommended to also model accessibility relevant things as equipment on the VEHICLE and physical elements, if real-time information is needed. | Accessibility. |
| + | SiteFacilitySet | optional | 1..* | SiteFacilitySetStructure | Set of enumerated FACILITY values that are relevant to a SITE (names based on TPEG classifications, augmented with UIC etc.). | Accessibility. |
| + | SiteFacilitySetRef | optional | 0..* | SiteFacilitySetRefStructure | Reference to a SITE FACILITY SET. | Accessibility. TODO: EPIAP wants the SiteFacilitySets being defined here, referernces may be wrong. |
|  | levels | expected | 0..1 | levels_RelStructure | LEVELs found within SITe. | Accessibility. Mandatory if the StopPlace has more than one level. |
| + | [Level](./tables/Level.md) | expected | 0..* | Level_VersionStructure | Level of a Building or SITE. | Accessibility. Mandatory if the StopPlace has more than one level. |
| + | [Level](./tables/Level.md) | expected | 0..* | Level_VersionStructure | Level of a Building or SITE. | Accessibility. Mandatory if the StopPlace has more than one level. |
|  | entrances | expected | 0..1 | pointOfInterestEntrances_RelStructure | ENTRANCEs to and within SITE. | Accessibility. |
| + | [Entrance](./tables/Entrance.md) | expected | 0..* | SiteEntrance_VersionStructure | Entrance to a SITE. | Accessibility. |
|  | equipmentPlaces | optional | 0..1 | equipmentPlaces_RelStructure | EQUIPMENT PLACEs within SITE COMPONENT. | Accessibility. TODO |
|  | placeEquipments | optional | 0..1 | placeEquipments_RelStructure | Items of fixed EQUIPMENT that may be located in places within the SITE ELEMENT. | Accessibility. TODO |
|  | localServices | expected | 0..1 | localServices_RelStructure | LOCAL SERVICEs that may be located in PLACEs within the SITE ELEMENT. | Accessibility. |
| + | AssistanceServiceRef | optional | 0..* | AssistanceServiceRefStructure | Identifier of an ASSISTANCE SERVICE. | Accessibility. |
|  | accessSpaces | expected | 0..1 | accessSpaces_RelStructure | ACCESS SPACEs within the STOP PLACE. | Accessibility. |
| + | [AccessSpace](./tables/AccessSpace.md) | expected | 0..* | AccessSpace_VersionStructure | An area within a STOP PLACE that does not give direct access to transport vehicles. May be connected to QUAYS by PATH LINKs. | Accessibility. |





### Example


```xml
<?xml version="1.0" encoding="UTF-8"?>
<StopPlace id="ch:1:sloid:7000" version="1">
  <ValidBetween>
    <FromDate>2025-12-14T00:00:00</FromDate>
    <ToDate>2026-12-12T23:59:59</ToDate>
  </ValidBetween>
  <keyList>
    <KeyValue>
      <Key>HafasPriority</Key>
      <Value>4</Value>
    </KeyValue>
    <KeyValue>
      <Key>HafasKMInfo</Key>
      <Value>1000</Value>
    </KeyValue>
  </keyList>
  <privateCodes>
    <PrivateCode type="didok">7000</PrivateCode>
    <PrivateCode type="sloid">ch:1:sloid:7000</PrivateCode>
  </privateCodes>
  <Name>Bern</Name>
  <ShortName/>
  <PrivateCode/>
  <Centroid>
    <Name/>
    <Location>
      <Longitude>7.43913088992</Longitude>
      <Latitude>46.94883228914</Latitude>
      <Altitude>540.2</Altitude>
    </Location>
  </Centroid>
  <AccessibilityAssessment id="generated" version="1">
    <!-- Accessibility. -->
    <MobilityImpairedAccess>true
      <!-- Accessibility. -->
    </MobilityImpairedAccess>
  </AccessibilityAssessment>
  <alternativeNames>
    <AlternativeName id="ch:1:sloid:7000:it" version="1">
      <NameType>alias</NameType>
      <Name lang="it">Berna</Name>
    </AlternativeName>
  </alternativeNames>
  <Covered>covered
    <!-- Accessibility. -->
  </Covered>
  <AllAreasWheelchairAccessible>true
    <!-- Accessibility. -->
  </AllAreasWheelchairAccessible>
  <facilities>
    <!-- Accessibility. -->
    <SiteFacilitySet id="ch:1:sitefacilityset:7000:1" version="1">
      <!-- Accessibility. -->
    </SiteFacilitySet>
    <SiteFacilitySetRef ref="generated" version="1">
      <!-- Accessibility. TODO: EPIAP wants the SiteFacilitySets being defined here, referernces may be wrong. -->
    </SiteFacilitySetRef>
  </facilities>
  <TopographicPlaceRef ref="BE-bern" version="1"/>
  <Locale>
    <TimeZone>Europe/Zurich</TimeZone>
  </Locale>
  <levels>
    <!-- Accessibility. Mandatory if the StopPlace has more than one level. -->
    <Level id="ch:1:level:7000:0" version="1">
      <!-- Accessibility. Mandatory if the StopPlace has more than one level. -->
    </Level>
    <Level id="ch:1:level:7000:-1" version="1">
      <!-- Accessibility. Mandatory if the StopPlace has more than one level. -->
    </Level>
  </levels>
  <entrances>
    <!-- Accessibility. -->
    <Entrance id="ch:1:entrance:7000:1" version="1">
      <!-- Accessibility. -->
    </Entrance>
  </entrances>
  <equipmentPlaces>
    <!-- Accessibility. TODO -->
  </equipmentPlaces>
  <placeEquipments>
    <!-- Accessibility. TODO -->
  </placeEquipments>
  <localServices>
    <!-- Accessibility. -->
    <AssistanceServiceRef ref="generated" version="1">
      <!-- Accessibility. -->
    </AssistanceServiceRef>
  </localServices>
  <StopPlaceType>railStation</StopPlaceType>
  <LimitedUse>interchangeOnly</LimitedUse>
  <Weighting>preferredInterchange</Weighting>
  <quays>
    <Quay id="ch:1:sloid:7000:5:9" version="1"/>
  </quays>
  <accessSpaces>
    <!-- Accessibility. -->
    <AccessSpace id="ch:1:accessspace:7000:1" version="1">
      <!-- Accessibility. -->
    </AccessSpace>
  </accessSpaces>
</StopPlace>
```



*→ [Template](./templates/StopPlace_withAccessibility.xml)*



