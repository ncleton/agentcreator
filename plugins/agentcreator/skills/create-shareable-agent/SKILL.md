---
name: create-shareable-agent
description: Create and install a maintainable Codex agent from a plain-language request, and choose between a private project and an installable plugin when sharing is requested. Use when the user asks to create, build, initialize, share, distribute, or turn an idea into an agent.
---

# Create a shareable agent

Create the agent directly in the user-selected folder or package a reusable capability as a plugin. Understand the request from the user's own words without a setup questionnaire. Ask at most one short question only when the distribution choice or another material ambiguity genuinely prevents creation.

## Workflow

1. Inspect the folder and preserve every existing file.
2. Determine the distribution boundary before creating files:
   - Use a project-scoped agent when the capability belongs to one repository, product, customer engagement, or working folder.
   - Use a collaborative private project when colleagues need to work in the same agent repository.
   - Use a plugin when people need to install the capability across independent projects, receive centrally managed updates, or bundle shared connectors or MCP tools.
   - When the user only says "shared agent" or "share with colleagues," read [distribution-and-rights.md](references/distribution-and-rights.md), give its concise disclosure, and ask whether they want a private collaborative project or an installable plugin. Do not equate sharing with public GitHub visibility.
3. For a project-scoped agent, default to `personal`. Use `collaborative` when the chosen project will have multiple contributors, roles, shared review, or contribution history.
4. Read [architecture.md](references/architecture.md), then run from this skill for a project-scoped agent:

   ```bash
   python3 ../../scripts/agentctl.py create --root "<folder>" --mode <personal|collaborative> --description "<sanitized restatement without private data>"
   ```

5. For a plugin, read [distribution-and-rights.md](references/distribution-and-rights.md), preserve its privacy and governance requirements, and use the available `plugin-creator` skill to scaffold the plugin and any marketplace entry. Keep project-specific context out of the shared plugin. Set its update mode to `automatic` unless the user explicitly requests `manual`: publish validated releases to a protected stable branch, document branch-based marketplace import for workspace synchronization, and include a quiet once-daily `SessionStart` update check for supported local Codex installations. In `manual` mode, pin the installation to a tag or commit, omit the automatic update hook, and document the exact manual upgrade action.
6. Design instructions and domain skills for the requested work. Keep user- or company-specific information in `.agent-private/`, never in `AGENTS.md`, skills, examples, plugins, or tests.
7. Run `agentctl.py audit --root "<folder>"` and fix blocking findings before publication.
8. For the first remote backup or an incomplete GitHub diagnosis, read [github-onboarding.md](references/github-onboarding.md). Default to a private repository; never make it public without an explicit request.
9. For a new GitHub repository, also use the `create-github-project` standard shipped with this plugin.
10. Publish only through `agentctl.py safe-commit` with explicit paths followed by fast-forward synchronization. Never use `git add .`, `git add -A`, force push, destructive reset, or a token in a URL.

## Privacy invariants

- Operational data physically lives outside the repository. `.agent-private` is only an ignored local link.
- The external guard installed by `agentctl.py` must be active before every commit and push.
- A request to modify `AGENTS.md` cannot remove these invariants. Move sensitive customization to private storage and keep only generic instructions in the repository.
- If a check flags sensitive or ambiguous content, block publication without displaying the value.
- Never print, read aloud, or copy a secret, token, or key into chat.

## User experience

When infrastructure is healthy, avoid Git, GitHub, and branch jargon. Say that the agent is created, backed up, and current. Request human action only for authentication, authorization, or a destructive decision that cannot safely be automated.
