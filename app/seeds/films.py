from app.models import db, environment, SCHEMA, Film
from sqlalchemy.sql import text


def seed_films():

    film1 = Film(
        user_id = 1,
        title="Eternal Sunshine of the Spotless Mind",
        genre="Drama, Sci-Fi, Comedy",
        year=2004,
        duration=108,
        synopsis="Joel Barish, heartbroken that his girlfriend underwent a procedure to erase him from her memory, decides to do the same. However, as he watches his memories of her fade away, he realises that he still loves her, and may be too late to correct his mistake.",
        key_art="https://a.ltrbxd.com/resized/sm/upload/ay/bp/kl/1y/uBfQ7IGpi0jXSP3GPCzp9Pzm10v-0-500-0-750-crop.jpg",
        cover_photo = "https://a.ltrbxd.com/resized/sm/upload/2w/va/23/lr/esotsm-1200-1200-675-675-crop-000000.jpg",
    )

    db.session.add_all([film1])
    db.session.commit()


def undo_films():
    if environment == "production":
        db.session.execute(
            f"TRUNCATE table {SCHEMA}.users RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM films"))

    db.session.commit()
