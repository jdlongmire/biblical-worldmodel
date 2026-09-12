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
- **Model candidates** (approximate September 2026 pricing from secondary aggregators — MEDIUM confidence, confirm at [openrouter.ai/models](https://openrouter.ai/models) before final selection). Three tiers, none pre-favored — all clear the same AC-03 adversarial-prompt-set bar before selection:
  - **Gemini 1.5 Flash** (~$0.075/M input tokens) — cost-optimized commercial candidate.
  - **Claude 3.5 Haiku** (~$0.80/M input tokens) — reliability-optimized commercial candidate, given this ecosystem's existing trust in Claude's instruction-following.
  - **Nontraditional/open-weight tier**, per JD's direction 2026-09-12: **DeepSeek V3** (~$0.01/M input tokens, cost-floor candidate) plus current Llama, Qwen or Mistral releases surveyed at implementation time rather than pinned now — the appeal (cost, reduced dependence on a few frontier labs) is real, but guardrail/refusal-fidelity under adversarial input is unverified here and must clear the same bar as the commercial tier, not a lower one. One nontraditional-specific check (OWASP LLM03): OpenRouter often serves the same open-weight model through several backend providers with different data-retention policies — pin a specific provider route with a stated no-training policy, don't just take the cheapest route.
  - Don't pre-commit to a model or tier — run AC-03's adversarial prompt set against all shortlisted candidates and let the result decide.
- **Retrieval:** no hosted vector database. The corpus is 19 pages — compute embeddings once at build time, ship them as a static JSON asset, search in-memory in the Worker. This removes OWASP LLM08 as a category rather than mitigating it, by not having a separately-hosted index at all.
- **Bot mitigation:** Cloudflare Turnstile (native to the same platform).
- **Rate limiting:** Cloudflare's native Rate Limiting Rules, not a hand-rolled Workers KV counter — confirmed against Cloudflare's own pricing docs that the KV free tier caps at 1,000 writes/day, which a naive per-message counter could hit on an ordinary busy day (or during the exact abuse burst the limiter exists to stop). KV, if used at all, stays for lighter bookkeeping.
- **Cost ceiling:** two independent caps, not a forecast — an AI Gateway budget alert and the dedicated OpenRouter key's own spend limit, both starting around **$10-20/month**, tuned upward from real post-launch usage rather than a pre-launch traffic estimate. Fixed infrastructure cost at this site's scale is effectively zero: Workers free tier is 100K requests/day (~3M/month) and AI Gateway's core features are free on every Cloudflare plan — both confirmed against Cloudflare's own pricing pages.

### Considered and declined: hosting on the PeakAI server

JD raised reusing PeakAI's existing infrastructure rather than standing up a new Cloudflare project. Declined: PeakAI's available infrastructure is generic compute, not the specific LLM-guardrail tooling (Turnstile, AI Gateway's rate limiting/budgets/caching) that does most of the LLM10 mitigation work here, so moving there would mean building that tooling from scratch rather than reusing anything. It would also share fault/resource blast radius with Peak Solutions' own production services and the Ologos suite for a feature whose entire job is accepting adversarial public input, and it would entangle this package with another runtime in exactly the way ADR-BWM-0001's "clean publication product" boundary and this package's own Home-isolation principle exist to avoid. Cost was not the deciding factor either way — Workers/AI Gateway are free at this site's scale, so PeakAI's "already available" doesn't offset real spend.

## Scope

- Threat model against all ten categories above, with a named mitigation for each.
- Confirm the recommended architecture above with JD (or record changes) before provisioning anything; confirm current OpenRouter pricing at the primary source.
- Guardrail policy: answers grounded only in this site's own pages, cited, with explicit refusal of off-topic, pastoral-counseling, and doctrinal-authority requests.
- Abuse controls: per-session/per-IP rate limits via native Rate Limiting Rules, a starting $10-20/month cost ceiling enforced at both the AI Gateway and OpenRouter layers, bot mitigation (Turnstile), and abuse logging that doesn't over-collect visitor PII.
- Output sanitization before anything the model returns reaches the page.
- A non-public prototype, red-teamed against the threat model before any live-activation request.

**Out of scope:** provisioning paid API accounts/credentials, a publicly reachable live endpoint, or ongoing API cost — all gated on a separate explicit authorization once architecture is chosen and the threat model, guardrails, and an independent security review are all in place.

## Acceptance criteria

See `package.yaml` for the full list, including AC-08: the OpenRouter key this feature uses must be dedicated and spend-limited, distinct from any key thinx's own tooling uses, set before the prototype's first live model call. Design-stage acceptance is JD's review of the threat model, architecture, and guardrail/abuse-control policy; live-activation acceptance additionally requires a red-team pass and an independent security review. A working prototype alone does not authorize public deployment.

`package.yaml` owns current status, authority and evidence.

Human-Curated, AI-Enabled (HCAE)
