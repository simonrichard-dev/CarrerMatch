# back-end/models/match.py
from sqlalchemy import Column, Integer, Enum, TIMESTAMP, ForeignKey
from app import db

class Match(db.Model):
    __tablename__ = 'matches'  # Nom de la table dans la base de données

    match_id = Column(Integer, primary_key=True)  # Identifiant unique du match
    user_id = Column(Integer, ForeignKey('users.user_id'), nullable=False)  # Référence vers l'utilisateur
    posting_id = Column(Integer, ForeignKey('job_postings.posting_id'), nullable=False)  # Référence vers l'annonce
    status = Column(Enum('pending', 'accepted', 'rejected', name='match_status'), nullable=False)  # Statut du match (en attente, accepté, refusé)
    created_at = Column(TIMESTAMP, nullable=False, default=db.func.current_timestamp())  # Date de création du match
