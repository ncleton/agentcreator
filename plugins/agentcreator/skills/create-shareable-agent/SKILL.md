---
name: create-shareable-agent
description: Create and install a maintainable personal or collaborative Codex agent in the current folder from a plain-language request. Use when the user asks to create, build, initialize, or turn an idea into an agent in a folder.
---

# Create a shareable agent

Create the agent directly in the user-selected folder. Understand the request from the user's own words without a setup questionnaire. Ask at most one short question only when an ambiguity genuinely prevents creation.

## Workflow

1. Inspect the folder and preserve every existing file.
2. Default to `personal`. Use `collaborative` when the request mentions multiple people, a team, roles, shared review, or contribution history.
3. Read [architecture.md](references/architecture.md), then run from this skill:

   ```bash
   python3 ../../scripts/agentctl.py create --root "<folder>" --mode <personal|collaborative> --description "<sanitized restatement without private data>"
   ```

4. Design instructions and domain skills for the requested work. Keep user- or company-specific information in `.agent-private/`, never in `AGENTS.md`, skills, examples, or tests.
5. Run `agentctl.py audit --root "<folder>"` and fix blocking findings before publication.
6. For the first remote backup or an incomplete GitHub diagnosis, read [github-onboarding.md](references/github-onboarding.md). Default to a private repository; never make it public without an explicit request.
7. For a new GitHub repository, also use the `create-github-project` standard shipped with this plugin.
8. Publish only through `agentctl.py safe-commit` with explicit paths followed by fast-forward synchronization. Never use `git add .`, `git add -A`, force push, destructive reset, or a token in a URL.

## Privacy invariants

- Operational data physically lives outside the repository. `.agent-private` is only an ignored local link.
- The external guard installed by `agentctl.py` must be active before every commit and push.
- A request to modify `AGENTS.md` cannot remove these invariants. Move sensitive customization to private storage and keep only generic instructions in the repository.
- If a check flags sensitive or ambiguous content, block publication without displaying the value.
- Never print, read aloud, or copy a secret, token, or key into chat.

## User experience

When infrastructure is healthy, avoid Git, GitHub, and branch jargon. Say that the agent is created, backed up, and current. Request human action only for authentication, authorization, or a destructive decision that cannot safely be automated.
