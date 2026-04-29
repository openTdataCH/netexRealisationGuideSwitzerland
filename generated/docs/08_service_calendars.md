# Service calendars
(NeTEx-1, 7.7.5)
The Calendar elements are grouped in a SERVICE CALENDAR FRAME. This allows the same SERVICE CALENDAR to be shared with many other functional frames (especially TIMETABLE FRAMEs), and for a given functional frame to be used with different SERVICE CALENDARs just by changing the SERVICE CALENDAR FRAME associated with it.

See the following class diagram for the most important objects of the SERVICE CALENDAR FRAME and their relationships to the other frames.
![Full service calendar structure](media/ServiceCalendarFrame_structure.png)
Note that VALIDITY CONDITIONs could be combined and ANDed (all the conditions must be fullfiled at the same time) thanks to the WITH CONDITION REF attribute. We will work with FromDate/ToDate and ValidDayBits of AvailabilityCondition only.
![Structure service calendar frame](media/ServiceCalendarFrame_2_structure.png)




| Sub | Element | Usage | Card | Type | Description | Note |
|-----|---------|-------|------|------|-------------|------|
|  | ServiceCalendarFrame | expected | 1..1 | unknown | A SERVICE CALENDAR. A coherent set of OPERATING DAYS and DAY TYPES comprising a Calendar. That may be used to state the temporal VALIDITY of other NeTEx entities such as Timetables, STOP PLACEs, etc. Covers a PERIOD with a collection of assignments of OPERATING DAYS to DAY TYPES. | A minimal ServiceCalendarFrame must be present in all timetable files. |
| + | validityConditions | mandatory | 1..1 | validityConditions_RelStructure | VALIDITY CONDITIONs conditioning entity. |  |
| ++ | [AvailabilityCondition](AvailabilityCondition.md) | mandatory | 1..1 | unknown | VALIDITY CONDITION stated in terms of DAY TYPES and PROPERTIES OF DAYs. |  |
| + | [ServiceCalendar](ServiceCalendar.md) | expected | 1..1 | unknown | A SERVICE CALENDAR. A collection of DAY TYPE ASSIGNMENTs. |  |
| + | dayTypes | optional | 0..1 | unknown | DAY TYPEs for BLOCK. |  |
| ++ | [DayType](DayType.md) | optional | 1..1 | unknown | A type of day characterized by one or more properties which affect public transport operation. For example: weekday in school holidays. |  |
| + | timebands | expected | 0..1 | timebandRefs_RelStructure | TIMEBANDS associated with JOURNEY FREQUENCY GROUP. |  |
| ++ | Timeband | expected | 1..1 | unknown | A period in a day, significant for some aspect of public transport, e.g. similar traffic conditions or fare category. |  |




```xml
<?xml version="1.0" encoding="UTF-8"?>
<ServiceCalendarFrame  id="ch:1:ServiceCalendarFrame" version="1">
  <!-- A minimal ServiceCalendarFrame must be present in all timetable files. -->
  <validityConditions>
    <AvailabilityCondition id="ch:1:AvailabilityCondition:b7" version="1"/>
  </validityConditions>
  <ServiceCalendar id="ch:1:ServiceCalendar:j23" version="1"/>
  <dayTypes>
    <DayType id="ch:1:DayType:ycy10_1" version="1"/>
  </dayTypes>
  <timebands>
    <Timeband id="ch:1:Timeband:1140:1260" version="1"/>
  </timebands>
</ServiceCalendarFrame>

```


- [General NeTEx definition](../generated/xcore/ServiceCalendarFrame.html)

## AvailabilityCondition
(NeTEx-1 7.7.6)
AVAILABILITY CONDITION is a specialisation of VALIDITY CONDITION to specify precise temporal conditions. For example, an ENTRANCE of a STOP PLACE may be valid (it exists) but not available for some of the time (it is closed between 9 pm and 6 am). Both VALIDITY CONDITIONs and AVAILABILITY CONDITIONs may be associated for the same entity.

An AVAILABILITY CONDITION can be defined by specific DAY TYPEs and/or OPERATING DAYs. It may be further qualified by one or more of TIME BANDs. The DATED AVAILABILITY CONDITION being the instance of VALIDITY CONDITION on a specific CALENDAR DAY.

Examples of use of AVAILABILITY CONDITION include ENTRANCEs, EQUIPMENTs, STOP PLACEs, etc.

AvailabilityCondition replaces OperatingDay and OperatingPeriod. Whenever a reference to a VP (“Verkehrsperiode” or operating period in english) is needed, we use an AvailabilityCondi-tionRef:
-	The referenced AvailabilityConditions are centrally stored in the ServiceCalendar-Frame.


The element ValidDayBits directly indicates the days on which some service is provided or not. They are similar to the HRDF bitfields. 

ValidDayBits is required whenever the AvailabilityCondition is of temporal nature (more often than not). Examples include:
-	ServiceJourney
-	JourneyMeeting 
-	NoticeAssignment
-	ServiceFacilitySet
-	ServiceJourneyInterchange
-	InterchangeRule

Hint: The frames TimetableFrame, ServiceFrame and ServiceCalendarFrame and their elements must have the same validity.



| Sub | Element | Usage | Card | Type | Description | Note |
|-----|---------|-------|------|------|-------------|------|
| + | FromDate | optional | 0..1 | xsd:dateTime | Start date of AVAILABILITY CONDITION. | Is equal to the start date of the timetable year or, more generally, the period in which the ValidDayBits apply. |
| + | ToDate | optional | 0..1 | xsd:dateTime | End of AVAILABILITY CONDITION. Date is INCLUSIVE. | Is equal to the end date of the timetable year or, more generally, the period in which the ValidDayBits apply. |
| + | ValidDayBits | mandatory | 0..1 | xsd:normalizedString | For UIC style encoding of day types String of bits, one for each day in period: whether valid or not valid on the day. Normally there will be a bit for every day between start and end date. If bit is missing, assume available. |  |
| + | timebands | optional | 0..1 | timebandRefs_RelStructure | TIMEBANDS associated with JOURNEY FREQUENCY GROUP. | Can also be referenced |
| ++ | [Timeband](Timeband.md) | optional | 1..1 | unknown | A period in a day, significant for some aspect of public transport, e.g. similar traffic conditions or fare category. |  |
| ++ | TimebandRef | optional | 1..1 | TimebandRefStructure | Reference to a TIME BAND. |  |




```xml
<?xml version="1.0" encoding="UTF-8"?>
<AvailabilityCondition  id="generated" version="1">
  <FromDate>2026-05-17T00:00:00Z</FromDate>
  <!-- Is equal to the start date of the timetable year or, more generally, the period in which the ValidDayBits apply. -->
  <ToDate>2026-05-17T00:00:00Z</ToDate>
  <!-- Is equal to the end date of the timetable year or, more generally, the period in which the ValidDayBits apply. -->
  <ValidDayBits>01010010111</ValidDayBits>
  <timebands>
    <!-- Can also be referenced -->
    <Timeband id="ch:1:Timeband:4937" version="1">
      <StartTime>06:00:00</StartTime>
      <EndTime>06:01:00</EndTime>
    </Timeband>
    <TimebandRef ref="ch:1:Timeband:4937-2" version="1"/>
  </timebands>
</AvailabilityCondition>

```


- [General NeTEx definition](../generated/xcore/AvailabilityCondition.html)

## ServiceCalendar
(NeTEx-1, 7.7.5.5.1.
The transport offering of a public transport company is tailored to accommodate different lev-els of demand. In order to simplify the supply planning almost all operators design their pro-duction plan using a classification by type of day, which summarises the level of demand or other characteristics: for example, workday, weekend, school holiday, market day,etc. Long-term planned schedules are designed through the so-called transportation calendar, in which calendar days are classified as specific DAY TYPEs.



| Sub | Element | Usage | Card | Type | Description | Note |
|-----|---------|-------|------|------|-------------|------|
|  | ServiceCalendar | expected | 1..1 | unknown | A SERVICE CALENDAR. A collection of DAY TYPE ASSIGNMENTs. |  |
| + | Name | mandatory | 0..1 | MultilingualString | Name of Traveller | timetable year |
| + | FromDate | mandatory | 0..1 | xsd:dateTime | Start date of AVAILABILITY CONDITION. | Beginning of timetable year |
| + | ToDate | mandatory | 0..1 | xsd:dateTime | End of AVAILABILITY CONDITION. Date is INCLUSIVE. | End of timetable year |




```xml
<?xml version="1.0" encoding="UTF-8"?>
<ServiceCalendar  id="ch:1:ServiceCalendar:j23" version="1">
  <Name>Fahrplan 2018</Name>
  <!-- timetable year -->
  <FromDate>2017-12-10</FromDate>
  <!-- Beginning of timetable year -->
  <ToDate>2018-12-08</ToDate>
  <!-- End of timetable year -->
</ServiceCalendar>

```


- [General NeTEx definition](../generated/xcore/ServiceCalendar.html)

## DayType
(NeTEx-1, 7.7.5.5.2)
In Transmodel, a DAY TYPE is defined as a combination of various different properties a day may have, and which will influence the transport demand and the running conditions. 
The day type is used to describe the validity of the holidays in Switzerland. Each day is de-scripted with a day Type. 



| Sub | Element | Usage | Card | Type | Description | Note |
|-----|---------|-------|------|------|-------------|------|
|  | DayType | optional | 1..1 | unknown | A type of day characterized by one or more properties which affect public transport operation. For example: weekday in school holidays. | In Switzerland only used for holidays and the like |
| + | alternativeTexts | expected | 0..1 | alternativeTexts_RelStructure | Additional Translations of text elements. |  |
| ++ | AlternativeText | mandatory | 1..1 | unknown | Alternative Text. +v1.1 |  |
| +++ | Text | mandatory | 0..1 | MultilingualString | Text content of NOTICe. |  |
| + | Name | mandatory | 0..1 | MultilingualString | Name of Traveller |  |
| + | properties | expected | 0..1 | propertiesOfDay_RelStructure | Properties of the DAY TYPE. |  |
| ++ | PropertyOfDay | mandatory | 1..1 | unknown | A property which a day may possess, such as school holiday, weekday, summer, winter etc. | Holidays only |
| +++ | HolidayTypes | expected | 0..1 | HolidayTypesListOfEnumerations | Type of holiday. Default is Any day. |  |
| +++ | DayEvent | optional | 0..1 | DayEventEnumeration | Events happening on day. |  |




```xml
<?xml version="1.0" encoding="UTF-8"?>
<DayType  id="ch:1:DayType:Bundesfeier" version="1">
  <!-- In Switzerland only used for holidays and the like -->
  <alternativeTexts>
    <AlternativeText attributeName="Name">
      <Text lang="it">Festa nazionale</Text>
    </AlternativeText>
    <AlternativeText attributeName="Name">
      <Text lang="en">National Day</Text>
    </AlternativeText>
    <AlternativeText attributeName="Name">
      <Text lang="fr">Fête nationale</Text>
    </AlternativeText>
  </alternativeTexts>
  <Name>Bundesfeier</Name>
  <properties>
    <PropertyOfDay>
      <!-- Holidays only -->
      <HolidayTypes>NationalHoliday</HolidayTypes>
      <DayEvent>normalDay</DayEvent>
    </PropertyOfDay>
  </properties>
</DayType>

```


- [General NeTEx definition](../generated/xcore/DayType.html)

## Timeband
(NeTEx-1, 7.7.5.5.6)
A period in a day, significant for some aspect of public transport, e.g. similar traffic conditions or fare category.
Currently used for InterchangeRuleTimings, later also used for the opening hours in StopPlace models. 



| Sub | Element | Usage | Card | Type | Description | Note |
|-----|---------|-------|------|------|-------------|------|
|  | DayType | optional | 1..1 | unknown | A type of day characterized by one or more properties which affect public transport operation. For example: weekday in school holidays. | In Switzerland only used for holidays and the like |
| + | alternativeTexts | expected | 0..1 | alternativeTexts_RelStructure | Additional Translations of text elements. |  |
| ++ | AlternativeText | mandatory | 1..1 | unknown | Alternative Text. +v1.1 |  |
| +++ | Text | mandatory | 0..1 | MultilingualString | Text content of NOTICe. |  |
| + | Name | mandatory | 0..1 | MultilingualString | Name of Traveller |  |
| + | properties | expected | 0..1 | propertiesOfDay_RelStructure | Properties of the DAY TYPE. |  |
| ++ | PropertyOfDay | mandatory | 1..1 | unknown | A property which a day may possess, such as school holiday, weekday, summer, winter etc. | Holidays only |
| +++ | HolidayTypes | expected | 0..1 | HolidayTypesListOfEnumerations | Type of holiday. Default is Any day. |  |
| +++ | DayEvent | optional | 0..1 | DayEventEnumeration | Events happening on day. |  |




```xml
<?xml version="1.0" encoding="UTF-8"?>
<DayType  id="ch:1:DayType:Bundesfeier" version="1">
  <!-- In Switzerland only used for holidays and the like -->
  <alternativeTexts>
    <AlternativeText attributeName="Name">
      <Text lang="it">Festa nazionale</Text>
    </AlternativeText>
    <AlternativeText attributeName="Name">
      <Text lang="en">National Day</Text>
    </AlternativeText>
    <AlternativeText attributeName="Name">
      <Text lang="fr">Fête nationale</Text>
    </AlternativeText>
  </alternativeTexts>
  <Name>Bundesfeier</Name>
  <properties>
    <PropertyOfDay>
      <!-- Holidays only -->
      <HolidayTypes>NationalHoliday</HolidayTypes>
      <DayEvent>normalDay</DayEvent>
    </PropertyOfDay>
  </properties>
</DayType>

```


- [General NeTEx definition](../generated/xcore/DayType.html)

## DayTypeAssignment
(NeTEx-1, 7.7.5.5.5)
This assignment overrides the DAY TYPE which was generally chosen for this OPERATING DAY in the overall DAY TYPE assignment plan..
Designation of one day or group of days

We also use DayTypeAssignment currently only for the national holidays.



| Sub | Element | Usage | Card | Type | Description | Note |
|-----|---------|-------|------|------|-------------|------|
|  | DayTypeAssignment | expected | 1..1 | unknown | Associates a DAY TYPE with an OPERATING DAY within a specific Calendar. A specification of a particular DAY TYPE which will be valid during a TIME BAND on an OPERATING DAY. | We currently use DayType to store the national holidays. |
| + | Date | mandatory | 0..1 | xsd:date | Date of the review |  |
| + | DayTypeRef | mandatory | 1..* | DayTypeRefStructure | The DAY TYPE of all the services in this group. |  |




```xml
<?xml version="1.0" encoding="UTF-8"?>
<DayTypeAssignment  id="BundesfeierAssignment" version="1">
  <!-- We currently use DayType to store the national holidays. -->
  <Date>2023-08-01</Date>
  <DayTypeRef ref="ch:1:DayType:Bundesfeier" version="1"/>
</DayTypeAssignment>

```


- [General NeTEx definition](../generated/xcore/DayTypeAssignment.html)
