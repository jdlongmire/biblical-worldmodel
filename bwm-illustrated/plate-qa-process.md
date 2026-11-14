# BWM Illustrated Plate QA Process

Adopted 2026-11-14 (JD directive), after the BWM-IL-018 Covenants of God
plate went through avoidable revision cycles: five generations garbling
the same compartment, three failed surgical repair builds, an audit read
at mismeasured coordinates, and a typeset substitution the author
rejected on sight. This process is designed so each of those failure
modes is stopped by a gate before it costs another cycle.

Scope: all BWM Illustrated plates (BWM-IL series) from brief to filing.
The Illustrated Systematics lane keeps its own QA-PROCESS.md; where the
two lanes share a rule, this document follows the stricter form.

## Stage 0 - Brief freeze

- The plate's texts (account, key elements, strip captions, compartment
  bodies, footer) are frozen in a brief file before the first generation.
  Any later text change re-opens the brief and is recorded as a change,
  not an edit in passing.
- The brief names the reference images: the Visual Series Style Guide
  plate and at least one approved, filed exemplar plate. No generation
  is ever run text-only or from memory of the style.

## Stage 1 - Generation (roll budget)

- At most 3 generations per plate on one brief. Each roll is logged with
  a one-line defect census (roll id, file hash, zones defective).
- If 3 rolls are defective, rolling stops. The next step is a planned
  composite (whole-compartment or whole-line donors among the rolls,
  chosen from the census) or an escalation to JD with the census and
  options. Rolling a fourth time on hope is not a step in this process.
- A generator edit pass counts as a new generation and re-enters at
  Stage 2 in full.

## Stage 2 - Full audit (before anything is shown or filed)

- Every text zone is read at 3x magnification or better, from the saved
  file, letter by letter for names, Scripture references, and the
  plate's known problem words. Zones: running header (all three
  segments), banner and subtitle, account column, key elements column,
  strip captions (every panel), each bottom compartment, footer.
- Results are logged in the per-plate audit checklist (AUDIT-CHECKLIST.md
  template): zone, text as printed, pass/fail, defect verbatim if failed.
- Art content is logged separately as observations (for example a strip
  panel whose image does not match its caption's subject). Observations
  are reported to JD; they are never silently repaired and never block
  a lettering pass by themselves.
- A plate with any failed zone is a defective plate. It may be shown to
  JD only labelled as such, with the census attached.

## Stage 3 - Repair (when the audit fails a zone)

- Native glyphs only. Computer-font or typeset substitution for
  generated lettering is prohibited unless JD approves it for that
  plate in advance, in which case the approval and the substitution
  are both disclosed in the plate record.
- Donor preference order: whole compartment body, whole line, whole
  word, single letter. A donor extract image is read and confirmed
  before any paste.
- Coordinates come from two independent instruments that agree: a
  component map (ink components at native resolution) AND a labeled
  grid crop or ASCII pixel map. Grid coordinates are converted from
  the crop origin and scale by computation, never estimated by eye
  from a rendered crop. (Both audit failures in this lane's history -
  the PR #58 repair and the 2026-11-14 semicolon erasures - were
  single-instrument coordinate errors.)
- One repair at a time. Each repair is crop-verified at the exact
  worked coordinates before the next begins.
- Attempt caps: at most 2 surgical attempts per defect site, at most
  2 rebuilds per compartment. A failed attempt is discarded and the
  next attempt rebuilds from the pristine generation; patches are
  never stacked on patches.
- On hitting a cap: stop, and escalate to JD with the defect census,
  what was tried, and the remaining options. No silent third attempt.

## Stage 4 - Final verification

- Verification is read from the FINAL saved file: a full-plate read
  plus a magnified crop of every text zone, each checked against the
  brief text word by word.
- A pixel diff against the base generation confirms change is confined
  to the declared worked zones.
- Hashes are recorded for: the base generation, each donor, and the
  final file. The audit checklist is completed and signed off in the
  plate's working notes before the plate is presented or filed.

## Stage 5 - Presentation to JD

One message contains:
- the plate image itself;
- the audit table (every zone, pass/fail);
- every repair disclosure (what was transplanted or erased, from
  where, at whose direction);
- the defect census of rejected rolls;
- art observations, labelled as observations.
A defect discovered after presentation is reported in the same turn it
is discovered, with its root cause named.

## Stage 6 - Filing gate

- The companion record carries: the audit result per zone, the full
  repair history (including failed and superseded attempts), the
  generation census, and the SHA-256 of the filed image.
- Local verify-build passes; CI is read on the exact PR head before
  any merge; after merge, the live served asset is verified
  byte-identical to the filed file.
- Known post-presentation defects in a live asset are corrected by a
  follow-up PR in the same session they are confirmed, with the
  correction disclosed in the record.

## Standing prohibitions

- No plate numbers on artwork (JD ruling, 2026-11-13).
- No em dashes in authored text; plate texts follow the brief exactly.
- No presenting a build as verified from crops taken at offsets other
  than the ones worked.
- No treating a collaborator's or a tool's success report as
  verification; the destination file is the evidence.
