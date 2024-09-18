#back-end/models/proposal.py
from sqlalchemy import Column, Integer, String, TIMESTAMP, ForeignKey
from sqlalchemy.orm import relationship
from app import db

class Proposal(db.Model):
    __tablename__ = 'proposals'

    proposal_id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(255), nullable=False)
    pdf_url = Column(String(255), nullable=True)  # URL du CV ou de l'annonce au format PDF
    video_url = Column(String(255), nullable=True)  # URL de la vidéo de présentation
    type = Column(String(50), nullable=False)  # 'job' pour les entreprises, 'cv' pour les individus
    created_at = Column(TIMESTAMP, nullable=False, default=db.func.current_timestamp())
    updated_at = Column(TIMESTAMP, nullable=False, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())

    # Foreign Key pour l'utilisateur
    user_id = Column(Integer, ForeignKey('users.user_id'), nullable=False)
    
    # Relation avec User
    user = relationship('User', backref='proposals')

    def __repr__(self):
        return f"<Proposal {self.title}>"
