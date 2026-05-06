# Centroid

| Sub | Element | Usage | Card | Type | Description | Note |
|-----|---------|-------|------|------|-------------|------|
| + | Location | mandatory | 0..1 | LocationStructure | Absolute location of EQUIPMENT. | Note concerning coordinates - The main coordinates are given as **WSG84**. - The Swiss coordinates are added as well if available. (**TODO** How?)- INFO+ will not use the data from the import, instead DIDOK master data will be used for all Swiss coordinates. INFO+ will use the data of foreign places. |
| ++ | Longitude | mandatory | 1..1 | LongitudeType | Longitude from Greenwich Meridian. -180 (East) to +180 (West). |  |
| ++ | Latitude | mandatory | 1..1 | LatitudeType | Latitude from equator. -90 (South) to +90 (North). |  |
| ++ | Altitude | optional | 0..1 | AltitudeType | Altitude. |  |
