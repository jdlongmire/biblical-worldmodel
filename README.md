# Biblical WorldModel

A public home for exploring Scripture, observations, historical interpretation, and the research programmes informing the Biblical WorldModel.

**Repository foundation established. The public website is not deployed yet.**

This repository is the public explanation and navigation layer. Technical programme claims remain authoritative in their Atlas-designated research repositories. An accessible explanation, graphic, or narration must preserve its source's status and uncertainty.

## Repository structure

Created from `jdlongmire/longmire-repo-template`; the `00`–`06` structure is retained:

- `00-meta-model/`: work model, repository profile and layout decisions.
- `01-strategic-baseline/`: audience, purpose and objectives.
- `02-systems-baseline/`: requirements, architecture, interfaces and verification.
- `03-solutions-baseline/`: future site implementation under `site/`.
- `04-work-packages/`: delivery backlog and migrated bridge requirements.
- `05-mxm-construct/`: repository-scoped guidance and continuity; no new assistant runtime.
- `06-operations/`: contribution and recovery instructions.

## Work remaining

| Package | Work | State |
|---|---|---|
| [WP-BWM-0001](04-work-packages/WP-BWM-0001-public-site-standup/README.md) | MkDocs Material site and GitHub Actions → Pages | Planned |
| [WP-BWM-0002](04-work-packages/WP-BWM-0002-visual-assets/README.md) | Responsive visual assets | Planned |
| [WP-BWM-0003](04-work-packages/WP-BWM-0003-community-contact/README.md) | Community interaction and private contact | Planned |
| [WP-BWM-0004](04-work-packages/WP-BWM-0004-repository-foundation/README.md) | Template foundation and backlog transfer | See package evidence |

Narrated-media conventions belong to 0001; actual narration production remains deferred until approved site content and graphics are stable. Nothing here deploys Home services or acquires Home credentials.

## Checks

Requires Git and Python 3.10+; foundation checks need no third-party packages.

```sh
python3 00-meta-model/verify-repository-layout.py
python3 -m unittest discover -s 00-meta-model -p 'test_*.py'
python3 -m unittest discover -s 05-mxm-construct/means/scripts/tests
python3 05-mxm-construct/means/scripts/session-wrap.py
```

See [onboarding](06-operations/runbooks/ONBOARDING.md) and [migration provenance](04-work-packages/WP-BWM-0004-repository-foundation/migration.json).

Human-Curated, AI-Enabled (HCAE)
