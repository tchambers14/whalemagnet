from app import db

"""
from sqlalchemy.dialects.postgresql import JSON
JSON Can be stored directly in Postgres
"""


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password = db.Column(db.String(120))

    def __repr__(self):
        return '<User {}>'.format(self.username)
