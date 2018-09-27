from sqlalchemy import UniqueConstraint
import json

from app import *

class SQLCounter(App.db.Model):
	__tablename__ = 'counters'
	id = App.db.Column(App.db.Integer, primary_key=True)
	value = App.db.Column(App.db.Integer, nullable=False)
	def json(self):
		return json.dumps({'value':self.value, 'id':self.id})

class SQLUser(App.db.Model):
	__tablename__ = 'users'
	id = App.db.Column(App.db.Integer, primary_key=True)
	name = App.db.Column(App.db.String(length=32), nullable=False)
	pwd = App.db.Column(App.db.String(length=32), nullable=False)
	UniqueConstraint('name', name='unique_user_name')
	def json(self):
		return json.dumps({'name':self.name, 'pwd': self.pwd, 'id':self.id})
