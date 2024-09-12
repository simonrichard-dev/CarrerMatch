import os
import MySQLdb
from dotenv import load_dotenv

# Charger les variables d'environnement depuis le fichier .env
load_dotenv()

# Connexion à la base de données MySQL
try:
    db = MySQLdb.connect(
        host=os.getenv('DB_HOST'),
        user=os.getenv('DB_USERNAME'),
        passwd=os.getenv('DB_PASSWORD'),
        db=os.getenv('DB_NAME')
    )
    
    # Créer un curseur pour exécuter des requêtes
    cursor = db.cursor()
    
    # Exécuter une requête simple
    cursor.execute("SHOW TABLES;")
    
    # Afficher les tables trouvées dans la base de données
    print("Tables dans la base de données :")
    for table in cursor.fetchall():
        print(table)
    
    # Fermer la connexion
    db.close()

except MySQLdb.Error as e:
    print(f"Erreur de connexion : {e}")
