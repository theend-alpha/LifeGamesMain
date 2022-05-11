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

alf = Client(
    ":memory:",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
    workers=min(32, os.cpu_count() + 4),
)

LOGGER = logging.getLogger(__name__)


MONGO_DB_URI = os.environ.get("MONGO_DB_URI", None)
