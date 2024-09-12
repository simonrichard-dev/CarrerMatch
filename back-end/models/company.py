from sqlalchemy import Column, Integer, String, TIMESTAMP
from sqlalchemy.orm import relationship
from app import db

class Company(db.Model):
    __tablename__ = 'companies'  # Nom de la table dans la base de données

    company_id = Column(Integer, primary_key=True)  # Identifiant unique de l'entreprise ou porteur de projet
    name = Column(String(255), nullable=False)  # Nom de l'entreprise ou porteur de projet
    email = Column(String(255), unique=True, nullable=False)  # Email unique de l'entreprise ou porteur de projet
    password = Column(String(255), nullable=False)  # Mot de passe (hashé)
    company_video = Column(String(255), nullable=True)  # URL de la vidéo de présentation
    created_at = Column(TIMESTAMP, nullable=False, default=db.func.current_timestamp())  # Date de création du profil

    # Relation avec la table `job_postings`
    job_postings = relationship('JobPosting', backref='company')
