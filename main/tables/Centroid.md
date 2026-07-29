# Centroid

Global or national location

*Table: Centroid*

| Sub | Element | Usage | Card | Type | Description | Note |
|-----|---------|-------|------|------|-------------|------|
|  | Name | expected | 0..1 | MultilingualString | STOP PLACEs in frame. | Global or national location |
|  | Location | mandatory | 0..1 | LocationStructure | STOP PLACEs in frame. | Note concerning coordinates - The main coordinates are given as **WSG84**. |
| + | Longitude | mandatory | 0..1 | LongitudeType | STOP PLACEs in frame. |  |
| + | Latitude | mandatory | 0..1 | LatitudeType | STOP PLACEs in frame. |  |
| + | Altitude | optional | 0..1 | AltitudeType | STOP PLACEs in frame. |  |
| + | pos | optional | 0..1 | gml:DirectPositionType | STOP PLACEs in frame. | EPSG:2056 is LV95. We use it in the INFO+ export. |
| ++ | @srsName | mandatory | 1..1 | xsd:string | Attribute srsName | |
