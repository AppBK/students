from flask.cli import AppGroup
from .users import seed_users, undo_users
from .films import seed_films, undo_films
from .people import seed_people, undo_people
from .roles import seed_roles, undo_roles
from .seen_films import seed_seen_films, undo_seen_films
from .reviews import seed_reviews, undo_reviews


from app.models.db import db, environment, SCHEMA

# Creates a seed group to hold our commands
# So we can type `flask seed --help`
seed_commands = AppGroup('seed')


# Creates the `flask seed all` command
@seed_commands.command('all')
def seed():
    if environment == 'production':
        # Before seeding in production, you want to run the seed undo 
        # command, which will  truncate all tables prefixed with 
        # the schema name (see comment in users.py undo_users function).
        # Make sure to add all your other model's undo functions below
        undo_reviews()
        undo_seen_films()
        undo_roles()
        undo_people()
        undo_films()
        undo_users()
    seed_users()
    seed_films()
    seed_people()
    seed_roles()
    seed_seen_films()
    seed_reviews()

    # Add other seed functions here


# Creates the `flask seed undo` command
@seed_commands.command('undo')
def undo():
    undo_reviews()
    undo_seen_films()
    undo_roles()
    undo_people()
    undo_films()
    undo_users()
    # Add other undo functions here
