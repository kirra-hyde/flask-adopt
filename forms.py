from flask_wtf import FlaskForm
from wtforms import StringField,BooleanField,RadioField,TextAreaField

"""Forms for adopt app."""

class AddPetForm(FlaskForm):
    name = StringField('name')
    species = StringField('species')
    photo_url = StringField('photo_url')
    age = RadioField(
        choices = [
            ('baby','Baby'),
                ('young','Young'),
                ('adult','Adult'),
                ('senior','Senior')]
    )
    notes = TextAreaField('notes')
