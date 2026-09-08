# Annex: Relevant differences between EPIP, EPIAP and the Swiss realisation guide 2.0

Note: The following list is not necessarily comprehensive.
>**LATER** https://github.com/openTdataCH/netexRealisationGuideSwitzerland/blob/main/docs/A2_annex_comparison_EPIP_EPIAP.md

## Main differences

EPIAP describes the following additional elements that need to be considered. 

**AccessibilityAssessment**
* `AccessibilityAssessment` for: 
    * StopPlace 
    * Quay. 
    * Entrance


**Basic Orientation**

* `Level` - mandatory if > 1
* `Entrance`


**Private Mobility**

* `Parking` ?
* `VehicleMeetingPoint` ?


**Path Navigation**

* `SitePathLink` - noch nicht?
* `PathJunction` - noch nicht?
* `AccessSpace` for routing


**Facilities & Equipments**

* `EquipmentPlace` (in Quay, Entrance, StopPlace (indirecty via `AccessSpace`)) 
* `AccessSpace` - rules tbd
* `SiteFacilitySet`, `ServiceFacilitySet`
* `RampEquipment`, `LiftEquipment`, `TicketingEquipment`, `SanitaryEquipment`, `PassengerInformationEquipment` ?


**Service Contacts**

* `Operator` - `ContactDetails`
* `AssistanceService`
* `AssistanceBookingService`


**Vehicles**

* `VehicleType`
    * `equipments`
    * `facilities`
    * `equipmentProfiles` - `VehicleEquipmentProfile`


**Vehicle Stop Interaction**

* `BoardingPosition` in TrainStopAssignment
* `PlatformHeight`, `GapToPlatform`



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
...


### Table
- [Swiss profile NeTEx definition](../site/tables/AccessibilityAssessment.md)

*→ [General NeTEx definition ](../xcore/netex/elements/AccessibilityAssessment.html)*

### Example
- [Example snippet](../site/xml-snippets/AccessibilityAssessment.xml)

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
|`EscalatorFreeAccess`|Reachable without using an escalator.|
|`LiftFreeAccess`|Reachable without using an elevator.|
|`RampFreeAccess`|Reachable without using a ramp that doesn't fit the UN Design [Considerations](https://euc-word-edit.officeapps.live.com/we/wordeditorframe.aspx?ui=nl-nl&rs=nl-nl&wopisrc=https%3A%2F%2Fitxptorg.sharepoint.com%2Fsites%2FEU.DATA4PT.NETEX%2F_vti_bin%2Fwopi.ashx%2Ffiles%2Fc2c9167177c34bc1bb50e4880ff7b6ac&wdenableroaming=1&mscc=1&hid=12869e13-00bf-76bc-9351-10ac590e57c1-730&uiembed=1&uih=teams&uihit=files&hhdr=1&dchat=1&sc=%7B%22pmo%22%3A%22https%3A%2F%2Fteams.microsoft.com%22%2C%22pmshare%22%3Atrue%2C%22surl%22%3A%22%22%2C%22curl%22%3A%22%22%2C%22vurl%22%3A%22%22%2C%22eurl%22%3A%22https%3A%2F%2Fteams.microsoft.com%2Ffiles%2Fapps%2Fcom.microsoft.teams.files%2Ffiles%2F2441637157%2Fopen%3Fagent%3Dpostmessage%26objectUrl%3Dhttps%253A%252F%252Fitxptorg.sharepoint.com%252Fsites%252FEU.DATA4PT.NETEX%252FShared%2520Documents%252FGeneral%252FCEN_Accessibility_Profile%252F20210326%2520PrTS%252016614-6.docx%26fileId%3Dc2c91671-77c3-4bc1-bb50-e4880ff7b6ac%26fileType%3Ddocx%26ctx%3Daggregate%26scenarioId%3D730%26locale%3Dnl-nl%26theme%3Ddefault%26version%3D21100501100%26setting%3Dring.id%3Ageneral%26setting%3DcreatedTime%3A1639152919292%22%7D&wdorigin=TEAMS-ELECTRON.aggregatefiles.aggregate&jsapi=1&jsapiver=v1&newsession=1&corrid=ce9d3917-7c65-4632-a7d4-9644eb2f8575&usid=ce9d3917-7c65-4632-a7d4-9644eb2f8575&sftc=1&sams=1&accloop=1&sdr=6&scnd=1&sat=1&hbcv=1&htv=1&hodflp=1&instantedit=1&wopicomplete=1&wdredirectionreason=Unified_SingleFlush&rct=Medium&ctp=LeastProtected#_ftn1) (for instance, because they are too steep or a landing is missing in case of a ramp of more than 10 m). [[1]](https://euc-word-edit.officeapps.live.com/we/wordeditorframe.aspx?ui=nl-nl&rs=nl-nl&wopisrc=https%3A%2F%2Fitxptorg.sharepoint.com%2Fsites%2FEU.DATA4PT.NETEX%2F_vti_bin%2Fwopi.ashx%2Ffiles%2Fc2c9167177c34bc1bb50e4880ff7b6ac&wdenableroaming=1&mscc=1&hid=12869e13-00bf-76bc-9351-10ac590e57c1-730&uiembed=1&uih=teams&uihit=files&hhdr=1&dchat=1&sc=%7B%22pmo%22%3A%22https%3A%2F%2Fteams.microsoft.com%22%2C%22pmshare%22%3Atrue%2C%22surl%22%3A%22%22%2C%22curl%22%3A%22%22%2C%22vurl%22%3A%22%22%2C%22eurl%22%3A%22https%3A%2F%2Fteams.microsoft.com%2Ffiles%2Fapps%2Fcom.microsoft.teams.files%2Ffiles%2F2441637157%2Fopen%3Fagent%3Dpostmessage%26objectUrl%3Dhttps%253A%252F%252Fitxptorg.sharepoint.com%252Fsites%252FEU.DATA4PT.NETEX%252FShared%2520Documents%252FGeneral%252FCEN_Accessibility_Profile%252F20210326%2520PrTS%252016614-6.docx%26fileId%3Dc2c91671-77c3-4bc1-bb50-e4880ff7b6ac%26fileType%3Ddocx%26ctx%3Daggregate%26scenarioId%3D730%26locale%3Dnl-nl%26theme%3Ddefault%26version%3D21100501100%26setting%3Dring.id%3Ageneral%26setting%3DcreatedTime%3A1639152919292%22%7D&wdorigin=TEAMS-ELECTRON.aggregatefiles.aggregate&jsapi=1&jsapiver=v1&newsession=1&corrid=ce9d3917-7c65-4632-a7d4-9644eb2f8575&usid=ce9d3917-7c65-4632-a7d4-9644eb2f8575&sftc=1&sams=1&accloop=1&sdr=6&scnd=1&sat=1&hbcv=1&htv=1&hodflp=1&instantedit=1&wopicomplete=1&wdredirectionreason=Unified_SingleFlush&rct=Medium&ctp=LeastProtected#_ftnref1) [https://www.un.org/esa/socdev/enable/designm/AD2-01.htm](https://www.un.org/esa/socdev/enable/designm/AD2-01.htm)|
|`AudibleSignalsAvailable`|Whether audible signals for the visually impaired are present.|
|`VisualSignsAvailable`|PRM TSI: visual information as signposting, pictograms and dynamic information.|
|`TactileGuidanceAvailable`|Whether the object has tactile guidance (for the visually impaired). If absent assume `unknown`.<br>PRM TSI: obstacle-free route to each Quay for the visually impaired passengers equipped with tactile information.  <br>For bus- and tram stops:  <br>1.  Groundsurfaceindicator (at location first door) and/or full-length guideline (for boarding at all entrances)<br>2.   Tactile guideline or boarding position connected to (natural) guideline in environment|

#### Remarks `RampFreeAccess`

* Note that `RampFreeAccess` may very well include ramps - provided their slopes are only moderate.
* It seems obvious that `RampFreeAccess`should also include `StairFreeAccess` and `StepFreeAccess` - this isn't explicitely stated in EPIAP, however. 
* `RampFreeAccess`is thus a stronger form of `WheelchairAccess` excluding steeper slopes.


#### Lifts, Entrances - OPEN QUESTIONS

If, e.g., `WheelchairAccess` or `StairFreeAccess` requires using a lift, this information cannot easily be conveyed. It would, however, be of interest: requires more time, knowing the location(s) might be helpful. Do we need navigation paths?

According to EPIAP definitions, a quay has, e.g., `WheelchairAccess` if it is reachable from *any* entrance. It may be that `WheelchairAccess` only works from a secondary entrance, not from the main entrance. Should we be able to express such situations?


## StopPlace - the Additional Elements



### Table
- [Swiss profile NeTEx definition](../site/tables/StopPlace_withAccessibility.md)


### Example
- [Example snippet](../site/xml-snippets/StopPlace_withAccessibility.xml)

*→ [Template](./templates/StopPlace_withAccessibility.xml)*


---
---


**TEMPLATES FOR THIS DOCUMENT**


## NewElementX
*→ [Glossary definition](A4_annex_glossary.md#accessibilityassessment)* TODO

### Purpose
...


### Table
- [Swiss profile NeTEx definition](../site/tables/AccessibilityAssessment.md)

*→ [General NeTEx definition ](../xcore/netex/elements/AccessibilityAssessment.html)*

### Example
- [Example snippet](../site/xml-snippets/AccessibilityAssessment.xml)

*→ [Template](./templates/AccessibilityAssessment.xml)*


## ExistingElementY - the Additional Elements



### Table
- [Swiss profile NeTEx definition](../site/tables/StopPlace_withAccessibility.md)


### Example
- [Example snippet](../site/xml-snippets/StopPlace_withAccessibility.xml)

*→ [Template](./templates/StopPlace_withAccessibility.xml)*



