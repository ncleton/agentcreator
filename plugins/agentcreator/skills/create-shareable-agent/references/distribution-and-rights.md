# Distribution and rights

Read this reference when the user wants to share an agent, distribute it to colleagues, install it across projects, or manage it through an enterprise workspace.

## Choose the distribution model

| Need | Recommended model |
| --- | --- |
| One repository, product, customer engagement, or working folder | Project-scoped agent |
| Several contributors improving the same private agent repository | Collaborative private project |
| The same capability installed across independent projects or teams | Plugin |
| Central installation, role assignment, and managed updates | Enterprise workspace plugin |
| Shared engine with project-specific rules | Plugin plus a thin project-local `AGENTS.md` and project skills |

"Shared" does not mean "public." Both a project-scoped agent and a plugin marketplace can live in a private GitHub repository.

## Ask once when "shared" is ambiguous

Before creating anything, briefly explain the material difference and ask one question:

> Should colleagues collaborate in one private GitHub project, or should they install this capability as a plugin across multiple projects?

Do not ask this question when the request already establishes the answer. A request tied to one repository is project-scoped. A request for cross-project installation, centrally managed updates, enterprise role assignment, or bundled connectors is a plugin request.

## Default update policy

Every newly created shared plugin uses `update_mode: automatic` unless the user explicitly asks to control upgrades manually.

In `automatic` mode:

- Publish only validated, reviewed releases to a protected stable branch such as `main`.
- Tell workspace administrators to import that branch, or leave the revision empty to follow the repository's default branch. New marketplaces synchronize daily, and administrators can also request **Sync now**.
- For supported local Codex installations, include a quiet `SessionStart` hook that checks the plugin's own marketplace for an update at most once every 24 hours. A one-time hook approval may be required. New code applies in a new session.
- Keep releases backward compatible and migrations additive and idempotent because a stable-branch update reaches every authorized installation following that channel.

In `manual` mode:

- Use it only after an explicit user choice; it is never the creation default.
- Pin the workspace import or local installation to a version tag or immutable commit and do not add the once-daily update hook.
- Document the exact manual marketplace upgrade or version-change action for administrators and local users.

"All users update" means every installed and authorized copy that still follows the creator's stable channel. It does not include disconnected installations, forks, copied source, installations pinned to another revision, or workspaces whose GitHub authorization has expired. An update is distributable only after it passes validation and is merged to the followed branch.

## Required disclosure before creating a plugin

Keep the disclosure concise, but cover these consequences:

- Installed plugin skills become available in new supported conversations. Codex initially exposes skill names, descriptions, and paths, then loads full instructions only when a skill is selected. The initial skill list has a context budget, but a large catalog can reduce discoverability.
- Automatic updates are the default. After a reviewed source change is merged and synchronized, it affects every user assigned to and following that release channel. Manual, pinned updates require an explicit choice.
- Workspace roles control who may use or install a plugin. They do not provide a documented per-user editable copy of the same shared plugin.
- Source editing remains governed by the private GitHub repository. Contributors propose changes; maintainers review and merge them.
- Personal or repository-specific customization belongs in project-local `AGENTS.md`, `.agents/skills`, or `.codex/agents`, not in the shared plugin.
- Installing a plugin does not grant access to connected services, repositories, secrets, or data. Those permissions remain separate.
- Never put operational, customer, employee, credential, or company-private data in the plugin or marketplace.

Official references:

- [Build skills](https://learn.chatgpt.com/docs/build-skills)
- [Plugin management](https://learn.chatgpt.com/docs/enterprise/plugin-management)
- [Plugin controls](https://learn.chatgpt.com/docs/enterprise/apps-and-connectors)
- [Roles and workspace permissions](https://learn.chatgpt.com/docs/enterprise/roles-and-workspace-permissions)

## Rights model

Treat these as separate control planes:

1. **GitHub source access:** who can read, propose, approve, and merge changes to the private source repository.
2. **Workspace availability:** which roles or groups can see, install, or use the plugin.
3. **Connected-service authorization:** which data and actions each authenticated identity may access.
4. **Runtime permissions:** what local or cloud execution may do with files, network access, commands, and approvals.

Access in one plane never grants access in another.

## Safe customization and release patterns

- Follow a protected stable branch by default so reviewed releases propagate automatically.
- Pin a tag or immutable commit only when the user explicitly chooses manual updates or reproducibility over automatic delivery.
- Use a separately named `preview` plugin or branch for pilot groups and faster updates without destabilizing the automatic stable channel.
- Put an individual user's variation in that user's project. Do not edit the shared source for a personal preference.
- Create a separately named team variant only when the behavior should remain centrally maintained for that group.
- Give ordinary users installation or usage rights, contributors pull-request rights, and a small maintainer group merge and release rights.

If the user chooses a collaborative project, every collaborator who needs the files must have access to the private repository. If the user chooses an enterprise plugin, the GitHub account authorizing the workspace import must be able to read every referenced private repository; workspace administrators then assign plugin availability and installation policies to eligible roles.
