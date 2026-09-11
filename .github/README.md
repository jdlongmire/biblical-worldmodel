# .github/

Admits GitHub as a platform target alongside `.gitea/`, so a repository instantiated from this
template is forge-agnostic from creation rather than implying a single Git host.

This directory is currently empty of workflows/templates by design — there was nothing to mirror
from `.gitea/` at the time it was added (this template does not yet carry a `.gitea/` directory
either). Add `workflows/`, `ISSUE_TEMPLATE/`, or `pull_request_template.md` here as a repository
instantiated from this template actually needs CI or process templates; an empty directory with
this README documenting *why* it's here is the deliberate placeholder, not a stub awaiting
content nobody will add.
