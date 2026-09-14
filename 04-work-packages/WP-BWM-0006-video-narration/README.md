# Narrated video adaptation of the Tier 1 story

**WP-BWM-0006 — completed 2026-09-14; revision 3 published.**

Turn the JD-approved Tier 1 "the-story" narrative into a narrated short-form video, using ThinxAI's existing video-narration pipeline (cloned-voice text-to-speech + Remotion, 9:16 vertical by default).

Depends on: WP-BWM-0005 accessible narrative (Tier 1 approved 2026-09-12 — supplies the narration source text) and WP-BWM-0002 visual assets (production imagery; draft graphics-library extracts may stand in as clearly-marked placeholders until that package completes).

## Scope

- Derive a narration script from the approved Tier 1 text, keeping its plain-language and theological framing intact.
- Select storyboard scenes from WP-BWM-0005's visual/storyboard opportunities list: Adam's mature state, the wine at Cana, the video-game-world thought experiment, starting-state comparison, and Creation through Flood to later Earth history.
- Synthesize narration and render the video.
- Produce the full provenance set `06-operations/runbooks/site/media.md` requires for any future media artifact: a manifest (source repo/commit, source page/graphics, output revision, approved script reference, duration, language, hosting URL, status), a text transcript and WebVTT captions with language metadata, a thumbnail with alt text and a link back to the source page, and a hash of the rendered output.
- Deliver the finished set to Console Drive Artifacts and this package's evidence folder for JD's review.

**Out of scope:** producing the site's production visual-asset library (WP-BWM-0002 owns that), Tier 2-4 narrative development (WP-BWM-0005), community/contact features (WP-BWM-0003), and publishing the finished set anywhere — writing into the site's `docs/media/<slug>/` tree, linking it from a reader page, or posting it to YouTube/TikTok/social. Per media.md, this package never configures or uses Home media services; production is its own authorized step, and promotion to the live site is a separate, later decision.

## Why now

Tier 1 was reviewed and approved by JD for site promotion on 2026-09-12, and WP-BWM-0005 already lists "Narration-ready approved source is handed to ThinxAI" as one of its own pending acceptance criteria and names ThinxAI as owner of "later narrated-media production from approved narrative source text." This package is that handoff, scoped as its own unit of work rather than folded into 0005.

## Acceptance criteria

- [x] Narration script stays within the Tier 1 plain-language standard (no programme acronyms, no specialist vocabulary).
- [x] No human depiction of Christ appears in any visual; visuals respect WP-BWM-0005's theological constraints.
- [x] Rendered output is a valid video file.
- [x] A media.md-conformant manifest exists (source repo/commit, source page/graphics, output revision, approved script reference, duration, language, hosting URL, status, output hash).
- [x] Transcript and WebVTT captions with language metadata are retained.
- [x] Thumbnail with alt text and a link back to the source page is retained.
- [x] Nothing produced here is written into `03-solutions-baseline/site/docs/media/` or linked from a live page.

Revision 3 is public on YouTube as **[Can a Calculated Age Differ From Actual History?](https://youtu.be/gnnMknpuDDQ)**. The external publication decision and Studio verification are owned by WP-BWM-0016.

`package.yaml` owns current status, authority and evidence.

Human-Curated, AI-Enabled (HCAE)
