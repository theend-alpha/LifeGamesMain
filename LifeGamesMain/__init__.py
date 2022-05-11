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

LOGGER = logging.getLogger(__name__)


MONGO_DB_URI = os.environ.get("MONGO_DB_URI", None)
