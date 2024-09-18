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
    from models.proposal import Proposal
    # from models.job_posting import JobPosting
    # from models.match import Match
    # from models.message import Message

    # Enregistrer les blueprints (routes)
    from .routes import main as main_blueprint
    app.register_blueprint(main_blueprint)

    # Test d'export de données à retirer (ne pas)
    # with app.app_context() :
    #     new_proposal = Proposal(
    #         title = 'Jérémy_proposal',
    #         pdf_url = 'jérémy@holberton.com/proposal_cv',
    #         video_url = 'jérémy@holberton.com/proposal_video',
    #         type = 'cv'
    #         )
    
    #     # new_user = User(
    #     #     email = 'jérémy@holberton.com',
    #     #     username = 'jérémy',
    #     #     address = '2 rue de l\'école 95000 Cergy',
    #     #     user_type = 'individual',
    #     # )
    
    #     # new_user.set_password('Typ3_Scripter!')  # Hash du mot de passe

    #     # new_message = Message(
    #     #     sender_id = 1,  # ou company_id
    #     #     sender_type = 'user',  # ou 'company'
    #     #     receiver_id = 1,  # ou user_id
    #     #     receiver_type = 'company',  # ou 'user'
    #     #     message_text = "Bonjour, je suis intéressé par votre annonce."
    #     #     )
    
    
    #     # db.session.add(new_company)
    #     # db.session.add(new_user)
    #     db.session.add(new_proposal)
    #     db.session.commit()

    return app
