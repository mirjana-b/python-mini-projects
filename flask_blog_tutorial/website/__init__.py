from os import path
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import login_manager


db = SQLAlchemy()
DB_NAME = "database.db"


def create_app():
    app = Flask(__name__, template_folder='template')
    app.config['SECRET_KEY'] = "helloworld"
    app.config['SQL_ALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix="/")
    app.register_blueprint(auth, url_prefix="/")

    create_database(app)

    return app

def create_database(app):
    if not path.exists("website/" + DB_NAME):
        db.create_all(app=app)
        print("Create database!")