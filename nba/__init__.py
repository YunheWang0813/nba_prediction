from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('nba.config')

db = SQLAlchemy(app)

import nba.views
