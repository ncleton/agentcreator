# Incident de confidentialité

## Détection locale ou indexée

Bloquer commit et envoi. Déplacer la donnée vers l'espace privé, puis la retirer de l'index avec `git rm --cached` sans supprimer la copie locale. Remplacer l'information dans les fichiers partageables par une variable neutre.

## Donnée déjà envoyée

Considérer la donnée comme exposée, même si le dépôt est privé. En priorité :

1. révoquer ou faire tourner tout secret ;
2. suspendre les publications ;
3. identifier les commits et les personnes ayant pu récupérer la donnée ;
4. préparer un nettoyage d'historique ;
5. obtenir une confirmation explicite avant réécriture et push forcé coordonné.

Ne jamais afficher la valeur détectée. Mentionner seulement le fichier, la catégorie de risque et l'action requise.
