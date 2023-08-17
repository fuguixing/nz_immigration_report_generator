## models.py
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

db = SQLAlchemy()

class User(db.Model):
    """User model for storing user information."""
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    education = Column(String(100), nullable=False)
    qualifications = Column(String(100), nullable=False)
    english_levels = Column(String(100), nullable=False)

    def __init__(self, education: str, qualifications: str, english_levels: str):
        self.education = education
        self.qualifications = qualifications
        self.english_levels = english_levels

    def update_info(self, education: str, qualifications: str, english_levels: str):
        self.education = education
        self.qualifications = qualifications
        self.english_levels = english_levels
        db.session.commit()

class Report(db.Model):
    """Report model for storing generated reports."""
    __tablename__ = 'reports'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship('User', backref='reports')
    content = Column(String, nullable=False)

    def __init__(self, user: User):
        self.user = user

    def generate(self):
        # TODO: Implement report generation logic
        pass

    def save(self):
        # TODO: Implement report saving logic
        pass

    def print(self):
        # TODO: Implement report printing logic
        pass
