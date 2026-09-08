---
name: auditer-agent
description: Auditer, expliquer, sécuriser, réparer ou remettre aux normes un agent Codex existant, y compris un agent créé sans ce plugin, et le convertir entre usage personnel et collaboratif. Utiliser pour les demandes comme comment améliorer cet agent, est-il partageable, audite-le, répare-le ou rends-le collaboratif.
---

# Auditer et améliorer un agent

Auditer le dossier courant sans supposer qu'il respecte une architecture connue. Préserver son comportement, ses personnalisations et les modifications non publiées.

## Choisir le niveau d'action

- Pour « comment puis-je l'améliorer ? », « audite-le » ou une demande d'avis : exécuter `python3 ../../scripts/agentctl.py audit --root "<dossier>"` et rendre un diagnostic court, priorisé et fondé sur les constats. Ne rien modifier.
- Pour « améliore-le », « répare-le » ou « mets-le aux normes » : lire [audit-et-migration.md](references/audit-et-migration.md), exécuter l'audit, puis `agentctl.py repair --root "<dossier>"`. Adapter ensuite les fichiers métier sans écraser le contenu existant.
- Pour une conversion collaborative : lire [collaboration.md](references/collaboration.md), puis exécuter `agentctl.py repair --root "<dossier>" --mode collaborative` avant d'ajouter les rôles et validations propres au projet.

## Ordre de priorité

1. Fuite ou risque de fuite de données.
2. Perte possible de travail local ou conflit de synchronisation.
3. Agent inutilisable, dépendances manquantes ou instructions contradictoires.
4. Maintenabilité, tests, ergonomie et collaboration.

## Incident de confidentialité

Si des fichiers sensibles sont suivis par Git ou détectés dans l'historique, lire [incident-confidentialite.md](references/incident-confidentialite.md). Bloquer toute nouvelle publication. Ne jamais prétendre qu'un simple `.gitignore` corrige une publication passée. La rotation d'un secret, la réécriture d'historique et la coordination avec des collaborateurs exigent une confirmation explicite.

Après une réparation, relancer l'audit et n'annoncer la conformité que si aucun constat critique ou élevé ne subsiste.
