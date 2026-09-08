# Créateur d'agents

Plugin Codex de Nicolas Cléton pour créer, auditer et sécuriser des agents partageables à partir d'une demande formulée naturellement.

## Installer dans un espace ChatGPT

L'administrateur du client ouvre **Administration > Plugins > Ajouter > Importer une marketplace**, puis indique :

- Source : `https://github.com/ncleton/agentcreator`
- Chemin : vide
- Branche : `main` ou vide pour suivre la branche par défaut

Il installe ensuite **Créateur d'agents** pour les rôles souhaités. Nicolas Cléton ne rejoint pas l'espace du client et n'accède à aucune de ses données. La marketplace vérifie automatiquement les mises à jour chaque jour.

## Installer dans Codex local

```bash
codex plugin marketplace add ncleton/agentcreator --ref main
codex plugin add createur-agents@createur-agents
```

Démarrer ensuite une nouvelle tâche Codex afin de charger les skills.

Lors du premier démarrage, Codex peut demander d'examiner et d'approuver le hook de maintenance fourni par le plugin. Cette validation unique permet la recherche quotidienne de mises à jour locales. Si le hook n'est pas approuvé, le plugin reste utilisable mais l'actualisation locale doit être demandée manuellement.

## Utiliser

Dans le dossier qui doit recevoir l'agent, demander simplement :

> Crée-moi un agent pour gérer mes factures.

Dans un agent existant :

> Comment puis-je améliorer cet agent ?

Ou, pour appliquer les corrections :

> Mets cet agent aux normes pour le partager.

Le mode personnel est choisi par défaut. Le mode collaboratif est activé lorsque la demande mentionne une équipe, plusieurs contributeurs ou un circuit de validation.

## Protection des données

Les données réelles restent dans un espace privé local hors Git. Le plugin installe aussi un `.gitignore`, une liste blanche de chemins publiables, un scanner de contenu, des hooks Git externes et un contrôle CI. Voir la [politique de confidentialité](docs/privacy.md).

La documentation de maintenance se trouve dans [distribution et mises à jour](docs/distribution.md).
