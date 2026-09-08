# Collaborative conversion

Add collaboration without exposing local data:

1. configure contributor identity locally, never in repository files;
2. share only sanitized task context;
3. isolate each change in a branch or worktree;
4. require human or automated review before integration;
5. run checks against the exact commit;
6. preserve publication evidence and attribution history.

Limit automatic synchronization to fast-forward operations. When histories diverge or conflict, preserve both versions and request a decision. Never force push.

Issues, branch names, commit messages, and review requests must not contain customer data, document excerpts, identifiers, or secrets.
