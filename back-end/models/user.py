# back-end/models/user.py
from sqlalchemy import Column, Integer, String, TIMESTAMP
from sqlalchemy.orm import relationship
from werkzeug.security import generate_password_hash, check_password_hash
from app import db

class User(db.Model):
    __tablename__ = 'users'

    user_id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(255), unique=True, nullable=False)
    email = Column(String(255), unique=True, nullable=False)
    password = Column(String(255), nullable=False)
    address = Column(String(255), nullable=False)
    profile_picture = Column(String(255), nullable=True)
    bio = Column(String(2040), nullable=True)
    user_type = Column(String(50), nullable=False)  # 'individual' ou 'company'
    created_at = Column(TIMESTAMP, nullable=False, default=db.func.current_timestamp())
    updated_at = Column(TIMESTAMP, nullable=False, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())

    # One-to-One pour l'individu
    proposal = relationship('Proposal', uselist=False, backref='user', foreign_keys='Proposal.user_id', cascade="all, delete-orphan")
    
    # Méthode pour définir le mot de passe (enregistre le hash dans password_hash)
    def set_password(self, password):
        self.password = generate_password_hash(password)
    
    # Méthode pour vérifier le mot de passe
    def check_password(self, password):
        return check_password_hash(self.password, password)
    
    def __repr__(self):
        return f"<User {self.username}>"

    
