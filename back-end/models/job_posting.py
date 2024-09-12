from sqlalchemy import Column, Integer, String, Text, TIMESTAMP, Enum, ForeignKey
from sqlalchemy.orm import relationship
from app import db

class JobPosting(db.Model):
    __tablename__ = 'job_postings'  # Nom de la table dans la base de données

    posting_id = Column(Integer, primary_key=True)  # Identifiant unique de l'annonce
    company_id = Column(Integer, ForeignKey('companies.company_id'), nullable=False)  # Référence vers l'ID de l'entreprise
    title = Column(String(255), nullable=False)  # Titre de l'annonce
    description = Column(Text, nullable=False)  # Description de l'annonce
    video_url = Column(String(255), nullable=True)  # URL de la vidéo associée à l'annonce
    type = Column(Enum('internship', 'job', 'project', name='posting_type'), nullable=False)  # Type d'annonce (stage, emploi, projet)
    created_at = Column(TIMESTAMP, nullable=False, default=db.func.current_timestamp())  # Date de création de l'annonce
    updated_at = Column(TIMESTAMP, nullable=True, onupdate=db.func.current_timestamp())  # Dernière mise à jour de l'annonce

    # Relation avec la table `matches`
    matches = relationship('Match', backref='job_posting')
