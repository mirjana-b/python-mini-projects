from os import path
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import login_manager


def create_app():
    app = Flask(__name__, template_folder='template')
    app.config['SECRET_KEY'] = "helloworld"

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix="/")
    app.register_blueprint(auth, url_prefix="/")
    return app
