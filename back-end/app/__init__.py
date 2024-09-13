#back-end/app/__init__.py
import email
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from dotenv import load_dotenv
import os

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    # Charger les variables d'environnement
    load_dotenv()

    app = Flask(__name__)

    # Charger la configuration depuis config.py
    from app.config import Config
    app.config.from_object(Config)

    # Initialiser les extensions
    db.init_app(app)
    migrate.init_app(app, db)

    # Importer les modèles pour que Flask-Migrate puisse les détecter
    from models.user import User
    from models.company import Company
    from models.job_posting import JobPosting
    from models.match import Match
    from models.message import Message

    # Enregistrer les blueprints (routes)
    from .routes import main as main_blueprint
    app.register_blueprint(main_blueprint)

    # Test d'export de données à retirer (ne pas)
    new_company = Company(
        company_id = 2,
        name = 'HolbertonSchool',
        email = 'holberton@holbertonschool.com',
        password = 'abc123!$'
        )
    
    new_user = User(
        user_id = 1,
        name = 'Jérémy',
        email = 'jeremy@holberton.com',
        password = 'Jeremytypescript'
    )
    
    new_message = Message(
        sender_id = 1,  # ou company_id
        sender_type = 'user',  # ou 'company'
        receiver_id = 1,  # ou user_id
        receiver_type = 'company',  # ou 'user'
        message_text = "Bonjour, je suis intéressé par votre annonce."
        )
    
    with app.app_context() :
        db.session.add(new_company)
        db.session.commit()
        db.session.add(new_user)
        db.session.commit()
        db.session.add(new_message)
        db.session.commit()

    return app
