# TransportMode
NeTEx definies the physical Model for reusable transport mode. It is normally implemented as a`TransportMode`together with a `XXXSubmode`. Both values area standardised.

List for `TransportModeEnumeration`:

| Name       | Description  | Part of the data |
|------------|--------------|------------------|
| air        | 	Air         | n/a              |
| bus        | 	Bus         | yes              |
| coach      | 	Coach       | special file     |
| funicular  | 	Funicular   | yes              |
| metro      | 	Metro       | yes              |
| rail       | 	Rail        | yes              |
| trolleyBus | 	Trolley Bus | yes              |
| tram       | 	Tram        | yes              |
| water      | 	Water       | yes              |
| cableway   | 	Cableway    | yes              |
| other      | 	Other mode  | n/a              |


In Switzerland the elements were standardised in chapter 6.2 of the ["Übergangsdokument Branchenstandard"](https://www.oev-info.ch/sites/default/files/2025-12/%C3%9Cbergangsdokument.pdf#page=26&zoom=100,91,541)

The [mapping tables](media/Mappingtabellen_NeTEx_v2.0.xls) contain both transforms as far as we use them.

# ProductCategory
The relevant marketing name as defined in 3.15 of the Swiss sector standard is put into the `ProductCategory`.
