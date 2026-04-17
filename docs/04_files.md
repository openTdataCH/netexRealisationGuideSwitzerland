# Files
The file will be compressed with the ZIP algorithm.

## File sent by data provider to SKI 
We suggest that the partner name consists of the short name of the partner and necessary additions to identify the system. In addition, the number of the timetable period is to be indicat-ed in the name, as well as the date and time of creation of the file

Examples.: "test_zvv_2024_20231112_095217.zip“, "prod_tl_2024_20231114_152836.zip“

The file name must be agreed on between the data provider and SKI.
Also SKI and the data provider have to agree on:
* delivey as network, operator or lines.
* reduced base data or not
* handling of partial deliveries and mixed lines **TODO**

## File sent by SKI to data receivers 
As the quantity of data is very large for a single XML-file, SKI provides the data in several XML files. In addition to the XML files, SKI provides a README file listing the contents of each XML file. 

The name of each XML file is composed of the following information:

The name of each XML file is composed of the following information:

| IT-Environement|	DEV,TEST,INT,PROD	| |
| Format and content of the file |	NETEX_TT |	(Describe the format (NETEX) und the content (TimeTable)) |
| Version |	|	Number of the version of the NeTEx .xsd schema |
| Country	|CHE|ISO code of the country in which the file was produced |
| Provider	|SKI	|Name of the provider|
| Time period	 ||	Time|period of he data |
| Name of Export	|oev-schweiz	|Defines the scope of the timetable data |
| Frame | |	Name des Frame |
| Number | |		Number of the file of a specific frame |
| Total	| |	Number of files of the identical frame |
| Date and Time | |		Datum und Zeit der Produktion des Files Format : YYYYMMDDHHMM |

Example: 
-	test_NETEX_TT_1.10_CHE_SKI_2023_OEV-SCHWEIZ_COMMON_1_1_202301250401.xml
-	OJP-NAP_NETEX_TT_1.10_CHE_SKI_2023_OEV-SCHWEIZ_COMMON_1_1_202301250401.xml

All Files are embedded in a zip-File. The name of the zip-file is composed of the following in-formation:

| IT-Environement	 | DEV,TEST,INT	 | In the production environment, the prefix PROD is not written in the name | 
| Format and content of the file	 | ojp-nap:NETEX_TT	 | Describe the format (NETEX) und the content (TimeTable)  | 
| Version |  | 		Number of the version of the NeTEx .xsd schema | 
| Country	 | CHE	 | ISO code of the country in which the file was produced | 
| Provider	 | SKI	 | Name of the provider | 
| Time period	 |  |  	Time period of he data  | 
| Name of Export	 | oev-schweiz	 | Defines the scope of the timetable data | 
| Number |  | 		Number of the file of a specific frame | 
| Total	 |  | 	Number of files of the identical frame | 
| Date and Time	 |  | 	Datum und Zeit der Produktion des Files Format : YYYYMMDDHHMM | 

Example : 
•	test_ojp-nap_netex_tt_1.10_che_ski_2023_oev-schweiz__1_1_202302010402.zip
•	ojp-nap_netex_tt_1.10_che_ski_2023_oev-schweiz__1_1_202302010402.zip



# Zip structure
We propose different structures:
1. a simple import format that delivers for a line or an operator only the information not already present in ATLAS (basically line, operator or network based)
2. the standardised export format (the whole network with files for minimised export of lines)
3. we will add a base data export for Atlas data (which is derived from 2).

Network for us is always the whole network as defined by the public transport in Switzerland.

The zip file shall contain the following files (with allowed content and explanations). The order of the files in the zip shall be as defined here.
* resources.xml: contain ResourceFrame.xml (must be valid)
* sites.xml: contain SiteFrame, StopPlace, Quay (must be valid)
* services.xml: contain ServiceFrame, Line, (Direction), Organisation (must be valid)
* for each Line there exists a Line_<slnid>.xml:
  * containing a minimal set of the relevant Frames that are needed for validation (e.g. minimal line, no site elements, no passenger stop assignments.
* psa.xml: Contains all PassengerStopAssignments within a xxx (this file alone can't be validated)
* interactions.xml: Contains JourneyMeeting, InterchangeRules etc. this file alone can't be validated)

**TODO** more details needed.    

# Encoding
All data is encoded as UTF-8 without BOM.

# Sender identifier
The URL should contain an id for the sender already.

Beside the sender of the message (system), participants must also identify the environment from wich the message is sent. Both parts are concatenated by a “_”.
Example:
•	`<environment>_<partner system >`

The following examples are the standard environment names used in Switzerland:
* Development:	entw
* Test:	test
* Integration:	inte
* Production:	prod

Other platform identifiers can be used only after mutual agreement. It is not necessary for a partner to have all these environments. However, a mapping between the two involved envi-ronment sets is necessary.

# Data transfer

## Protocols
The data are to be exchanged on a secure FTP. 
- The public transport partners make their files available on a secure FTP
-	Export from SKI will also be provided via https://opentransportdata.swiss/ for down-load.

## Sender identification 
The URL should contain an id for the sender already.

Beside the sender of the message (system), participants must also identify the environment from wich the message is sent. Both parts are concatenated by a “_”.
Example:
-	<environment>_<partner system >

The following examples are the standard environment names used in Switzerland:
- Development:	entw
- Test:	test
- Integration_	inte
- Production:	prod

Other platform identifiers can be used only after mutual agreement. It is not necessary for a partner to have all these environments. However, a mapping between the two involved envi-ronment sets is necessary.

