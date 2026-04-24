# Transfers

## Mapping between HRDF and NeTEx 

The following table shows how we will map HRDF tables into NeTEX.

| HRDF     | NeTEx RG1         | NeTEx RG2                                                                                                    | Use Case                                   |
|----------|-------------------|--------------------------------------------------------------------------------------------------------------|--------------------------------------------|
| UMSTEIGZ | InterchangeRule   | **InterchangeRule**, alternativ ServiceJourneyInterchange                                                        | Fahrtbezogene Umsteigezeit                 |
| UMSTEIGL | InterchangeRule   | **InterchangeRule**, alternativ ServiceJourneyInterchange                                                        | Linien- und Richtungsbezogene Umsteigezeit |
| UMSTEIGB | DefaultConnection | **DefaultConnection**                                                                                        | Standardumsteigezeit pro Haltestelle       |
| METABHF  | SiteConnection    | **SiteConnection**                                                                                           | Umsteigezeit zwischen Haltestellen         |
| UMSTEIGV | DefaultConnection | **DefaultConnection**                                                                                        | Verwaltungsbezoge Umsteigezeit             |
| DURCHBI  | JourneyMeeting    | **ServiceJourneyInterchange**<br>Alternativ für Flügelzug, Vereinigung: <br>JourneyParts, JourneyPartsCouple<br> | Durchbindung, Flügelzug, Vereinigung       |



**TODO** details from  Powerpoint to be included
## General transfer time between modes
- [Example](../generated/xml-snippet/DefaultConnection_Modes.xml)


## Transfer times at a given StopPlace
**TODO** details from  Powerpoint to be included

- [Example](../generated/xml-snippet/DefaultConnection_UMSTEIGB.xml)


## Operator related transfer times
**TODO** details from  Powerpoint to be included

- [Example](../generated/xml-snippet/DefaultConnection_UMSTEIGV.xml)


## Line and Direction-oriented transfer times
**TODO** details from  Powerpoint to be included

- [Example](../generated/xml-snippet/InterchangeRule_UMSTEIGL.xml)


## ServiceJourney related transfer times
**TODO** details from  Powerpoint to be included

Connection between two services. 

The following situations exist: 
- I.	The connection should not take place. (Prohibition) 
- II.	The connection must take place, and the traveller must change ve-hicles
- III.	The connection has to take place, and the passenger can stay in the vehicle

The differences between the various situations are to be differentiated with the value in some attributes.
**TODO** copy stuff from 10.2

- [Example](../generated/xml-snippet/InterchangeRule_UMSTEIGZ.xml)


## Transfer times between StopPlaces
**TODO** details from  Powerpoint to be included

The differences between the various situations are to be differentiated with the value in some attributes.

- [Example](../generated/xml-snippet/SiteConnection.xml)
