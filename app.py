"""Flask app for adopt app."""

import os

from flask import Flask, render_template, request, redirect
from flask_debugtoolbar import DebugToolbarExtension
from forms import AddPetForm, EditPetForm
# from flask_wtf import FlaskForm

from models import connect_db, db, Pet

app = Flask(__name__)

app.config['SECRET_KEY'] = "secret"

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get(
    "DATABASE_URL", "postgresql:///adopt")

connect_db(app)

# Having the Debug Toolbar show redirects explicitly is often useful;
# however, if you want to turn it off, you can uncomment this line:
#
# app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

toolbar = DebugToolbarExtension(app)


@app.get('/')
def show_homepage():
    """Displays the homepage!"""

    pets = Pet.query.all()
    return render_template(
        "homepage.html",
        pets=pets)


@app.route("/add", methods=["GET", "POST"])
def handle_add_pet_form():
    """
    GET: Displays the add pet form.
    POST: processes the add pet form and redirects to homepage.
    """

    form = AddPetForm()

    if form.validate_on_submit():

        # grab form data
        name = form.name.data
        species = form.species.data
        photo_url = form.photo_url.data
        age = form.age.data
        notes = form.notes.data

        # create pet instance
        pet = Pet(name=name,
                  species=species,
                  photo_url=photo_url,
                  age=age,
                  notes=notes)

        db.session.add(pet)
        db.session.commit()

        return redirect("/")

    else:
        return render_template("add_pet_form.html", form=form)


@app.route("/<int:pet_id>", methods=["GET", "POST"])
def show_details_and_handle_edits(pet_id):
    """
    GET: Displays the pet details.
    POST: Processes the edit pet form and redirects back to /pet_id.
    """

    pet = Pet.query.get_or_404(pet_id)
    form = EditPetForm(obj=pet)

    if form.validate_on_submit():

        # grab form data
        photo_url = form.photo_url.data
        notes = form.notes.data
        available = form.available.data

        # update pet
        pet.photo_url = photo_url
        pet.notes = notes
        pet.available = available

        db.session.commit()

        return redirect(f"/{pet_id}")

    else:
        return render_template(
            "pet_details.html",
            form=form,
            pet=pet,
        )
