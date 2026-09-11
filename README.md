# longmire-repo-template

A new personal aide starts with thinx's current **Meta-Harness** structure:

```text
00-meta-model/          work model, architecture, repo decisions and profiles
01-strategic-baseline/  vision, strategy, objectives, alignment
02-systems-baseline/    requirements, architecture, behavior, interfaces, verification
03-solutions-baseline/  released solution descriptions
04-work-packages/       bounded delivery records
05-mxm-construct/
  meta-harness/        Mission, Mind, Morals, Memory/Methods pointers, profile
  memory/              durable notes, wiki, current session focus
  means/               canonical README and executable scripts/tests
06-operations/         capability inventory, onboarding and recovery
AGENTS.md              cross-harness adapter with explicit Codex loading
CLAUDE.md              imports AGENTS.md
MXM.md                 canonical framework declaration
MEMORY.md              operational memory index
README.md              human entry point
```

.gitignore and optional .github/.claude adapter folders are also allowed.
There are no separate root decisions/, profiles/, flat MxM files or 04-construct/.
The template deliberately ships a real Meta-Harness profile. The previous
General Work default is superseded by [ADR-LAYOUT-0002](00-meta-model/ADR-LAYOUT-0002-thinx-root-parity.md).

## Create an aide

Use GitHub's template action or your authenticated CLI:

```text
gh repo create OWNER/NAME --private --template jdlongmire/longmire-repo-template --clone
cd NAME
python 00-meta-model/verify-repository-layout.py
python 05-mxm-construct/means/scripts/session-start.py
```

Requires Python 3.10+ and Git; use python3 where appropriate. No third-party
Python packages. The template contains no principal identity, personal memory,
credentials, live services or inherited account permissions.

Before operational use, set aide_name, principal_operator and repository_owner
in [profile.json](05-mxm-construct/meta-harness/profile.json) from confirmed
human instructions. Replace the generic personal-aide profile label in MXM.md
and record the decision. Customize Mission and priorities; keep unknowns explicit.
Then follow [onboarding](06-operations/runbooks/ONBOARDING.md).
UNCONFIGURED means no operator authority has been established.

## Validate and maintain

```text
python -m unittest discover -s 00-meta-model -p 'test_*.py'
python -m unittest discover -s 05-mxm-construct/means/scripts/tests
python 05-mxm-construct/means/scripts/session-wrap.py
```

The layout gate rejects unexpected roots, missing baselines, shadow contracts
and broken adapter chains. The session gate invokes it; wrap also requires a
clean Git tree. These are explicit checks, not installed tool hooks or CI.
Tests establish local code behavior; validate actual instruction loading in a
fresh session on the target harness. No full thinx console or service is bundled.

Human-Curated, AI-Enabled (HCAE)
