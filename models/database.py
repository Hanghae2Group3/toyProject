from pymongo import MongoClient

class dbInfo:
	client = MongoClient('mongodb://localhost', 27017)
	db = client['team3toy']
	userDB = db['user']
