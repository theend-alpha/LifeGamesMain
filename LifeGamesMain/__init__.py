from telethon import TelegramClient
from Config import API_ID, API_HASH, BOT_TOKEN

ALF = TelegramClient('ALF', API_ID, API_HASH).start(bot_token=BOT_TOKEN)
