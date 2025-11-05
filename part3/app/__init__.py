from flask import Flask
from flask_restx import Api
from flask_sqlalchemy import SQLAlchemy
from app.api.v1.users import api as users_ns
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt()

db = SQLAlchemy()

db.init_app(app)


def create_app(config_class="config.DevelopmentConfig"):
    app = Flask(__name__)
    app.config.from_object(config_class)
    bcrypt.init_app(app)


    # Register the users namespace
    api.add_namespace(users_ns, path='/api/v1/users')
    api.add_namespace(places_ns, path='/api/v1/places')
    api.add_namespace(reviews_ns, path='/api/v1/reviews')
    api.add_namespace(amenities_ns, path='/api/v1/amenities')

    return app
