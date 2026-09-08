# Conversion collaborative

Ajouter la collaboration sans exposer les données locales :

1. une identité de contributeur configurée localement, jamais codée dans le dépôt ;
2. une tâche partagée ne contenant que du contexte assaini ;
3. une branche ou un espace de travail isolé par intervention ;
4. une validation humaine ou automatisée avant intégration ;
5. des contrôles exécutés sur le commit exact ;
6. une preuve de publication et un historique indiquant qui a fait quoi.

La synchronisation automatique est limitée à l'avance rapide. En cas de divergence ou de conflit, préserver les deux versions et demander une décision. Ne jamais utiliser de push forcé.

Les tickets, branches, messages de commit et demandes de validation ne doivent contenir ni données clients, ni extraits de documents, ni identifiants, ni secrets.
