---
id: BWM-IL-INDEX
title: "Illustrated Plates - Index and Register"
kind: index
series: BWM Illustrated
status: production register - restarted 2026-11-13; concept candidates, none print-ready
version: 0.2
date: 2026-11-13
owner: "James (JD) Longmire"
authority: "Plate style guide in ../plate-style-guide.md; plate template in ../plate-template.md; production specification in ../production-specification.md"
keywords: [illustrated-plates, register, index, bwm-illustrated]
---

# Illustrated Plates - Index

This folder is the home of record for the plates of *The Biblical World Model: An Illustrated Atlas of Creation, History, and Reality* (see [BWM Illustrated](../README.md)).

**Production restarted on 2026-11-13 at JD's direction.** The first round of concept material (BWM-IL-000 to BWM-IL-005: the supplied portrait plates, the Spread 001 pages, and the first cover mock) is archived unchanged in [Archive - First Concepts](../archive/first-concepts/README.md). Its numbers are retired and will not be reused. Production now runs in the ruled format: individual landscape page plates at 12 x 9 in trim, under the adopted plate style guide, with no plate numbers on the artwork.

Each plate lives here as a pair of files with the same stem:

- the **plate image** itself (`.jpg`), and
- a **companion record** (`.md`) carrying that plate's front matter, transcription summary, claim status, and review-gate state.

An image alone is never the record. The front matter is what makes a plate findable, citable, and checkable: id, title, entry it serves, Scripture, the asset file with its dimensions and SHA-256 hash, provenance, print status, claim status, and review gates. The companion record and this register must agree; if they ever differ, the companion record governs and this register is corrected to match.

## Register - production line

| ID | Plate | Entry | Scripture | Files | Status |
|---|---|---|---|---|---|
| BWM-IL-006 | Day 1 - Light and Order (landscape candidate) | Entry 001 (subject area) | Gen. 1:1-5; John 1:4; Rev. 21:23; 22:5 | [image](006-day-1-light-and-order-landscape.jpg) / [record](006-day-1-light-and-order-landscape.md) | Concept prototype - generated candidate, JD-approved as the style benchmark for the landscape line, unreviewed, not print-ready; one-word glyph repair disclosed in its companion record |
| BWM-IL-007 | Cover - The Biblical World Model (landscape) | Front cover | - | [image](007-cover-landscape.jpg) / [record](007-cover-landscape.md) | Concept prototype - generated candidate, first filing of the restarted production, unreviewed, not print-ready |
| BWM-IL-008 | Day 2 - The Expanse (landscape) | Entry 001 (subject area) | Gen. 1:6-8; Ps. 148:4; Rev. 21:23; 22:5 | [image](008-day-2-the-expanse-landscape.jpg) / [record](008-day-2-the-expanse-landscape.md) | Concept prototype - generated candidate, unreviewed, not print-ready; line repair disclosed in its companion record (record v0.2, including the superseded first repair) |
| BWM-IL-009 | Day 3 - The Dry Land and the Seas (landscape) | Entry 001 (subject area) | Gen. 1:9-13; Ps. 95:5 | [image](009-day-3-the-dry-land-and-seas-landscape.jpg) / [record](009-day-3-the-dry-land-and-seas-landscape.md) | Concept prototype - generated candidate, unreviewed, not print-ready; disclosed hybrid construction (v1 body, v6 account interior) in its companion record; landmass Pangea-type with large freshwater seas and lakes, per JD |

## Adding a plate

1. Give the plate the next BWM-IL number and a file stem of `NNN-short-title`. Numbers are never reused, including archived ones.
2. File the image; record its byte size, pixel dimensions, and SHA-256 in the companion record. If a higher-resolution master exists, record where it lives - do not describe this folder's copy as the master unless it is.
3. Write the companion record with the full front matter field set used by BWM-IL-006. Record what is printed on the plate exactly; flag conflicts in the record notes instead of silently harmonising them.
4. Transcribe or summarise the printed text, list the callouts in order, and state the claim classes (T / E / O / M / H / U, per ../plate-template.md).
5. Add the plate to the register table above, in production order.
6. A plate's status advances only when its review gates pass: Scripture and ESV wording checked, theological review, scientific / historical review where applicable, visual accuracy check, and typography and print proof. Embedded AI-rendered lettering is never authoritative, and a concept-resolution copy is never print-ready.

## Rulings and open items

- **Orientation and trim (RULED 2026-11-13):** book trim is 12 x 9 in landscape; the production unit is the individual landscape page plate under the adopted plate style guide (`../plate-style-guide.md`). Page raster 3600 x 2700 px at 300 ppi for a print master.
- **Plate numbers on the artwork (RULED 2026-11-13):** plate numbers do not appear on plate artwork; numbering is carried by the records, this register, and captions.
- **Plate style guide (ADOPTED 2026-11-13):** adopted with JD's two amendments (landscape 12 x 9 pages; no plate numbers on plates), implemented in `../plate-style-guide.md`, `../plate-template.md`, and `../plate-production-checklist.md`. BWM-IL-006 is the JD-approved exemplar of the adopted style for the production line.
- **Restart (2026-11-13):** production restarted from the beginning, starting with the book cover, filed as BWM-IL-007. The editorial questions raised by the archived concepts (part names, chapter scheme, cover arc against the provisional contents) lapse with the restart and will be settled afresh in the new production contents; the six-term arc itself is carried into the new cover by design.
- **Archived aesthetic reference (closed by the restart):** the style guide's approved Day 6 raster was never received into this repository; the question is closed with the archiving of the first concepts, the landscape line taking BWM-IL-006 as its reference.

Human-Curated, AI-Enabled (HCAE)
