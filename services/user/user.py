from flask import Flask, render_template, make_response, request
from flask_restful import Resource, reqparse
from flask_jwt_extended import jwt_required
from session_token import *

import json
import os, sys
import socket
import logging

from dbOps import *
from app import *

@App.api.representation('application/json')
def output_json(data, code, headers=None):
	try:
		resp = make_response(data.json(), code)
	except:
		resp = make_response(json.dumps(data), code)
	resp.headers.extend(headers or {})
	return resp

@App.jwt.claims_verification_failed_loader
def claimsFailed():
	logging.error('claims Failed')
	return 'oups', 404

class ApiError:
	def __init__(self, msg):
		self.msg = msg
	def json(self):
		return json.dumps({'error':self.msg})

class User(Resource):
	@jwt_required
	def get(self, id):
		logging.info('user.get.{}'.format(id))
		user = getUserById(id)
		if user is None:
			return ApiError('user not found'), 404
		return user, 200

class Login(Resource):
	def post(self):
		args = request.get_json()
		name = args.get('name')
		pwd = args.get('pwd')
		return loginAPI(name, pwd)

class Register(Resource):
	def post(self):
		args = request.get_json()
		name = args.get('name')
		pwd = args.get('pwd')
		return createUserAPI(name, pwd)

def loginAPI(name, pwd):
	user = authenticate(name, pwd)
	if user is None:
		logging.info('user.login.failed')
		return ApiError('could not login user'), 404

	# generate the auth token
	auth_token = encode_auth_token(user.id)
	return {'id':user.id, 'token':auth_token}, 200

def createUserAPI(name, pwd):
	if name is None or pwd is None:
		logging.info('user.register.wrong_args.failed')
		return ApiError('wrong params {}, {}'.format(name, pwd)), 401
	user = createUser(name, pwd)
	if user is None:
		logging.info('user.register.existing.failed')
		return ApiError('could not create user'), 402
	logging.info('user.register.success')
	return user, 200


if __name__ == "__main__":
	connectDB()
	App.api.add_resource(Register, "/user")
	App.api.add_resource(Login, "/login")
	App.api.add_resource(User, "/user/<int:id>")
	App.app.run(host='0.0.0.0', port=Config.port)
