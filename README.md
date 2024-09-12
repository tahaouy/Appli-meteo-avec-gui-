

# Gestion des Villes et Météo

Version ameliorée de l'ancienne aplication , plus intuitive et plus facile à manier avec une interface graphique cette fois

## Fonctionnalités

**Connexion des utilisateurs** : Les utilisateurs peuvent se connecter avec leurs identifiants ou créer un nouveau compte. - 
**Gestion des villes** : Les utilisateurs peuvent ajouter ou supprimer des villes de leur liste personnelle. 
- **Affichage des prévisions** : Consultation des prévisions météorologiques pour les villes ajoutées à la liste de l'utilisateur. 
- **Interface utilisateur intuitive** : Conçue avec PyQt6 pour une interaction facile.

## Prérequis

Avant de pouvoir exécuter cette application, assurez-vous d'avoir installé les éléments suivants : - [Python version 3.x](https://www.python.org/downloads/)

### Bibliothèques nécessaires


Exécutez les commandes suivantes dans votre terminal pour installer les dépendances nécessaires :
 ``bash 
 python -m pip install PyQt6 
 python -m pip install requests``

## Connexion Internet

Une connexion Internet est requise pour obtenir les données météorologiques depuis l'API OpenWeatherMap.

## Cloner le dépôt

Pour utiliser ce projet, commencez par cloner le dépôt GitHub sur votre machine locale. Ouvrez votre terminal et exécutez la commande suivante :

``bash git clone https://github.com/tahaouy/Appli-meteo-avec-gui-``



## Lancer le programme

Accédez au répertoire du projet :

executer le fichier `main.py` 


## Utilisation

Suivez les instructions à l'écran pour ajouter, supprimer ou afficher vos villes. Lorsque vous souhaitez obtenir les données météorologiques, saisissez le nom de la ville souhaitée.

## Structure du Projet

-   **main.py** : Fichier principal qui lance l'application.
-   **base_d.py** : Contient les fonctions de connexion à la base de données et de création de tables.
-   **utilisateurs.py** : Gère les opérations liées aux utilisateurs (ajout, suppression, recherche).
-   **villes.py** : Gère les opérations liées aux villes (ajout, suppression, affichage).
-   **meteo.py** : Contient la logique pour obtenir les prévisions météorologiques.
