# Biblical WorldModel

**God’s Word. God’s world.**

Biblical WorldModel (BWM) is an integrative research and publication programme for examining creation, history, nature, and human experience under a Scripture-first epistemic framework. It distinguishes what Scripture states, what observation establishes, what models infer, and what remains unresolved.

**[Visit the live site](https://worldmodel.thinxai.net/) · [Read the story](https://worldmodel.thinxai.net/the-story/) · [Start here](https://worldmodel.thinxai.net/start-here/)**

**James (JD) Longmire**  
Senior Technical Fellow, Aerospace and Defense Sector  
ORCID: [0009-0009-1383-7698](https://orcid.org/0009-0009-1383-7698)  
Correspondence: jdlongmire@outlook.com

Part of the [oddXian](https://oddxian.com) portfolio. See [`AUTHOR.md`](AUTHOR.md) for the canonical repository author/correspondence block.

## What this repository owns

This repository is the BWM integration and publication layer. It owns:

- the public Biblical WorldModel website and reader-facing publications;
- BWM-specific requirements, architecture, interfaces, integration artifacts, and canonicalized synthesis;
- governed work packages, evidence, and disposition records;
- graphics and publication assets used by BWM;
- repository-scoped MxM guidance and operational runbooks.

Some technical research programmes retain their own authoritative repositories. BWM consumes those programmes through explicit interfaces and does not silently fork their source-of-truth research. In particular, TRT, LRT, Semantic Actualism, DFM, CHFM, FCD, and CAC remain authoritative in their designated research repositories. BWM records the interfaces, implications, cross-domain constraints, and public synthesis needed by the WorldModel.

## Intellectual architecture

BWM separates its substantive content into four categories. The accepted architecture is defined in [`bwm-component-architecture.md`](02-systems-baseline/2.2-architecture/bwm-component-architecture.md).

| Category | Role | Current examples |
|---|---|---|
| **Foundations** | Governing ontology, epistemology, and hermeneutics | TRT/LRT/SA programme interfaces, Scripture-first epistemic hierarchy |
| **Historical intervals, boundaries, and hypotheses** | BWM historical categories and hypotheses, informed by programme interfaces | creation/initialization boundary [DFM], pre-Fall interval [PFH hypothesis space], Flood boundary [CHFM] |
| **World Domains** | Subject-matter areas to which foundations and frameworks are applied | Cosmology, Earth history/geology, biology, anthropology, archaeology/chronology, covenant/redemptive history |
| **Integration** | Cross-framework and cross-domain synthesis | invariants, framework/domain mapping, chronology, evidence ledgers, model comparison, open problems, predictions and falsifiers |

The current historical backbone is:

`Foundations -> creation/initialization [DFM] -> pre-Fall interval [PFH hypothesis space] -> Fall -> post-Fall/pre-Flood history -> Flood catastrophe [CHFM] -> post-Flood history -> covenant/redemptive history -> consummation`

This is a historical sequence, not a hierarchy. Foundations apply across every stage.

## Epistemic discipline

Scripture is BWM’s primary epistemic authority for biblical-historical claims. Nature supplies real evidence and is interpreted within that framework. BWM therefore keeps several categories distinct:

- textual datum and warranted textual inference;
- observation and operational measurement;
- model assumption and explanatory inference;
- retrodictive age and actual elapsed history;
- accepted architecture and active hypothesis;
- established result and unresolved tension.

Scientific explanations, historical reconstructions, and BWM hypotheses remain open to scrutiny. Accessibility does not authorize strengthening a source beyond its evidence.

## Start exploring

| Your interest | Start here |
|---|---|
| Plain-language introduction | [The Story](https://worldmodel.thinxai.net/the-story/) |
| Observations and interpretation | [Evidence](https://worldmodel.thinxai.net/evidence/) |
| Framework and methodology | [The WorldModel](https://worldmodel.thinxai.net/worldmodel/) and [Methodology](https://worldmodel.thinxai.net/methodology/) |
| Current research programmes | [Research Programmes](https://worldmodel.thinxai.net/research-programmes/) |
| Published BWM articles | [Publications](03-solutions-baseline/site/docs/publications/articles/index.md) |
| Critical examination | [Objections](https://worldmodel.thinxai.net/objections/) and [Open Problems](https://worldmodel.thinxai.net/open-problems/) |
| Canonical component architecture | [BWM Component Architecture](02-systems-baseline/2.2-architecture/bwm-component-architecture.md) |
| Active and completed delivery work | [Work Package Register](04-work-packages/README.md) |

## Repository map

BWM retains the `00`–`06` operating structure inherited from [longmire-repo-template](https://github.com/jdlongmire/longmire-repo-template). This lifecycle structure is independent of the intellectual architecture above.

| Directory | Responsibility |
|---|---|
| [`00-meta-model/`](00-meta-model/) | Work model, repository architecture, decisions, and structural verification |
| [`01-strategic-baseline/`](01-strategic-baseline/) | Vision, strategy, objectives, and alignment |
| [`02-systems-baseline/`](02-systems-baseline/) | Requirements, canonical architecture, interfaces, behavior, and verification |
| [`03-solutions-baseline/`](03-solutions-baseline/) | Implemented BWM publication product and site |
| [`04-work-packages/`](04-work-packages/) | Governed delivery/research work, evidence, provenance, and disposition |
| [`05-mxm-construct/`](05-mxm-construct/) | Repository-scoped MxM guidance, memory, means, and meta-harness material |
| [`06-operations/`](06-operations/) | Contributor, publication, recovery, and operational runbooks |
| [`graphics-library/`](graphics-library/README.md) | Source graphics, catalog, and provenance |

Important front-door files:

- [`AUTHOR.md`](AUTHOR.md) — canonical author and correspondence metadata;
- [`AGENTS.md`](AGENTS.md) — repository instructions for AI agents;
- [`MXM.md`](MXM.md) — repository MxM bootstrap and continuity contract;
- [`04-work-packages/README.md`](04-work-packages/README.md) — current work register;
- [`02-systems-baseline/2.2-architecture/README.md`](02-systems-baseline/2.2-architecture/README.md) — canonical architecture index;
- [`03-solutions-baseline/site/README.md`](03-solutions-baseline/site/README.md) — detailed site implementation and verification guide;
- [`06-operations/README.md`](06-operations/README.md) — operational entry point.

## Current product state

The public site is live at **https://worldmodel.thinxai.net/** and is built from this repository with MkDocs Material and GitHub Actions/GitHub Pages. Reader content, publications, navigation, responsive presentation, search, mathematics, and selected graphics are maintained under the Solutions Baseline.

BWM remains an active research programme. Canonicalized material and accepted architecture coexist with open hypotheses, unresolved questions, and proposed work. The authoritative delivery/status view is the [work-package register](04-work-packages/README.md); individual work packages retain detailed scope, evidence, verification, and disposition.

## Build and verify

The detailed implementation guide is [`03-solutions-baseline/site/README.md`](03-solutions-baseline/site/README.md). From the repository root, the primary site verification path is:

```sh
python3 -m venv .venv
.venv/bin/python -m pip install -r 03-solutions-baseline/site/requirements.txt
.venv/bin/python 03-solutions-baseline/site/scripts/verify-build.py
.venv/bin/python -m mkdocs build --strict -f 03-solutions-baseline/site/mkdocs.yml -d /tmp/bwm-site
```

Repository structural checks are maintained under [`00-meta-model/`](00-meta-model/). Browser verification and publication/recovery procedures remain in the site guide and [`06-operations/runbooks/`](06-operations/runbooks/), rather than being duplicated here.

Changes to `main` that affect the site are evaluated by the GitHub Pages workflow. Pull requests build without deploying; accepted changes to `main` may publish through the configured Pages environment.

## Contribute, question, or challenge

[Open a GitHub issue](https://github.com/jdlongmire/biblical-worldmodel/issues/new) for questions, objections, corrections, or collaboration proposals. Identify the page or claim, explain the concern, and provide primary sources where possible. Issues are public, so do not include private or sensitive information.

For code or content contributions, use an isolated branch/worktree, preserve source provenance, keep claims within their evidence, and include applicable verification evidence. See [`06-operations/runbooks/ONBOARDING.md`](06-operations/runbooks/ONBOARDING.md) and the relevant work package.

AI contributors begin with [`AGENTS.md`](AGENTS.md) and [`MXM.md`](MXM.md). J. D. Longmire retains project acceptance authority. Repository guidance does not create a separate assistant identity or grant access to external systems.

## License and reuse

See [`LICENSE`](LICENSE) for the controlling scope. Original published/shared content is licensed under **CC BY 4.0** and original reusable code under **MIT** where specified. Private records, drafts, staged material, and third-party works are excluded; existing third-party licenses and notices remain in force.

Human-Curated, AI-Enabled (HCAE)
