from .. import ForceBot
from telethon import events
from config import var

@ForceBot.on(events.NewMessage(incoming=True, pattern="/start"))
async def start(event):
    await event.reply("I'm [ForceHub bot](https://github.com/jainamoswal/ForceHub) by [J Projects](https://t.me/j_projects) maintained by [Jainam Oswal](https://github.com/jainamoswal).")
