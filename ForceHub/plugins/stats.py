import requests
from .. import ForceBot
from telethon import events
from config import var

def get_follwed():
    followed = 0
    github_data = requests.get(f"https://api.github.com/users/{var.GITHUB_USERNAME}/followers").json()
    for i in github_data:
        followed = followed + 1
    return followed

@ForceBot.on(events.NewMessage(incoming=True, pattern="/stats"))
async def stats_reply(event):
    await event.reply(f'{get_follwed()} people followed since....')
