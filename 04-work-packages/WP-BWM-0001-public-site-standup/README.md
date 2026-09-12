# Biblical WorldModel public site stand-up

**WP-BWM-0001 — deployed and verified; JD acceptance pending.**

[Open the live site](https://worldmodel.thinxai.net/).

The responsive landing page follows the supplied design references and routes four audiences to real reading pages. Search, mathematics, source links, diagrams, mobile navigation and the GitHub-hosted Pages deployment were verified. The repository provides editable Markdown, asset conventions and future media guidance.

[Verification evidence](evidence.md) retains source revision, successful deployment, browser screenshots and a deliberate failed-build control proving deployment is skipped. [Original requirements](requirements.md) remain available. `package.yaml` owns current status.

The ThinxHome transition remains outside scope: no Home service, runner, credential, shared environment or transition branch is used or changed. Full research content, advanced graphics, private contact, embedded discussions and narrated media remain later work; the live site identifies those limits.

## Post-deployment review findings

The following items are now part of WP-BWM-0001 acceptance/disposition rather than separate work packages:

1. **Canonical public domain metadata** — update the MkDocs `site_url` and any derived canonical/OpenGraph/Twitter/structured-data references to `https://worldmodel.thinxai.net/` rather than the native `github.io` URL. Rebuild and verify that generated canonical and social metadata use the custom domain.
2. **Landing-page search verification** — explicitly verify that the custom landing-page search dialog returns useful site-search results. The current form routes through the site source/search path and should be tested independently of the standard Material search UI.
3. **Public URL evidence** — acceptance evidence should record both the canonical public URL (`https://worldmodel.thinxai.net/`) and the underlying GitHub Pages deployment relationship.
4. **Regression check after domain correction** — verify navigation, assets, OpenGraph images, MathJax, and relative links after the canonical-domain update.

These are acceptance defects/verification items for the deployed site baseline. They do not change the scope boundary with WP-BWM-0002 or WP-BWM-0003.

Human-Curated, AI-Enabled (HCAE)

## Canonical-domain correction verified, 2026-09-12

The verifier correction is deployed and live canonical/social metadata checks pass; see [retained evidence](canonical-domain-fix.md). Landing-page search, mobile navigation and MathJax also passed live checks. The subsequently identified tablet overflow is now resolved and verified live at nine viewport widths; see [tablet correction evidence](tablet-overflow-fix.md).

## Homepage mobile styles, 2026-09-12

Captured and resolved BWM-HOME-01 (configured styles omitted by the homepage) and BWM-HOME-02 (missing verification coverage). Mobile hero v2 is now active, with hosted build and live nine-width browser verification passing. See [issue and deployment record](home-styles-integration.md).
