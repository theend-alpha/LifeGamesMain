import asyncio

import requests
from telethon import events
from telethon.tl.functions.messages import ImportChatInviteRequest as Get

from LifeGamesMain import Alf

from LifeGamesMain.sql.echo_sql import addecho, get_all_echos, is_echo, remove_echo

from LifeGamesMain import CMD_HNDLR as hl
