from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import UniqueConstraint
from flask_jwt_extended import JWTManager

from config import *
import os, logging, json

# Connect to SQL
logging.info('connecting to {}'.format(db_url))

app = Flask(__name__)
app.config['PROPAGATE_EXCEPTIONS'] = True #jwt error propagation
app.config['JWT_SECRET_KEY'] = token_secret
app.config['SQLALCHEMY_DATABASE_URI'] = db_url
jwt = JWTManager(app)
db = SQLAlchemy(app)

class SQLCounter(db.Model):
	__tablename__ = 'counters'
	id = db.Column(db.Integer, primary_key=True)
	value = db.Column(db.Integer, nullable=False)
	def json(self):
		return json.dumps({'value':self.value, 'id':self.id})

class SQLUser(db.Model):
	__tablename__ = 'users'
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(length=32), nullable=False)
	pwd = db.Column(db.String(length=32), nullable=False)
	UniqueConstraint('name', name='unique_user_name')
	def json(self):
		return json.dumps({'name':self.name, 'pwd': self.pwd, 'id':self.id})
