#!/usr/bin/env python
from flask import Flask
from flask.ext.bootstrap import Bootstrap
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.migrate import Migrate, MigrateCommand
from flask.ext.login import LoginManager
from flask.ext.mail import Mail
from flask.ext.moment import Moment
from flask.ext.pagedown import PageDown
from config import config

bootstrap = Bootstrap()
db = SQLAlchemy()
mail = Mail()
moment = Moment()
pagedown  =PageDown()
login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'
login_manager.login_message = "请先登录"

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])

    bootstrap.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)
    moment.init_app(app)
    pagedown.init_app(app)

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix = '/auth')

    from .game import game as game_blueprint
    app.register_blueprint(game_blueprint, url_prefix = '/game')

    return app