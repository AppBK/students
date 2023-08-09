from .db import db, environment, SCHEMA, add_prefix_for_prod
from datetime import datetime


class Role(db.Model):
    __tablename__ = 'roles'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    person_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('people.id')), nullable=False)
    film_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('films.id')), nullable=False)
    role = db.Column(db.String(255), nullable=False)
    createdAt = db.Column(db.DateTime, nullable=False, default=datetime.now())
    updatedAt = db.Column(db.DateTime, nullable=False, default=datetime.now())

    person = db.relationship('Person', back_populates='roles')
    film = db.relationship('Film', back_populates='roles')

    def to_dict(self):
        return {
            'id': self.id,
            'person_id': self.person_id,
            'film_id': self.film_id,
            'role': self.role,
        }
