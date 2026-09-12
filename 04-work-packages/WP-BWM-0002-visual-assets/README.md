# Responsive visual assets

**WP-BWM-0002 — proposed; implementation pending.**

Produce and integrate hero desktop/mobile substrates, four audience cards, conceptual maps and support graphics; preserve provenance, accessibility, crop safety and theological constraints. Full-page raster mockups are references only. Narration is excluded.

Depends on: WP-BWM-0001 asset conventions.

[Imported requirements](requirements.md) retain the complete source scope and acceptance checklist. `package.yaml` owns current status and authority; inherited source status does not imply implementation. See WP-BWM-0004 migration evidence for provenance.

Human-Curated, AI-Enabled (HCAE)

## Completed decomposition slice

[graphics-library](../../graphics-library/README.md) contains 24 extracted draft PNGs, original references, catalog and provenance manifest. See [verification evidence](extraction-evidence.md). These files are source-resolution extracts, not recovered SVG or full-resolution originals. Production approval and site integration remain pending.

## Post-deployment review findings

The following items are part of WP-BWM-0002 implementation and acceptance:

1. **True mobile hero asset** — the current `hero-mobile-source.png` is a landscape extraction, not a mobile-first portrait composition. Produce or approve a mobile-specific hero substrate with crop-safe focal placement and no embedded explanatory text or controls.
2. **Responsive image delivery** — after a mobile-specific hero exists, prefer `<picture>`/`srcset` or equivalent responsive delivery so mobile clients do not need to download and crop the desktop hero unnecessarily.
3. **Audience-card production approval** — the current extracted audience images are drafts. Review crop quality, focal placement, contrast, compression, and suitability under HTML overlays before marking them production-approved.
4. **Concept graphic review** — review `worldmodel-layers-labelled.png` for legibility, intrinsic text dependence, and whether an SVG/HTML-labelled replacement would improve accessibility and responsive behavior.
5. **Manifest promotion state** — update graphics-library provenance/status metadata when individual assets move from extracted draft to approved/integrated.

These items do not require changes to WP-BWM-0001 except where responsive asset integration touches site templates or CSS.
