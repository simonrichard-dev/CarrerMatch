# back-end/models/company.py
from sqlalchemy import Column, Integer, String, TIMESTAMP
from sqlalchemy.orm import relationship
from app import db

class Company(db.Model):
    __tablename__ = 'companies'

    company_id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    email = Column(String(255), unique=True, nullable=False)
    password = Column(String(255), nullable=False)
    company_video = Column(String(255), nullable=True)
    created_at = Column(TIMESTAMP, nullable=False, default=db.func.current_timestamp())

    # # Relations pour les messages
    # messages_sent = relationship('Message', foreign_keys='Message.sender_id', backref='company_sender', primaryjoin="and_(Message.sender_id==Company.company_id, Message.sender_type=='company')")
    # messages_received = relationship('Message', foreign_keys='Message.receiver_id', backref='company_receiver', primaryjoin="and_(Message.receiver_id==Company.company_id, Message.receiver_type=='company')")
