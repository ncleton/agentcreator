# Audit and migration

## Observe before changing

Review architecture, Git state, instructions, skills, scripts, dependencies, tests, and data paths. Do not read business-document content when names and locations are sufficient for diagnosis. Never copy a sensitive value into the report.

Classify findings as `critical`, `high`, `medium`, or `low`. Lead with concrete risk, then usability improvements.

## Repair without breaking behavior

`agentctl.py repair` backs up control files locally before installing missing protections. It does not replace an existing `AGENTS.md`; it only adds or updates the managed privacy block.

After that deterministic baseline:

1. remove contradictory instructions;
2. extract substantial domain procedures into focused skills;
3. move sensitive data and customization into `.agent-private`;
4. replace shareable occurrences with neutral variables or clearly fictional examples;
5. add only tests that verify real behavior.

Do not publish a migration that leaves a critical or high finding.
