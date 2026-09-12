# Biblical WorldModel

**God’s Word. God’s world.**

Biblical WorldModel explores how to understand the world in light of Scripture and what we observe. It begins with a plain-language story, then offers routes into evidence, historical interpretation, objections, and the research programmes behind the framework.

**[Visit the website](https://worldmodel.thinxai.net/) · [Read the story](https://worldmodel.thinxai.net/the-story/) · [Choose your path](https://worldmodel.thinxai.net/start-here/)**

A project of **J. D. Longmire**, part of the [oddXian](https://oddxian.com) portfolio.

## Start exploring

The public explanation begins with two questions: **How much was already there when God made the world? What happened after that?** It introduces the distinction between a starting state and subsequent history through concrete examples before moving into technical vocabulary.

| Your interest | Start here |
|---|---|
| A plain-language introduction | [The Story](https://worldmodel.thinxai.net/the-story/) |
| Observations and their interpretation | [Evidence](https://worldmodel.thinxai.net/evidence/) |
| The framework and its foundations | [The WorldModel](https://worldmodel.thinxai.net/worldmodel/) and [Methodology](https://worldmodel.thinxai.net/methodology/) |
| Critical examination | [Objections](https://worldmodel.thinxai.net/objections/) and [Open Problems](https://worldmodel.thinxai.net/open-problems/) |
| Technical arguments and sources | [Research Programmes](https://worldmodel.thinxai.net/research-programmes/) and [Sources & Glossary](https://worldmodel.thinxai.net/sources/) |

## What this repository owns

This is the source repository for the **public explanation and publication site**: reader pages, navigation, visual presentation, selected graphics, build tooling, and the delivery backlog.

Scripture is the framework’s stated authority. Scientific explanations and historical reconstructions remain open to scrutiny. Public content must distinguish observation, interpretation, assumptions, and unresolved problems; accessibility must preserve the source’s uncertainty rather than strengthen its claims.

Technical programme claims remain authoritative in their own research repositories. The [programme index](03-solutions-baseline/site/docs/research-programmes.md) links to Designed Functional Maturity (DFM), the Catastrophic Hydrotectonic Flood Model (CHFM), Triadic Reality Theory (TRT), and Logic Realism Theory (LRT). This publication layer does not replace those sources or imply that every programme claim is established.

## Current status

As of **September 12, 2026**, the site is live at **https://worldmodel.thinxai.net/** and publishes through GitHub Actions to GitHub Pages.

- The approved Tier 1 story is published and featured on the homepage.
- Responsive navigation, site search, mathematical rendering, and selected graphics are implemented. Retained live-browser checks cover nine viewport widths from 320 to 1440px.
- Canonical-domain metadata, tablet navigation overflow, and mobile hero stylesheet integration have been corrected and verified. Evidence is retained in [WP-BWM-0001](04-work-packages/WP-BWM-0001-public-site-standup/README.md).
- Tier 2 material is in development. Captured notes are not an approved public explainer.
- Public participation currently uses GitHub Issues. Embedded discussion, dedicated private contact, and narrated media remain future work.

Verification records describe the revisions checked; they do not establish human acceptance of every work package or guarantee future revisions.

## Find the right file

| Area | Purpose |
|---|---|
| [Site content](03-solutions-baseline/site/docs/) | Reader-facing Markdown pages, page metadata, styles and scripts |
| [Site configuration](03-solutions-baseline/site/mkdocs.yml) | Navigation, canonical URL, theme, ordered stylesheets and extensions |
| [Page templates](03-solutions-baseline/site/overrides/) | Custom homepage and reader-page overrides |
| [Graphics library](graphics-library/README.md) | Source assets, catalog and provenance; selected folders are copied into the site during builds |
| [Build and browser checks](03-solutions-baseline/site/scripts/) | Strict builds, path checks, stylesheet integration and browser verification |
| [Publication workflow](.github/workflows/pages.yml) | GitHub-hosted build and Pages deployment |
| [Work packages](04-work-packages/README.md) | Scope, requirements, progress, evidence and disposition |

The repository retains its `00`–`06` structure from [longmire-repo-template](https://github.com/jdlongmire/longmire-repo-template):

| Directory | Responsibility |
|---|---|
| [00-meta-model](00-meta-model/) | Work model, repository profile and structural checks |
| [01-strategic-baseline](01-strategic-baseline/) | Purpose, audiences, objectives and alignment |
| [02-systems-baseline](02-systems-baseline/) | Requirements, architecture, interfaces and verification |
| [03-solutions-baseline](03-solutions-baseline/) | Implemented website and its dependencies |
| [04-work-packages](04-work-packages/) | Governed delivery work and evidence |
| [05-mxm-construct](05-mxm-construct/) | Repository working guidance and continuity |
| [06-operations](06-operations/) | Contributor, publication, recovery and media runbooks |

## Build and verify

Run these commands from the repository root. Use Git and Python 3.11 to match hosted CI, with an isolated virtual environment. The complete site dependency set is pinned; no shared application environment is needed.

```sh
python3 -m venv .venv
.venv/bin/python -m pip install -r 03-solutions-baseline/site/requirements.txt
.venv/bin/python 03-solutions-baseline/site/scripts/verify-build.py
.venv/bin/python -m mkdocs build --strict -f 03-solutions-baseline/site/mkdocs.yml -d /tmp/bwm-site
```

`verify-build.py` checks strict generation, local links and resources, required graphics, and configured homepage stylesheets in order. Negative controls prove that broken Markdown links and missing stylesheet integration are rejected. Generated output belongs outside the tracked source tree.

Repository checks require no third-party Python packages:

```sh
python3 00-meta-model/verify-repository-layout.py
python3 -m unittest discover -s 00-meta-model -p 'test_*.py'
python3 -m unittest discover -s 05-mxm-construct/means/scripts/tests
python3 05-mxm-construct/means/scripts/session-wrap.py
```

For UI changes, also run [browser verification](03-solutions-baseline/site/README.md#browser-verification). It requires Playwright and Chromium separately from the build dependencies. It can inspect a built artifact through browser request interception without starting an HTTP server, or check the deployed site. It exercises responsive layout, menus, mobile hero spacing, images, search, mathematics and reader routes.

## Publish changes

Relevant changes to `main` trigger the [Pages workflow](.github/workflows/pages.yml). It validates the build, creates and checks the publication artifact, then deploys. Pull requests build without deploying. If the build fails, deployment is skipped and the previous publication remains live.

Before publishing, review the change and run its applicable checks. After publication, verify the exact commit’s [Actions run](https://github.com/jdlongmire/biblical-worldmodel/actions) and live behavior. A successful build alone does not prove that a visual change is loaded by the page.

See the [publication and recovery runbook](06-operations/runbooks/site/publication.md) for failure handling and the deliberate failed-build control. This product uses GitHub-hosted infrastructure; changes to the assistant’s Home runtime, services, credentials or shared environments are outside this repository’s scope.

## Roadmap

| Package | Current delivery position | Remaining work |
|---|---|---|
| [0001: Public site](04-work-packages/WP-BWM-0001-public-site-standup/README.md) | Deployed; verification evidence retained | Complete outstanding acceptance/disposition |
| [0002: Visual assets](04-work-packages/WP-BWM-0002-visual-assets/README.md) | Draft extraction complete; selected assets integrated | Production approval, mobile-specific hero artwork and responsive delivery |
| [0003: Community and contact](04-work-packages/WP-BWM-0003-community-contact/README.md) | GitHub Issues provides interim public intake | Discussions/embedded conversation, structured intake, moderation and private contact |
| [0004: Repository foundation](04-work-packages/WP-BWM-0004-repository-foundation/README.md) | Foundation and backlog transfer verified | Retained acceptance/disposition |
| [0005: Accessible narrative](04-work-packages/WP-BWM-0005-accessible-narrative/README.md) | Tier 1 approved and published; Tier 2 principles captured | Short form, Tier 2 explainer, verified dating case studies, reader variants and storyboard |
| [0006: Video narration](04-work-packages/WP-BWM-0006-video-narration/README.md) | Proposed; opened once Tier 1 was approved | Script, storyboard, render, and the media.md provenance set; no production started |
| [0007: Ross/RTB DFM harvest](04-work-packages/WP-BWM-0007-ross-dfm-harvest/README.md) | Proposed backlog | Source-family survey and primary-trace harvest; no work started |

Package records own detailed scope and evidence. Narration remains deferred until source content and graphics are approved; [media conventions](06-operations/runbooks/site/media.md) define the future provenance, transcript and caption requirements — WP-BWM-0006 is scoped to produce that exact set without promoting it into the live site.

## Contribute, question or challenge

[Open an issue](https://github.com/jdlongmire/biblical-worldmodel/issues/new) for questions, objections, corrections or collaboration proposals. Identify the page or claim, explain the concern, and include primary sources where possible. Substantive disagreement is welcome; address arguments rather than people. Issues are public, so do not include private or sensitive information. A dedicated private-contact route is not active yet.

For code or content contributions, use an isolated branch/worktree, keep the change focused, preserve source provenance, and include verification evidence in your pull request. Consult [contributor onboarding](06-operations/runbooks/ONBOARDING.md), the [site development guide](03-solutions-baseline/site/README.md), and the relevant work package.

AI contributors start with [AGENTS.md](AGENTS.md) and [MXM.md](MXM.md). J. D. Longmire holds project acceptance authority; repository guidance does not create a new assistant identity or grant access to other systems.

Human-Curated, AI-Enabled (HCAE)
