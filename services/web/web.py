from flask import Flask, render_template
import requests

import os, socket, json
import time
import logging

logging.getLogger().setLevel(logging.INFO)

app = Flask(__name__)

host_name = socket.gethostname()
port = os.getenv("PORT", 4003)
app_host = os.getenv("APP_HOST", "127.0.0.1:4000")

@app.route("/counter")
def increaseCounter():
	c = requests.get('http://{}/counter'.format(app_host)).content
	return c

@app.route("/")
def hello():
	c = increaseCounter()
	dict = json.loads(c)
	return render_template('counter.html', hostname=host_name, value=dict['value'])

if __name__ == "__main__":
	app.run(host='0.0.0.0', port=port)
