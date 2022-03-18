from models import db, User
from app import app

# Create all tables
db.drop_all()
db.create_all()

# Add user

u = User(
    username="BambisMom",
    password="BambisMom",
    email="emmagomezxolo@gmail.com",
    first_name="Emma",
    last_name="Gomez Xolo"
)

db.session.add(u)
db.session.commit()