# back-end/models/user.py
from sqlalchemy import Column, Integer, String, TIMESTAMP
from sqlalchemy.orm import relationship
from app import db

class User(db.Model):
    __tablename__ = 'users'

    user_id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    email = Column(String(255), unique=True, nullable=False)
    password = Column(String(255), nullable=False)
    profile_video = Column(String(255), nullable=True)
    profile_cv = Column(String(255), nullable=True)
    created_at = Column(TIMESTAMP, nullable=False, default=db.func.current_timestamp())

    # # Relations pour les messages
    # messages_sent = relationship('Message', foreign_keys='Message.sender_id', backref='user_sender', primaryjoin="and_(Message.sender_id==User.user_id, Message.sender_type=='user')")
    # messages_received = relationship('Message', foreign_keys='Message.receiver_id', backref='user_receiver', primaryjoin="and_(Message.receiver_id==User.user_id, Message.receiver_type=='user')")
