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

## Recommended architecture (pending JD's confirmation)

Captured 2026-09-12 per JD's direction to leverage his existing OpenRouter account for an inexpensive model. Not yet acted on — no infrastructure or credential is provisioned by recording this.

- **Compute:** Cloudflare Workers, a project of its own — isolated from thinx-home's existing Cloudflare tunnels/zones, so this reuses infrastructure JD already trusts without touching Home's.
- **Gateway:** Cloudflare AI Gateway in front of the model call. It natively proxies OpenRouter ([confirmed via Cloudflare's own provider docs](https://developers.cloudflare.com/ai-gateway/usage/providers/openrouter)) and gives request rate limiting, cost budgets/alerts, response caching and logging largely through configuration — most of the OWASP LLM10 mitigation before any guardrail code is written.
- **Model access:** JD's existing OpenRouter account, through a **dedicated API key minted specifically for this feature** — not the key thinx's own workstation tooling uses — with its own OpenRouter-side spend limit. A worst-case abuse run against the public chat then can't draw against JD's general OpenRouter credits, and the key can be revoked independently without touching anything else.
- **Model candidates** (approximate September 2026 pricing from secondary aggregators — MEDIUM confidence, confirm at [openrouter.ai/models](https://openrouter.ai/models) before final selection):
  - **Gemini 1.5 Flash** (~$0.075/M input tokens) — cost-optimized candidate, strong cost/quality balance for high-volume simple tasks.
  - **Claude 3.5 Haiku** (~$0.80/M input tokens) — reliability-optimized candidate, given this ecosystem's existing trust in Claude's instruction-following and its relevance to guardrail adherence specifically.
  - Near-zero-cost models (DeepSeek V3 and similar) are available but not recommended as a starting point given this feature's premium on reliable refusal behavior under adversarial input — a fallback worth testing later if cost pressure warrants it.
  - Don't pre-commit: run AC-03's adversarial prompt set against both shortlisted candidates and let the result decide.
- **Retrieval:** no hosted vector database. The corpus is 19 pages — compute embeddings once at build time, ship them as a static JSON asset, search in-memory in the Worker. This removes OWASP LLM08 as a category rather than mitigating it, by not having a separately-hosted index at all.
- **Bot mitigation:** Cloudflare Turnstile (native to the same platform).
- **Additional rate-limit state:** Workers KV, per-session/per-IP, layered on top of AI Gateway's own limits rather than relying on either alone.

## Scope

- Threat model against all ten categories above, with a named mitigation for each.
- Confirm the recommended architecture above with JD (or record changes) before provisioning anything; confirm current OpenRouter pricing at the primary source.
- Guardrail policy: answers grounded only in this site's own pages, cited, with explicit refusal of off-topic, pastoral-counseling, and doctrinal-authority requests.
- Abuse controls: per-session/per-IP rate limits (Workers KV), a hard cost ceiling with automatic kill-switch (AI Gateway budgets plus the OpenRouter key's own spend limit), bot mitigation (Turnstile), and abuse logging that doesn't over-collect visitor PII.
- Output sanitization before anything the model returns reaches the page.
- A non-public prototype, red-teamed against the threat model before any live-activation request.

**Out of scope:** provisioning paid API accounts/credentials, a publicly reachable live endpoint, or ongoing API cost — all gated on a separate explicit authorization once architecture is chosen and the threat model, guardrails, and an independent security review are all in place.

## Acceptance criteria

See `package.yaml` for the full list, including AC-08: the OpenRouter key this feature uses must be dedicated and spend-limited, distinct from any key thinx's own tooling uses, set before the prototype's first live model call. Design-stage acceptance is JD's review of the threat model, architecture, and guardrail/abuse-control policy; live-activation acceptance additionally requires a red-team pass and an independent security review. A working prototype alone does not authorize public deployment.

`package.yaml` owns current status, authority and evidence.

Human-Curated, AI-Enabled (HCAE)
