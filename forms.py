"""Forms for adopt app."""

from flask_wtf import FlaskForm
from wtforms import StringField,BooleanField,RadioField,TextAreaField
from wtforms.validators import AnyOf, InputRequired, URL, Optional


class AddPetForm(FlaskForm):
    """defines the form to add a pet"""

    name = StringField('name') #make required

    species = StringField(
        'species',
        validators=[AnyOf(["cat", "dog", "porcupine"])]
    )

    photo_url = StringField(
        'Photo URL',
        validators=[Optional(),URL()]) #optional or url

    age = RadioField(
        choices = [
            ('baby','Baby'),
            ('young','Young'),
            ('adult','Adult'),
            ('senior','Senior')
        ],
        # validators=[AnyOf(["baby", "young", "adult", "senior"])]
    )

    notes = TextAreaField('notes') #optional min characters


class EditPetForm(FlaskForm):
    """defines the form to edit a pet"""

    photo_url = StringField('photo_url')
    notes = TextAreaField('notes')
    available = BooleanField('available')