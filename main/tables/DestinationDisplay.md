# DestinationDisplay

We only allow fully formed content of destinationDisplays

*Table: DestinationDisplay*

| Sub | Element | Usage | Card | Type | Description | Note |
|-----|---------|-------|------|------|-------------|------|
|  | @id | mandatory | 1..1 | xsd:string | Attribute id | |
|  | @version | mandatory | 1..1 | xsd:string | Attribute version | |
|  | Name | mandatory | 0..* | MultilingualString | Name of Traveller | Is always language neutral. The data is taken from the Des-tination or from the reference in *R (HRDF). If DURCHBI is used then the destination display shows the final destination. |
| + | @lang | mandatory | 1..1 | xsd:string | Attribute lang | |
|  | DriverDisplayText | optional | 0..1 | MultilingualString | Text to show to Driver or Staff for the DESTINATION DISPLAY. | Text to display to DRIVER. |
