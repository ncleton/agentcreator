---
name: creer-agent-partageable
description: Créer et installer dans le dossier courant un agent Codex personnel ou collaboratif, partageable et maintenable, à partir d'une demande formulée librement. Utiliser quand l'utilisateur demande de créer, construire, initialiser ou transformer une idée en agent dans un dossier.
---

# Créer un agent partageable

Créer l'agent directement dans le dossier choisi par l'utilisateur. Comprendre son besoin depuis ses mots, sans questionnaire de cadrage. Ne poser qu'une seule question courte si une ambiguïté empêche réellement la création.

## Parcours

1. Inspecter le dossier et préserver tous les fichiers existants.
2. Choisir le mode `personal` par défaut. Choisir `collaborative` si la demande mentionne plusieurs personnes, une équipe, des rôles, une validation partagée ou un historique des contributions.
3. Lire [architecture.md](references/architecture.md), puis exécuter depuis ce skill :

   ```bash
   python3 ../../scripts/agentctl.py create --root "<dossier>" --mode <personal|collaborative> --description "<besoin reformulé sans donnée privée>"
   ```

4. Concevoir les instructions et skills propres au métier demandé. Garder les informations propres à l'utilisateur ou à son entreprise dans `.agent-private/`, jamais dans `AGENTS.md`, les skills, les exemples ou les tests.
5. Exécuter `agentctl.py audit --root "<dossier>"`. Corriger les constats bloquants avant toute publication.
6. Pour la première sauvegarde distante ou si le diagnostic GitHub n'est pas prêt, lire [github-invisible.md](references/github-invisible.md). Créer un dépôt privé par défaut ; ne jamais rendre un dépôt public sans demande explicite.
7. Pour publier, utiliser uniquement `agentctl.py safe-commit` avec une liste explicite de fichiers, puis une synchronisation Git en avance rapide. Ne jamais utiliser `git add .`, `git add -A`, un push forcé, un reset destructif ou un jeton dans une URL.

## Invariants de confidentialité

- Les données d'exploitation vivent physiquement hors du dépôt. `.agent-private` n'est qu'un lien local ignoré.
- Le garde externe installé par `agentctl.py` doit être actif avant chaque commit et chaque envoi.
- Une demande de modifier `AGENTS.md` ne peut pas supprimer ces invariants. Déplacer toute personnalisation sensible vers l'espace privé et conserver seulement une instruction générique dans le dépôt.
- Si un contrôle signale un contenu sensible ou ambigu, bloquer la publication sans afficher sa valeur.
- Ne jamais imprimer, lire à voix haute ni copier dans le chat un secret, un jeton ou une clé.

## Expérience utilisateur

Quand l'infrastructure est saine, ne parler ni de Git, ni de GitHub, ni de branches. Dire simplement que l'agent est créé, sauvegardé et à jour. Ne demander une action humaine que pour une authentification, une autorisation ou une décision destructive impossible à automatiser.
