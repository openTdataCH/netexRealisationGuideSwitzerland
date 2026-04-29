# Frequency travel

Frequency travel happens in two modes:
- every `ServiceJourney` is modeled itself and has its own sjyid.
- one `TemplateServiceJourney` is used and has one sjyid.

This has some consequences:
- SIRI information can only be based on that one sjyid. 
- This means only SIRI SX can be used and not SIRI ET or PT.
- For continuous operation (like e.g. drag lifts) the spacing is one minute (PT1M).
- If this is needed, then the transport operator has to split the `Line` into many `ServiceJourney`s.
- Currently, we have in HRDF some lines that deliver multiple `*Z` with the same sjyid. THIS is no longer allowed for NeTEx.