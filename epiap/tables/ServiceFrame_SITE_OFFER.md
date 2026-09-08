# ServiceFrame_SITE_OFFER

There is a partial ServiceFrame in the SITE_OFFER

*Table: ServiceFrame*

| Sub | Element | Usage | Card | Type | Description | Note |
|-----|---------|-------|------|------|-------------|------|
|  | [lines](lines.md) | optional | 0..1 | lineRefs_RelStructure | LINEs in frame. |  |
|  | [groupsOfLines](groupsOfLines.md) | optional | 0..1 | groupsOfLinesInFrame_RelStructure | GROUPs of LINEs in frame. |  |
| + | [SiteConnection](SiteConnection.md) | expected | 1..1 | SiteConnection_VersionStructure | The physical (spatial) possibility to connect from one point to another in a SITE. | SiteConnection are used only in the main file and not in timetable files. |
| + | [DefaultConnection](DefaultConnection.md) | expected | 1..1 | DefaultConnection_VersionStructure | Specifies the default transfer times to transfer between MODEs and / or OPERATORs within a region. | DefaultConnection is only used in the site file |
