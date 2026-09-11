# Landing page and GitHub Pages verification — 2026-09-11

**Implemented, deployed and verified. JD acceptance remains separate.**

Live URL: https://jdlongmire.github.io/biblical-worldmodel/

Source revision: `8b666356aca1b2750268218637fdc26fc47bb725`. [Successful hosted run](https://github.com/jdlongmire/biblical-worldmodel/actions/runs/34600015810). [Publication evidence](evidence/publication.json).

## What shipped

Custom responsive HTML landing page using the supplied landscape and audience assets, five guiding principles, four reader journeys, a layered conceptual graphic, public feedback routes and a search dialog. Seventeen supporting Markdown pages provide orientation and explicit preparation notices where substantive treatments are not ready. Native SVG interface icons remain crisp; the extracted PNG landscapes retain their original resolution.

MkDocs Material builds under the product's site directory. Exact Python dependency versions and action commit SHAs are pinned. GitHub-hosted Actions builds, validates and uploads before a separate Pages deployment job. There are no Home runner, DNS, service or credential dependencies.

## Verification

- Strict MkDocs build passed from the clean hosted checkout; all local navigation and resource paths passed across 19 generated HTML pages (18 content pages and the 404 page).
- `scripts/verify-build.py` proved a nonexistent Markdown target causes strict-mode failure, using a temporary negative fixture without modifying real content.
- Live Chromium checks passed at widths 1440, 768, 390 and 320: no horizontal overflow; all landing images loaded; four reader routes reached their real headings; mobile menu opened and closed; all landing images carried alt attributes; the diagram had alt text and a caption.
- Actual landing search for “observation” returned matching documents. MathJax rendered the equation and inline variables on the methodology page. Browser checks reported zero JavaScript errors and zero HTTP errors. [Browser results](evidence/browser-results.json).
- Visually reviewed [desktop](evidence/desktop.png), [mobile](evidence/mobile.png), [search](evidence/search.png), and [mathematics](evidence/mathematics.png). The live desktop/mobile screenshots match the inspected local rendering.
- DFM, CHFM, TRT and LRT repository routes were checked using authenticated GitHub metadata and found public. Their names were cross-checked against Atlas `00-meta-model/assignments.yaml`. Programme pages link outward and explicitly leave technical claims/status with those sources; no fresh scientific validation is claimed.
- [Deliberate hosted failure control](https://github.com/jdlongmire/biblical-worldmodel/actions/runs/34600082664): build failed at the named negative-control step, artifact creation/upload were skipped, and deployment was skipped. The live page remained HTTP 200 and byte-identical to the verified local artifact afterwards. This failed run is expected test evidence, not an unresolved production failure.
- Product worktree/path checks and the clean session-wrap gate passed before publication. Builds used isolated product tooling and hosted runners. No Home files, service state, global dependencies, configuration or transition branches were changed by this task.

## Scope and handoff

Written content remains editable Markdown; landing layout/copy resides in `overrides/home.html`. The site README documents this split, build commands, exact dependencies, publication, asset copying and browser verification. `06-operations/runbooks/site/media.md` specifies future source-revision manifests, transcripts, captions, thumbnails and playback conventions.

No video, private contact provider, embedded Giscus/Discussions, or narrated-media pipeline is presented as live. Public interaction currently uses GitHub issues. Those community/production features remain later scoped work. Original mockups are not deployed as whole-page images. Low-resolution source crops have not been presented as full-resolution originals; advanced diagrams and asset-production approval remain WP-BWM-0002 work.

The evidence is ready for the bridge/content handoff in this canonical product record; no separate email or chat was sent. Framework/deployment approach follows the official [Material customization](https://squidfunk.github.io/mkdocs-material/customization/) and [GitHub Pages workflow](https://docs.github.com/en/pages/getting-started-with-github-pages/using-custom-workflows-with-github-pages) documentation, checked during implementation.

Human-Curated, AI-Enabled (HCAE)
