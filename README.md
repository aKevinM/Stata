# Stata

Ce répertoire contient 4 scripts Python utilisés pour préparer la base de données Lichess (parties et puzzles).

Résumé
- Extraire_PGN.py : Transforme un PGN en document .csv avec une colonne ouverture, Elo joueur blanc et Elo joueur noir.
- Nettoyer_Puzzles.py : nettoie la base de puzzles Lichess en supprimant les lignes sans "OpeningTags". Cela accélère le processus de Matcher_Ouvertures.py.
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
- Lancer Extraire_PGN.py
- Lancer Nettoyer_Puzzles.py
- Lancer Nettoyer_Suite.py
- Lancer Matcher_Ouvertures.py
- Lancer le do file sur STATA

Notes

Le matching des ouvertures n'est pas parfait. Il ne consèrve uniquement les ouvertures les plus faciles à matcher et supprime souvent les variations des ouvertures.








