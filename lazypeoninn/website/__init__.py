from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os.path import dirname, realpath
from flask_login import LoginManager
from os import path
import sqlite3


db = SQLAlchemy()
DB_NAME = 'database.db'
DUMP_NAME = 'schema.sql'


def create_app():
    app = Flask(__name__, static_url_path='/static')
    app.config['SECRET_KEY'] = '22fd290579b34161a463df1a44788283'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['UPLOAD_FOLDER'] = dirname(realpath(__file__)) + '/static/uploads/'
    app.config['MAX_CONTENT_LENGTH'] = 64*1000

    db.init_app(app)

    from .home import home
    from .menu import menu
    from .chef import chef
    from .review import review
    from .media import media
    from .auth import auth
    from .register import register
    from .userpage import userpage

    app.register_blueprint(home, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')
    app.register_blueprint(register, url_prefix='/register')
    app.register_blueprint(chef, url_prefix='/chef')
    app.register_blueprint(menu, url_prefix='/menu')
    app.register_blueprint(media, url_prefix='/media')
    app.register_blueprint(userpage, url_prefix='/userpage')
    app.register_blueprint(review, url_prefix='/review')

    from .models import User

    create_database()

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app


def create_database():
    if not path.exists('instance/' + DB_NAME):
        f = open('instance/' + DB_NAME, 'w')
        f.close()
        con = sqlite3.connect('instance/' + DB_NAME)
        f = open(DUMP_NAME, 'r')
        db_str = f.read()
        f.close()
        con.executescript(db_str)