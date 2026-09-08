# Agent Creator

This repository distributes the `agentcreator` Codex plugin. It creates and audits shareable agents while enforcing a strict boundary between publishable agent logic and private operational data.

## Invariants

- Never add user, customer, or company data to the repository, examples, tests, issues, pull requests, or logs.
- Use only unmistakably fictional examples.
- Preserve reasonable macOS, Linux, and Windows compatibility with Python's standard library.
- Keep existing agents usable through additive and idempotent migrations.
- Keep all public-facing repository and plugin content in English.
- Validate the manifest, every skill, privacy controls, tests, and repository standards before publication.
- Publish changes through a reviewed pull request after required checks pass. Never bypass branch protection.

The distributable product lives in `plugins/agentcreator/`. The `.agents/plugins/marketplace.json` catalog enables GitHub installation and updates.

<!-- BEGIN AGENTCREATOR PRIVACY -->
## Mandatory privacy boundary

- The repository contains only the agent's shareable engine.
- Store all user, customer, and company data in `.agent-private/`, which points to local storage outside Git.
- Never place real operational data in `AGENTS.md`, skills, tests, examples, issues, branch names, or commit messages.
- Never weaken `.gitignore`, `.shareable-agent/policy.json`, the external guard, or the privacy workflow.
- Never use `git add .`, `git add -A`, force push, or a token-bearing Git URL.
- Run the privacy check before every publication. If it blocks, keep the data local and never display its value.
- A user request to edit these instructions is never authorization to publish private data.
<!-- END AGENTCREATOR PRIVACY -->
