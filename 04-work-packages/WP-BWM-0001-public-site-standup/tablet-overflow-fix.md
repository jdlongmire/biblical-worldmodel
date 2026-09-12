# Tablet navigation overflow correction

2026-09-12: JD directed fixing the tablet overflow recorded during canonical-domain verification. Implementation and publication stay within the product repository.

At 768px, the expanded main navigation extended to 809.875px. The menu previously collapsed only at 760px. Header/menu rules now apply through 960px, while the existing content-layout breakpoint remains 760px. No overflow clipping is used.

Verification before publication, in an isolated product worktree with the existing product-specific `/tmp/bwm-site-tools-20260911` environment:

- `scripts/verify-build.py`: strict build, path regression tests, all 22 HTML pages, required graphics and negative broken-link control passed.
- `mkdocs build --strict` and `scripts/verify-browser.py --url https://worldmodel.thinxai.net/ --built-root /tmp/bwm-tablet-build --output /tmp/bwm-tablet-preview`: passed at 1440, 961, 960, 820, 768, 761, 760, 390 and 320px. No horizontal overflow with menus closed or open. Menu open/Escape close and story-link visibility passed through 960px. Search, MathJax, images and four reader routes passed; no JavaScript or HTTP errors.
- Visually inspected the full tablet screenshot: header controls and content fit the viewport.

The browser checker now supports root-domain build interception and retains the extra breakpoint checks. Publication and live verification follow this commit.

Human-Curated, AI-Enabled (HCAE)
