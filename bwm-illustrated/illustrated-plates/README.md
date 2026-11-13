---
id: BWM-IL-INDEX
title: "Illustrated Plates - Index and Register"
kind: index
series: BWM Illustrated
status: active register - concept prototypes, none print-ready
version: 0.1
date: 2026-11-13
owner: "James (JD) Longmire"
authority: "Spread template and quality gates in ../spread-template.md; production specification in ../production-specification.md"
keywords: [illustrated-plates, register, index, bwm-illustrated]
---

# Illustrated Plates - Index

This folder is the home of record for the plates of *The Biblical World Model: An Illustrated Atlas of Creation, History, and Reality* (see [BWM Illustrated](../README.md)).

Each plate lives here as a pair of files with the same stem:

- the **plate image** itself (`.jpg`), unchanged from the copy supplied, and
- a **companion record** (`.md`) carrying that plate's front matter, transcription summary, claim status, and review-gate state.

An image alone is never the record. The front matter is what makes a plate findable, citable, and checkable: id, title, entry and spread it belongs to, the part and chapter and book page exactly as printed, Scripture, the asset file with its dimensions and SHA-256 hash, provenance, print status, claim status, and review gates. The companion record and this register must agree; if they ever differ, the companion record governs and this register is corrected to match.

## Register

| ID | Plate | Book page | Entry / spread | Scripture | Files | Status |
|---|---|---|---|---|---|---|
| BWM-IL-000 | Cover - The Biblical World Model: An Illustrated Atlas of Creation, History, and Reality | Front cover | None - book cover, also the sub-site hero image | None | [image](000-cover.jpg) / [record](000-cover.md) | Concept prototype - supplied, unreviewed, not print-ready |
| BWM-IL-001 | The Creation of the World - The Six Days of Genesis 1 | 24 | Entry 001, Spread 001 left (overview) | Gen. 1:1 to 2:3; Ex. 20:11 | [image](001-creation-of-the-world.jpg) / [record](001-creation-of-the-world.md) | Concept prototype - supplied, unreviewed, not print-ready |
| BWM-IL-002 | Day 1 - Light and Order / Day 4 - The Heavenly Lights | 25 | Entry 001, Spread 001 right (detail) | Gen. 1:3-5; 1:14-19; Ps. 19:1; 104:19 | [image](002-day-1-and-day-4.jpg) / [record](002-day-1-and-day-4.md) | Concept prototype - supplied, unreviewed, not print-ready |
| BWM-IL-003 | Day 1 - Light and Order (Plate I) | - | Day-plate sub-series, Day 1 | Gen. 1:1-5; John 1:4 | [image](003-day-1-light-and-order.jpg) / [record](003-day-1-light-and-order.md) | Concept prototype - supplied, unreviewed, not print-ready |
| BWM-IL-004 | Day 4 - The Heavens Appointed (Plate IV) | - | Day-plate sub-series, Day 4 | Gen. 1:14-19; Ps. 19:1 | [image](004-day-4-the-heavens-appointed.jpg) / [record](004-day-4-the-heavens-appointed.md) | Concept prototype - supplied, unreviewed, not print-ready |
| BWM-IL-005 | Day 6 - The Procession and Naming (Plate VI) | - | Day-plate sub-series, Day 6 | Gen. 1:24-31; 2:7-25 | [image](005-day-6-the-procession-and-naming.jpg) / [record](005-day-6-the-procession-and-naming.md) | Concept prototype - supplied, unreviewed, not print-ready; lettering defects in one panel, recorded in its companion record |
| BWM-IL-006 | Day 1 - Light and Order (landscape candidate) | - | Day-plate sub-series, Day 1 (landscape candidate) | Gen. 1:1-5; John 1:4; Rev. 21:23; 22:5 | [image](006-day-1-light-and-order-landscape.jpg) / [record](006-day-1-light-and-order-landscape.md) | Concept prototype - generated candidate, unreviewed, not print-ready; one-word repair disclosed in its companion record |

## How the plates group

BWM-IL-001 and BWM-IL-002 are not two separate entries. Together they form the two pages of **Spread 001** for [Entry 001 - The Creation of the World](../entries/001-creation-six-days.md): the overview plate first, then the companion plate contrasting Day 1 (light provided) with Day 4 (the heavenly lights appointed to govern). File plates in spread order, and register a plate under the entry it serves, not as a free-standing item.

## The day-plate sub-series

BWM-IL-003, 004, and 005 begin a second grouping: **day plates**, one plate per creation day under the header "Creation: The Six Days", numbered with Roman numerals on the plates themselves (Plate I, IV, VI). Each is a stand-alone deep treatment of its day - biblical account, key elements, theological significance, a Designed Functional Maturity panel, and an interpretive status panel that labels what is directly stated and what is model. They expand days also covered by Spread 001; they are not pages of that spread, and no book page is printed on them. Register day plates in day order after the spread plates. State at filing: Plates I (Day 1), IV (Day 4), and VI (Day 6) received; Plates II (Day 2), III (Day 3), and V (Day 5) outstanding. BWM-IL-006 opens a parallel line of landscape candidates under the adopted style guide and ruled trim: generated in-session at JD's direction, beginning with a Day 1 candidate; landscape candidates are registered in this same table and do not displace the supplied portrait concepts.

## Adding a plate

1. Give the plate the next BWM-IL number and a file stem of `NNN-short-title`.
2. File the image unchanged; record its byte size, pixel dimensions, and SHA-256 in the companion record. If a higher-resolution master exists, record where it lives - do not describe this folder's copy as the master unless it is.
3. Write the companion record with the full front matter field set used by BWM-IL-001 and BWM-IL-002. Record the part, chapter, and book page exactly as printed on the plate, even when they conflict with the provisional contents; flag the conflict in the record notes instead of silently harmonising it.
4. Transcribe or summarise the printed text, list the callouts in order, and state the claim classes (T / E / O / M / H / U, per ../spread-template.md).
5. Add the plate to the register table above, in spread order.
6. A plate's status advances only when its review gates pass: Scripture and ESV wording checked, theological review, scientific / historical review where applicable, visual accuracy check, and typography and print proof. Embedded AI-rendered lettering is never authoritative, and a supplied low-resolution copy is never print-ready.

## Open reconciliations recorded with the first plates

- **Part name:** BWM-IL-001 reads "Part I: Origins"; ../table-of-contents.md (v0.1) places the six days under "Part II: Beginnings". Awaiting JD's ruling.
- **Chapter scheme:** BWM-IL-002 reads "Chapter 1"; the provisional contents are organised by parts only. Awaiting JD's ruling.
- **Orientation and trim (RULED 2026-11-13):** JD ruled the book trim as 12 x 9 in landscape. The production unit is the individual landscape page plate under the adopted plate style guide (`../plate-style-guide.md`); every plate filed to date is a portrait concept and would be recomposed, not cropped, for the landscape page. The production specification (v0.2) and creative direction carry the ruling.
- **Asset register:** ../assets/README.md still describes Prototype 001 as "not yet committed" and proposes `assets/prototypes/` as its home. Filing this folder supersedes that proposal; the register should be updated to point here. (Resolved 2026-11-13: the asset register now points to this folder.)
- **Cover framework line:** the BWM-IL-000 cover names six terms - Creation, Humanity, The Flood, Nations, Redemption, The World to Come - against the provisional contents' six parts on a different scheme. Whether the cover terms become the part structure awaits JD's ruling.
- **Internal references on public plates:** BWM-IL-004 and BWM-IL-005 print programme work-package codes (WP-022, WP-028, WP-029) in their interpretive status panels. Whether a rebuilt plate retains them, expands them to plain language, or moves them to the companion record awaits JD's ruling.
- **Plate numbers on the artwork (RULED 2026-11-13):** JD ruled that plate numbers are not to appear on the plate. The day plates as supplied print PLATE I, IV, and VI in their headers; corrected plates are to omit the printed numeral, and numbering is carried by the records, this register, and captions. Rebuild item for BWM-IL-003, 004, and 005.
- **Plate style guide (ADOPTED 2026-11-13):** JD adopted the individual-plate style guide handed off via ai-bridge, with two amendments (landscape 12 x 9 pages; no plate numbers on plates), implemented in `../plate-style-guide.md`, `../plate-template.md`, and `../plate-production-checklist.md`. Open item: the guide's approved Day 6 aesthetic-reference raster is not in this repository and has not been received here; BWM-IL-005 is not designated the approved aesthetic prototype.

Human-Curated, AI-Enabled (HCAE)
