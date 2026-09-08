# Créateur d'agents

Ce dépôt distribue le plugin Codex `createur-agents`. Il crée et audite des agents partageables en maintenant une frontière stricte entre leur moteur publiable et leurs données privées.

## Invariants

- Ne jamais ajouter de donnée utilisateur, client ou entreprise au dépôt, aux exemples, aux tests ou aux journaux.
- Utiliser seulement des exemples manifestement fictifs.
- Conserver la compatibilité macOS, Linux et Windows avec Python standard quand elle est raisonnable.
- Toute évolution du plugin doit conserver les anciens agents utilisables et migrer leur structure de façon additive.
- Valider le manifeste, les skills et les tests de confidentialité avant publication.

Le contenu de `plugins/createur-agents/` est le produit distribué. Le catalogue `.agents/plugins/marketplace.json` permet son import et sa synchronisation depuis GitHub.
