# Chapter exports

Generated document renders of the canonical chapter Markdown, for handing to David Williams as a
reviewable, markup-able file (Word comments/track-changes) rather than raw Markdown.

**The Markdown files one directory up are the source of truth.** Files here are derived,
regenerate-on-change artifacts — if a chapter's Markdown is edited, its export here is stale until
regenerated. Do not hand-edit a `.docx` in this folder and treat that as the authoritative text;
correct the Markdown and re-render.

Rendered with productivity-suite's `manuscript` brand kit (`brand/manuscript.yaml`) — Times New
Roman, black text, double-spaced, page numbers, no color/logo chrome. See methods-approach.md §14
for why this is the export baseline rather than the default `general` (business/deck) kit.

## Current exports

- `01-the-timing-problem.docx` — rendered from `../01-the-timing-problem.md` (post voice-fix,
  commit `64d031e`), 19 sections + references, ~7,376 words, `manuscript` brand kit.
