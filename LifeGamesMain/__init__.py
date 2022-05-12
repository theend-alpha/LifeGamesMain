import logging
import os
import sys
import json
import asyncio
import time
from telethon import TelegramClient
from telethon.sessions import StringSession
from telethon.sessions import MemorySession
from pyrogram.types import Message
from pyrogram import Client, errors
from pyrogram.errors.exceptions.bad_request_400 import PeerIdInvalid, ChannelInvalid
from pyrogram.types import Chat, User
from config import API_ID, API_HASH, BOT_TOKEN 


LOGGER = logging.getLogger(__name__)

MONGO_DB_URI = "mongodb+srv://keshavalpha:keshavalpha@cluster0.htiys.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"

alf = Client(
    ":memory:",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
    workers=min(32, os.cpu_count() + 4),
)
