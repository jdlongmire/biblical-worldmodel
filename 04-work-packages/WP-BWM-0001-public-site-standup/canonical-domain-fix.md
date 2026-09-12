# Canonical-domain publication correction

2026-09-12: JD authorized fixing the failed publication and deploying the correction in the active product conversation.

The site URL correction in `0dd7789` exposed a verifier assumption: only root-relative URLs beginning with `/biblical-worldmodel/` were mapped into the build directory. Custom-domain root-relative URLs were interpreted as filesystem-absolute paths. The verifier now derives the deployment base from `mkdocs.yml`, maps root-relative URLs into the build directory, and retains file-existence and containment checks.

Verification in an isolated product worktree using the existing product-specific `/tmp/bwm-site-tools-20260911` environment:

- `python 03-solutions-baseline/site/scripts/verify-build.py`: passed strict build, all 22 generated HTML pages, graphic inclusion/exclusion, and deliberate broken-Markdown-link rejection.
- The build verifier now runs `test-verify-assets.py`: root-domain and project-subpath fixtures pass; missing paths, out-of-base paths, plain and encoded traversal fail as expected.

Publication and live metadata verification are the remaining delivery steps at this commit. No site content, workflow YAML, DNS, or Home runtime changes are part of this correction.

Human-Curated, AI-Enabled (HCAE)
