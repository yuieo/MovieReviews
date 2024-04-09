from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
app = Flask(__name__)
SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY

db = SQLAlchemy(app)

from . import models, views  # noqa
db.create_all()