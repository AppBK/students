from app.models import db, environment, SCHEMA, Review
from sqlalchemy.sql import text


def seed_reviews():

    review1 = Review(
        user_id=1,
        film_id=1,
        rating=5,
        review_text="The greatest movie of all time!!!"
    )

    db.session.add_all([review1])
    db.session.commit()


def undo_reviews():
    if environment == "production":
        db.session.execute(
            f"TRUNCATE table {SCHEMA}.users RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM reviews"))

    db.session.commit()
