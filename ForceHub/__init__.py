from telethon import TelegramClient
import logging
import time
from config import var

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

APP_ID = var.APP_ID
API_HASH = var.API_HASH
BOT_TOKEN = var.BOT_TOKEN

ForceBot = TelegramClient('Bot', int(APP_ID), API_HASH).start(bot_token=BOT_TOKEN) 
