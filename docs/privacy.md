# Confidentialité

Le plugin fonctionne localement et ne fournit aucun serveur, connecteur ou compte auquel son éditeur aurait accès. Nicolas Cléton ne devient ni membre, ni administrateur, ni collaborateur de l'espace de travail qui installe le plugin.

Le plugin peut utiliser Git et GitHub CLI sur la machine de l'utilisateur pour sauvegarder les agents que celui-ci lui demande de créer. L'authentification reste dans le trousseau de la machine et les dépôts appartiennent au compte ou à l'organisation choisis par l'utilisateur.

Les données utilisateur, client et entreprise sont destinées à un espace privé local placé hors du dépôt. Des contrôles locaux bloquent les chemins privés, les fichiers de données et plusieurs familles de secrets ou d'identifiants avant un commit ou un envoi.

Aucun détecteur automatique ne remplace le contrôle d'accès à la machine et au compte GitHub. Une personne qui contourne volontairement les protections avec ses propres outils reste responsable de ses actions.
