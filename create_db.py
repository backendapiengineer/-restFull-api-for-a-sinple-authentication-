from database import db
from database import app

with app.app_context():
    db.create_all()