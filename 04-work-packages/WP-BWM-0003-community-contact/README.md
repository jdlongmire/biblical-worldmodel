# Community interaction and private contact

**WP-BWM-0003 — proposed; implementation pending.**

Establish categorized Discussions, question/objection/error intake, optional Giscus, moderation/routing, and private contact with abuse controls. No Home inbox, bot, service or credentials are reused or modified.

Depends on: WP-BWM-0001 public site.

[Imported requirements](requirements.md) retain the complete source scope and acceptance checklist. `package.yaml` owns current status and authority; inherited source status does not imply implementation. See WP-BWM-0004 migration evidence for provenance.

Human-Curated, AI-Enabled (HCAE)

## Post-deployment review findings

The current public site uses GitHub Issues as an interim participation path. That is acceptable for questions, objections, corrections, and collaboration intake, but it does not yet complete the intended community/contact architecture.

WP-BWM-0003 should explicitly disposition the following:

1. **GitHub Discussions** — enable and categorize Discussions for genuine conversation, questions, objections, and research dialogue where issue-tracker semantics are too restrictive.
2. **Giscus or equivalent** — evaluate embedded discussion on substantive pages so public comments can remain attached to the content being discussed without requiring a separate bespoke comment database.
3. **Issue templates** — retain GitHub Issues for actionable correction/error reports and any objection intake that benefits from structured triage; use templates for target claim, argument, evidence/source, and requested response.
4. **Private contact** — implement a non-public contact path with basic abuse controls and a documented destination. Do not route private messages into public issues.
5. **Research collaboration route** — distinguish serious collaboration inquiries from general comments/questions so they can be triaged appropriately.
6. **Moderation and provenance** — document moderation standards and preserve traceability when a substantive public objection results in a correction, bridge-ledger entry, or canonical programme review.
7. **Landing-page labels** — once Discussions are active, update any `Discuss on GitHub` action so it points to the intended discussion surface rather than the generic issue tracker.

Until these are implemented, the site's current community page should continue to describe Issues as an interim public route and state clearly that private contact is not yet active.
