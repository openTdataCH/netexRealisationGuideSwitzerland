# TrainNumber

The TrainNumber are currently a maximum of 6 digits long. TrainNumber for advertisment und production are identical. It is the number from *Z in HRDF. Must be unique per operating day in Switzerland.

*Table: TrainNumber*

| Sub | Element | Usage | Card | Type | Description | Note |
|-----|---------|-------|------|------|-------------|------|
|  | @id | mandatory | 1..1 | xsd:string | Attribute id | |
|  | @version | mandatory | 1..1 | xsd:string | Attribute version | |
|  | ForAdvertisement | expected | 0..1 | xsd:normalizedString | A coherent set of timetable data (VEHICLE JOURNEYs and BLOCKs) to which the same VALIDITY CONDITIONs have been assigned. | TrainNumber to use for advertisement to public. Use if different from ID. |
|  | ForProduction | optional | 0..1 | xsd:normalizedString | A coherent set of timetable data (VEHICLE JOURNEYs and BLOCKs) to which the same VALIDITY CONDITIONs have been assigned. | TrainNumber to use for production purposes, for instance towards technical systems that require an odd or even value according to safety regulations. Use iff different from ID. |
