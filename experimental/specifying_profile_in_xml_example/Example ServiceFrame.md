
# Example ServiceFrame

Starting point is the XMLmplate for ServiceFrame, see https://github.com/openTdataCH/netexRealisationGuideSwitzerland/blob/main/examples/templates/ServiceFrame.xml

## Comments

- Verschachtelte `forbidden`, Vorschlag: nur oberstes forbidden, Sub-Elemente ohne usage-specs - dann werden die Sub-Elemente nicht angezeigt
- Idee wäre: ch-usage ist obligatorisch, damit Element in Tabelle erscheint
- Attributes, how they could be annotated:
- ```
  <Line id="a swiss line id" version="1" responsibilitySetRef="dsa">
							<!-- ch-ATTR: id ch-usage: mandatory ch-note: "use swiss line id where possible" -->
							<!-- ch-ATTR: responsibilitySetRef ch-usage: mandatory ch-referenced -->
							<!-- ch-usage: mandatory -->
  ```


## Table

This is the table that should correspond to the XML template.

### ServiceFrame

A minimal ServiceFrame must be present in all timetable files. TODO: analyse which part is in the general one.

| Sub        | Element                             | Usage     | Card | Type                                | Description | Note                                                                                            |
| ---------- | ----------------------------------- | --------- | ---- | ----------------------------------- | ----------- | ----------------------------------------------------------------------------------------------- |
| ATTR       | id                                  | mandatory | 1..1 | ServiceFrameIdType                  |             | Can be described with `<!-- ch-ATTR: id ch-usage: mandatory ch-note: "Can be described..." -->` |
|            | directions                          | forbidden | 0..0 |                                     |             | We don't use directions, but only direction type                                                |
|            | lines                               | mandatory | 1..1 |                                     |             | Only Line is used and not FlexibleLine                                                          |
| >>         | Line                                | mandatory | 1..* | Line                                |             |                                                                                                 |
| >> >> ATTR | id                                  | mandatory | 0..1 | LineId                              |             | use swiss line id where possible                                                                |
| >> >> ATTR | responsibilitySetRef                | mandatory | 1..1 | responsibilitySetRef                |             |                                                                                                 |
| >> >>      | Name                                | mandatory | 1..1 | MultilingualString                  |             |                                                                                                 |
| >>         | FlexibleLine                        | forbidden | 0..0 | FlexibleLine                        |             | Not used                                                                                        |
|            | groupsOfLines                       | forbidden | 0..0 |                                     |             | Not used                                                                                        |
|            | destinationDisplays                 | expected  | 0..1 |                                     |             | We only allow fully formed content of destinationDisplays                                       |
| >> <<      | DestinationDisplay                  | expected  | 0..* | DestinationDisplay                  |             | We only allow fully formed content of destinationDisplays                                       |
|            | scheduledStopPoints                 | mandatory | 1..1 | xsd:string                          |             | Swiss ScheduledStopPoint are using the sloid in the id, when possible                           |
| >> <<      | ScheduledStopPoint                  | mandatory | 1..* | ScheduledStopPoint                  |             | TODO full or not                                                                                |
|            | connections                         | expected  | 0..1 |                                     |             |                                                                                                 |
| >>         | Access                              | forbidden | 0..0 | Access                              |             |                                                                                                 |
| >> <<      | SiteConnection                      | optional  | 0..* | SiteConnection                      |             | SiteConnection are used only in the main file and not in timetable files.                       |
| >> <<      | Connection                          | optional  | 0..* | Connection                          |             | Connection is used only used in the site file                                                   |
| >> <<      | DefaultConnection                   | optional  | 0..* | DefaultConnection                   |             | DefaultConnection is only used in the site file                                                 |
|            | stopAssignments                     | optional  | 0..1 |                                     |             |                                                                                                 |
| >> <<      | PassengerStopAssignment             | optional  | 0..* | PassengerStopAssignment             |             | are only ued in a special PSA file in the export.                                               |
| >> <<      | PassengerBoardingPositionAssignment | optional  | 0..* | PassengerBoardingPositionAssignment |             | are only ued in a special PSA file in the export.                                               |
| >> <<      | TrainStopAssignment                 | optional  | 0..* | TrainStopAssignment                 |             | are only ued in a special PSA file in the export.                                               |
| >> <<      | TrainComponentStopAssignment        | optional  | 0..* | TrainComponentStopAssignment        |             | are only ued in a special PSA file in the export.                                               |
| >>         | DeckEntranceAssignment              | forbidden | 0..0 |                                     |             |                                                                                                 |
| >>         | NavigationPathAssignment            | forbidden | 0..0 |                                     |             |                                                                                                 |
|            | notices                             | optional  | 0..1 |                                     |             | notices may be present or not                                                                   |
| >> <<      | Notice                              | mandatory | 1..* |                                     |             | if notices are present, one Notice must be.                                                     |
|            |                                     |           |      |                                     |             |                                                                                                 |


