import os

from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, Message, CallbackQuery
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

smooch = "https://te.legra.ph/file/2bd00c6b47f9f3a7bfe1d.jpg"

@Client.on_callback_query()
async def _callbacks(bot: Client, callback_query: CallbackQuery):
    user = await bot.get_me()
    # user_id = callback_query.from_user.id
    mention = user["mention"]
    query = callback_query.data.lower()
   
    if query == "smooch":
        chat_id = callback_query.from_user.id
        if target_id == chat_id
        await callback_query.message.reply_photo(smooch,
                                                 caption=AlphaIsAlone.SMOOCHA.format(message.reply_to_message.from_user.mention, message.from_user.mention))
           
