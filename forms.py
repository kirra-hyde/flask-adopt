from flask_wtf import FlaskForm
from wtforms import StringField,BooleanField,RadioField,TextAreaField
from wtforms.validators import AnyOf

"""Forms for adopt app."""

class AddPetForm(FlaskForm):
    name = StringField('name')
    species = StringField('species',
        validators=[AnyOf(["cat", "dog", "porcupine"])]
    )
    photo_url = StringField('photo_url')
    age = RadioField(
        choices = [
            ('baby','Baby'),
            ('young','Young'),
            ('adult','Adult'),
            ('senior','Senior')
        ],
        validators=[AnyOf(["baby", "young", "adult", "senior"])]
    )
    notes = TextAreaField('notes')
