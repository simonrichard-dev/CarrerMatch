#back-end/app/__init__.py
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

    return app
