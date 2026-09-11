# WP-BRIDGE-0002 Companion: Community Interaction and Contact Architecture

**Status:** ACTIVE DESIGN INPUT  
**Parent work package:** [`WP-BRIDGE-0002-biblical-worldmodel-publication.md`](../WP-BWM-0001-public-site-standup/requirements.md)  
**Operational owner:** ThinxAI / thinx  
**Content/workflow owner:** ChatGPT with JD oversight  
**Target repository:** `jdlongmire/biblical-worldmodel`

## Purpose

Define how the Biblical WorldModel site should support public discussion, substantive objections, error reporting, research collaboration, and private contact without turning the site into an unmanaged social feed or creating a second source of truth.

The interaction model should preserve traceability from public engagement into the bridge and, where warranted, into the canonical research programmes.

## Interaction Channels

| Need | Recommended channel | Rationale |
|---|---|---|
| Public page discussion | GitHub Discussions, embedded with Giscus where practical | Durable, moderated, repository-native discussion without maintaining a custom database |
| Ask a question | GitHub Discussion template | Encourages public, reusable answers |
| Submit an objection | Structured GitHub Discussion or Issue template | Captures target claim, argument, evidence, and requested disposition |
| Report factual/source/site error | GitHub Issue template | Creates actionable maintenance record |
| Research collaboration | Dedicated Discussion category and/or contact form category | Separates serious collaboration from general comments |
| Private contact | Static-site contact form routed to a dedicated project inbox, with email fallback | Supports non-public communication on a static GitHub Pages site |

## Recommended Public Actions

Expose these actions consistently in the site footer and on relevant pages:

- **Discuss**
- **Ask a Question**
- **Submit an Objection**
- **Report an Error**
- **Research Collaboration**
- **Contact Us**

The wording may be refined for final design, but the functional separation should remain.

## GitHub Discussions Architecture

Recommended initial categories:

| Category | Purpose |
|---|---|
| Questions | General reader questions about the Biblical WorldModel |
| Objections | Substantive challenges to claims, models, or inferences |
| Research Discussion | Technical or scholarly engagement with canonical programmes |
| Site Feedback | Usability, navigation, accessibility, or presentation feedback |
| Announcements | Maintainer-controlled publication updates if needed |

### Giscus / Embedded Comments

Where practical, substantive pages may embed discussion through Giscus backed by GitHub Discussions.

Implementation requirements:

- map each page to a stable discussion thread or mapping mode;
- avoid creating duplicate threads on URL changes where practical;
- support light/dark theme integration;
- make GitHub authentication requirements clear;
- provide a direct link to the underlying Discussion for readers who prefer GitHub-native interaction;
- allow comments to be disabled on pages where discussion adds little value.

## Structured Objection Intake

A public objection should capture enough information to distinguish a serious challenge from a generic assertion.

Recommended fields:

1. **Target claim or page**
2. **Objection in one sentence**
3. **Full argument**
4. **Evidence / primary source / citation**
5. **Why the objection matters**
6. **What result the submitter believes follows**
7. **Whether this appears to duplicate an existing objection**

The public form/template should not require technical jargon from casual readers. The structure may be progressively disclosed.

## Objection Triage Flow

```text
Public objection / review comment
        ↓
Initial moderation and duplicate check
        ↓
Classify target programme/domain
        ↓
Public response or acknowledgement
        ↓
If substantive/new: bridge objections ledger
        ↓
Canonical programme review where applicable
        ↓
Disposition / research action
        ↓
Public status or response updated
```

### Routing Rules

- DFM initialization/history objection → DFM bridge objections ledger, then canonical DFM as warranted.
- CHFM mechanism objection → CHFM bridge objections ledger, then canonical CHFM as warranted.
- TRT/LRT ontology/formalization objection → TRT bridge objections ledger, then canonical TRT/LRT as warranted.
- Weltmodell-wide objection → route to the programme owning the primary claim; add cross-reference elsewhere rather than duplicate-counting.
- Site-only factual or citation error → public repository issue; no research-ledger promotion unless the correction changes substantive programme content.

## Contact Us Architecture

Because GitHub Pages is static, private contact requires an external submission mechanism or mailto fallback.

### Preferred pattern

A simple `Contact Us` page with:

- contact form;
- category selector;
- name;
- email;
- message;
- optional source/page reference;
- privacy notice;
- direct-email fallback.

Recommended categories:

- General question
- Research collaboration
- Source/citation correction
- Technical/site problem
- Media/interview inquiry
- Private objection or critique
- Other

### Form Backend

ThinxAI should select a low-maintenance form endpoint appropriate for a public static site. Selection criteria:

- no custom server required;
- spam protection;
- rate limiting or abuse controls;
- email forwarding or webhook delivery;
- privacy-conscious handling;
- accessible forms;
- simple GitHub Pages integration;
- ability to change destination without rewriting the site architecture.

The form provider should not become authoritative storage for research objections. Material worth preserving should be promoted into the appropriate GitHub/bridge record.

## Moderation Policy

The site should publish a concise moderation policy.

### Welcome

- substantive disagreement;
- skeptical questions;
- source-based criticism;
- alternative interpretations;
- requests for clarification;
- corrections and replication challenges.

### Subject to moderation

- spam;
- personal attacks;
- threats or harassment;
- repetitive flooding;
- unrelated polemics;
- malicious links;
- impersonation;
- content that exposes private information;
- repeated reposting of a resolved or duplicate claim without new argument/evidence.

Moderation should focus on conduct and relevance, not agreement with the Biblical WorldModel.

## Public Transparency Rule

When a serious objection materially changes the programme:

- preserve the original objection where appropriate;
- link to the disposition or revised public page;
- identify whether a claim was clarified, downgraded, revised, or retired;
- avoid silently rewriting history in a way that obscures the criticism that caused the change.

This is especially important for the site's stated commitment to falsifiability and open problems.

## Privacy and Safety

The site should not solicit or publish sensitive personal information.

Contact-form copy should state that users should not submit credentials, medical information, financial information, or other sensitive personal data.

Private contact should remain private unless the sender explicitly authorizes publication or quotation.

## ThinxAI Implementation Responsibilities

ThinxAI should:

1. enable/configure GitHub Discussions for the public repository;
2. create the initial categories;
3. evaluate and configure Giscus or an equivalent GitHub Discussions-backed comment layer;
4. create question, objection, and issue templates;
5. establish the private-contact form endpoint and spam controls;
6. integrate footer/page actions;
7. document moderation/admin procedures;
8. validate accessibility and mobile behavior;
9. return configuration and deployment evidence through the bridge.

## ChatGPT Responsibilities

ChatGPT should:

- develop public wording for question/objection templates;
- help triage substantive objections;
- maintain public objection-response summaries;
- promote qualifying objections into bridge ledgers;
- update public pages when canonical dispositions change;
- help draft moderation responses and technical dispositions;
- maintain consistency between public discussions and canonical programme status.

## Acceptance Criteria

The community/contact layer is acceptable when:

- [ ] GitHub Discussions is enabled and categorized.
- [ ] At least one test page can host or link to a discussion thread.
- [ ] A structured "Ask a Question" workflow exists.
- [ ] A structured "Submit an Objection" workflow exists.
- [ ] A "Report an Error" issue template exists.
- [ ] A private `Contact Us` path works from the live Pages site.
- [ ] Spam/abuse controls are documented.
- [ ] A moderation policy is publicly accessible.
- [ ] The site footer exposes discussion/contact actions.
- [ ] At least one end-to-end test demonstrates an objection or question can be submitted and traced to its GitHub record.
- [ ] Private contact does not expose sender data publicly.
- [ ] The workflow for promoting a substantive objection into the bridge/canonical review process is documented.

## Evidence Requested from ThinxAI

Return:

- Discussions URL;
- category configuration summary;
- Giscus/comment integration evidence if implemented;
- template paths;
- Contact Us page URL;
- form backend/provider choice and rationale;
- moderation-policy URL/path;
- test issue/discussion references;
- any operational limitations or recommended changes.
