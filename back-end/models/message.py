# back-end/models/message.py
from sqlalchemy import Column, Integer, Text, TIMESTAMP, ForeignKey, Enum
from sqlalchemy.orm import relationship
from app import db

class Message(db.Model):
    __tablename__ = 'messages'  # Nom de la table dans la base de données

    message_id = Column(Integer, primary_key=True)  # Identifiant unique du message
    match_id = Column(Integer, ForeignKey('matches.match_id'), nullable=True)  # Référence vers le match (optionnel)
    sender_id = Column(Integer, nullable=False)  # ID de l'expéditeur (User ou Company)
    sender_type = Column(Enum('user', 'company', name='sender_type'), nullable=False)  # Type de l'expéditeur (User ou Company)
    receiver_id = Column(Integer, nullable=False)  # ID du destinataire (User ou Company)
    receiver_type = Column(Enum('user', 'company', name='receiver_type'), nullable=False)  # Type du destinataire (User ou Company)
    message_text = Column(Text, nullable=False)  # Contenu du message
    created_at = Column(TIMESTAMP, nullable=False, default=db.func.current_timestamp())  # Date de création du message

    # Relations pour les utilisateurs et entreprises
    user_sender = relationship('User', foreign_keys=[sender_id], backref='messages_sent', primaryjoin="and_(Message.sender_id==User.user_id, Message.sender_type=='user')")
    company_sender = relationship('Company', foreign_keys=[sender_id], backref='messages_sent', primaryjoin="and_(Message.sender_id==Company.company_id, Message.sender_type=='company')")
    
    user_receiver = relationship('User', foreign_keys=[receiver_id], backref='messages_received', primaryjoin="and_(Message.receiver_id==User.user_id, Message.receiver_type=='user')")
    company_receiver = relationship('Company', foreign_keys=[receiver_id], backref='messages_received', primaryjoin="and_(Message.receiver_id==Company.company_id, Message.receiver_type=='company')")
