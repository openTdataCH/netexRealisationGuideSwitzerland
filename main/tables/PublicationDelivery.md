# PublicationDelivery

For PublicationDelivery have a good look at how the attributes must be done in the provided examples.

*Table: PublicationDelivery*

| Sub | Element | Usage | Card | Type | Description | Note |
|-----|---------|-------|------|------|-------------|------|
|  | @xmlns | mandatory | 1..1 | xsd:string | Attribute xmlns | |
|  | @xlmns:xsi | mandatory | 1..1 | xsd:string | Attribute xlmns:xsi | |
|  | @version | mandatory | 1..1 | xsd:string | Attribute version | |
|  | @xsi:schemaLocation | mandatory | 1..1 | xsd:string | Attribute xsi:schemaLocation | |
|  | @xmlns:gml | mandatory | 1..1 | xsd:string | Attribute xmlns:gml | |
|  | @xmlns:siri | mandatory | 1..1 | xsd:string | Attribute xmlns:siri | |
|  | PublicationTimestamp | mandatory | 1..1 | xsd:dateTime | Time of output of data. |  |
|  | ParticipantRef | mandatory | 1..1 | siri:ParticipantCodeType | Identifier of system requesting Data. |  |
|  | Description | optional | 0..1 | MultilingualString |  |  |
|  | dataObjects | mandatory | 0..1 | dataObjects |  |  |
| + | [CompositeFrame](CompositeFrame.md) | mandatory | 0..* | unknown |  |  |
