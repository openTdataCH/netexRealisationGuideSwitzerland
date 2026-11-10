# FlexibleStopPlace

Service area (Bediengebiet) of a demand responsive service of type 3 (corridor), 4 or 5 (area-wide). Delivered in SITE_OFFER. Linked to the timetable by a FlexibleStopAssignment in the ServiceFrame. See uc16_drt.

*Table: FlexibleStopPlace*

| Sub | Element | Usage | Card | Type | Description | Note |
|-----|---------|-------|------|------|-------------|------|
|  | @id | mandatory | 1..1 | xsd:string | Attribute id | |
|  | @version | mandatory | 1..1 | xsd:string | Attribute version | |
|  | Name | expected | 0..1 | MultilingualString | Name of STOP PLACE. |  |
|  | ShortName | optional | 0..1 | MultilingualString | Name of STOP PLACE. |  |
|  | TransportMode | optional | 0..1 | AllPublicTransportModesEnumeration | Primary PT MODE. |  |
|  | areas | mandatory | 0..1 | parkingAreaRefs_RelStructure | Areas in FLEXIBLE STOP PLACE. |  |
| + | FlexibleArea | mandatory | 0..* | FlexibleArea_VersionStructure | Specialisation of a FLEXIBLE QUAY (which is abstract) to identify what is the catchment area for a flexible service (so that a stop finder can find the nearest available types of transport). It is a named zone visited by a particular mode of transport. It is part of the SITE data set rather than the service data set, since it can be defined and exists independently of an actual service. | The area itself. HailAndRideArea is not used. |
| ++ | @id | mandatory | 1..1 | xsd:string | Attribute id | |
| ++ | @version | mandatory | 1..1 | xsd:string | Attribute version | |
| ++ | Name | expected | 0..1 | MultilingualString |  |  |
| +++ | @lang | mandatory | 1..1 | xsd:string | Attribute lang | |
| ++ | ShortName | optional | 0..1 | MultilingualString |  |  |
| ++ | members | optional | 0..1 | singleJourneyRefs_RelStructure |  | Collection points (TypeOfPlace drtCollectionPoint) of the area, if the service has any. Omitted for services without fixed stops (type 5). The references point to ScheduledStopPoints, which are not part of SITE_OFFER. Therefore versionRef is used instead of version: with version, the XSD key reference requires the ScheduledStopPoint in the same document. |
| +++ | ScheduledStopPointRef | optional | 0..* | ScheduledStopPointRefStructure | Reference to a SCHEDULED STOP POINT. |  |
| ++ | Polygon | expected | 1..1 | gml:PolygonType |  | Decision: mandatory. Either gml:Polygon or gml:MultiSurface (choice in the XSD), in EPSG:4326. Not checked by the schematron, because the annotations cannot express the choice and do not handle the gml namespace. Coordinates shortened for the template. |
| +++ | exterior | expected | 0..1 | AbstractRingPropertyType | A boundary of a surface consists of a number of rings. In the normal 2D case, one of these rings is distinguished as being the exterior boundary. In a general manifold this is not always possible, in which case all boundaries shall be listed as interior boundaries, and the exterior will be empty. |  |
| ++ | TransportMode | optional | 0..1 | AllPublicTransportModesEnumeration | Primary PT MODE. |  |
| ++ | BoardingUse | optional | 0..1 | boolean | Whether space can be used for boarding or en route to boarding. Default is true. | Default true. |
| ++ | AlightingUse | optional | 0..1 | boolean | Whether space can be used for alighting or en route to boarding. Default is true. | Default true. |
