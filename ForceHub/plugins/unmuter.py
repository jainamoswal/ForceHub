from .. import ForceBot
from telethon import events, Button
from ..helpers.github import follow_me
from datetime import datetime
import re

@ForceBot.on(events.callbackquery.CallbackQuery(data=re.compile(b'v_')))
async def un_mute(event):
    group_id, user_id = event.data.decode('utf-8').replace('v_', '').split('_')
    if event.sender_id != int(user_id):
        await event.answer("That wasn't for you.", alert=True)
    else:
        ans = follow_me(event.sender_id)
        if ans == 'True':
            await ForceBot.edit_permissions(event.chat.id, event.sender_id, send_messages=True)
            await event.answer('Well, You may procced now. I\'ve unmuted you.', alert=True)
            await event.edit(f"Group ID :- {group_id}\nUser ID :- {user_id}\nVerified on  :- {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")
        if ans == 'False':
            await event.answer("Uhhh, You have just authenticated your github username, not followed still.", alert=True)
        if ans == '0':
            await event.answer('How can I unmute without being yourself authenticated and without following ?', alert=True)
            
        
