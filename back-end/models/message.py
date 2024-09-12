from sqlalchemy import Column, Integer, Text, TIMESTAMP, ForeignKey
from sqlalchemy.orm import relationship
from app import db

class Message(db.Model):
    __tablename__ = 'messages'  # Nom de la table dans la base de données

    message_id = Column(Integer, primary_key=True)  # Identifiant unique du message
    match_id = Column(Integer, ForeignKey('matches.match_id'), nullable=False)  # Référence vers le match
    sender_id = Column(Integer, ForeignKey('users.user_id'), nullable=False)  # Référence vers l'utilisateur qui a envoyé le message
    message_text = Column(Text, nullable=False)  # Contenu du message
    created_at = Column(TIMESTAMP, nullable=False, default=db.func.current_timestamp())  # Date de création du message

    # Relations avec les tables `matches` et `users`
    match = relationship('Match', backref='messages')
    sender = relationship('User', backref='messages_sent')
