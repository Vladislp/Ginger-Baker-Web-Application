# This file going to make folder "Website" a python package
# Essentially means that we can import this folder here and whatever's inside of this "__init__.py" file will run automatically
# Once we import this folder

# Setup flask environment
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager
from flask_babelex import Babel, gettext

# Way to initialise database object (To modify)
db = SQLAlchemy()
# Pick database name
DB_NAME = "database.db"

# Fun fact: The documentation suggests that you "usually" create the Flask instance by passing __name__ for this argument, without going into any details on why.
def create_app():
    # Name of the file application package
    app = Flask(__name__)
    # Secure cookis
    app.config['SECRET_KEY'] = "123"
    # Telling flask, where are we storing our database, in Website folder
    # f beforehand --> evaluate as a string
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    app.config['BABEL_DEFAULT_LOCALE'] = 'en'
    babel = Babel(app)


    db.init_app(app)

    # import views/url to __init__.py. So we can access everything after launch
    from .views import views
    from .auth import auth
    # Need to register out blueprints
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    # We adding this not because we gonna use something like any other import...
    # We want to be sure, that when creating database our "models.py" initialise early, so that there were not be any problems with DB.
    from .models import User, Note

    create_database(app)

    login_manager = LoginManager() 
    # Where do we need to go, when we are not logged ing
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app

# Function to check, if our database is created. If not, create...but if we have, then we don't want to override it because we have data there
def create_database(app):
    # Since we store our database in "Website" folder, we want to look inside and check whether the DB exist in our folder...
    # With defined earlier variable
    if not path.exists('Website/' + DB_NAME):
        # Create database with passing app, because we need to the SQLAlchemy for wich app are we creating DB.
        db.create_all(app=app)
        print('Created Database!')