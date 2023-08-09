from flask import Blueprint, jsonify, request
from flask_login import login_required, current_user
from app.models import db, Film
from app.forms.film_form import FilmForm
from app.api.auth_routes import validation_errors_to_error_messages

film_routes = Blueprint('films', __name__)

# Get all films
@film_routes.route("")
def get_all_films():
    """
    Query for all films and returns them in a list of film dictionaries
    """
    return jsonify([film.to_dict() for film in Film.query.all()])

@film_routes.route('/current')
@login_required
def get_user_films():
    """
    Query for all films created by the current user and return them in a list of film dictionaries
    """
    user_films = Film.query.filter(Film.user_id == current_user.id)
    films_dict = [film.to_dict() for film in user_films]
    return jsonify(films_dict)

# Get film by id
@film_routes.route("/<int:id>")
def get_film_by_id(id):
    """
    Query for a film by id and returns that film in a dictionary
    """
    film = Film.query.get(id)
    return jsonify(film.to_dict())

# Add new film
@film_routes.route('/new', methods=['POST'])
@login_required
def add_new_film():
    form = FilmForm()
    form['csrf_token'].data = request.cookies['csrf_token']

    form.data['user_id'] = current_user.id # do i need this line?
    if form.validate_on_submit():

        new_film = Film (
            user_id = current_user.id,
            title = form.data['title'],
            genre = form.data['genre'],
            year = form.data['year'],
            duration = form.data['duration'],
            synopsis = form.data['synopsis'],
            key_art = form.data['key_art'],
            cover_photo = form.data['cover_photo']
        )

        db.session.add(new_film)
        db.session.commit()

        return jsonify(new_film.to_dict())

    return { 'errors': validation_errors_to_error_messages(form.errors) }, 400

# Edit a film
@film_routes.route('/<int:id>/edit', methods=['PUT'])
@login_required
def edit_film(id):
    form = FilmForm()
    form['csrf_token'].data = request.cookies['csrf_token']

    if form.validate_on_submit():
        film = Film.query.get(id)

        if film is None or film.user_id != current_user.id:
            return { 'errors': 'Film not found'}, 404

        film.title = form.data['title'],
        film.genre = form.data['genre'],
        film.year = form.data['year'],
        film.duration = form.data['duration'],
        film.synopsis = form.data['synopsis'],
        film.key_art = form.data['key_art'],
        film.cover_photo = form.data['cover_photo']

        db.session.commit()

        return jsonify(film.to_dict())

    return { 'errors': validation_errors_to_error_messages(form.errors) }, 400

# Deleting an Album created by the user
@film_routes.route('/<int:id>/delete', methods=['DELETE'])
@login_required
def delete_album(id):
    film = Film.query.get(id)

    if film is None or film.user_id != current_user.id:
        return {'errors': 'Film not found'}, 404

    db.session.delete(film)
    db.session.commit()

    return { 'message': 'Successfully Deleted'}
