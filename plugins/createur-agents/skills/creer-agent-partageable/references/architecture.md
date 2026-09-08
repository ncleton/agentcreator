# Architecture recommandée

## Frontière de partage

Le dépôt contient uniquement le moteur partageable : `AGENTS.md`, skills, scripts, tests, documentation générique et configuration sans identifiant. Les données réelles sont placées dans le répertoire privé du système et exposées dans le projet par le lien ignoré `.agent-private`.

Le `.gitignore` est une protection secondaire. La protection décisive est le garde externe installé hors du dépôt, complété par une liste blanche de chemins publiables et un contrôle du contenu sortant.

## Structure minimale

```text
agent/
├── AGENTS.md
├── .agents/skills/
├── .shareable-agent/policy.json
├── .github/workflows/privacy.yml
├── scripts/agent-privacy-check.py
├── .gitignore
└── .agent-private -> espace privé hors Git
```

## Contenu de l'agent

`AGENTS.md` décrit le rôle, le parcours, les limites et les sorties attendues. Les procédures métier substantielles vivent dans des skills déclenchés par des demandes précises. Les scripts sont réservés aux contrôles ou transformations qui gagnent à être déterministes.

Créer uniquement les fichiers utiles au besoin exprimé. Ne pas remplir l'agent de placeholders ou de documentation générique.

## Modes

- `personal` : un utilisateur, dépôt privé par défaut, synchronisation simple en avance rapide.
- `collaborative` : identité locale par contributeur, travail isolé, validation avant intégration, CI sur le commit exact et traçabilité des contributions.

La conversion vers le mode collaboratif doit rester additive et ne jamais déplacer des données privées dans le dépôt.
