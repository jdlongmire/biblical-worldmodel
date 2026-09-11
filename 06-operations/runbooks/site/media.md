# Future media integration

Narration is deferred until its source pages and graphics are approved. No render job is launched by the site build.

For each future artifact, retain under the site's `docs/media/<slug>/` directory:

- A manifest identifying source repository, source commit, source page/graphics, output revision, approved script reference, duration, language, hosting URL and current status.
- A text transcript and WebVTT captions (including language metadata).
- A thumbnail with alt text and a link back to the source page.
- Published output hashes where an external media host carries the binary.

Use a native HTML video element with controls, a poster and caption track, or an accessible external embed. Always provide direct playback and transcript links. Audio-only derivatives retain the same provenance and transcript. Large binaries may be hosted separately; provider selection, cost and credentials belong to their own authorized production step.

Narration must preserve uncertainty and canonical programme status. Producing a polished video never elevates a hypothesis into an established result. Never configure or use Home media services from this publication package.
