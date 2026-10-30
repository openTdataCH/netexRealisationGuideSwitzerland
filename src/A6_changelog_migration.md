# Changelog of Swiss profile 1.0 to 2.0

This changelog compares version 1.00.1of the realisation guide based on NeTEx XSD 1.10, with version 2.

## 1. Global changes

### Schema and conventions
- **NeTEx basis changed from XSD 1.10 to NeTEx 2.1** 
- **`version="any"` replaced by `version="1"` everywhere**, `versionRef="1"` for cross-file references .
- **`created`, `changed`, `modification` remain unused**; new rules documented for `responsibilitySetRef`, `nameOfRefClass` and `versionRef`.
- **ID semantics redefined**: v1 required global uniqueness at import; v2 defines uniqueness per object type within one delivery, introduces an explicit **ID-stability convention** (most elements "must be kept stable between exports", some explicitly don't need to, e.g. `PassengerStopAssignment`, `Notice`, `AvailabilityCondition`), and drops `PublicKey`/`PrivateKey` in favour of `KeyList` and `privateCodes/PrivateCode`.
- **`privateCodes/PrivateCode` with `type` attribute replaces v1's `keyList`/`KeyValue` and plain `PrivateCode`** for business keys: sjyid (`type="sjyid"`), region (`type="rn"`), SBOID/GO number on operators, DIDOK (`type="didok"`) on stops, SLNID on lines.
- **Translations now use repeated `<Text>` elements with `lang` inside MultilingualString**; `AlternativeText` is no longer used; `AlternativeName` is restricted to `alias` only.

- **New whole-model orientation section** ("A First Glimpse") and new general rules on element ordering, geometries (none in profile) and FromDate/ToDate semantics (always operating days, `T00:00:00` / `T23:59:59`)

### File exchange
- **Three new file types**: `SITE_OFFER` (sites/stops), `NETWORK_OFFER` (resource/calendar/service/timetable frames, self-sufficient refs), `INTERCHANGE` (interchanges, joining/splitting, through-services; cross-file validity via `versionRef` instead of `version`).
- **Environment identifiers renamed**: `entw/test/inte/prod` → `DEV/TEST/INT/PROD`, used as file-name prefixes; the v1 sender-identification rule (`<environment>_<partner system>`) is dropped .
- **File-name version component changes from `1.10` to `2.1`**; new "type of file" component; underscores forbidden inside export names; v1's `OJP-NAP_` name prefixes and frame number/total components disappear.
- **Transport protocol**: v1's secure-FTP requirement dropped; "The data transfer will be defined by INFO+". The v1 statements on web services (not supported) and weekly full-file production by SKI are gone.
- **New role model**: Owner (= "Konzessionär" per Atlas) is responsible for the overall delivery, per partial line delivery may be delegated; new rules on completeness of delivery (all journeys incl. those driven by other operators in the owner's name), shared responsibilities for planning, and an explicit **prohibition of partial deliveries and incremental updates**
- **Kept**: UTF-8 without BOM; README file rule; provider naming conventions (partner short name, timetable period, creation date).

### Time formatting
- v1's per-call `DayOffset=1` rule replaced: only `DepartureDayOffset` on `ServiceJourney`/`TemplateServiceJourney` marks journeys starting after midnight; midnight crossings during the journey are **implicit** (times are calculated from `TimeDemandType` run/wait times).

## 2. Chapter-by-chapter changes

### Preliminary remarks 
- Binding-nature text and mapping-table rule carried over nearly verbatim.
- Referenced-documents list moved to annex `A1` and expanded (Transmodel EN 12896, SIRI, EPIP/EPIAP, Nordic/France/Slovenia profiles, tutorials).
- New: roadmap with milestones (RC1 2026-07, RC2 2026-09, release planned 2026-12), imprint, AGPL-3.0 licence, example XML repository.
- Dropped: v1's scope-limiting rule that deviations must be discussed with SKI.

### ResourceFrame
- **`Organisation` and `Authority` are no longer used**; only `Operator` . `OperatorRef` on a `Line` is always the Konzessionär; a deviating journey operator is set via `OperatorRef` on the `ServiceJourney`.
- **SBOID becomes the primary identifier** for operators (v1: GO number, SBOID "from 2024"); SBOID and GO number must be stored in both `KeyList` and `privateCodes/PrivateCode` .
- `ResponsibilitySet`: purpose changed from "hierarchy between lines and sub-lines" to modelling roles of participating companies; **StakeholderRoleType values reduced** to `Operation` and `EntityLegalOwnership` (`FareManagement`, `Planning` dropped); the separate `ResponsibilityRoleAssignment` section is merged into `ResponsibilitySet`.
- `TypeOfNotice`: values `Zugname` (2), `Gleis-Angabe` (3) and `Region` (11) deprecated; Region replaced by `privateCodes/PrivateCode type="rn"` on the journey .
- `TypeOfProductCategory`: restriction to V580/allianceswisspass values kept; new rule that `Line` also references `TypeOfProductCategory`; TypeOf… ids must be stable between exports.
- New sections without v1 counterpart: **`SiteFacilitySet`**, **`VehicleType`**, **`TypesOfPlace`** (`regularStop`, `drtCollectionPoint`), `ServiceFacilitySet` , `TypeOfService` .

### SiteFrame 
- **DIDOK transport changed**: v1's plain `PrivateCode` + `DIDOK`/`SLOID` KeyValues → v2 requires `privateCodes/PrivateCode type="didok"` **and** a matching `keyList` entry; SLOID in `PrivateCode` where it exists.
- **`ShortName` forbidden on `StopPlace`** (v1 carried the DIDOK number there — "discontinued under RV 2.0").
- `ValidBetween` on StopPlace: v1 example had FromDate and ToDate; v2 requires **FromDate only, no ToDate**.
- HafasPriority/HafasKMInfo moved from `Extensions` into `keyList` KeyValues ("only used in exports by INFO+").
- **Quay ID scheme defined**: `{StopPlace SLOID}_gen:{Quay SLOID}_pf:{Platform Code}` with `missingSLOID` fallback and special-character replacement (v1 used ad-hoc ids like `ch:1:Quay:8503000-10`); `PublicCode` on Quay now mandatory; SLOID moved from Quay keyList to `privateCodes`.
- New Quay elements: `QuayType`, `ParentQuayRef` (sectors; hierarchy now modelled in Atlas), `AccessibilityAssessment` (`MobilityImpairedAccess`, `AccessModes`).
- `TopographicPlace`: values extended (country, state/canton, county, municipality); StopPlace should reference its canton.
- **Centroid**: coordinate reference formalised as WGS84 / LV95 (EPSG:2056) with 4+ decimal accuracy; INFO+ relies on Atlas master data (v1: DIDOK master data); v1's typo "WSG84" corrected.
- **New `AccessibilityAssessment` interpretation** (stricter than EPIAP) for StopPlace/Quay with limitation tables (StepFreeAccess, EscalatorFreeAccess, LevelAccessIntoVehicle with PRM-TSI gap values, RampFreeAccess) and entrance criteria; full site model (entrances, levels, equipment, paths) deferred to `uc09_accessibility.md` (work in progress).
- `alternativeTexts` (multilingual names) dropped throughout the site chapter; translations go via MultilingualString.

### ServiceFrame 
- **`Direction` object abolished** (v1's mandatory `ch:1:Direction:H`/`:R` pair "will no longer be supported"); only `DirectionType` on the pattern/journey is used.
- **Line**: SLNID becomes the primary identifier (in `@id` "wherever possible", `privateCodes/PrivateCode` and `KeyList`); slnid concepts Dispositionslinie/Temporäre Linie modelled as regular Lines, "Betriebliche Linie" not modelled; partial lines get a main line; v1's "NoLine" placeholder concept dropped; mixed-line handling in `uc17_mixed_lines.md`.
- **New `GroupOfLines` section** (only for mixed lines, `GroupOfLinesType` restricted to `administrative`).
- **DestinationDisplay more prescriptive**: journey destination via `ServiceJourney/Destination/DestinationDisplayRef` (no redundant inline Name), mid-run changes on `StopPointInJourneyPattern/DestinationDisplayRef`; destination-change use case in `uc13_changes_in_destination.md`.
- **ScheduledStopPoint**: sloid used directly as `@id` where it exists; SSPs used in TimingLinks/JourneyPatterns should be quay-level.
- **PassengerStopAssignment**: when linking to a Quay both `QuayRef` and `StopPlaceRef` must be set; goal is always a QuayRef (artificial quays for foreign data); `BoardingPosition` not used; new `passengerBoardingPositionAssignments` for formations (quay sectors); ids explicitly need not be stable; v1's quay-split example (arrival 2A / departure 2D) dropped.
- `DefaultConnection` / `SiteConnection`: details moved to `uc03_transfers.md` (HRDF mapping UMSTEIGB/UMSTEIGV/UMSTEIGZ/UMSTEIGL/METABHF/DURCHBI); ids must be stable; v1's footnote on modelling large interchange times dropped.
- `Notice`: must only be used for information not expressible by specific elements (facilities, DayType, ForAlighting/ForBoarding); recommendation to translate (DE/IT/FR, possibly EN).
- **`NoticeAssignment` becomes a documented element** of the ServiceFrame (v1: prose only); `StartPointInPatternRef`/`EndPointInPatternRef` allow part-of-journey notices.
- **New pattern/timing sections**: `TimingLink`, `ServiceJourneyPattern` (shared between journeys with identical sequences), `TimeDemandType` — the foundation of the new timing model.

### ServiceCalendarFrame 
- **DayType/DayTypeAssignment now used only for national holidays** (v1: full-year day types); journey operating days are governed exclusively by `AvailabilityConditionRef` with ValidDayBits.
- `AvailabilityCondition` additionally supports `timebands` as third constraint type; ValidDayBits "expected" rather than required for recurring patterns; none of FromDate/ToDate, ValidDayBits, timebands individually mandatory.
- Nested `dayTypes`/`dayTypeAssignments` inside `ServiceCalendar` are **not used**; they are declared as siblings in the frame; `ServiceCalendar` narrowed to a label for the timetable year.
- `DayType`: `HolidayTypes` restricted to `nationalHoliday`, `DayEvent` only `anyDay`/`normalDay`; multilingual `alternativeTexts` dropped.
- `Timeband`: main use is now the daily operating window of frequency-based lines (chairlift/shuttle); InterchangeRuleTiming use not applicable in RG 2.0; `StartEvent`/`EndEvent`/`Duration` not used; times as `hh:mm:ss` with seconds always `00`; note distinguishing Timeband from `HeadwayJourneyGroup` first/last departure (pointer to `uc14_frequencies.md`).

### TimetableFrame 
- **New timing model — the biggest change**: `Call`, `Arrival`, `Departure` and `TimetabledPassingTime` are removed (deprecated); each `ServiceJourney`/`TemplateServiceJourney` references exactly one **`ServiceJourneyPattern`** (authoritative stop sequence; carries `LineRef`) and exactly one **`TimeDemandType`** (JourneyRunTime/JourneyWaitTime); passing times are calculated by a documented algorithm.
- **`ServiceJourney`**: `LineRef` removed; `validityConditions` mandatory with a single `AvailabilityConditionRef`; `TypeOfProductCategoryRef` mandatory; sjyid moved to `privateCodes/PrivateCode type="sjyid"` (not keyList); `@id` may not be the sjyid; `DepartureTime` in local time without UTC offset; `DepartureDayOffset` (incl. rare negative values) replaces per-call DayOffset; `DatedServiceJourney` explicitly not used; new `parts`/`JourneyPart`, `checkConstraints`, `VehicleTypeRef`, `occupancies`/`OccupancyView` (not used).
- **`JourneyPart`** (new, `uc05_journey_parts.md`): segmentation for facility changes (`PurposeOfJourneyPartition:FacilityChange` replaces v1's `Extensions/facilities` on calls) and product-category changes; **not** to be used for train-number changes (use two ServiceJourneys + `ServiceJourneyInterchange`).
- **`JourneyMeeting` removed**; replaced by **`ServiceJourneyInterchange`** (new element with `StaySeated`, `CrossBorder`, `ChangeWithinVehicle`, `MaximumWaitTime`, `FromPointRef`/`ToPointRef`, concrete `From/ToServiceJourneyRef`); v1's `FromJourneyRef`/`ToJourneyRef` must not be used .
- **`InterchangeRule`, `InterchangeRuleParameter`, `InterchangeRuleTiming` deprecated/removed**: filter-based interchange rules are resolved to concrete `ServiceJourneyInterchange`s per journey pair during import/export (`uc03_transfers.md`).
- **`CheckConstraint`**: moved out of Arrival/Departure to a top-level element on ServiceJourney/ServiceJourneyPattern, always instantiated inline; new restrictions (`bothWays` forbidden; CheckProcess only `alighting`/`boarding`/`queue`); `MinimumLikelyDelay` replaced by `AverageDelay`/`MaximumLikelyDelay`; expanded use cases in `uc07_checkconstraints.md` (TGV doors, carTransportRail/touristic waiting times, HRDF CI/CO).
- **`HeadwayJourneyGroup`**: exactly one frequency per TemplateServiceJourney; `FirstDepartureTime`/`LastDepartureTime`/`First/LastDayOffset` dropped (timing via `DepartureTime`/`DepartureDayOffset`); `HeadwayDisplay` restricted to `displayPassingTimesOnly` (v1 example contradicted its own rule); `RhythmicalJourneyGroup` explicitly not used; frequency policy in `uc14_frequencies.md` (SIRI SX only for template journeys; multiple `*Z` sharing one sjyid no longer allowed).
- **`TrainNumber`**: one per journey, unique per operating day, equals the HRDF `*Z` number; schema allows multiple refs in principle; non-rail modes also get TrainNumbers.
- **`TypeOfService`**: only `PublicJourney` (`ch:1:TypeOfService:1`); `GarageRunIn/Out`, `ThroughCoach` struck through.
- `NoticeAssignment`, `AvailabilityCondition`, `Timeband`, `ServiceFacilitySet` relocated to their owning-frame chapters (06/07/09); `08_timetable.md` keeps cross-references.
- New frame content: `journeyInterchanges`, `vehicleTypes` placeholder for formations; explicit rule that only passenger-available journeys are modelled.

### Appendix 
- **TransportMode**: v1's 11-value list replaced by the NeTEx 2.1 20-value enumeration, with a new per-value usage column (part of the data / special file / not used) and the rule "Only use sub modes that are approved in the mapping!"; submode mapping now via the "Übergangsdokument Branchenstandard" and `Mappingtabellen_NeTEx_v2.0.xlsx` (v1: HRDF V.580 mapping on oev-info.ch); new `ProductCategory` section.
- **Connection times **: the abstract 9-rule framework (criteria matrices, explicit hierarchy rules) is rebuilt around the HRDF source tables in `uc03_transfers.md`; rules 3, 4 and 7 (product-category-based connection times) have no v2 counterpart; v1's dual representation of rule 5 (`DefaultConnection` **and** `SiteConnection`) reduced to `DefaultConnection`; UMSTEIGZ semantics (`!` = guaranteed) and Verkehrstagebitfeldnummer documented.
- **Transfer time**: METABHF/SiteConnection survives essentially intact; new rule that this data lives only in the master data file (SITE_OFFER), not in timetable files; ends may now be any SiteElement.

## 3. New in v2 (no v1 counterpart)

- **17 use-case chapters** (`uc01`–`uc17`): Durchbindung, joining/splitting, transfers, service facilities, JourneyParts, modes/submodes, check constraints, Kurswagen, accessibility, journeys passing midnight, touristic offers (in progress), car transport rail (in progress), changes in destination, frequencies, formations (draft), demand-responsive traffic (draft), mixed lines.
- **New elements documented for the first time**: `ServiceJourneyInterchange`, `JourneyPart`, `TimeDemandType`, `TimingLink`, `ServiceJourneyPattern`, `GroupOfLines`, `SiteFacilitySet`, `VehicleType`, `TypesOfPlace`, `AccessibilityAssessment`, `PassengerBoardingPositionAssignment`, `Locale`/`TimeZone`, `StopPlaceType`/`LimitedUse`, `QuayType`, `ParentQuayRef`, `TemplateVehicleJourneyType`, `OccupancyView` (not used), `vehicleTypes`/`CompoundTrain` placeholder.
- **New annexes**: `A1` references, `A2` EPIP/EPIAP comparison, `A3` France/Norway profile comparison (draft), `A4` glossary (~70 terms with "not used in the Swiss profile" flags), `A5` element index.
- **New general content**: roadmap, role model, guiding principles for delivery, ID-stability convention, ordering rule for sequences, geometries policy, example XML repository, AGPL licence, imprint.

## 4. Removed / deprecated summary

| v1 concept                                                                           | v2 status                                                                                                        |
|--------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------|
| `Direction` objects (`ch:1:Direction:H`/`R`)                                         | Not supported; only `DirectionType`                                                                              |
| `AlternativeText`                                                                    | Not used; MultilingualString repeated `Text`                                                                     |
| `Call` / `Arrival` / `Departure` / `TimetabledPassingTime`                           | Deprecated; ServiceJourneyPattern + TimeDemandType                                                               |
| Per-call `DayOffset`                                                                 | Only `DepartureDayOffset` on the journey                                                                         |
| `JourneyMeeting` (+ `FromJourneyRef`/`ToJourneyRef`)                                 | Must not be used; `ServiceJourneyInterchange`                                                                    |
| `InterchangeRule`, `InterchangeRuleParameter`, `InterchangeRuleTiming`               | Deprecated; `ServiceJourneyInterchange`                                                                          |
| `CoupledJourney` / `JourneyPartCouple` for splitting/joining                         | Not used                                                                                                         |
| `RhythmicalJourneyGroup`, `DatedServiceJourney`, `BoardingPosition`                  | Explicitly not used                                                                                              |
| `Organisation`, `Authority`                                                          | Not used; `Operator` only                                                                                        |
| sjyid/sloid/DIDOK/SLNID in `keyList` KeyValue                                        | `privateCodes/PrivateCode` (keyList kept only for specific INFO+ keys)                                           |
| `ShortName` (DIDOK) on StopPlace                                                     | Discontinued                                                                                                     |
| `Extensions` for facilities on journeys/calls, `Condition` on ServiceFacilitySet     | `JourneyPart` facilities / `Extensions/Priority`                                                                 |
| `MinimumLikelyDelay` on CheckConstraint                                              | `AverageDelay`/`MaximumLikelyDelay`                                                                              |
| sFTP transfer, sender identification, weekly production statement, web-services note | Dropped (transfer defined by INFO+)                                                                              |
| `StopUse`/`RequestStop`/`VisitNumber`/`DynamicStopAssignment` (per-call)             | No direct v2 equivalent found in the guide text (patterns carry repeated visits; StopUse semantics under review) |

## 5. Notes and open points
- Internal v2 inconsistencies noticed while comparing (not v1 changes): the SKI delivery section says "SITE_OFFER.xml" while the file type is `STOP_OFFER`; file-name tables say version `2.1` but examples use `2.0`; two TODOs remain in `05_stops.md` (RampFreeAccess constraint, VisualSignsAvailable language independence).
- v1 items whose v2 home could not be confirmed: v1 §10.5 `StopUse` values, `RequestStop`, `DynamicStopAssignment`, and the v1 rule linking ScheduledStopPoint ids to StopPlace ids; they may be pending in the work-in-progress use cases (uc09, uc15, uc16).
- Dropped: rule to copy TypeOfValues from SKI files; "The operators must be set" MUST-rule.

