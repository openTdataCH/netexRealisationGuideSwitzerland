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


## StopPlace - the Additional Elements



### Table
- [Swiss profile NeTEx definition](../site/tables/StopPlace_withAccessibility.md)


### Example
- [Example snippet](../site/xml-snippets/StopPlace_withAccessibility.xml)

*→ [Template](./templates/StopPlace_withAccessibility.xml)*


---
---


**TEMPLATES FOR THIS DOCUMENT**


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


## StopPlace - the Additional Elements



### Table
- [Swiss profile NeTEx definition](../site/tables/StopPlace_withAccessibility.md)


### Example
- [Example snippet](../site/xml-snippets/StopPlace_withAccessibility.xml)

*→ [Template](./templates/StopPlace_withAccessibility.xml)*



