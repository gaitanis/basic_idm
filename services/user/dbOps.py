from dbModel import *

import time

def connectDB(max_retries=10):
	retries = 0
	while True:
		try:
			App.db.create_all()
			break
		except Exception as err:
			logging.error(err)
			pass
		retries += 1
		if retries >= max_retries:
			logging.error("Could not connect to DB after {} retries.".format(retries))
			exit(100)
		logging.info("waiting for DB...")
		time.sleep(1)

def authenticate(name, pwd):
	user = SQLUser.query.filter(SQLUser.name == name).first()
	if user is None or user.pwd != pwd:
		return None
	return user

def getUserById(id):
    return SQLUser.query.filter(SQLUser.id == id).first()

def createUser(name, pwd):
    user = SQLUser.query.filter(SQLUser.name == name).first()
    if user != None:
        return None

    user = SQLUser(name=name, pwd=pwd)
    App.db.session.add(user)
    App.db.session.commit()
    return user
