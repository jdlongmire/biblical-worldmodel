# Biblical WorldModel website

MkDocs Material with a custom responsive landing page matching the supplied design references. The landing page lives in `overrides/home.html`; styling is in `docs/styles/site.css`. Reader pages are editable Markdown under `docs/`. `mkdocs.yml` owns navigation and theme configuration.

## Build

Use an isolated environment inside this product's site folder, never Home's shared environment:

```sh
python3 -m venv .venv
.venv/bin/pip install -r requirements.txt
.venv/bin/python scripts/verify-build.py
.venv/bin/mkdocs build --strict -f mkdocs.yml -d /tmp/bwm-site
```

The complete build dependency set is pinned in `requirements.txt`. MkDocs remains pinned to 1.6.1; Material to 9.7.7. Update them deliberately together and rerun verification.

## Publication

GitHub Actions builds on relevant changes to `main`, runs strict-build and link checks, uploads the artifact, then deploys using the Pages environment. Pull requests build but cannot deploy. A failed build leaves the previous deployment intact. Pages uses its own GitHub-hosted runner and the default `jdlongmire.github.io/biblical-worldmodel/` address. No Home service, runner, DNS, environment or credential configuration is involved.

The workflow's optional `negative_control=true` dispatch intentionally fails the build job; use it to verify that the deployment job is skipped. The normal input is false.

## Assets

The build hook copies selected `graphics-library/` asset folders into the published `/graphics/` directory. Original reference sheets, provenance metadata and the catalog do not ship as page imagery. Images remain source-resolution PNGs; the responsive HTML owns prose, headings, links and controls. Inline SVG interface icons are code-native, not mislabelled raster crops. Keep technical diagrams source-grounded and preserve alt text and captions.

## Browser verification

Install `playwright==1.62.0` in a separate verification environment and use an available Chromium binary. `scripts/verify-browser.py` currently uses `/usr/bin/chromium` and checks four viewports, navigation, images, search, and mathematical rendering:

```sh
python scripts/verify-browser.py --output /tmp/bwm-browser-evidence
```

Its optional `--built-root` and `--url` arguments intercept requests in the browser for a local artifact check; no local HTTP service is started. MathJax 3.2.2 is loaded from jsDelivr. Landing-page navigation works without this dependency; mathematics on reader pages requires the CDN script.

The community page exposes current public GitHub issue routes. Embedded Discussions, private contact and narration are pending separate work; no non-existent video or private endpoint is advertised as operational.

Human-Curated, AI-Enabled (HCAE)
