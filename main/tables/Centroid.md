# Centroid

Global or national location

*Table: Centroid*

| Sub | Element | Usage | Card | Type | Description | Note |
|-----|---------|-------|------|------|-------------|------|
|  | Name | expected | 0..1 | MultilingualString | STOP PLACEs in frame. | Global or national location |
|  | Location | mandatory | 0..1 | LocationStructure | STOP PLACEs in frame. | Note concerning coordinates - The main coordinates are given as **WSG84**. |
| + | Longitude | mandatory | 1..1 | LongitudeType | Longitude from Greenwich Meridian. -180 (West) to +180 (East). Decimal degrees. eg 2.356 |  |
| + | Latitude | mandatory | 1..1 | LatitudeType | Latitude from equator. -90 (South) to +90 (North). Decimal degrees. eg 56.356 |  |
| + | Altitude | optional | 0..1 | AltitudeType | Altitude (metres) Above sea level. |  |
| + | pos | optional | 0..1 | gml:DirectPositionType |  | EPSG:2056 is LV95. We use it in the INFO+ export. |
| ++ | @srsName | mandatory | 1..1 | xsd:string | Attribute srsName | |
