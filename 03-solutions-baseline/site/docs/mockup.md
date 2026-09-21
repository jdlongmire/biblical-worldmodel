---
title: BWM redesign mockup
description: A mobile-first narrative mockup for the Biblical WorldModel redesign.
---

<style>
body:has(.bwm-mockup) .md-header,body:has(.bwm-mockup) .md-tabs,body:has(.bwm-mockup) .md-footer{display:none}body:has(.bwm-mockup) .md-main__inner{margin-top:0}body:has(.bwm-mockup) .md-content{max-width:none}body:has(.bwm-mockup) .md-content__inner{margin:0;padding:0}
.bwm-mockup{--night:#031923;--panel:#0a2634;--cyan:#62dcff;--muted:#a8c0ca;--ivory:#f5f1e8;--amber:#f1b96e;background:var(--night);color:var(--ivory);margin:0 calc(50% - 50vw);padding:0 18px 48px;font-family:Inter,ui-sans-serif,system-ui,sans-serif}
.bwm-mockup *{box-sizing:border-box}.bwm-mockup h1,.bwm-mockup h2,.bwm-mockup h3{font-family:Georgia,serif;font-weight:400;letter-spacing:-.035em;color:var(--ivory)}
.bwm-mockup a{color:inherit}.bwm-brand{display:flex;align-items:center;gap:12px;padding:26px 0 20px;border-bottom:1px solid #62dcff38}.bwm-mark{font:400 35px/1 Georgia,serif;letter-spacing:-.08em}.bwm-brand-divider{height:31px;border-left:1px solid var(--cyan)}.bwm-brand-name{font-size:10px;line-height:1.45;letter-spacing:.28em}.bwm-kicker{color:var(--cyan);font-size:9px;letter-spacing:.28em;text-transform:uppercase}.bwm-hero{padding:42px 0 30px}.bwm-hero h1{font-size:clamp(42px,11vw,82px);line-height:.98;margin:15px 0 18px}.bwm-hero-lead{color:var(--muted);font:20px/1.45 Georgia,serif;max-width:600px}.bwm-hero-note{color:var(--muted);font-size:14px;line-height:1.65;max-width:600px}.bwm-video{border:1px solid #62dcff80;border-radius:8px;overflow:hidden;background:#000;box-shadow:0 20px 55px #0008;margin:24px 0}.bwm-video iframe{display:block;width:100%;aspect-ratio:16/9;border:0}.bwm-actions{display:flex;flex-wrap:wrap;gap:10px;margin-top:22px}.bwm-button{display:inline-flex;align-items:center;justify-content:center;border:1px solid var(--cyan);border-radius:3px;padding:13px 18px;text-decoration:none;font-size:12px;letter-spacing:.04em}.bwm-button-primary{background:#0a8db6;color:#fff}.bwm-distinction{border-top:1px solid #62dcff55;border-bottom:1px solid #62dcff55;padding:34px 0}.bwm-distinction h2{font-size:31px;line-height:1.1;margin:12px 0 24px}.bwm-equation{display:grid;gap:8px}.bwm-term{border:1px solid #62dcff55;background:linear-gradient(145deg,#0c2b3a,#061d28);padding:18px 15px;min-height:112px}.bwm-term strong{display:block;color:var(--cyan);font-size:10px;letter-spacing:.2em;text-transform:uppercase;margin-bottom:9px}.bwm-term span{color:var(--muted);font:18px/1.25 Georgia,serif}.bwm-arrow{text-align:center;color:var(--cyan);font-size:24px}.bwm-paths{padding:38px 0 15px}.bwm-paths>h2{font-size:36px;line-height:1.05;margin:12px 0 8px}.bwm-paths>p{color:var(--muted);line-height:1.6;margin:0 0 22px}.bwm-card{position:relative;overflow:hidden;border:1px solid #62dcff55;border-radius:6px;background:var(--panel);padding:22px 18px;margin:12px 0;min-height:220px}.bwm-card:after{content:"";position:absolute;inset:auto 0 0;height:75px;background:linear-gradient(transparent,#061923);pointer-events:none}.bwm-card h3{font-size:29px;margin:8px 0}.bwm-card p{position:relative;z-index:1;color:var(--muted);line-height:1.55;max-width:480px}.bwm-card ul{position:relative;z-index:1;list-style:none;padding:0;margin:18px 0 0;border-top:1px solid #ffffff20}.bwm-card li{display:flex;justify-content:space-between;padding:8px 0;border-bottom:1px solid #ffffff20;color:#d9e5e7;font-size:13px}.bwm-card li::after{content:"›";color:var(--cyan);font-size:20px;line-height:13px}.bwm-quote{text-align:center;color:var(--ivory);font:italic 24px/1.35 Georgia,serif;padding:40px 16px 25px}.bwm-quote:after{content:"";display:block;width:44px;border-top:2px solid var(--cyan);margin:19px auto 0}.bwm-mockup .md-typeset{color:var(--ivory)}
@media(min-width:760px){.bwm-mockup{padding:0 42px 70px}.bwm-brand{padding-top:34px}.bwm-hero{display:grid;grid-template-columns:minmax(0,1fr) minmax(360px,520px);gap:48px;align-items:center;padding:76px 0 68px}.bwm-hero h1{font-size:clamp(54px,6vw,86px)}.bwm-video{margin:0}.bwm-equation{grid-template-columns:1fr 30px 1fr 30px 1fr 30px 1fr;align-items:stretch}.bwm-arrow{align-self:center}.bwm-paths{padding-top:55px}.bwm-card-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:14px}.bwm-card{margin:0;min-height:310px;padding:24px 20px}.bwm-quote{padding-top:65px}}
</style>

<style>
.bwm-mockup{--muted:#d1e1e6}
.bwm-mockup .bwm-button{color:var(--ivory)!important;text-decoration:none!important}
.bwm-mockup .bwm-button-primary{color:#fff!important}
.bwm-mockup .bwm-card-grid{display:grid;grid-template-columns:1fr;gap:18px;max-width:980px}
.bwm-mockup .bwm-card{min-height:0;margin:0;padding:28px 26px 26px}
.bwm-mockup .bwm-card h3{font-size:34px;margin:10px 0 12px}
.bwm-mockup .bwm-card p{color:#d1e1e6;max-width:760px;font-size:16px;line-height:1.65}
.bwm-mockup .bwm-card li{color:#e5f0f2;padding:11px 0}
.bwm-mockup .bwm-card a{color:#7ee7ff!important}
</style>

<style>
.bwm-transcript{border:1px solid #62dcff55;border-radius:5px;background:#061f2b;padding:16px 18px;margin:0 0 30px;color:var(--muted);font-size:14px;line-height:1.65}.bwm-transcript summary{color:var(--ivory);cursor:pointer;font-weight:600}.bwm-transcript p{margin:15px 0 0}.bwm-card a{position:relative;z-index:2;color:var(--cyan);font-size:12px;text-decoration:underline;text-underline-offset:3px}.bwm-source-links{border-top:1px solid #62dcff55;margin-top:28px;padding-top:22px;color:var(--muted);font-size:13px;line-height:1.7}.bwm-source-links a{color:var(--cyan)}.bwm-status{border-left:3px solid var(--amber);padding:10px 15px;margin:24px 0;color:var(--muted);font-size:13px}.bwm-status strong{color:var(--ivory)}
</style>

<style>
.bwm-purpose{color:#e4eef0;font:21px/1.5 Georgia,serif;max-width:680px;margin:0 0 18px}.bwm-purpose-secondary{color:#d1e1e6;line-height:1.65;max-width:680px}.bwm-contract{border-left:3px solid var(--cyan);padding:15px 18px;margin:28px 0 0;color:#e4eef0;font-size:15px;line-height:1.65}.bwm-story-preview{border-top:1px solid #62dcff55;border-bottom:1px solid #62dcff55;padding:34px 0;margin-top:0}.bwm-story-preview h2{font-size:34px;margin:10px 0}.bwm-story-preview p{color:#d1e1e6;max-width:760px;line-height:1.65}.bwm-story-preview a{color:#7ee7ff!important}.bwm-tagline{color:var(--muted);font-size:10px;letter-spacing:.28em;text-transform:uppercase;margin:0;padding:12px 0 0}
</style>

<div class="bwm-mockup">
<header class="bwm-brand"><span class="bwm-mark">BWM</span><span class="bwm-brand-divider"></span><span class="bwm-brand-name">BIBLICAL<br>WORLD MODEL</span></header>
<p class="bwm-tagline">Same observations. A different question.</p>

<section class="bwm-hero">
<div><div class="bwm-kicker">Start here</div>
<h1>Can a Calculated Age Differ From Actual History?</h1>
<p class="bwm-purpose">The Biblical WorldModel explores whether the Genesis account can provide a coherent framework for understanding a relatively young Earth and universe while taking the observations of modern science seriously.</p>
<p class="bwm-purpose-secondary">Rather than beginning by rejecting scientific measurements or redefining Genesis to accommodate deep time, BWM asks a prior question:</p>
<p class="bwm-hero-lead">Do the ages we calculate from the present necessarily tell us how much history actually occurred?</p>
<div class="bwm-actions"><a class="bwm-button bwm-button-primary" href="/the-story/">Read The Story →</a><a class="bwm-button" href="/evidence/">Explore the Evidence →</a></div><div class="bwm-contract">BWM does not ask you to ignore what we observe. It asks us to distinguish carefully between observation, interpretation, and reconstructed history.</div></div>
<div class="bwm-video"><iframe src="https://www.youtube.com/embed/gnnMknpuDDQ" title="Can a Calculated Age Differ From Actual History?" loading="lazy" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe></div>
</section>
<details class="bwm-transcript"><summary>Read the argument in text</summary><p>The video introduces a distinction between a present state and the history used to explain it. A mature object can be real without having experienced every ordinary stage that would normally produce that maturity. In the same way, a measurement can be accurate while the history inferred from a model remains underdetermined. BWM asks whether a calculated or extrapolated age always equals the actual elapsed history of the system. That question does not settle a chronology by itself. It identifies which assumptions about starting conditions, continuity, and later processes need to be tested. The written pages below continue the argument with Scripture, observations, competing explanations, and open problems.</p><p><a href="https://youtu.be/gnnMknpuDDQ">Open the video on YouTube</a></p></details>

<section class="bwm-distinction"><div class="bwm-kicker">The key distinction</div><h2>A measured present does not automatically reveal the whole path behind it.</h2>
<div class="bwm-equation"><div class="bwm-term"><strong>Observed state</strong><span>What we presently measure.</span></div><div class="bwm-arrow">＋</div><div class="bwm-term"><strong>Model assumptions</strong><span>Initial conditions, processes, continuity.</span></div><div class="bwm-arrow">→</div><div class="bwm-term"><strong>Extrapolated age</strong><span>A temporal value from a model.</span></div><div class="bwm-arrow">≠</div><div class="bwm-term"><strong>Historical age</strong><span>The elapsed history of the system.</span></div></div></section>

<section class="bwm-story-preview"><div class="bwm-kicker">The accessible doorway</div><h2>The Story</h2><p>Adam, the wine Jesus made, and an initialized video-game world make the central distinction concrete before the reader meets programme names. Start with the plain-language narrative, then examine the proposal from the model, evidence, and testing routes below.</p><a href="/the-story/">Read The Story →</a></section>

<section class="bwm-paths" id="paths"><div class="bwm-kicker">Examine the proposal</div><h2>Three ways to examine it.</h2><p>Choose the question that brought you here, then follow it as far as you want.</p>
<div class="bwm-card-grid"><article class="bwm-card"><div class="bwm-kicker">01 · A coherent framework</div><h3>The Model</h3><p>From creation to the present, BWM connects models that explain the observable world. Start with the reader-facing framework before entering programme vocabulary.</p><ul><li><a href="/worldmodel/">WorldModel overview</a></li><li><a href="/creation/">Creation and starting conditions</a></li><li><a href="/research-programmes/">Canonical programmes</a></li></ul></article>
<article class="bwm-card"><div class="bwm-kicker">02 · What the world reveals</div><h3>The Evidence</h3><p>Nature provides real data. We separate observations from the assumptions and historical reconstructions used to explain them.</p><ul><li><a href="/evidence/">Evidence checklist</a></li><li><a href="/methodology/">Observation and inference</a></li><li><a href="/compare/">Compare explanations</a></li></ul></article>
<article class="bwm-card"><div class="bwm-kicker">03 · A research programme</div><h3>The Tests</h3><p>Models must make testable predictions and remain open to falsification. This is an active research path, not a claim that every question is settled.</p><ul><li><a href="/open-problems/">Open problems</a></li><li><a href="/objections/">Strong objections</a></li><li><a href="/research-programmes/">Research status</a></li></ul></article></div>
<div class="bwm-status"><strong>Read the status carefully.</strong> The site explains and routes. Canonical repositories own technical claims, and unresolved burdens remain visible while research develops.</div><div class="bwm-source-links">Continue with <a href="/the-story/">The Story</a>, <a href="/start-here/">Start Here</a>, or the <a href="/sources/">Sources &amp; Glossary</a>. These links preserve the existing reader routes while the redesign is evaluated.</div></section>

<p class="bwm-quote">Sola Scriptura, Natura secundus, Soli Deo Gloria.</p>
</div>
