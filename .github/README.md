# GitHub integration

This directory contains GitHub-specific automation and repository integration for Biblical WorldModel.

## Workflows

[`workflows/`](workflows/) contains the GitHub-hosted workflows used by the repository. The Pages publication workflow builds and verifies the MkDocs site on relevant pull requests and publishes accepted `main` changes through GitHub Pages.

The canonical public site is `https://worldmodel.thinxai.net/`.

Detailed build and browser-verification instructions live in [`../03-solutions-baseline/site/README.md`](../03-solutions-baseline/site/README.md). Publication, recovery, and operational procedures live under [`../06-operations/runbooks/`](../06-operations/runbooks/).

GitHub-specific configuration belongs here only when BWM actually uses it. Do not retain upstream template placeholders that describe absent capabilities once the repository has implemented them.
