from app.models import db, environment, SCHEMA, SeenFilm
from sqlalchemy.sql import text


def seed_seen_films():

    seen_film1 = SeenFilm(
        user_id = 1,
        film_id = 1
    )

    db.session.add_all([seen_film1])
    db.session.commit()


def undo_seen_films():
    if environment == "production":
        db.session.execute(
            f"TRUNCATE table {SCHEMA}.users RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM seen_films"))

    db.session.commit()
