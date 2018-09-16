import os, socket, logging
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager

class Config:
	db_schema = os.getenv("DB_SCHEMA", "mysql")
	db_user = os.getenv("DB_USER", "root")
	db_password = os.getenv("DB_PWD", "Test1234")
	db_host = os.getenv("DB_HOST", "127.0.0.1:32000")
	db_name = os.getenv("DB_NAME", "db")
	db_url = '{schema}://{user}:{pwd}@{host}/{db}'.format(schema=db_schema,
														  user=db_user,
														  pwd=db_password,
														  host=db_host,
														  db=db_name)
	host_name = socket.gethostname()
	env_name = os.getenv("NAME", "Development")
	port = os.getenv("PORT", 4002)
	token_secret = os.getenv("TOKEN_SECRET", "myprecious")

logging.getLogger().setLevel(logging.INFO)
logging.info('connecting to {}'.format(Config.db_url))

app = Flask(__name__)
app.config['PROPAGATE_EXCEPTIONS'] = True #jwt error propagation
app.config['JWT_SECRET_KEY'] = Config.token_secret
app.config['SQLALCHEMY_DATABASE_URI'] = Config.db_url
jwt = JWTManager(app)
db = SQLAlchemy(app)
