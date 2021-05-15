from pymongo import MongoClient
from config import var

cluster = MongoClient(var.MONGO_URL)

def db():
	return cluster['github-bot']['data']
