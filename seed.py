from models import db, Pet
from app import app #useful in ipython

db.drop_all()
db.create_all()

lucky = Pet(
    name="Lucky",
    species="cat",
    photo_url='https://placekitten.com/200/200',
    age="baby",
    )

db.session.add(lucky)
db.session.commit()