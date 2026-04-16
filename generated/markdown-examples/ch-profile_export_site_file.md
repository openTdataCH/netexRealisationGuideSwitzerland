# ch-profile_export_site_file

| Sub | Element | Usage | Card | Type | Description | Note |
|-----|---------|-------|------|------|-------------|------|
|  | PublicationDelivery | mandatory | 1..1 | PublicationDeliveryStructure | A set of NeTEx objects as assembled by a publication request or other service. Provides a general purpose wrapper for NeTEx data content. |  |
| + | PublicationTimestamp | mandatory | 1..1 | xsd:dateTime | Time of output of data. |  |
| + | ParticipantRef | mandatory | 1..1 | siri:ParticipantCodeType | Identifier of system requesting Data. | Use here a distinctive name |
| ++++ | [SiteFrame](SiteFrame.md) | mandatory | 1..1 | None | A coherent set of SITE data to which the same frame VALIDITY CONDITIONs have been assigned. |  |
