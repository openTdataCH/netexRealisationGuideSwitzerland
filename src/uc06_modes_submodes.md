# TransportMode
NeTEx defines the physical concept for reusable transport mode. It is normally implemented as a `TransportMode`together with a `XXXSubmode`. Both values are standardised.

List for `AllPublicTransportModesEnumeration`:

 Name          | Description              | Part of the data |
|---------------|--------------------------|-------------------|
| air           | Air                      | n/a               |
| all           | All (wildcard)           | not used          |
| anyMode       | Any Mode (wildcard)      | not used          |
| bus           | Bus                      | yes               |
| cableway      | Cableway                 | yes               |
| coach         | Coach                    | special file      |
| ferry         | Ferry                    | yes               |
| funicular     | Funicular                | yes               |
| intercityRail | Intercity Rail           | not used          |
| lift          | Lift                     | not used          |
| metro         | Metro                    | yes               |
| other         | Other mode               | n/a               |
| rail          | Rail                     | yes               |
| selfDrive     | Self-Drive               | not used          |
| snowAndIce    | Snow and Ice Vehicle     | not used          |
| taxi          | Taxi                     | not used          |
| tram          | Tram                     | yes               |
| trolleyBus    | Trolley Bus              | yes               |
| unknown       | Unknown                  | not used          |
| urbanRail     | Urban Rail               | not used          |
| water         | Water                    | yes               |


In Switzerland the elements were standardised in chapter 6.2 of the ["Übergangsdokument Branchenstandard"](https://www.oev-info.ch/sites/default/files/2025-12/%C3%9Cbergangsdokument.pdf#page=26&zoom=100,91,541)

The [mapping tables](src/examples/media/Mappingtabellen_NeTEx_v2.0.xlsx) contain both transforms as far as we use them. Only use sub modes that are approved in the mapping!

# ProductCategory
The relevant marketing name as defined in 3.15 of the Swiss sector standard is put into the `ProductCategory`. 
["Übergangsdokument Branchenstandard"](https://www.oev-info.ch/sites/default/files/2025-12/%C3%9Cbergangsdokument.pdf#page=176)
