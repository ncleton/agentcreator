# Agent Creator

[![CI](https://github.com/ncleton/agentcreator/actions/workflows/validate.yml/badge.svg)](https://github.com/ncleton/agentcreator/actions/workflows/validate.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

Agent Creator is a Codex plugin that creates, audits, secures, and publishes personal or collaborative agents from plain-language requests. Shareable agent logic stays in Git; user and company data stays in protected local storage outside the repository.

## What it provides

- `create-shareable-agent`: creates a project-scoped agent or routes a cross-project capability to a private installable plugin.
- `audit-agent`: audits, repairs, secures, or converts an existing agent.
- `create-github-project`: creates or upgrades an exemplary GitHub repository with privacy, governance, CI, and security controls.
- External Git guards that block private files, credentials, and personal data before commit or push.
- Daily plugin update checks for local Codex installations.
- Automatic stable-channel updates by default for every shared plugin it creates, with an explicit manual-update option.

## Install in a ChatGPT workspace

In **Administration > Plugins > Add > Import marketplace**, use:

- Source: `https://github.com/ncleton/agentcreator`
- Path: leave empty
- Revision: `main`, or leave empty to follow the default branch

Install **Agent Creator** for the desired roles. The maintainer does not join the customer workspace and cannot access customer data. The marketplace checks for updates automatically.

## Install in Codex

```bash
codex plugin marketplace add ncleton/agentcreator --ref main
codex plugin add agentcreator@agentcreator
```

Start a new Codex task after installation so the skills are loaded. Codex may ask for one-time approval of the maintenance hook.

## Use

Ask naturally from the folder that should contain the agent or repository:

> Create an agent that manages my invoices.

> Audit this agent and make it safe to share.

> Publish this folder as an exemplary GitHub project.

Project scope is the default. When a request only says "shared agent," Agent Creator explains the choice and asks whether colleagues should collaborate in one private GitHub project or install a plugin across multiple projects. Collaborative project mode is used for multiple contributors to the same repository. Plugin distribution is used for cross-project installation, centrally managed updates, enterprise role assignment, or bundled connectors. Shared plugins follow their creator's protected stable branch and update automatically by default; pinning a version for manual updates requires an explicit choice. GitHub repositories are private by default unless the user explicitly requests public visibility.

## Security and privacy

Real operational data lives outside Git in local private storage. Agent Creator combines a protected `.gitignore`, a publishable-path allowlist, content scanning, external Git hooks, and CI checks. See [Security](SECURITY.md) and [Privacy](docs/privacy.md).

## Project documentation

- [Contributing](CONTRIBUTING.md)
- [Governance](GOVERNANCE.md)
- [Support](SUPPORT.md)
- [Changelog](CHANGELOG.md)
- [Distribution and updates](docs/distribution.md)
