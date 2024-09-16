# back-end/models/user.py
from sqlalchemy import Column, Integer, String, TIMESTAMP
from sqlalchemy.orm import relationship
from werkzeug.security import generate_password_hash, check_password_hash
from app import db

class User(db.Model):
    __tablename__ = 'users'

    user_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False)
    email = Column(String(255), unique=True, nullable=False)
    password = Column(String(255), nullable=False)
    profile_video = Column(String(255), nullable=True)
    profile_cv = Column(String(255), nullable=True)
    created_at = Column(TIMESTAMP, nullable=False, default=db.func.current_timestamp())

    # Méthode pour définir le mot de passe (enregistre le hash dans password_hash)
    def set_password(self, password):
        self.password = generate_password_hash(password)
    
    # Méthode pour vérifier le mot de passe
    def check_password(self, password):
        return check_password_hash(self.password, password)

    # # Relations pour les messages
    # messages_sent = relationship('Message', foreign_keys='Message.sender_id', backref='user_sender', primaryjoin="and_(Message.sender_id==User.user_id, Message.sender_type=='user')")
    # messages_received = relationship('Message', foreign_keys='Message.receiver_id', backref='user_receiver', primaryjoin="and_(Message.receiver_id==User.user_id, Message.receiver_type=='user')")
