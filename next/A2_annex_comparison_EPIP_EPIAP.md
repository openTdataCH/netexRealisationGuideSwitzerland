# Annex: Relevant differences between EPIP, EPIAP and the Swiss realisation guide 2.0

> **NOTE**: The following list is not necessarily comprehensive. 


## Main differences

The following lists aim to give an overview of all elements related to accessibility information as they were defined by EPIP/EPIAP. Most of them are described in the EPIAP document, while a few are documented in greater detail in Part 1 of NeTEx (in particular, various Services and enumerations). 

The elements in ***italics*** are the ones that are part of the Swiss profile. How the Swiss profile covers accessibility is more precisely and extensively documented [here](uc09_accessibility.md).


### AccessibilityAssessment

***AccessibilityAssessment*** for:
- ***StopPlace***
- ***Quay***
- ***StopPlaceEntrance***
- SitePathLink
- ***SanitaryEquipment***
- any SiteElement

### Basic Orientation

***Level*** 
- AccessibilityAssessment
- ***Description***
- ***Name***


Entrance
- EntranceType
- Height 
- IsEntry
- IsExit
- IsExternal 
- Width
- checkConstraints
- placeEquipments

AccessSpace


### Private Mobility

***Parking***
- ***ParkingType***
- ***ParkingUserType***
- ParkingVehicleType
- RechargingAvailable
- PrincipalCapacity
- TotalCapacity
- etc.

VehicleMeetingPoint

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


### Path Navigation

SitePathLink
- AccessFeatureType
- AccessibilityAssessment
- AllAreasWheelchairPassable
- AllowedUse 
- Covered 
- Distance 
- FlooringType 
- Gated 
- Gradient
- LeftSideBorder
- Lighting 
- MinimumWidth 
- NumberOfSteps 
- PassageType 
- PublicUse 
- RightSideBorder
- TactileGuidingStrip 
- TactileWarningStrip 
- TiltAngle 
- TiltType 
- Towards 
- TransferDuration
- Transition
- checks
- placeEquipments

PathLinkEnd
- EntranceRef
- LevelRef
- PlaceRef

PathLinkSequence
- Instruction
- Label
- PathLinkRef
- Reverse

PathJunction
- AllAreasWheelchair
- Covered
- Gated
- Label
- Lighting
- PublicUse
- SiteComponentRef

ConnectionEnd
- MobilityRestrictedTravellerDuration


NavigationPath
- AccessibilityAssessment
- Covered
- Gated
- Lighting
- NavigationType
- TransferDuration


WalkTransferduration (in SiteConnection, DefaultConnection)
- MobilityRestrictedTravellerDuration




### Facilities & Equipments


EquipmentPlace (in Quay, Entrance, StopPlace (indirecty via AccessSpace)


any Site
- ***entrances***
- equipmentPlaces
- ***levels***
- ***localServices***
- ***placeEquipments***


any SiteElement
- AccessibilityAssessment
- Covered
- Gated
- Lighting
- ***facilities***
- etc.


any Equipment
- ***Description***
- Image
- Name
- ***Note***
- OutOfService
- TypeOfEquipmentRef


EquipmentPosition
- Description
- Location
- ReferencePointRef
- XOffset
- YOffset


EntranceEquipment
- AcousticSensor 
- AudioOrVideolntercom 
- AudioPassthroughindicator 
- AutomaticDoor
- Barrier
- GlassDoor
- Door 
- DoorstepMark 
* DropKerbOutside 
- EntranceAttention 
- EntranceRequiresStaffing 
- EntranceRequiresTicket
- KeptOpen 
- NecessaryForceToOpen 
- NumberOfGates 
- RampDoorbell
- RevolvingDoor 
- TurningSpacePosition 
- WheelchairPassable 
- WheelchairTurningCircle
- etc.



EscalatorEquipment
- DogsMustBeCarried
- TactileActuators
- etc.


LiftEquipment
- AudioAnnouncements 
- Automatic
- BrailleButtons
- ButtonsHeight 
- CallButtonHeight
- Depth 
- DirectionButtonHeight 
- ExternalFloorSelection 
- GroundMarkalignedWithButton 
- HandrailHeight 
- HandrailType 
- InternalWidth 
- LowerHandrailHeight 
- MagneticinductionLoop 
- MaximumLoad 
- MirrorOnOppositeSide 
- RaisedButtons 
- ReachedFloorAnnouncement 
- SignageToLift 
- TactileActuators 
- TactileGroundFloorButton 
- WheelchairTurningCircle 
- etc.



RampEquipment
- Gradient
- GradientType
- HandrailHeight
- HandrailType
- Length
- Pedestal
- RestStopDistance
- SafetyEdge



TravelatorEquipment
- Gradient
- TactileActuators
- SafeForGuideDog
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



LuggageLockerEquipment
- BlindAccessible
- WheelchairAccepted
- NumberOfLockers
- etc.


TrolleyStandEquipment
- FreeToUse


PassengerEquipment
- Fixed

PassengerSafetyEquipment
- AcousticAnnouncements
- AcousticAnnouncementsTrigger
- AnnouncementTriggeringMethod
- HeightOfSosPanel
- Lighting
- PanicButton
- SosPanel



***SanitaryEquipment***
- ***AccessibilityAssessment***
- CallButtonAvailable
- DrinkingWater 
- Gender 
- HandWashing
- KeyScheme
- LockedAccess
- Staffing 
- SupportBarHeigth 
- ***ToiletsType*** 
- WheelchairTurningCircle 

***TicketingEquipment*** 
- DisabledPriority 
- HeightOfLowCounter 
- HeightOfMachinelnterface 
- ***InductionLoops*** 
- ***LowCounterAccess*** 
- NumberOfMachines
- ***TactilelnterfaceAvailable*** 
- ***TicketCounter*** 
- ***TicketMachines*** 
- ***WheelchairSuitable*** 


QueingEquipment
- DisabledPriority
- QueingSeatedPossible
- RailedQueue
- TicketedQueue


RubbishDisposalEquipment


TicketValidatorEquipment
- AudioValidationFeedback
- TactileValidationFeedback
- ValidationGuidance
- VisualValidationFeedback


ShelterEquipment
- DistanceFromNearestKerb
- Enclosed


WaitingEquipment
- AirConditioned
- Heated
- Seats
- SmokingAllowed
- StepFree
- WheelchairAreaLength
- WheelchairAreaWidth
- etc.


WaitingRoomEquipment
- Facilities
- TypeOfFareClass


SignEquipment
- AsBraille
- AudioTriggerMethod
- Contrast
- FontSize
- etc.


Accommodation
- AcommodationFacility
- PassengercommsFacilityList
- ToiletFacility


***localServices*** in StopPlace

***AssistanceService***
- AccessibilityTrainedStaff
- ***AssistanceAvailability***
- SafetyFacilityList
- ***etc.***

***AssistanceBookingService***

LostPropertyService

LuggageService
- LuggageMaximalWeigth
- LuggageTrolleys
- WheelchairLuggageTrolleys
- etc.

MeetingPointService
- Label
- MeetingPointType

TicketingService
- MobileDeviceTickets
- OnboardPurchase
- TicketCounterService



***SiteFrame***
- siteFacilitySets

***SiteFacilitySet for***
- ***StopPlace***
- ***Quay***


***SiteFacilitySet***
- ***AccessFacilityList***
- ***AccessibilityInfoFacilityList***
- AccessibilityToolList
- ***AssistanceFacilityList***
- LuggageLockerFacilityList 
- LuggageServiceFacilityList 
- ***MobilityFacilityList***
- SafeteyFacilityList
- ***ParkingFacilityList*** 
- ***SanitaryFacilityList***
- TicketingServiceFacilityList 
- etc.


ServiceFacilitySet
- VehicleAccessFacilityList
- AccommodationFacilityList - pushchair, wheelchair
- LuggageCarriageFacilityList - pushchairsAllowed, cyclesAllowed, etc.
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

VehicleType
- Description
- HasHoist
- HasLiftOrRamp
- Height 
- Length
- LowFloor
- equipments
- facilities
- equipmentProfiles - VehicleEquipmentProfile - WheelchairVehicleEquipment
- PassengerCapacity
	- WheelchairPlaceCapacity
- etc.

PlatformHeight, GapToPlatform

BoardingPosition
- BoardingPositionType
- Label

TrainStopAssignment
- BoardingPositionRef
- EntranceToVehicle
- PassengerStopAssignmentRef
- TrainRef
- TrainComponentRef




## Other noteworthy differences
* EPIAP requires AlternativeText, Swiss profile excludes it



