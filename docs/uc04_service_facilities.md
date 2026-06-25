# Service Facilities

We also address `SiteFacility` here beside `ServiceFacility`.

Facilities are properties of site elements or services / vehicles. 
There is a wide range of things that can be stored there (only first class, Wi-Fi etc.). It is more properties, and we don't say anything about the actual equipment. A restaurant is also a Facility.

We use things from BS KI to be modeled here.

The "Angebote" are represented as Facilitys. For convenience, we also will transfer the am `Notice` in addition to the `FacilitySet`.

A `ServiceJourney` or a `Quay` can have multiple facilities. We therefore prefer to have facilities in elementar and modular elements. This also means that we can use the service attribute (e.g. "1") in the id `"ch:1:ServiceFacilitySet:A___1"`.

We also use this for the `Notice` with the id `ch:1:Notice:A___1"`.


The structures are define here:
* [ServiceFacilitySet](10_common.md#servicefacilityset)
* [SiteFacilitySet](10_common.md#sitefacilityset)
* The actual relevant Facilities are defined in [mapping table for NeTEX 2.0](media/Mappingtabellen_NeTEx_v2.0.xlsx).