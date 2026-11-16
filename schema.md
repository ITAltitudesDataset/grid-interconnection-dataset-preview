# Grid Interconnection Dataset — Data Dictionary & Schema

**Publisher:** IT Altitudes Inc.  
**Edition:** 2026  
**Original source attribution:** Lawrence Berkeley National Laboratory (LBNL), *Queued Up: 2026 Edition* (as identified in the publisher's certificate)  
**Preview size:** 50 project records  
**Preview formats:** Excel (`.xlsx`), CSV (`.csv`), JSON (`.json`), and Parquet (`.parquet`)

## Scope and verification

This document describes the **13 field names visible in the published 50-row CSV preview**. The publisher's certificate describes the full commercial dataset as containing **38,201 project records and 30 fields**. The additional 17 full-dataset fields have **not** been verified from the publicly visible CSV preview and are intentionally not invented here.

Field explanations below are **interpretive guidance based on the column names**, not independently confirmed definitions from the original LBNL codebook. Refer to the original source documentation for authoritative definitions, units, coding conventions, and project status values.

## Preview data dictionary

| # | Exact column name | Suggested logical type | Description / interpretation |
|---|---|---|---|
| 1 | `q_id` | Text | Queue or project identifier; preserve as text to retain formatting. |
| 2 | `q_status` | Text / category | Reported interconnection queue or project status. Interpret using source status definitions. |
| 3 | `q_date` | Date / text | Queue-related date. Confirm its precise meaning and format in source documentation. |
| 4 | `prop_date` | Date / text | Proposed or reported project date; specific event meaning requires source confirmation. |
| 5 | `state` | Text | State associated with the project or queue entry. |
| 6 | `county` | Text | County associated with the project; may be missing or source-reported. |
| 7 | `region` | Text / category | Reported geographic or interconnection region; exact classification requires source confirmation. |
| 8 | `utility` | Text | Reported utility or related organization; role requires source confirmation. |
| 9 | `project_type` | Text / category | Project technology or type as reported in the data. |
| 10 | `type_clean` | Text / category | Standardized project-type label; transformation rules require confirmation. |
| 11 | `mw_1` | Numeric (decimal) | Capacity-related value apparently expressed in MW; exact capacity definition requires confirmation. |
| 12 | `q_year` | Integer / nullable | Queue-related year, potentially derived from `q_date`; verify derivation. |
| 13 | `prop_year` | Integer / nullable | Proposed-project year, potentially derived from `prop_date`; verify derivation. |

**Note:** Logical types are recommendations for downstream parsing, not verified physical data types in each uploaded format.

## Preview files

- [CSV preview](IT_Altitudes_Grid_50_Row_Preview_CSV.csv)
- [Excel preview](IT_Altitudes_Grid_50_Row_Preview_XL.xlsx)
- [JSON preview](Grid_Interconnection_50_Row_JSON_Preview_Download.json)
- [Parquet preview](Grid%20Interconnection_50_Row_Preview.parquet)

## Recommended handling

- Keep identifiers such as `q_id` as text.
- Parse dates only after confirming source date conventions.
- Treat blank cells, JSON `null`, and missing Parquet values as missing, not as zero.
- Do not interpret a blank `mw_1` as zero capacity.
- Retain source-reported categories and keep any standardized labels separately.
- Do not assume queue inclusion means project approval, construction, or operation.
- Verify field equivalence across formats before automated integration.

## Source, limitations, and rights

The dataset is a **static historical reference**, not a live queue monitoring or engineering decision system. Project status, capacity, location, and timing may change after the source snapshot. Verify operational decisions against current authoritative records.

Original source information and third-party materials remain subject to their applicable rights. IT Altitudes Inc.'s licensing terms apply only to original protected contributions it owns or is authorized to license.

- [License & Usage Terms](LICENSE.md)
- [Source & Liability Disclaimer](DISCLAIMER.md)
- [Publisher-Issued Certificate](CERTIFICATES.md)

## Complete buyer kit

[View the Grid Interconnection Dataset on Gumroad](https://italtitudes.gumroad.com/l/lavlcx)

**Support:** support@italtitudesdataset.zohodesk.in

---

*Prepared by IT Altitudes Inc. — Preview schema documentation, 2026.*
