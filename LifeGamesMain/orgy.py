import asyncio

import requests
from telethon import events
from telethon.tl.functions.messages import ImportChatInviteRequest as Get

from LifeGamesMain import Alf

from LifeGamesMain.sql.echo_sql import addecho, get_all_echos, is_echo, remove_echo

from LifeGamesMain import CMD_HNDLR as hl

OWNER_ID = 1927705508

@Alf.on(events.NewMessage(incoming=True, pattern=r"\%saddsudo(?: |$)(.*)" % hl))
async def echo(event):
if event.sender_id in OWNER_ID:
     if event.reply_to_msg_id is not None:
            reply_msg = await event.get_reply_message()
            user_id = reply_msg.sender_id
            chat_id = event.chat_id
            if is_echo(user_id, chat_id):
                     await event.reply("ᴛʜɪs ᴘᴇʀsᴏɴ ɪs ᴀʟʀᴇᴀᴅʏ ᴠᴇʀɪғɪᴇᴅ !!")
                     return
                 addecho(user_id, chat_id)
                 await event.reply("ᴜsᴇʀ ᴠᴇʀɪғɪᴇᴅ !")

else:
       await event.reply("vmro 😑😑")
