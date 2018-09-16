from sqlalchemy import UniqueConstraint
import json

from config import *

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
