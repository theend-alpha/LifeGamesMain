import os
import sys
import random
import asyncio
import telethon.utils
from telethon import TelegramClient, events
from decouple import config
from os import getenv
import logging
import time
from Config import API_ID, API_HASH, BOT_TOKEN

Alf = TelegramClient('Alf', API_ID, API_HASH).start(bot_token=BOT_TOKEN)

DB_URI = config("DATABASE_URL", None)

CMD_HNDLR = getenv("CMD_HNDLR", default="/")
