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
| BWM-IL-001 | The Creation of the World - The Six Days of Genesis 1 | 24 | Entry 001, Spread 001 left (overview) | Gen. 1:1 to 2:3; Ex. 20:11 | [image](001-creation-of-the-world.jpg) / [record](001-creation-of-the-world.md) | Concept prototype - supplied, unreviewed, not print-ready |
| BWM-IL-002 | Day 1 - Light and Order / Day 4 - The Heavenly Lights | 25 | Entry 001, Spread 001 right (detail) | Gen. 1:3-5; 1:14-19; Ps. 19:1; 104:19 | [image](002-day-1-and-day-4.jpg) / [record](002-day-1-and-day-4.md) | Concept prototype - supplied, unreviewed, not print-ready |

## How the plates group

BWM-IL-001 and BWM-IL-002 are not two separate entries. Together they form the two pages of **Spread 001** for [Entry 001 - The Creation of the World](../entries/001-creation-six-days.md): the overview plate first, then the companion plate contrasting Day 1 (light provided) with Day 4 (the heavenly lights appointed to govern). File plates in spread order, and register a plate under the entry it serves, not as a free-standing item.

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
- **Orientation:** both plates are portrait; the creative direction and production specification describe a landscape or near-square trim. Awaiting JD's ruling.
- **Asset register:** ../assets/README.md still describes Prototype 001 as "not yet committed" and proposes `assets/prototypes/` as its home. Filing this folder supersedes that proposal; the register should be updated to point here.

Human-Curated, AI-Enabled (HCAE)
