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
