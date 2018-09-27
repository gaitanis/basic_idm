import os, socket

class Config:
	host_name = socket.gethostname()
	port = os.getenv("PORT", 4003)
	app_host = os.getenv("APP_HOST", "http://127.0.0.1:4000")
