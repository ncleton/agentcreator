# Distribution and updates

## Stable channel

This repository is the canonical source owned by Nicolas Cléton. The default branch is the stable channel, and `.agents/plugins/marketplace.json` references `plugins/agentcreator` in the same repository. Automatic updates are the default for Agent Creator and for every shared plugin it creates.

In a ChatGPT workspace, an administrator imports the repository URL from **Administration > Plugins > Add > Import marketplace**. Leave the revision empty or select the stable branch. This branch-following configuration is the default update mode.

The distribution repository is public so the maintainer can remain outside the customer's GitHub team. Customers authorize the import with their own account and control which workspace roles may install the plugin. A private repository also works, but every importing account then needs read access.

New marketplaces are synchronized automatically each day. Administrators can also use **Sync now**. If a new plugin version is invalid, the last working version remains available.

Official OpenAI sources:

- https://learn.chatgpt.com/docs/enterprise/plugin-management
- https://learn.chatgpt.com/docs/plugins

## Release process

1. Preserve compatibility or provide an additive, idempotent migration.
2. Update the semantic version in `.codex-plugin/plugin.json` and `CHANGELOG.md`.
3. Run `make validate` plus the official plugin and skill validators.
4. Review the complete diff and privacy scan.
5. Open a pull request and wait for the required `validate` check.
6. Merge only through the protected default branch.
7. Create an annotated semantic-version tag and GitHub release from the merged commit. Use a signed tag when signing is configured and verifiable.

Customers do not need to use Git to receive a validated version. Reauthentication is needed only if the marketplace authorization expires or ownership changes.

For local Codex installations configured as the `agentcreator` marketplace, the `SessionStart` hook requests a quiet update at most once per day. New code applies to new sessions; an existing session finishes with the version it loaded. This complements rather than replaces workspace-native synchronization.

Codex requires one-time review and approval for unmanaged hooks. A changed hook may require renewed approval. Without approval, users can update manually with `codex plugin marketplace upgrade agentcreator`.

```bash
codex plugin marketplace add ncleton/agentcreator --ref main
codex plugin add agentcreator@agentcreator
```

## Manual update mode

Manual updates are an explicit opt-out from the default. Pin the workspace import to a release tag or immutable commit, omit the local once-daily update hook, and give administrators or local users the exact upgrade action. Never select this mode merely because the user did not mention updates.

## Compatibility

- Do not abruptly remove a published command or policy field.
- Migrations must be safe to rerun without duplicating managed blocks.
- Existing agents retain their private data and customizations.
- The latest external guard is installed during the next create, repair, or protection check.
