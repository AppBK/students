from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, IntegerField
from wtforms.validators import DataRequired

class FilmForm(FlaskForm):
    title = StringField("title", validators=[DataRequired()])
    genre = StringField("genre", validators=[DataRequired()])
    year = IntegerField("year", validators=[DataRequired()])
    duration = IntegerField("duration", validators=[DataRequired()])
    synopsis = StringField("synopsis", validators=[DataRequired()])
    key_art = StringField("key_art", validators=[DataRequired()])
    cover_photo = StringField("cover_photo")
    submit = SubmitField("Submit")
