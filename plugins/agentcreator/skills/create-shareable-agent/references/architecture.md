# Recommended architecture

## Sharing boundary

The repository contains only the shareable engine: `AGENTS.md`, skills, scripts, tests, generic documentation, and identifier-free configuration. Real data lives in private system storage and is exposed to the project through the ignored `.agent-private` link.

`.gitignore` is a secondary safeguard. The decisive protection is an external guard installed outside the repository, combined with a publishable-path allowlist and outgoing-content checks.

## Minimum structure

```text
agent/
├── AGENTS.md
├── .agents/skills/
├── .shareable-agent/policy.json
├── .github/workflows/privacy.yml
├── scripts/agent-privacy-check.py
├── .gitignore
└── .agent-private -> private storage outside Git
```

## Agent content

`AGENTS.md` describes the role, workflow, boundaries, and expected outputs. Substantial domain procedures belong in skills triggered by precise requests. Scripts are reserved for checks or transformations that benefit from deterministic behavior.

Create only files that support the expressed need. Do not fill the agent with placeholders or generic documentation.

## Modes

- `personal`: one user, private repository by default, simple fast-forward synchronization.
- `collaborative`: local identity per contributor, isolated work, review before integration, CI on the exact commit, and contribution traceability.

Conversion to collaborative mode must remain additive and never move private data into the repository.
