import logging
from config import *
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api
from flask_jwt_extended import JWTManager

logging.getLogger().setLevel(logging.INFO)
logging.info('connecting to {}'.format(Config.db_url))

class App:
	app = None
	jwt = None
	db = None
	api = None

if App.app is None:
	App.app = Flask(__name__)
	App.jwt = JWTManager(App.app)
	App.db = SQLAlchemy(App.app)
	App.api = Api(App.app)
	App.app.config['PROPAGATE_EXCEPTIONS'] = True #jwt error propagation
	App.app.config['JWT_SECRET_KEY'] = Config.token_secret
	App.app.config['SQLALCHEMY_DATABASE_URI'] = Config.db_url
