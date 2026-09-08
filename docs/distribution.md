# Distribution et mises à jour

## Canal stable

Ce dépôt est la source détenue par Nicolas Cléton. La branche par défaut constitue le canal stable. Le catalogue `.agents/plugins/marketplace.json` référence `plugins/createur-agents` dans le même dépôt.

Dans un espace de travail ChatGPT, un administrateur importe l'URL du dépôt depuis **Administration > Plugins > Ajouter > Importer une marketplace**. Il laisse le champ de révision vide ou choisit la branche stable, jamais un SHA fixe s'il souhaite recevoir les mises à jour.

Le dépôt de distribution doit être public pour que Nicolas reste totalement extérieur à l'équipe du client sans gérer d'invitations GitHub. Le client autorise l'import avec son propre compte et administre lui-même les rôles autorisés à installer le plugin. Un dépôt privé fonctionnerait aussi, mais chaque compte importateur devrait alors recevoir un accès en lecture.

Les nouvelles marketplaces sont synchronisées automatiquement chaque jour. Une synchronisation manuelle reste possible avec **Synchroniser maintenant**. Si une nouvelle version du plugin est invalide, la dernière version fonctionnelle est conservée.

Sources officielles OpenAI :

- https://learn.chatgpt.com/docs/enterprise/plugin-management
- https://learn.chatgpt.com/docs/plugins

## Publication d'une version

1. Faire évoluer le plugin de façon rétrocompatible ou fournir une migration additive.
2. Incrémenter la version sémantique de `.codex-plugin/plugin.json`.
3. Exécuter les tests, la validation des deux skills et celle du plugin.
4. Examiner le diff et le contrôle de confidentialité.
5. Fusionner seulement une version validée sur la branche stable.

Les clients n'ont pas à manipuler Git pour recevoir une version validée. La reconnexion du compte de l'administrateur n'est nécessaire que si l'autorisation GitHub de la marketplace expire ou change de propriétaire.

Pour une installation Codex locale issue d'une marketplace Git configurée sous le nom `createur-agents`, le hook `SessionStart` demande silencieusement une actualisation au maximum une fois par jour. La version nouvellement chargée s'applique aux nouvelles sessions ; la session déjà ouverte termine avec la version qu'elle a chargée. Ce complément ne remplace pas la synchronisation native d'un espace de travail.

Installation locale depuis le dépôt public :

```bash
codex plugin marketplace add nicolascleton/createur-agents --ref main
codex plugin add createur-agents@createur-agents
```

## Compatibilité

- Ne jamais supprimer brutalement une commande ou un champ de politique déjà diffusé.
- Les migrations doivent pouvoir être relancées sans dupliquer les blocs gérés.
- Les agents existants gardent leurs données privées et leurs personnalisations.
- Une nouvelle version du garde externe est réinstallée lors de la prochaine création, réparation ou vérification de l'agent.
