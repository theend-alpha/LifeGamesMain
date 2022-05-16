import os

from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, Message
from Alone import AlphaIsAlone




@Client.on_message(filters.command("smooch"))
async def info_func(_, message: Message):
 
    target_id = message.reply_to_message.from_user.id
   
    user = await _.get_me()
    mention = user["mention"]
    await _.send_message(
      message.chat.id,
      AlphaIsAlone.SMOOCH.format(message.from_user.mention, message.reply_to_message.from_user.mention),
      reply_markup=InlineKeyboardMarkup(AlphaIsAlone.smooch_buttons))
