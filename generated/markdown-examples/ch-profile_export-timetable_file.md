# ch-profile_export-timetable_file

| Sub | Element | Usage | Card | Type | Description | Note |
|-----|---------|-------|------|------|-------------|------|
| + | PublicationTimestamp | mandatory | 1..1 | xsd:dateTime | Time of output of data. |  |
| + | ParticipantRef | mandatory | 1..1 | siri:ParticipantCodeType | Identifier of system requesting Data. |  |
| + | dataObjects | mandatory | 0..1 | None | NeTEx Entities of any type. |  |
| ++ | CompositeFrame | mandatory | 1..1 | None | A container VERSION FRAME that groups a set of content VERSION FRAMsE to which the same VALIDITY CONDITIONs have been assigned. |  |
| +++ | frames | mandatory | 0..1 | frames_RelStructure | Content frames in COMPOSITE FRAME. |  |
| ++++ | [ResourceFrame](ResourceFrame.md) | expected | 1..1 | None | A coherent set of reference values for TYPE OF VALUEs , ORGANISATIONs, VEHICLE TYPEs etc that have a common validity, as specified by a set of frame VALIDITY CONDITIONs. Used to define common resources that will be referenced by other types of FRAME. |  |
| ++++ | [ServiceFrame](ServiceFrame.md) | expected | 1..1 | None | A coherent set of Service data to which the same frame VALIDITY CONDITIONs have been assigned. |  |
| ++++ | [ServiceCalendarFrame](ServiceCalendarFrame.md) | expected | 1..1 | None | A SERVICE CALENDAR. A coherent set of OPERATING DAYS and DAY TYPES comprising a Calendar. That may be used to state the temporal VALIDITY of other NeTEx entities such as Timetables, STOP PLACEs, etc. Covers a PERIOD with a collection of assignments of OPERATING DAYS to DAY TYPES. |  |
| ++++ | [TimetableFrame](TimetableFrame.md) | mandatory | 1..1 | None | A coherent set of timetable data (VEHICLE JOURNEYs and BLOCKs) to which the same VALIDITY CONDITIONs have been assigned. |  |
