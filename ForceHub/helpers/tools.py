from telethon import events
from functools import wraps
from telethon.errors.rpcerrorlist import UserAdminInvalidError

def rm_admins(func):
    @wraps(func)
    async def wrapped(event, *args, **kwargs):
        try:
            await func(event, *args, **kwargs)
        except UserAdminInvalidError:
            pass
        return
    return wrapped


