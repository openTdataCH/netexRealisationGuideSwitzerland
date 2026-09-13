# Annex: Relevant differences between EPIP, EPIAP and the Swiss realisation guide 2.0

Note: The following list is not necessarily comprehensive.
>**LATER** https://github.com/openTdataCH/netexRealisationGuideSwitzerland/blob/main/docs/A2_annex_comparison_EPIP_EPIAP.md

## Main differences

The following lists aim to give an overviiew of all elements related to accessibility information. Most of them are described in EPIAP, while a few are documented in greater detail in Part 1 of NeTEx (in particular, various Services and enumerations). 

The elements in ***italics*** are the ones that are (tentatively) elected for being included in the Swiss profile. Note that, in contrast, the French profile includes practically the totality of EPIAP. 

TODO Link to profile definition - see "Special Use Cases" - "Accessibility"


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


