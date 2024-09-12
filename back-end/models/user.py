from sqlalchemy import Column, Integer, String, Text, TIMESTAMP
from sqlalchemy.orm import relationship
from app import db

class User(db.Model):
    __tablename__ = 'users'  # Nom de la table dans la base de données

    user_id = Column(Integer, primary_key=True)  # Identifiant unique de l'utilisateur
    name = Column(String(255), nullable=False)  # Nom complet de l'utilisateur
    email = Column(String(255), unique=True, nullable=False)  # Email unique de l'utilisateur
    password = Column(String(255), nullable=False)  # Mot de passe (hashé)
    profile_video = Column(String(255), nullable=True)  # URL de la vidéo de présentation
    profile_cv = Column(String(255), nullable=True)  # URL du CV
    created_at = Column(TIMESTAMP, nullable=False, default=db.func.current_timestamp())  # Date de création du profil

    # Relation avec les tables `matches` et `messages`
    matches = relationship('Match', backref='user')
    messages_sent = relationship('Message', foreign_keys='Message.sender_id', backref='sender')
