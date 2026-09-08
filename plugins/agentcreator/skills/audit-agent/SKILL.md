---
name: audit-agent
description: Audit, explain, secure, repair, or standardize an existing Codex agent, including one created without this plugin, and convert between personal and collaborative use. Use for requests to improve, audit, repair, secure, share, or make an agent collaborative.
---

# Audit and improve an agent

Audit the current folder without assuming a known architecture. Preserve behavior, customization, and unpublished changes.

## Choose the action level

- For advice such as "How can I improve this agent?" or "Audit it": run `python3 ../../scripts/agentctl.py audit --root "<folder>"` and return a concise, prioritized, evidence-based diagnosis without modifying files.
- For "Improve it", "Repair it", or "Bring it up to standard": read [audit-and-migration.md](references/audit-and-migration.md), run the audit, then `agentctl.py repair --root "<folder>"`. Adapt domain files without overwriting existing content.
- For collaborative conversion: read [collaboration.md](references/collaboration.md), then run `agentctl.py repair --root "<folder>" --mode collaborative` before adding project-specific roles and review gates.

## Priority order

1. Data exposure or exposure risk.
2. Possible loss of local work or synchronization conflict.
3. Unusable agent, missing dependencies, or contradictory instructions.
4. Maintainability, tests, usability, and collaboration.

## Privacy incident

If Git tracks sensitive files or history scanning detects them, read [privacy-incident.md](references/privacy-incident.md) and block publication. Never claim that `.gitignore` repairs past disclosure. Secret rotation, history rewriting, and coordinated force pushing require explicit confirmation.

After repair, rerun the audit and claim compliance only when no critical or high finding remains.
