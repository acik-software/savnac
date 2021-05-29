from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager
from os import environ

db = SQLAlchemy()

def create_app():
	app = Flask(__name__)
	app.config['SECRET_KEY'] = environ['SECRET_KEY']
	app.config['SQLALCHEMY_DATABASE_URI'] = environ['DATABASE_URL_1']
	db.init_app(app)

	from .pages import pages
	from .auth import auth
	
	app.register_blueprint(pages,url_prefix='/')
	app.register_blueprint(auth,url_prefix='/')

	from .models import User

	db.create_all(app=app)

	login_manager = LoginManager()
	login_manager.login_view = 'auth.login'
	login_manager.init_app(app)

	@login_manager.user_loader
	def load_user(id):
		return User.query.get(int(id))

	return app
