# GitHub invisible

## Diagnostic silencieux

Exécuter `python3 ../../scripts/agentctl.py github-doctor --root "<dossier>" --json`. Ne montrer aucun détail technique si l'état est prêt.

Vérifier Git, GitHub CLI, l'authentification active, l'identité locale du dépôt, l'absence de jeton dans les URL distantes et le garde de confidentialité. Avec `--repair`, réparer uniquement les configurations sans risque.

## Première connexion

Si GitHub CLI manque, installer le paquet officiel adapté au système. Si aucun compte n'est connecté, expliquer en une phrase que cette connexion sauvegarde et met à jour l'agent, ouvrir la page GitHub dans le navigateur Codex quand il est disponible, puis lancer `gh auth login --web` et `gh auth setup-git`.

L'utilisateur effectue lui-même la création de compte, le CAPTCHA, la double authentification et l'autorisation dans le navigateur. Ne jamais lui demander de copier un jeton dans le chat.

## Usage quotidien

- Synchroniser uniquement en avance rapide.
- Protéger le travail non publié ; ne jamais le stasher, le réinitialiser ou le rebaser automatiquement.
- N'ajouter que des chemins explicites via `agentctl.py safe-commit`.
- Vérifier le commit distant après l'envoi.
- En cas d'authentification expirée, demander seulement de réactiver la connexion et ouvrir la page utile.

Ne jamais utiliser `gh auth token`, `--show-token`, une URL contenant des identifiants ou un fichier de secrets dans le dépôt.
