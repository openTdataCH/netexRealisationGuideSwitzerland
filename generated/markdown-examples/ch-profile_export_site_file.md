# ch-profile_export_site_file

| Sub | Element | Usage | Card | Type | Description | Note |
|-----|---------|-------|------|------|-------------|------|
|  | PublicationDelivery | mandatory | 1..1 | PublicationDeliveryStructure | A set of NeTEx objects as assembled by a publication request or other service. Provides a general purpose wrapper for NeTEx data content. |  |
| + | ParticipantRef | mandatory | 1..1 | siri:ParticipantCodeType | Use here a distinctive name |  |
| + | PublicationTimestamp | mandatory | 1..1 | xsd:dateTime | Time of output of data. |  |
| ln++++ | [SiteFrame](SiteFrame.md) | mandatory | 1..1 | unknown |  |  |
