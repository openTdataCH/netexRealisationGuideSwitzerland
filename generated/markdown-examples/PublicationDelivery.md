# PublicationDelivery

| Sub | Element | Usage | Card | Type | Description | Note |
|-----|---------|-------|------|------|-------------|------|
|  | PublicationDelivery | mandatory | 1..1 | PublicationDeliveryStructure | A set of NeTEx objects as assembled by a publication request or other service. Provides a general purpose wrapper for NeTEx data content. |  |
| + | PublicationTimestamp | mandatory | 1..1 | xsd:dateTime | Time of output of data. |  |
| + | ParticipantRef | mandatory | 1..1 | siri:ParticipantCodeType | Identifier of system requesting Data. |  |
| + | dataObjects | mandatory | 0..1 | unknown | NeTEx Entities of any type. |  |
| ++ | [CompositeFrame](CompositeFrame.md) | mandatory | 1..1 | unknown | A container VERSION FRAME that groups a set of content VERSION FRAMsE to which the same VALIDITY CONDITIONs have been assigned. |  |
