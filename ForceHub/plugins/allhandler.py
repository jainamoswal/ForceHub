from .. import ForceBot
from telethon import events, Button
import asyncio
from ..helpers.github import follow_me
from telethon.errors.rpcerrorlist import UserAdminInvalidError
from ..helpers.tools import rm_admins
from config import var

@ForceBot.on(events.NewMessage(func=lambda e: e.is_group))
@rm_admins
async def allmsg(event):
    result = follow_me(event.sender_id)
    if result == 'False':
        await ForceBot.edit_permissions(event.chat.id, event.sender_id, send_messages=False)
        await event.reply("You have just authorised yourself with www.github.com, Didn't followed my owner still.\nDo that and come back. Till that, Shhhh! 🤫", buttons=[
            [Button.inline("Unmute Me", data=f'{event.chat.id}_{event.sender_id}')]
        ])
    if result == '0':
        await ForceBot.edit_permissions(event.chat.id, event.sender_id, send_messages=False)
        await event.reply(f"You need to Authorise first and follow my owner's [GitHub profile](https://www.github.com/{var.GITHUB_USERNAME}) to chat in this group.", buttons=[
                        [Button.auth("⚡️ Authenticate ⚡️", url=f'{var.APP_DOMAIN}/new', write_access=True, fwd_text="Don't try to be a noob.")],
                        [Button.inline("Unmute Me", data=f'v_{event.chat.id}_{event.sender_id}')]
                        
                    ], link_preview=False)
    else:
        pass
