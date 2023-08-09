from .db import db, environment, SCHEMA, add_prefix_for_prod
from datetime import datetime


class Film(db.Model):
    __tablename__ = 'films'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('users.id')), nullable=False)
    title = db.Column(db.String(255), nullable=False)
    genre = db.Column(db.String(255), nullable=False)
    year = db.Column(db.Integer, nullable=False)
    duration = db.Column(db.Integer, nullable=False)
    synopsis = db.Column(db.String(1000), nullable=False)
    key_art = db.Column(db.String(255), nullable=False)
    cover_photo = db.Column(db.String(255))
    createdAt = db.Column(db.DateTime, nullable=False, default=datetime.now())
    updatedAt = db.Column(db.DateTime, nullable=False, default=datetime.now())

    user = db.relationship('User', back_populates='films')
    reviews = db.relationship('Review', back_populates='film', cascade="all, delete")
    roles = db.relationship('Role', back_populates='film', cascade="all, delete")
    seen_films = db.relationship('SeenFilm', back_populates='film', cascade="all, delete")

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'genre': self.genre,
            'year': self.year,
            'duration': self.duration,
            'synopsis': self.synopsis,
            'key_art': self.key_art,
            'cover_photo': self.cover_photo,
            'user': self.user.to_dict(),
            # 'reviews': [review.to_dict() for review in self.reviews],
            # 'roles': [role.to_dict() for role in self.roles],
            # 'seen_films': [seen_film.to_dict() for seen_film in self.seen_films]
        }
