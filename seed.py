from models import db, Pet
from app import app

db.drop_all()
db.create_all()

pet1 = Pet(
    name="Lucky",
    species="Cat",
    photo_url='https://placekitten.com/200/200',
    age="Baby",
    )

db.session.add(pet1)
db.session.commit()