from .db import db, environment, SCHEMA, add_prefix_for_prod
from datetime import datetime


class Person(db.Model):
    __tablename__ = 'people'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey(
        add_prefix_for_prod('users.id')), nullable=False)
    name = db.Column(db.String(255), nullable=False)
    featured_photo = db.Column(db.String(255))
    bio = db.Column(db.String(1000))
    createdAt = db.Column(db.DateTime, nullable=False, default=datetime.now())
    updatedAt = db.Column(db.DateTime, nullable=False, default=datetime.now())

    user = db.relationship('User', back_populates='people')
    roles = db.relationship('Role', back_populates='person', cascade="all, delete")

    def to_dict(self):
      return {
        'id': self.id,
        'name': self.name,
        'featured_photo': self.featured_photo,
        'bio': self.bio,
        'user': self.user.to_dict(),
        'roles': [role.to_dict() for role in self.roles]
      }
