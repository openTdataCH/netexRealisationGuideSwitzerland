# Files
* All files are transfered as one zip-file.

## File name for delivery to INFO+
tbd 2.7.1

## File name for export to opentransportdata.swiss
tbd 2.7.1

# Zip structure
The zip file shall contain the following files (with allowed content and explanations). The order of the files in the zip shall be as defined here.

* resources.xml: contain ResourceFrame.xml (must be valid)
* sites.xml: contain SiteFrame, StopPlace, Quay (must be valid)
* services.xml: contain ServiceFrame, Line, (Direction), Organisation (must be valid)
* for each Line there exists a Line_<slnid>.xml:
  * containing a minimal set of the relevant Frames that are needed for validation (e.g. minimal line, no site elements, no passenger stop assignments.
* psa.xml: Contains all PassengerStopAssignments within a xxx (this file alone can't be validated)
* interactions.xml: Contains JourneyMeeting, InterchangeRules etc. this file alone can't be validated)

tbd more details needed.    

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

