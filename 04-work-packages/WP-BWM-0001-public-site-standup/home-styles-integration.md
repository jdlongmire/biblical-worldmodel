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

## Disposition

Both BWM-HOME-01 and BWM-HOME-02 are resolved. Implementation `4ff9a4f3308fe12c185a805bc0175cbc4c1d7d10` deployed in [successful Actions run 34687531623](https://github.com/jdlongmire/biblical-worldmodel/actions/runs/34687531623).

The full browser suite passed against `https://worldmodel.thinxai.net/` at all nine widths, including mobile hero top padding at or below 80px, no overflow, navigation, search, MathJax and reader routes, with no JavaScript or HTTP errors. Initial concurrent browser probes hit local thread/resource limits; a sequential rerun passed. The earlier local preview suite also passed. Deployment success is supported by actual live behavior, not only the workflow result.
 No DNS, Home runtime or narrative-content changes.

Human-Curated, AI-Enabled (HCAE)
