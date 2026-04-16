# TimetableFrame

| Sub | Element | Usage | Card | Type | Description | Note |
|-----|---------|-------|------|------|-------------|------|
| + | vehicleJourneys | expected | 0..1 | journeysInFrame_RelStructure | VEHICLE JOURNEYs in frame. | Contains the ServiceJourneys and TemplateServiceJourneys. |
| ++ | [ServiceJourney](ServiceJourney.md) | expected | 1..1 | unknown | A passenger carrying VEHICLE JOURNEY for one specified DAY TYPE. The pattern of working is in principle defined by a SERVICE JOURNEY PATTERN.

The VIEW includes derived ancillary data from referenced entities. | ServiceJourney is used for common Journeys. |
| ++ | [TemplateServiceJourney](TemplateServiceJourney.md) | expected | 1..1 | unknown | A VEHICLE JOURNEY with a set of frequencies that may be used to represent a set of similar journeys differing only by their time of departure. | TemplateServiceJourney is only to be used if a line is serviced at a certain frequency. |
| + | trainNumbers | expected | 0..1 | trainNumbersInFrame_RelStructure | TRAIN NUMBERs in frame. |  |
| ++ | [TrainNumber](TrainNumber.md) | mandatory | 1..1 | unknown | Specification of codes assigned to particular VEHICLE JOURNEYs when operated by TRAINs of COMPOUND TRAINs according to a functional purpose (passenger information, operation follow-up, etc). |  |
| + | serviceFacilitySets | optional | 0..1 | serviceFacilitySetsInFrame_RelStructure | SERVICE FACILITies in frame. |  |
| ++ | [ServiceFacilitySet](ServiceFacilitySet.md) | expected | 1..1 | unknown | Service FACILITY. Set of enumerated FACILITY values (Where available names are based on TPEG classifications, augmented with UIC etc.). |  |
| + | typesOfService | expected | 0..1 | typesOfServiceInFrame_RelStructure | TYPEs of SERVICE in frame. |  |
| ++ | TypeOfService | optional | 1..1 | unknown | Classification of a Service. | This is exactly how the TypeOfService should be defined for Switzerland. Attention: Only once per file. |
| + | journeyMeetings | optional | 0..1 | journeyMeetingViews_RelStructure | JOURNEY MEETINGs for visit. |  |
| ++ | [JourneyMeeting](JourneyMeeting.md) | optional | 1..1 | unknown | A time constraint for one or several SERVICE JOURNEYs fixing interchanges between them and/or an external event (e.g. arrival or departure of a feeder line, opening time of the theatre, etc.). | Check latest policy - InterchangeRule may be the preferred alternative. **TODO** |
| + | interchangeRules | expected | 0..1 | interchangeRules_RelStructure | INTERCHANGE RULEs for visit. |  |
| ++ | [InterchangeRule](InterchangeRule.md) | expected | 1..1 | unknown | Conditions for considering journeys to meet or not to meet, specified indirectly: by a particular MODE, DIRECTION or LINE. Such conditions may alternatively be specified directly, indicating the corresponding services. In this case they are either a SERVICE JOURNEY PATTERN INTERCHANGE or a SERVICE JOURNEY INTERCHANGE. |  |
