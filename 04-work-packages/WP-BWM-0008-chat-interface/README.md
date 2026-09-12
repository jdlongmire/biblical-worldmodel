# Guarded chat interface for the public site

**WP-BWM-0008 — proposed; no design work started.**

Give site visitors a conversational way to explore Biblical WorldModel content — grounded strictly in the site's own published pages, in the site's own voice, with guardrails that keep it from being turned into something else.

Depends on: WP-BWM-0001 (the retrieval corpus is the site's own docs), WP-BWM-0005 (the chat must speak in the same Tier voice and theological register already established there), WP-BWM-0003 (adjacent moderation/abuse philosophy, different channel), and an architecture decision from JD that this package does not make for him.

## Why this needs its own package, not just "add a chatbot"

A public LLM-backed chat endpoint on an apologetics site is a real attack surface, not a UI feature. Two things make it worth a dedicated package rather than a quick add:

1. **The site has no backend.** It's static GitHub Pages. A chat feature needs somewhere to hold API keys, enforce rate limits, and run the model call server-side — and per this repository's own README and `06-operations/runbooks/site/media.md`, Home's runtime, services, and credentials are explicitly out of scope here. Where the backend actually lives is an open architecture question this package surfaces, not one it decides.
2. **"Not exploitable by bad actors" is a real, enumerable risk surface**, not a vague aspiration — see below.

## Threat model: OWASP Top 10 for LLM Applications (2025)

This package scopes its security work against the current OWASP LLM risk taxonomy rather than an invented checklist:

| Risk | What it means here |
|---|---|
| LLM01 Prompt Injection | A visitor's message (or injected content in a retrieved page) overrides the guardrail instructions |
| LLM02 Sensitive Information Disclosure | Leaking API keys, the system prompt, or other visitors' conversations |
| LLM03 Supply Chain | Vetting the model provider, SDK, and any retrieval/vector-store dependency |
| LLM04 Data and Model Poisoning | A compromised PR poisoning the retrieval corpus the chat draws answers from |
| LLM05 Improper Output Handling | Model output rendered unsanitized into the page (XSS) |
| LLM06 Excessive Agency | The chat must stay read-only/informational — no tool-calling, no side effects |
| LLM07 System Prompt Leakage | Resisting attempts to extract the guardrail instructions themselves |
| LLM08 Vector and Embedding Weaknesses | If a vector index backs retrieval, protecting it from inversion/leakage |
| LLM09 Misinformation | No hallucinated citations or theological/scientific claims — ground every answer in the site's own text |
| LLM10 Unbounded Consumption | Rate limits, cost ceilings, and bot mitigation against cost-abuse or denial-of-service |

Sources: [OWASP GenAI Top 10 for LLM Applications 2025](https://genai.owasp.org/resource/owasp-top-10-for-llm-applications-2025/).

## Scope

- Threat model against all ten categories above, with a named mitigation for each.
- Architecture options (backend hosting, retrieval corpus, model provider) with cost/security tradeoffs, for JD's decision.
- Guardrail policy: answers grounded only in this site's own pages, cited, with explicit refusal of off-topic, pastoral-counseling, and doctrinal-authority requests.
- Abuse controls: per-session/per-IP rate limits, a hard cost ceiling with automatic kill-switch, bot mitigation, and abuse logging that doesn't over-collect visitor PII.
- Output sanitization before anything the model returns reaches the page.
- A non-public prototype, red-teamed against the threat model before any live-activation request.

**Out of scope:** provisioning paid API accounts/credentials, a publicly reachable live endpoint, or ongoing API cost — all gated on a separate explicit authorization once architecture is chosen and the threat model, guardrails, and an independent security review are all in place.

## Acceptance criteria

See `package.yaml` for the full list. Design-stage acceptance is JD's review of the threat model, architecture options, and guardrail/abuse-control policy; live-activation acceptance additionally requires a red-team pass and an independent security review. A working prototype alone does not authorize public deployment.

`package.yaml` owns current status, authority and evidence.

Human-Curated, AI-Enabled (HCAE)
