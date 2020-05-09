from flask_sqlalchemy import SQLAlchemy
from os import getenv

db = SQLAlchemy()


def init_app(app):

    app.config['SQLALCHEMY_DATABASE_URI'] = getenv('DATABASE_URI')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
