from app.models import db, environment, SCHEMA, Person
from sqlalchemy.sql import text


def seed_people():

    person1 = Person(
        user_id = 1,
        name="Jim Carrey",
        featured_photo="https://image.tmdb.org/t/p/w342/u0AqTz6Y7GHPCHINS01P7gPvDSb.jpg",
        bio="James Eugene Carrey (born January 17, 1962) is a Canadian and American actor, comedian, writer, and producer known for his energetic slapstick performances."
    )

    db.session.add_all([person1])
    db.session.commit()


def undo_people():
    if environment == "production":
        db.session.execute(
            f"TRUNCATE table {SCHEMA}.users RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM people"))

    db.session.commit()
