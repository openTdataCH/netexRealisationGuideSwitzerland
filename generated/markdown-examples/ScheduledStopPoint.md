# ScheduledStopPoint

| Sub | Element | Usage | Card | Type | Description | Note |
|-----|---------|-------|------|------|-------------|------|
| + | ScheduledStopPoint | mandatory | 1..1 | unknown | A POINT where passengers can board or alight from vehicles. It is open, which hierarchical level such a point has. It can represent a single door (BoardingPosition) or a whole ZONE. The association to the physical model is done with STOP ASSIGNMENTs. | Swiss ScheduledStopPoint are using the sloid in the id, when possible. |
| ++ | keyList | mandatory | 1..1 | KeyListStructure | A list of alternative Key values for an element. |  |
| +++ | KeyValue | mandatory | 1..* | KeyValueStructure | Key value pair for Entity. | We expect a DIDOK key and a SLOID, whereever possible. |
| ++++ | Key | mandatory | 1..1 | xsd:normalizedString | Identifier of value e.g. System. |  |
| ++++ | Value | mandatory | 0..1 | xsd:anyType | Value associated with QUALITY STRUCTURE FACTOR. |  |
| ++ | Name | mandatory | 0..1 | MultilingualString | Name of Traveller | The names are the same in all languages. |
| ++ | ShortName | mandatory | 0..1 | MultilingualString | Short Name for service | StopPlace : Name of the Place, Quay : ShortName of the Quay |
