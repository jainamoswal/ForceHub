import requests
from functools import wraps
from telethon import events, Button
from ..helpers.database import db
from ForceHub import ForceBot
from config import var

db = db()

def follow_me(user_id):
    followed = '1'
    github_data = requests.get(f"https://api.github.com/users/{var.GITHUB_USERNAME}/followers")
    data = github_data.json()
    followers = [i['login'] for i in data]
    if db.find_one({"user_id":str(user_id)}) is None:
        return '0'
    elif db.find_one({"user_id":str(user_id)}, {'github_username':1})['github_username'] not in followers:
        return 'False'
    else:
        return 'True'
