# Biblical WorldModel public site stand-up

**WP-BWM-0001 — planned; implementation pending.**

Create an accessible public home for Biblical WorldModel with four depths of reading, clear links to canonical research, responsive diagrams, search and mathematics. Use MkDocs Material and GitHub-hosted Actions deploying to GitHub Pages. The site explains research; it does not own its technical claims.

## Protecting ThinxHome

JD explicitly directed that this work must not interrupt or clash with the transition. Work lives in this separate product repository and dedicated branch/worktree. Dependencies are product-local; builds and hosting run on GitHub. Home services, CI, authentication, credentials, tunnels, shared environments, live files and transition branches are outside scope. Home retains priority. Any newly discovered shared dependency pauses that dependent step for discussion.

## Delivery sequence

1. Build the navigation and reader journeys, with honest placeholders where content is pending.
2. Validate responsive assets, mathematics, search, canonical links and a clean build.
3. Publish through the product's own Actions/Pages path during authorized execution.
4. Retain deployment and browser evidence and prepare the bridge handoff for JD disposition.

Media manifests, captions, transcripts and embedding conventions belong in this phase. Narration and GPU production are deferred. Existing mockups are design references; actual text and controls remain responsive HTML.

## Source and status

Source: `jdlongmire/chatgpt-bridge`, WP-BRIDGE-0002 and its asset workspace, revision `dbe28033690be777aaf0a7f0e5e5bd2fa95b1916`. `package.yaml` contains scope, nine acceptance criteria, verification methods and evidence requirements; `execution.json` bounds writable paths.

The repository foundation and bridge transfer are tracked separately by WP-BWM-0004. [Imported requirements](requirements.md) preserve the complete source scope and checklist. Site implementation belongs under `03-solutions-baseline/site/`, per ADR-BWM-0001.

This package has no completed implementation criteria. Planned verification scripts will be created and exercised during implementation. The public repository is established by WP-BWM-0004; no site is deployed. Repository creation and source transfer do not complete site acceptance.

Human-Curated, AI-Enabled (HCAE)
