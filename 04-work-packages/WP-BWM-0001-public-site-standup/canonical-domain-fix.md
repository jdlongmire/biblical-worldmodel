# Canonical-domain publication correction

2026-09-12: JD authorized fixing the failed publication and deploying the correction in the active product conversation.

The site URL correction in `0dd7789` exposed a verifier assumption: only root-relative URLs beginning with `/biblical-worldmodel/` were mapped into the build directory. Custom-domain root-relative URLs were interpreted as filesystem-absolute paths. The verifier now derives the deployment base from `mkdocs.yml`, maps root-relative URLs into the build directory, and retains file-existence and containment checks.

Verification in an isolated product worktree using the existing product-specific `/tmp/bwm-site-tools-20260911` environment:

- `python 03-solutions-baseline/site/scripts/verify-build.py`: passed strict build, all 22 generated HTML pages, graphic inclusion/exclusion, and deliberate broken-Markdown-link rejection.
- The build verifier now runs `test-verify-assets.py`: root-domain and project-subpath fixtures pass; missing paths, out-of-base paths, plain and encoded traversal fail as expected.

## Publication and live verification

Correction `424f5ce32e1c0cbdbca26b0ca72d9cc5b70a3c73` deployed successfully in [Actions run 34686012930](https://github.com/jdlongmire/biblical-worldmodel/actions/runs/34686012930).

HTTP checks against `https://worldmodel.thinxai.net/`, `/the-story/`, and `/start-here/` returned 200 and confirmed canonical, OpenGraph URL/image and Twitter image metadata use the custom domain. No old GitHub Pages base URL remained in those three HTML responses. The social image returned HTTP 200.

The standard live-browser regression stopped at its tablet overflow assertion: a 768px viewport has 810px content width. A diagnostic copy retained that measurement instead of asserting, allowing the remaining checks to run: desktop (1440), mobile (390), and small mobile (320) have no horizontal overflow; landing images, mobile menu, real search results, rendered MathJax, and four reader routes passed with no JavaScript or HTTP errors. The diagnostic does not count as a passing full browser suite. Tablet layout remains a separate acceptance defect; this correction changes verifier code only.
 No site content, workflow YAML, DNS, or Home runtime changes are part of this correction.

Human-Curated, AI-Enabled (HCAE)
