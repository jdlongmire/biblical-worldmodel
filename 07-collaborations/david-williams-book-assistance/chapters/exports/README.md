# Chapter exports

Generated document renders of the canonical chapter Markdown, for handing to David Williams as a
reviewable, markup-able file (Word comments/track-changes) rather than raw Markdown.

**The Markdown files one directory up are the source of truth.** Files here are derived,
regenerate-on-change artifacts — if a chapter's Markdown is edited, its export here is stale until
regenerated. Do not hand-edit a `.docx` in this folder and treat that as the authoritative text;
correct the Markdown and re-render.

## Current exports

- `01-the-timing-problem.docx` — rendered from `../01-the-timing-problem.md` (post-assembly,
  commit `3d78665`/`ae3184b`), 19 sections + references, ~7,384 words.
