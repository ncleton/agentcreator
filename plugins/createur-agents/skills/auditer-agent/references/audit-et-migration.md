# Audit et migration

## Observer avant de modifier

Relever l'architecture, le statut Git, les instructions, les skills, les scripts, les dépendances, les tests et les chemins de données. Ne pas lire le contenu des documents métier si leurs noms et emplacements suffisent au diagnostic. Ne jamais recopier une valeur sensible dans le rapport.

Classer les constats en `critical`, `high`, `medium` et `low`. Donner d'abord les risques concrets, puis les améliorations de confort.

## Réparer sans casser

`agentctl.py repair` sauvegarde localement les fichiers de contrôle avant de poser les protections manquantes. Il ne remplace pas un `AGENTS.md` existant : il ajoute ou actualise uniquement le bloc de confidentialité géré.

Après ce socle automatique :

1. supprimer les contradictions entre instructions ;
2. extraire les procédures métier volumineuses dans des skills ciblés ;
3. déplacer les données et personnalisations sensibles vers `.agent-private` ;
4. remplacer leurs occurrences partageables par des variables ou exemples manifestement fictifs ;
5. ajouter uniquement les tests qui vérifient un comportement réel.

Ne pas publier automatiquement une migration qui laisse un constat critique ou élevé.
