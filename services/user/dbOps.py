from dbModel import *
import session_token

import time

def connectDB(max_retries=10):
	retries = 0
	while True:
		try:
			db.create_all()
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

def getCounterId():
	counter = SQLCounter.query.order_by(SQLCounter.id).limit(1).first()
	if counter == None:
		# Insert a SQLCounter in the counter table
		new_counter = SQLCounter(value=0)
		db.session.add(new_counter)
		db.session.commit()
		counter_id = new_counter.id
		return counter_id
	else:
		counter_id = counter.id
		return counter_id

def increaseCounter(id):
	counter = SQLCounter.query.filter(SQLCounter.id == id).first()
	if counter == None:
		return None

	counter.value += 1
	db.session.commit()
	return counter

def authenticate(name, pwd):
	user = SQLUser.query.filter(SQLUser.name == name).first()
	if user.pwd != pwd:
		return None
	return user

def getUserById(id):
    return SQLUser.query.filter(SQLUser.id == id).first()

def createUser(name, pwd):
    user = SQLUser.query.filter(SQLUser.name == name).first()
    if user != None:
        return None

    user = SQLUser(name=name, pwd=pwd)
    db.session.add(user)
    db.session.commit()
    return user
