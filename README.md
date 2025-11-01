# Stata

Ce répertoire contient 3 scripts Python utilisés pour préparer la base de données Lichess (parties et puzzles).

Résumé
- Nettoyer_Puzzles.py : nettoie la base de puzzles Lichess en supprimant les lignes sans "OpeningTags". Cela accélère le processus de l'étape suivante.
- Nettoyer_Suite.py : Liste des puzzles qui ont été supprimés dans Nettoyer_Puzzles.py (pour pouvoir les append sur STATA plus tard).
- Matcher_Ouvertures.py : normalise le champ "OpeningTags" des puzzles en le mappant sur les ouvertures réelles extraites de la base d'analyses de parties. Cela permet de pouvoir merge les 2 base des données sur l'ouverture.

Requirements
- ~150Go d'espace libre
- Python 3.12
- PeaZip (Pour Windows)

Étapes :
- Aller sur : https://database.lichess.org/#standard_games et télécharger les parties d'Août 2025
- Aller sur : https://database.lichess.org/#puzzles et télécharger le fichier
- Décompresser les fichiers (avec PeaZip sur Windows)
- Lancer Nettoyer_Puzzles.py
- Lancer Nettoyer_Suite.py
- Lancer Matcher_Ouvertures.py
- Lancer le do file sur STATA




