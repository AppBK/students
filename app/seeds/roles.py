from app.models import db, environment, SCHEMA, Role
from sqlalchemy.sql import text


def seed_roles():

    role1 = Role(
        person_id=1,
        film_id=1,
        role='Actor'
    )

    db.session.add_all([role1])
    db.session.commit()


def undo_roles():
    if environment == "production":
        db.session.execute(
            f"TRUNCATE table {SCHEMA}.users RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM roles"))

    db.session.commit()
