from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from flasks_object import app
from werkzeug.security import generate_password_hash

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///auth.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(length=20),unique=True, nullable=False)
    email = db.Column(db.String(length=50), unique=True, nullable=False)
    password = db.Column(db.String(length=30), nullable=False)
    date = db.Column(db.DateTime, default=datetime.now)