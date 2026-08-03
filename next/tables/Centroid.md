# Centroid

Global or national location

*Table: Centroid*

| Sub | Element | Usage | Card | Type | Description | Note |
|-----|---------|-------|------|------|-------------|------|
|  | Name | expected | 0..1 | MultilingualString | Name of VALIDITY CONDITION. | Global or national location |
|  | Location | mandatory | 0..1 | LocationStructure | The position of a POINT with a reference to a given LOCATING SYSTEM (e. g. coordinates). | Note concerning coordinates - The main coordinates are given as **WSG84**. |
| + | Longitude | mandatory | 1..1 | LongitudeType | Longitude from Greenwich Meridian. -180 (East) to +180 (West). |  |
| + | Latitude | mandatory | 1..1 | LatitudeType | Latitude from equator. -90 (South) to +90 (North). |  |
| + | Altitude | optional | 0..1 | AltitudeType | Altitude. |  |
| + | pos | optional | 1..1 | gml:DirectPositionType | Direct position instances hold the coordinates for a position within some coordinate reference system (CRS). Since direct positions, as data types, will often be included in larger objects (such as geometry elements) that have references to CRS, the srsName attribute will in general be missing, if this particular direct position is included in a larger element with such a reference to a CRS. In this case, the CRS is implicitly assumed to take on the value of the containing object's CRS. if no srsName attribute is given, the CRS shall be specified as part of the larger context this geometry element is part of, typically a geometric object like a point, curve, etc. | EPSG:2056 is LV95. We use it in the INFO+ export. |
| ++ | @srsName | mandatory | 1..1 | xsd:string | Attribute srsName | |
