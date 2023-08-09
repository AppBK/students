from .db import db, environment, SCHEMA, add_prefix_for_prod
from datetime import datetime


class Review(db.Model):
    __tablename__ = 'reviews'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey(
        add_prefix_for_prod('users.id')), nullable=False)
    film_id = db.Column(db.Integer, db.ForeignKey(
        add_prefix_for_prod('films.id')), nullable=False)
    rating = db.Column(db.Integer)
    review_text = db.Column(db.String(1000))
    createdAt = db.Column(db.DateTime, nullable=False, default=datetime.now())
    updatedAt = db.Column(db.DateTime, nullable=False, default=datetime.now())

    user = db.relationship('User', back_populates='reviews')
    film = db.relationship('Film', back_populates='reviews')

    def to_dict(self):
        return {
            'id': self.id,
            'rating': self.rating,
            'review_text': self.review_text,
            'user': self.user.to_dict(),
            'film': self.film.to_dict()
        }
