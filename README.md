# CarrerMatch
## Installation du Backend

### Prérequis

1. **Système d'exploitation** : Ubuntu 22.04 (via WSL2 sur Windows).
2. **Python** : Version 3.10.12
3. **Node.js** : Version 20.17.0 (si nécessaire pour le frontend ou d'autres outils)
4. **MySQL** : Version 8.0.39

### Étapes d'installation

1. **Cloner le dépôt :**
   ```bash
   git clone https://github.com/simonrichard-dev/CarrerMatch.git
   cd CarrerMatch/back-end
   ```

2. **Créer et activer un environnement virtuel Python:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Installer les dépendances :**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configurer les varialles d'environnement :**
   Créer un fichier `.env` dans le dossier `back-end` et y ajouter les variables d'environnement suivantes :
   ```env
   DB_USERNAME=votre_nom_utilisateur
   DB_PASSWORD=votre_mot_de_passe
   DB_HOST=localhost
   DB_NAME=careermatch
   SECRET_KEY=ma_cle_secrète
   ```
   Remplacez `nom_utilisateur`, `mot_de_passe`, `ma_cle_secrète` par vos valeurs spécifiques.

5. **Démarrer MySQL :**

   Assurez-vous que le serveur MySQL est en cours d'exécution. Vous pouvez démarrer MySQL avec la commande suivante, en fonction de votre système d'exploitation :

   Sur Ubuntu :

   ```bash
   Copier le code
   sudo service mysql start
   ```

7. **Initialiser la base de données :**

   Mise à jour des modèles pour la migration :

   ```bash
   flask db migrate -m message_de_commit
   ```

   Exécutez les migrations pour créer les tables nécessaires dans la base de données :

   ```bash
   flask db upgrade
   ```

8. **Démarrer l'application :**

   Lancez l'application Flask :

   ```bash
   flask run
   ```