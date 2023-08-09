from .db import db, environment, SCHEMA, add_prefix_for_prod
from datetime import datetime


class SeenFilm(db.Model):
    __tablename__ = 'seen_films'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('users.id')), nullable=False)
    film_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('films.id')), nullable=False)

    user = db.relationship('User', back_populates='seen_films')
    film = db.relationship('Film', back_populates='seen_films')

    def to_dict(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'film_id': self.film_id,
            'user': self.user.to_dict()
        }
