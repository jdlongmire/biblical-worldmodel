# Homepage stylesheet integration issues

2026-09-12: JD directed capturing and fixing issues found in the collaborating changes. This correction implements the existing mobile hero v2 design, within the product publication scope.

## BWM-HOME-01: configured styles absent from custom homepage

The standalone homepage template linked only `styles/site.css`, ignoring MkDocs `extra_css`. The deployed mobile hero v2 stylesheet therefore did not affect the homepage even though its build succeeded. At 390px the old hero minimum height was 730px with 260px top padding.

Correction: render `config.extra_css` in configured order through MkDocs' URL filter. This loads the base stylesheet, scoped link-contrast rules, and the selected mobile hero v2 override. The unused first hero draft remains historical source; it is not activated.

## BWM-HOME-02: missing stylesheet not detected by verification

Existing link checks caught missing files but not omitted stylesheet references. A deployment could be green while the intended design was never loaded.

Correction: the hosted build verifier compares generated homepage stylesheet URLs and order against configuration. A negative control supplies a homepage lacking configured styles and must fail. Browser verification additionally checks that mobile hero top padding is no more than 80px, catching the previous 260/280px layout.

## Verification

In the isolated product worktree, using `/tmp/bwm-site-tools-20260911`:

- `scripts/verify-build.py` passed strict generation of 22 pages, configured stylesheet order, missing-stylesheet negative control, asset paths, and broken-link rejection.
- `scripts/verify-browser.py --url https://worldmodel.thinxai.net/ --built-root /tmp/bwm-styles-build --output /tmp/bwm-styles-preview` checks nine viewports, menu behavior, hero spacing, search, MathJax, images and reader routes.
- Mobile screenshot inspected: copy appears near the top of the hero and both primary actions are visible without the former large leading gap.

Publication and live verification follow the implementation commit. No DNS, Home runtime or narrative-content changes.

Human-Curated, AI-Enabled (HCAE)
