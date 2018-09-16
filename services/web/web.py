from flask import Flask, render_template
import requests

import os, socket
import time
import logging

logging.getLogger().setLevel(logging.INFO)
	
app = Flask(__name__)

host_name = socket.gethostname()
port = os.getenv("PORT", 80)

@app.route("/counter")
def increaseCounter():
	c = requests.get('http://user/counter').content
	return c

@app.route("/")
def hello():
	c = increaseCounter()
	return render_template('counter.html', hostname=host_name, value=c)
    
if __name__ == "__main__":
	app.run(host='0.0.0.0', port=port)
