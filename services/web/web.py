from flask import Flask, render_template
from flask_jwt_extended import jwt_required, get_jwt_identity
import requests

import json
import logging

logging.getLogger().setLevel(logging.INFO)

app = Flask(__name__)

from config import *

@app.route("/")
def login():
	return render_template('login.html', config=Config)

@app.route("/user")
@jwt_required
def user():
	userId = get_jwt_identity()
	c = requests.get('http://{}/user/{}'.format(Config.app_host, userId)).get_json
	user = {'name': c.get('name'), 'pwd': c.get('pwd'), 'id':c.get('id')}
	return render_template('user.html', config=Config, user=user)

if __name__ == "__main__":
	app.run(host='0.0.0.0', port=Config.port)
