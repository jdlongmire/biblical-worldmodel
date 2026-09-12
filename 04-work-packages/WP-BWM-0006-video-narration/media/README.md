# Video narration storage — WP-BWM-0006

The in-repo storage spot for this package's video-narration evidence, established 2026-09-12. One subdirectory per narrated piece, named by slug (e.g. `the-story/`).

## What lives here

Per `06-operations/runbooks/site/media.md`'s convention, each `<slug>/` directory holds:

- `manifest.json` — source repository, source commit, source page/graphics, output revision, approved script reference, duration, language, hosting URL, status, output hash.
- `transcript.md` — the full spoken-word transcript.
- `captions.vtt` — WebVTT captions with language metadata.
- `thumbnail.png` — a thumbnail with alt text and a link back to the source page.
- `draft.md` — a copy of (or pointer to) the approved narration draft from the video-narration factory repo, so the review record travels with the package rather than living only in the factory repo's own `drafts/`.

## What does NOT live here

**The rendered video file itself is not committed to this repository.** Video binaries are large, git handles them poorly, and `06-operations/runbooks/site/media.md` already directs "large binaries may be hosted separately." The rendered MP4 is delivered to Console Drive Artifacts (the standing SOP for thinx's video-narration factory) and its `hosting_url` and content hash are recorded in `manifest.json` — that hash is how a reader confirms which binary a given manifest entry actually describes, without the binary living in git history.

## What this is not

This is **not** the site's live media directory. `03-solutions-baseline/site/docs/media/<slug>/` is the eventual *published* location, and WP-BWM-0006's authority boundary explicitly does not authorize writing there — this directory is pre-publication work-package evidence only. Promoting a narrated piece from here into the live site is a separate, later, explicitly authorized step.

Human-Curated, AI-Enabled (HCAE)
