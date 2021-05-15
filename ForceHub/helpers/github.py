import requests
from functools import wraps
from telethon import events, Button
from ..helpers.database import db
from ForceHub import ForceBot
from config import var

db = db()

def follow_me(user_id):
    followed = '1'
    followers = []
    github_data = requests.get(f"https://api.github.com/users/{var.GITHUB_USERNAME}/followers")
    data = github_data.json()
    for i in data:
        followers.append(i['login'])
    if db.find_one({"user_id":str(user_id)}) is None:
        followed = '0'
        return followed
    elif db.find_one({"user_id":str(user_id)}, {'github_username':1})['github_username'] not in followers:
        followed = 'False'
        return followed
    else:
        followed = 'True'
        return followed
    return followed
