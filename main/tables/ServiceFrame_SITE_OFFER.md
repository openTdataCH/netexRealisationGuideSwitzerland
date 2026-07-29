# ServiceFrame_SITE_OFFER

There is a partial ServiceFrame in the SITE_OFFER

*Table: ServiceFrame*

| Sub | Element | Usage | Card | Type | Description | Note |
|-----|---------|-------|------|------|-------------|------|
| + | [SiteConnection](SiteConnection.md) | expected | 1..1 | unknown | A coherent set of Service data to which the same frame VALIDITY CONDITIONs have been assigned. | SiteConnection are used only in the main file and not in timetable files. |
| + | [DefaultConnection](DefaultConnection.md) | expected | 1..1 | unknown | A coherent set of Service data to which the same frame VALIDITY CONDITIONs have been assigned. | DefaultConnection is only used in the site file |
