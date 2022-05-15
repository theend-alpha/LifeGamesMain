import os

from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, Message





@Client.on_message(filters.command("smooch"))
async def info_func(_, message: Message):
    if message.reply_to_message:
        target_id = message.reply_to_message.from_user.id
    elif not message.reply_to_message and len(message.command) == 1:
        target_id = message.from_user.id
    elif not message.reply_to_message and len(message.command) != 1:
        target_id = message.text.split(None, 1)[1]
