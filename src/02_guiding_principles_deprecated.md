# Guiding principles
In providing NeTEx files we will follow some guiding principles.

## Completeness

A delivery must always be complete: 
-	in the time dimension : for the whole timetable year (from December to December), but only one timetable.
-	in the scope of the information exchanged : for all operators and all their lines or sublines — the file must always contain everything.
This allows the receiver to overwrite the old delivery with the new one without loss of data

## Base data
Some reference data are maintained by SKI. These data are identified by business values (Abbreviation, Number, ID, …).
These Business identifiers shall be used by the deliveries to enable their integration and homogenisation for the collection of timetable information. 
If attributes of these reference data are transmitted in the deliveries, SKI does not adopt the values of these attributes. SKI takes these values from the reference system.

The relevant reference data that is already available/defined by SKI:
- Organisations - in Atlas
- StopPlaces, Quays and the whole physical model - in Atlas
- Lines (in a future phase) - in Atlas
- Direction - only inbound and outbound are allowed
- Notices – some specialised IDs and/or types, according to the [mapping excel](media/Mappingtabellen_NeTEx_v2.0.xlsx).
- TypeOfValues - according to the lists defined here (namely in [10_common.md](10_common.md)). E.g. ProductCategory - in the [mappingexcel](media/Mappingtabellen_NeTEx_v2.0.xlsx).
- ValueSets - in [10_common.md](10_common.md)
- Facilities - in [mapping excel](media/Mappingtabellen_NeTEx_v2.0.xlsx).

### Data supplier side
The data provider is responsible for the timely delivery of the complete timetable information with sufficient quality. Complete means all timetable data in the responsibility of the provider for the whole timetable period.

### SKI side
SKI is responsible for the timely delivery of the complete timetable information with sufficient quality of all timetable data for open data and for the consumption by the data consumers.

## Limits to scope
This realisation specification for public transport in Switzerland (NeTEx) is an addition to the official NeTEx standard. It contains the subset of NeTEx possibilities supported by SKI for the passenger information use case.

Beside this document there can be an agreement from SKI with each data provider about more technical and operational details of the delivery of the timetable. In general there are no differences in the implementation to this reference document. Any necessary technical changes need to be discussed with SKI.

## Harmonisation
Our profiles and data will try to converge on the 2028 new European profile, whenever possible.

## Easy for consumption
The data and file structures should allow for easy consumption. We do this by using a profile that adheres as much as possible to the future European profile.
