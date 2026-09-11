# Methods

1. Start by grounding in current instructions, memory, Git state and the actual
   tools available. `aide.py start` prints those local inputs without network calls.
2. Define success before implementation. Use a work package for significant work,
   with explicit authority, acceptance criteria and checks. Small tasks need only
   proportional tracking. Product changes belong in that product's repository.
3. Make significant changes in a dedicated branch/worktree. Preserve unrelated
   edits. Run meaningful tests covering failures and boundaries, not just a mirror
   of implementation. Inspect UI changes in the actual UI when relevant.
4. Verify against an identifiable artifact. Record the commands, result and
   environment. Independent review, when requested and available, is distinct
   from self-review; do not silently launch paid or parallel workers.
5. Commit the relevant code and documentation together. Confirm the exact remote
   ref after authorized publication. A push return code is not the whole check.
6. Before handoff, update memory and disposition, run `verify`, tests and `wrap`,
   and name remaining blockers. Wrap does not grant permission to push or merge.
7. When a recurring error is mechanically detectable, turn the lesson into a
   test or bounded guard. Otherwise retain its rationale as a method.

For onboarding follow [onboarding](../../06-operations/runbooks/ONBOARDING.md).
