# Transfers

## Mapping between HRDF and NeTEx 

| HRDF     | NeTEx RG1         | NeTEx RG2                                                                                                    | Use Case                                   |
|----------|-------------------|--------------------------------------------------------------------------------------------------------------|--------------------------------------------|
| UMSTEIGZ | InterchangeRule   | **InterchangeRule**, alternativ ServiceJourneyInterchange                                                        | Fahrtbezogene Umsteigezeit                 |
| UMSTEIGL | InterchangeRule   | **InterchangeRule**, alternativ ServiceJourneyInterchange                                                        | Linien- und Richtungsbezogene Umsteigezeit |
| UMSTEIGB | DefaultConnection | **DefaultConnection**                                                                                        | Standardumsteigezeit pro Haltestelle       |
| METABHF  | SiteConnection    | **SiteConnection**                                                                                           | Umsteigezeit zwischen Haltestellen         |
| UMSTEIGV | DefaultConnection | **DefaultConnection**                                                                                        | Verwaltungsbezoge Umsteigezeit             |
| DURCHBI  | JourneyMeeting    | **ServiceJourneyInterchange**<br>Alternativ für Flügelzug, Vereinigung: <br>JourneyParts, JourneyPartsCouple<br> | Durchbindung, Flügelzug, Vereinigung       |
